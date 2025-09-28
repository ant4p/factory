from django.views.generic import ListView, TemplateView

from about.models import CommandUnit


class ShowAbout(TemplateView):
    template_name = "about/about.html"


class ShowAboutBasic(TemplateView):
    template_name = "about/basic.html"


class ShowAboutOurTeam(ListView):
    template_name = "about/our_team.html"
    context_object_name = "items"
    paginate_by = 50

    def get_queryset(self):
        return CommandUnit.objects.all()


class ShowAboutBanksPartners(TemplateView):
    template_name = "about/banks_partners.html"


class ShowAboutValueCooperation(TemplateView):
    template_name = "about/value_cooperation.html"


class ShowAboutJob(TemplateView):
    template_name = "about/job.html"
