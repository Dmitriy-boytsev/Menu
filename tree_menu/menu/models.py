from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    named_url = models.CharField(max_length=200,blank=True, null=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children",on_delete=models.CASCADE)

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reversed(self.named_url)
        return "#"
    
    def __str__(self):
        return self.name