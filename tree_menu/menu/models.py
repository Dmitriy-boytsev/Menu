from django.db import models


class Menu(models.Model):
    """Представляет меню."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Возвращает строковое представление объекта меню."""
        return self.name


class MenuItem(models.Model):
    """Представляет элемент меню."""
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    named_url = models.CharField(max_length=200,blank=True, null=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children",on_delete=models.CASCADE)

    def get_url(self):
        """Возвращает URL элемента меню."""
        if self.url:
            return self.url
        elif self.named_url:
            return reversed(self.named_url)
        return "#"
    
    def __str__(self):
        """Возвращает строковое представление объекта меню."""
        return self.name