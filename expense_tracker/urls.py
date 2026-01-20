from django.urls                                import path
from .views                                     import ExpenseTrackerView
urlpatterns = [
    path('', ExpenseTrackerView.as_view(), name='add_expense'),
]