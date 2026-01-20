from django                                                                     import forms

from .models                                                                    import Expense

class NewExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['date_created']
        labels = {
            'amount': 'Amount (R)',
            'date': 'Date',
            'category': 'Category',
            'expense_name': 'Expense Name',
            'description': 'Description (Optional)',
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }



