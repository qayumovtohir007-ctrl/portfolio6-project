from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from app.form import ContactForm
from app.models import Portfolio, Service


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.all()
        context['services'] = Service.objects.all()
        return context


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        # messages.success(self.request, message="Xabaringiz yuborildi")
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy("index") + "#contact"


