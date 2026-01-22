from django.shortcuts                                       import render
from django.views                                           import View
from .forms                                                 import NewExpenseForm
from .models import Expense


# Create your views here.
class ExpenseTrackerView(View):

    template_name = 'overview.html'

    def get(self, request):
        form = NewExpenseForm()
        expenses = Expense.objects.all()

        context = {
            'form': form,
            'expenses': expenses,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = NewExpenseForm(request.POST)

        if form.is_valid():
            form.save()

        expenses = Expense.objects.all()

        context = {
            'form': NewExpenseForm(),
            'expenses': expenses,
        }

        return render(request, self.template_name, context)

class ExpenseListView(View):
    """
    Returns a list of all expenses.
    """
    template_name = 'expense_list.html'

    def get(self, request):
        expenses = Expense.objects.all()

        context = {
            'form': NewExpenseForm(),
            'expenses': expenses
        }

        render_response = render(request, self.template_name, context)

        return render_response
