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


class CategoryView(BaseView):
    def get(self,request,slug):
        ids = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = ids)

        return render(request,'category.html',self.views)


class BrandView(BaseView):
    def get(self,request,slug):
        ids = Brand.objects.get(slug = slug).id
        self.views['brand_products'] = Product.objects.filter(brand_id = ids)

        return render(request,'brand.html',self.views)

class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views['product_details'] = Product.objects.filter(slug=slug)
        return render(request,'product-detail.html',self.views)