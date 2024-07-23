from django import template
from menu.models import Menu, MenuItem
from django.urls import resolve

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = resolve(request.path_info).url_name
    menu = Menu.objects.get(name=menu_name)
    items = MenuItem.objects.filter(menu=menu).select_related('parent').prefetch_related('children')

    def build_menu_tree(parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(item)
                tree.append({'item': item, 'children': children})
        return tree

    menu_tree = build_menu_tree()
    return {'menu_tree': menu_tree, 'current_url': current_url}
