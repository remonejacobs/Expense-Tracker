import math
from django.utils                                           import timezone
from django.shortcuts                                       import render
from django.urls                                            import reverse_lazy
from django.views                                           import View
from django.views.generic                                   import DeleteView

from .forms                                                 import NewExpenseForm
from .models                                                import Expense


# Create your views here.
class ExpenseTrackerView(View):

    template_name = 'overview.html'

    def get(self, request):
        form = NewExpenseForm()
        expenses = Expense.objects.all()

        context = {
            'form': NewExpenseForm(),
            'expenses': expenses,
            'active_tab': self.template_name.replace('.html', '')
        }

        context = self.getcontext(request, expenses, context)
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

        context = self.getcontext(request, expenses, context)

        return render(request, self.template_name, context)

    def getcontext(self, request, expenses, context):
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

        labels = ["Fixed/Essential",
                  "Food & Daily Living",
                  "Transportation",
                  "Personal & Lifestyle",
                  "Health & Wellness",
                  "Education",
                  "Entertainment & Social",
                  "Work/Business",
                  "Giving & Miscellaneous"]
        data = self.pie_chart(request, expenses, labels)

        context['total_amount'] = amount_total
        context['expenses_count'] = expenses_count
        context['amount_month'] = amount_month
        context['expenses_this_month_count'] = expenses_this_month_count
        context['average_amount'] = round(average_amount, 2)
        context['data'] = data
        context['labels'] = labels

        return context

    def pie_chart(self, request, expenses, labels):
        category_amounts = []
        for label in labels:
            total_amount = 0
            for expense in expenses:
                if expense.category == label:
                    total_amount += expense.amount
            category_amounts.append(math.ceil(total_amount))


        return category_amounts



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

class ExpenseDelete(DeleteView):

    model = Expense
    template_name = 'expense-delete.html'
    success_url = reverse_lazy('expense_list')