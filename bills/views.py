from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings

class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        print settings.TEMPLATE_DIRS
        return render(
            request,
            self.template_name
        )
