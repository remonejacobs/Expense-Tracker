from django.contrib import admin
from django.urls import path

from views import CalendarView

url_patterns= [
    path('', CalendarView, name='calendar'),
]