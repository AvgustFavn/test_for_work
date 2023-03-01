from menu.models import Menu


def status_menu():
    res = Menu.objects.get(stat=True).name
    if res == 'menu.html':
        return 'menu.html'
    return 'empty_menu.html'