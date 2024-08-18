from django import template
from inventory.models import YourModel
from inventory.models import Category
from inventory.models import Product

register = template.Library()

@register.simple_tag
def changeStatement(status):
    #status=status+1
    related_product = Product.objects.filter(category=status).first()
    print('status :' + str(related_product))
    return related_product