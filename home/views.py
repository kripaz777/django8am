from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *

class BaseView(View):
    views ={}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['hot_products'] = Product.objects.filter(label = 'hot')
        self.views['new_products'] = Product.objects.filter(label='new')
        self.views['sale_products'] = Product.objects.filter(label='sale')
        return render(request,'index.html',self.views)