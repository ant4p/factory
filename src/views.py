from django.db.transaction import clean_savepoints
from django.views.generic import TemplateView


class ShowMainPage(TemplateView):
    template_name = "src/main.html"

class ShowContactPage(TemplateView):
    template_name = 'src/contacts.html'

class ShowUserAgreementPage(TemplateView):
    template_name = 'src/user_agreement.html'

class ShowPrivacyPolicyPage(TemplateView):
    template_name = 'src/privacy_policy.html'
