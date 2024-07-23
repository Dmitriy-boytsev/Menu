from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def page(request, page_name):
    context = {'page_name': page_name}
    return render(request, 'menu/draw_menu.html', context)
