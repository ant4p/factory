from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from about.models import CommandUnit, JobUnit, ValueUnit


# class ShowAbout(TemplateView):
#     template_name = "about/about.html"


class ShowAboutBasic(TemplateView):
    template_name = "about/basic.html"


class ShowAboutOurTeam(ListView):
    template_name = "about/our_team.html"
    context_object_name = "items"
    paginate_by = 50
    

    def get_queryset(self):
        return CommandUnit.objects.all()

class ShowCases(TemplateView):
    template_name = "about/cases.html"


class ShowAboutBanksPartners(TemplateView):
    template_name = "about/banks_partners.html"


class ShowAboutValueCooperation(ListView):
    template_name = "about/value_cooperation.html"
    context_object_name = "items"
    paginate_by = 8

    def get_queryset(self):
        return ValueUnit.objects.all()


class ShowAboutJob(ListView):
    template_name = "about/job.html"
    context_object_name = "items"
    paginate_by = 5

    def get_queryset(self):
        return JobUnit.objects.all()


class ShowVacancy(DetailView):
    model = JobUnit
    template_name = "about/vacancy.html"
    context_object_name = "item"

    def get_queryset(self):
        return JobUnit.objects.filter()

    def get_success_url(self):
        return reverse("vacancy", kwargs={"slug": self.obect.slug})
