from .models import Contact, Network, Setting, Kategory

# постоянные данные
def get_constanta():
    contact = Contact.objects.all()
    network = Network.objects.all()
    kategory = Kategory.objects.all()
    return {
        'contact': contact,
        'network': network,
        'kategory': kategory,
        }