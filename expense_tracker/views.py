from django.shortcuts                                       import render
from django.views                                           import View
from .forms                                                 import NewExpenseForm



# Create your views here.
class ExpenseTrackerView(View):

    template_name = 'overview.html'

    def get(self, request):
        form = NewExpenseForm()
        return render(request, self.template_name, {'form': form})

class ExpenseListView(View):
    template_name = 'expense_list.html'

    def get(self, request):
        form = NewExpenseForm()

        context = {'form': form}

        render_response = render(request, self.template_name, context)

        return render_response
