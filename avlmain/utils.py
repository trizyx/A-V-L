from .models import *

menu = [{'title': "HOME", 'url_name': 'home'},
        {'title': "SHOP", 'url_name': 'shop'},
        {'title': "ABOUT", 'url_name': 'about'}
]

menu2 = [{'title': "CART", 'url_name': 'cart'},
]

class DataMixin:


    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['keys'] = cats
        context['menu2'] = menu2
        if 'key_selected' not in context:
            context['key_selected'] = 0
        return context

