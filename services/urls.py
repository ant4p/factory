from django.urls import path

from services.views import (
    ShowServices,
    ShowServicesPageBG,
    ShowServicesPageCred,
    ShowServicesPageFactoring,
    ShowServicesPageInsurance,
    ShowServicesPageInternaionalPayments,
    ShowServicesPageLizing,
    ShowServicesBGItem44FZ,
    ShowServicesBGItem223FZ,
    ShowServicesBGItem275FZ,
    ShowServicesBGItem615PP,
    ShowServicesBGItemCommercial,
    ShowServicesBGItemPayment,
    ShowServicesBGItemAnotherNPA,
    ShowServicesCredItemWorkingCapital,
    ShowServicesCredItemTender,
    ShowServicesCredItemInvest,
    ShowServicesCredItemContract,
    ShowServicesCredItemRefinance,
    ShowServicesLizingItemCar,
    ShowServicesLizingItemTruck,
    ShowServicesLizingItemSpecialTech,
    ShowServicesLizingItemEquipment,
    ShowServicesLizingItemUsed,
    ShowServicesLizingItemOtherProperty,

)


app_name = "services"

urlpatterns = [
    path("", ShowServices.as_view(), name="services"),
    path("bg/", ShowServicesPageBG.as_view(), name="services_bg"),
    path("cred/", ShowServicesPageCred.as_view(), name="services_cred"),
    path("lizing/", ShowServicesPageLizing.as_view(), name="services_lizing"),
    path("factoring/", ShowServicesPageFactoring.as_view(), name="services_factoring"),
    path(
        "international_payments/",
        ShowServicesPageInternaionalPayments.as_view(),
        name="services_international_payments",
    ),
    path("insurance/", ShowServicesPageInsurance.as_view(), name="services_insurance"),
]

urlpatterns += [
    path("bg/44_fz/", ShowServicesBGItem44FZ.as_view(), name="services_bg_44_fz"),
    path("bg/223_fz/", ShowServicesBGItem223FZ.as_view(), name="services_bg_223_fz"),
    path("bg/275_fz/", ShowServicesBGItem275FZ.as_view(), name="services_bg_275_fz"),
    path("bg/615_fz/", ShowServicesBGItem615PP.as_view(), name="services_bg_615_pp"),
    path(
        "bg/commercial/",
        ShowServicesBGItemCommercial.as_view(),
        name="services_bg_commercial",
    ),
    path(
        "bg/payment/", ShowServicesBGItemPayment.as_view(), name="services_bg_payment"
    ),
    path(
        "bg/another_npa/",
        ShowServicesBGItemAnotherNPA.as_view(),
        name="services_bg_another_npa",
    ),
]

urlpatterns += [
    path(
        "cred/working_capital/",
        ShowServicesCredItemWorkingCapital.as_view(),
        name="services_cred_working_capital",
    ),
    path(
        "cred/tender/",
        ShowServicesCredItemTender.as_view(),
        name="services_cred_tender",
    ),
    path(
        "cred/invest/",
        ShowServicesCredItemInvest.as_view(),
        name="services_cred_invest",
    ),
    path(
        "cred/contract/",
        ShowServicesCredItemContract.as_view(),
        name="services_cred_contract",
    ),
    path(
        "cred/refinance/",
        ShowServicesCredItemRefinance.as_view(),
        name="services_cred_refinance",
    ),
]

urlpatterns += [
    path(
        "lizing/car/",
        ShowServicesLizingItemCar.as_view(),
        name="services_lizng_car",
    ),
     path(
        "lizing/truck/",
        ShowServicesLizingItemTruck.as_view(),
        name="services_lizng_truck",
    ),
     path(
        "lizing/special_tech/",
        ShowServicesLizingItemSpecialTech.as_view(),
        name="services_lizng_special_tech",
    ),
     path(
        "lizing/equipment/",
        ShowServicesLizingItemEquipment.as_view(),
        name="services_lizng_equipment",
    ),
     path(
        "lizing/used/",
        ShowServicesLizingItemUsed.as_view(),
        name="services_lizng_used",
    ),
     path(
        "lizing/other_property/",
        ShowServicesLizingItemOtherProperty.as_view(),
        name="services_lizng_other_property",
    ),

]
