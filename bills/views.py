from django.shortcuts import render
from django.views.generic import TemplateView

from django.conf import settings
from .forms import HostForm

class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(
            request,
            self.template_name
        )


class Host(TemplateView):
	form = HostForm
	template_name = 'host.html'

	def get(self, request):
		return render(
			request,
			self.template_name,
			{
				'form': self.form,
			}
		)

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
		return render(
			request,
			self.template_name,
			{
				'form': self.form,
			}
		)
