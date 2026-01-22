from django.urls                                import path
from .views                                     import ExpenseTrackerView, ExpenseListView, ExpenseDelete

urlpatterns = [
    path('', ExpenseTrackerView.as_view(), name='expense-tracker'),
    path('expenses/', ExpenseListView.as_view(), name='expense_list'),
    path('expense/<int:pk>/delete', ExpenseDelete.as_view(), name='expense_delete'),
]