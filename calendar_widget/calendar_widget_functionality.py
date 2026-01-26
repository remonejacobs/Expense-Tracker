import calendar
from datetime import date
import calendar_widget
from django.shortcuts import render
from django.views.generic import TemplateView

current_year = date.today().year
current_month = date.today().month

def generateCalendar(year = current_year, month = current_month):
    today = date.today()
    month = month
    year  = year
    # display_calendar = calendar_widget.Calendar(firstweekday=0)
    # days_list        = display_calendar.monthdayscalendar(year, month)  #gets list of days in every week
    cal = calendar.HTMLCalendar()
    # context = {
    #     "year": year,
    #     "month": month,
    #     "month_name": calendar_widget.month_name[month],
    #     "weekdays": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    #     "month_days": days_list,
    # }
    return cal.formatmonth(year, month)






