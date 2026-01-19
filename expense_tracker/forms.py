from django                                                                     import forms

from crispy_forms.helper                                                        import FormHelper
from crispy_forms.layout                                                        import Layout, Row, Column, Fieldset, Submit

from .models                                                                    import Expense

class NewExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        labels = {
            'amount': 'Amount (R)',
            'date': 'Date',
            'category': 'Category',
            'expense_name': 'Expense Name',
            'description': 'Description (Optional)',
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('New Expense',),
            Row(
                Column('amount', css_class='col-md-4'),
                Column('date', css_class='col-md-4'),
            ),
            Row(
                Column('category', css_class='col-md-4'),
                Column('expense_name', css_class='col-md-4'),
            ),
            Row(
                Column('description', css_class='col-md-6'),
            ),
            Row(
                Column(Submit('submit', 'Add Expense', css_class='btn btn-primary')),
            )
        )

