from django.urls import path

from about.views import (
    ShowAbout,
    ShowAboutBasic,
    ShowAboutOurTeam,
    ShowAboutBanksPartners,
    ShowAboutValueCooperation,
    ShowAboutJob,
)


app_name = "about"

urlpatterns = [
    path("", ShowAbout.as_view(), name="about"),
    path("basic/", ShowAboutBasic.as_view(), name="about_basic"),
    path("our_team/", ShowAboutOurTeam.as_view(), name="about_our_team"),
    path(
        "banks_partners/", ShowAboutBanksPartners.as_view(), name="about_banks_partners"
    ),
    path(
        "value_cooperation/",
        ShowAboutValueCooperation.as_view(),
        name="about_value_cooperation",
    ),
    path("job/", ShowAboutJob.as_view(), name="about_job"),
]
