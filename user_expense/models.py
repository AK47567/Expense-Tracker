from django.db import models

class UserData(models.Model):
    def calculate_ctc(self):
        
        return self.Fixed_salary + self.Variable_salary
    
    Name = models.CharField(max_length=100,primary_key=True)
    Date_of_birth = models.DateField()
    Profession = models.CharField(max_length=100)
    Address = models.TextField()
    Fixed_salary = models.DecimalField(max_digits=10,decimal_places=2)
    Variable_salary = models.DecimalField(max_digits=10,decimal_places=2)
    In_hand_salary = models.DecimalField(max_digits=10,decimal_places=2) 
    CTC= models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        ordering = ['Name']
        
    def __str__(self):
        return self.Name
    
class Account(models.Model):
    bank_name = models.CharField(max_length=100, verbose_name="Bank Name")
    account_number = models.CharField(max_length=20, verbose_name="Account Number", unique=True, primary_key=True)
    ifsc_code = models.CharField(max_length=11, verbose_name="IFSC Code")
    balance = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Balance")

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
    
class Savings(models.Model):
    user_data = models.ForeignKey(UserData, on_delete=models.CASCADE)
    emergency_fund = models.DecimalField(max_digits=10, decimal_places=2)
    retirement_savings = models.DecimalField(max_digits=10, decimal_places=2)
    education_savings = models.DecimalField(max_digits=10, decimal_places=2) 
    medical_savings = models.DecimalField(max_digits=10, decimal_places=2)
    account=models.ManyToManyField(Account) 
    others = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"Emergency Fund: {self.emergency_fund}, " \
               f"Retirement Savings: {self.retirement_savings}, " \
               f"Education Savings: {self.education_savings}, " \
               f"Medical Savings: {self.medical_savings}, " \
               f"Others: {self.others}"




class Category(models.Model):
     
    category = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.category} : {self.category_description}"
               


class Expenses(models.Model):
    user_data = models.ForeignKey(UserData,on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10,decimal_places=2)
    category= models.ManyToManyField(Category)
    account=models.ManyToManyField(Account)
    description=models.CharField(max_length=100,null=True)

    def __str__(self):
            return f"User Data: {self.user_data}, " \
                f"Amount {self.Amount}, " \
                f"Category: {self.category}, " 