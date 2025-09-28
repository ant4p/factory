from django.views.generic import TemplateView


class ShowServices(TemplateView):
    template_name = "services/services.html"


class ShowServicesPageBG(TemplateView):
    template_name = "services/bg.html"


class ShowServicesPageCred(TemplateView):
    template_name = "services/cred.html"


class ShowServicesPageLizing(TemplateView):
    template_name = "services/lizing.html"


class ShowServicesPageFactoring(TemplateView):
    template_name = "services/factoring.html"


class ShowServicesPageInternaionalPayments(TemplateView):
    template_name = "services/international_payments.html"


class ShowServicesPageInsurance(TemplateView):
    template_name = "services/insurance.html"

# bg_items
class ShowServicesBGItem44FZ(TemplateView):
    template_name = "services/bg/44_fz.html"

class ShowServicesBGItem223FZ(TemplateView):
    template_name = "services/bg/223_fz.html"

class ShowServicesBGItem275FZ(TemplateView):
    template_name = "services/bg/275_fz.html"

class ShowServicesBGItem615PP(TemplateView):
    template_name = "services/bg/615_pp.html"

class ShowServicesBGItemCommercial(TemplateView):
    template_name = "services/bg/commercial.html"

class ShowServicesBGItemPayment(TemplateView):
    template_name = "services/bg/payment.html"

class ShowServicesBGItemAnotherNPA(TemplateView):
    template_name = "services/bg/another_npa.html"

    
# cred_items
class ShowServicesCredItemWorkingCapital(TemplateView):
    template_name = "services/cred/working_capital.html"

class ShowServicesCredItemTender(TemplateView):
    template_name = "services/cred/tender.html"

class ShowServicesCredItemInvest(TemplateView):
    template_name = "services/cred/invest.html"

class ShowServicesCredItemContract(TemplateView):
    template_name = "services/cred/contract.html"

class ShowServicesCredItemRefinance(TemplateView):
    template_name = "services/cred/refinance.html"


# lizing_items
class ShowServicesLizingItemCar(TemplateView):
    template_name = "services/lizing/car.html"

class ShowServicesLizingItemTruck(TemplateView):
    template_name = "services/lizing/truck.html"

class ShowServicesLizingItemSpecialTech(TemplateView):
    template_name = "services/lizing/special_tech.html"

class ShowServicesLizingItemEquipment(TemplateView):
    template_name = "services/lizing/equipment.html"

class ShowServicesLizingItemUsed(TemplateView):
    template_name = "services/lizing/used.html"

class ShowServicesLizingItemOtherProperty(TemplateView):
    template_name = "services/lizing/other_property.html"
    