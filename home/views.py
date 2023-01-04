from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
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
        ids = Product.objects.get(slug=slug).subcategory_id
        self.views['related_products'] = Product.objects.filter(subcategory_id=ids)
        return render(request,'product-detail.html',self.views)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'This username is already taken!')
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'This email is already taken!')
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                data.save()
        else:
            messages.error(request, 'The password does not match!')
            return redirect('/signup')
    return render(request,'signup.html')