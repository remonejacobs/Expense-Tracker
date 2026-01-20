from django.urls                                import path
from .views                                     import ExpenseTrackerView, ExpenseListView

urlpatterns = [
    path('', ExpenseTrackerView.as_view(), name='expense-tracker'),
    path('expenses/', ExpenseListView.as_view(), name='expense_list'),
]