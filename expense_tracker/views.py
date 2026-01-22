
from django.utils                                           import timezone
from django.shortcuts                                       import render
from django.views                                           import View
from .forms                                                 import NewExpenseForm
from .models                                                import Expense


# Create your views here.
class ExpenseTrackerView(View):

    template_name = 'overview.html'

    def get(self, request):
        form = NewExpenseForm()
        expenses = Expense.objects.all()
        today = timezone.now().date()
        expenses_this_month = Expense.objects.filter(date__year=today.year, date__month=today.month)

        amount_total = 0
        expenses_count = expenses.count()
        for expense in expenses:
            amount_total += expense.amount

        amount_month = 0
        expenses_this_month_count = expenses_this_month.count()
        for expense in expenses_this_month:
            amount_month += expense.amount


        average_amount = amount_total / expenses_count


        context = {
            'form': form,
            'expenses': expenses,
            'total_amount': amount_total,
            'expenses_count': expenses_count,
            'amount_month': amount_month,
            'expenses_this_month_count': expenses_this_month_count,
            'average_amount': average_amount,
            'active_tab': self.template_name.replace('.html', '')
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
            'active_tab': self.template_name.replace('.html', '')
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
            'expenses': expenses,
            'active_tab': 'expenses'
        }

        render_response = render(request, self.template_name, context)

        return render_response
