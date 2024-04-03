from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import UserData, Savings, Category, Expenses
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serialzers import UserData_serializer, Savings_serializer, CategorySerializer,Expense_serializer
from .pagination import StandardResultspagination

class UserData_viewset(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by('Name')
    serializer_class = UserData_serializer
    pagination_class = StandardResultspagination
    
    @action(detail= False, methods=['post'])
    def create_userdata(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        else:
            return Response(serializer.errors, status = 400)
        
class SavingsViewSet(viewsets.ModelViewSet):
    queryset = Savings.objects.all()
    serializer_class = Savings_serializer

    @action(detail=False,methods=['post'])
    def create_savings(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        else:
            return Response(serializer.errors, status = 400)
    
    @action(detail=False,methods=['get'])
    def get_savings(self,request):
        queryset=self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)
        data=[]
        for i in serializer.data:
            total_savings = i['emergency_fund'] + i['retirement_savings'] + i['education_savings'] + i['medical_savings'] + i['others']
            emergency_fund_percentage = (i['emergency_fund'] / total_savings) * 100 
            education_savings_percentage = (i['education_savings'] / total_savings) * 100
            medical_savings_percentage = (i['medical_savings'] / total_savings) * 100

            if (emergency_fund_percentage > 30) and \
               (education_savings_percentage > 30) and \
               (medical_savings_percentage > 30):
                imbalance_message = 'Savings imbalance: Emergency fund, education savings, and medical savings each exceed 30%" of total savings'

            
            i['imbalance_message'] = imbalance_message
            data.append(i)

        return Response(data)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = Expense_serializer
    pagination_class=StandardResultspagination
    

    def create(self, request, *args, **kwargs):
        category_id = request.data.get('category', [])
        if category_id is None:
            return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        categories = Category.objects.filter(pk__in=category_id).all()

        if not categories.exists():
            return Response({'error': 'No valid categories found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            
            instance.category.set(categories)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
            
        pk = self.kwargs.get('pk')
        if pk is not None:
            obj = get_object_or_404(queryset, pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        else:
            return None
        