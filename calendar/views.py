from datetime import date
import calendar
from django.shortcuts import render
from django.views.generic import TemplateView


class CalendarView(TemplateView):
    template_name = "calendar.html"
    def get(self, request, *args, **kwargs):
        today = date.today()
        month = today.month
        year  = today.year

        if "year" in self.request.GET:
            year                  = self.request.GET["year"]

        if "month" in self.request.GET:
            month                 = self.request.GET["month"]

        display_calendar = calendar.Calendar(firstweekday=0)
        days_list        = display_calendar.monthdayscalendar(year, month)  #gets list of days in every week

        context = {
            "year": year,
            "month": month,
            "month_name": calendar.month_name[month],
            "weekdays": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "month_days": days_list,
        }

        response = render(request, self.template_name, context)
        return response






