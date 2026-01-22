from django.shortcuts                                       import render
from django.views                                           import View
from .forms                                                 import NewExpenseForm
from .models import Expense


# Create your views here.
class ExpenseTrackerView(View):

    template_name = 'overview.html'

    def get(self, request):
        form = NewExpenseForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewExpenseForm(request.POST)

        if form.is_valid():
            form.save()

        expenses = Expense.objects.all()

        return render(request, 'results.html', {'expenses': expenses})



class ExpenseListView(View):
    """
    Returns a list of all expenses.
    """
    template_name = 'expense_list.html'

    def get(self, request):
        expenses = Expense.objects.all()

        context = {'expenses': expenses}
        print(context)

        render_response = render(request, self.template_name, context)

        return render_response
