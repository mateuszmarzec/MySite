from BlogAPI.models.models_site import Menu


def context(request):
    menu = Menu.objects.all()
    return {'menu': menu}