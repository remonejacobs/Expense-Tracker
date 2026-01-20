from django.shortcuts                                       import render
from django.views                                           import View
from .forms                                                 import NewExpenseForm



# Create your views here.
class ExpenseTrackerView(View):

    template_name = 'base.html'

    def get(self, request):
        form = NewExpenseForm()
        return render(request, self.template_name, {'form': form})


