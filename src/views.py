from django.views.generic import TemplateView


class ShowMainPage(TemplateView):
    template_name = "src/main.html"

class ShowContactPage(TemplateView):
    template_name = 'src/contacts.html'
