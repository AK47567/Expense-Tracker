from rest_framework import serializers
from .models import UserData, Account, Savings, Expenses, Category

class UserData_serializer(serializers.ModelSerializer):
 

    class Meta:
        model = UserData
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'account': data}


class Savings_serializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'
    
    def validate(self, data):
        emergency_fund = data.get('emergency_fund', 0)
        education_savings = data.get('education_savings', 0)
        medical_savings = data.get('medical_savings', 0)
        retirement_savings = data.get('retirement_savings', 0)
        total_savings = emergency_fund + education_savings + medical_savings + retirement_savings

        
        if (emergency_fund / total_savings) > 0.3:
            raise serializers.ValidationError("Emergency fund exceeds thirty percent of total savings")

        if (education_savings / total_savings) > 0.3:
            raise serializers.ValidationError("Education savings exceeds thirty percent of total savings")
        if (medical_savings / total_savings) > 0.3:
            raise serializers.ValidationError("Medical savings exceeds thirty percent of total savings")
        
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class Expense_serializer(serializers.ModelSerializer):
    category=CategorySerializer(many=True, read_only=True)
    class Meta:
        model=Expenses
        fields='__all__'
        