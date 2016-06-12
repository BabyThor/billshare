from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone


from django.conf import settings
from .forms import HostForm
from .models import Bill, Item

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
        bill_name = request.POST.get('bill_name')
        list_item_name = request.POST.getlist('item_name')
        list_item_amount = request.POST.getlist('item_amount')
        list_item_price = request.POST.getlist('item_price')
        bill = Bill.objects.create(name=bill_name, date=timezone.now())
        for index in range(len(list_item_name)):
            Item.objects.create(
                bill=bill,
                name=list_item_name[index],
                amount=list_item_amount[index],
                price=list_item_price[index]
            )
        return HttpResponseRedirect(
            reverse(
                'share',
                kwargs={
                    'bill_id': bill.id,
                }
            )
        )


class Share(TemplateView):
    template_name = 'share.html'

    def get(self, request, bill_id):
        return render(
            request,
            self.template_name,
            {
                'bill_id': bill_id
            }
        )