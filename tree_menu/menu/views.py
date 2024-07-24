from django.shortcuts import render

def index(request):
    """Отображает главную страницу."""
    return render(request, 'menu/index.html')

def page(request, page_name):
    """Отображает страницу с указанным именем."""
    context = {'page_name': page_name}
    return render(request, 'menu/draw_menu.html', context)
