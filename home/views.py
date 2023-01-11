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
        self.views['reviews'] = Review.objects.all()
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
        self.views['product_reviews'] = ProductReview.objects.filter(slug = slug)
        return render(request,'product-detail.html',self.views)

class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query')
        if query != '':
            self.views['search_product'] = Product.objects.filter(name__icontains = query)
        else:
            return redirect('/')
        return render(request,'search.html',self.views)

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

def product_review(request,slug):
    username = request.user.username
    email = request.user.email
    import datetime
    x = datetime.datetime.now()
    date = str(x.strftime("%c"))
    if request.method == "POST":
        star = request.POST['star']
        comment = request.POST['comment']
        data = ProductReview.objects.create(
            username = username,
            email = email,
            star = star,
            comment = comment,
            slug = slug,
            date = date
        )
        data.save()
    return redirect(f'/detail/{slug}')

class CartView(BaseView):
    def get(self,request):
        grand_total = 0
        username = request.user.username
        self.views['cart_products'] = Cart.objects.filter(username = username,checkout = False)
        for i in self.views['cart_products']:
            grand_total =  grand_total + i.total
        self.views['all_total'] = grand_total
        self.views['grand_total'] = grand_total + 50

        return render(request,'cart.html',self.views)
def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(slug = slug,username = username,checkout = False).quantity
        quantity = quantity+1
        if discounted_price > 0:
            total = discounted_price * quantity
        else:
            total = price * quantity
        Cart.objects.filter(slug=slug, username=username, checkout=False).update(quantity =  quantity,total = total)
        return redirect('/cart')

    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            total = discounted_price
        else:
            total = price
        data = Cart.objects.create(
            username = username,
            slug = slug,
            total = total,
            items = Product.objects.get(slug = slug)
        )
        data.save()
        return redirect('/cart')


def reduce_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug=slug, username=username, checkout=False).exists():
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = Cart.objects.get(slug=slug, username=username, checkout=False).quantity
        if quantity >1:
            quantity = quantity - 1
            if discounted_price > 0:
                total = discounted_price * quantity
            else:
                total = price * quantity
            Cart.objects.filter(slug=slug, username=username, checkout=False).update(quantity=quantity, total=total)
    return redirect('/cart')

def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(slug=slug, username=username, checkout=False).delete()
    return redirect('/cart')