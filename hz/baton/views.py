from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import *
from .forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


def contacts(request):
    """Получение формы обратной связи"""
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['phone'],
                form.cleaned_data['email'],
                form.cleaned_data['message'],
            )
            context = {'success': 1}
            messages.success(request, 'Сообщение отправлено')
            return redirect('home')
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'baton/contact.html', context=context)


def send_message(name, phone, email, message):
    """Передача обратной связи"""
    text = get_template('baton/message.html')
    html = get_template('baton/message.html')
    context = {'name': name, 'email': email, 'phone': phone, 'message': message}
    subject = 'Обратная связь'
    from_email = 'talasov201@yandex.ru'
    text_content = text.render(context)
    hrml_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['talasov2017@yandex.ru'])
    msg.attach_alternative(hrml_content, 'text/html')
    msg.send()


class Home(ListView):
    """Вывод модели на главную"""
    model = Product
    template_name = 'baton/index.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Categories(ListView):
    """Получение модели по категориям"""
    template_name = 'baton/shop.html'
    context_object_name = 'products'
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


# class GetProduct(DetailView):
#     model = Product
#     template_name = 'baton/single.html'
#     context_object_name = 'product'
#     cart_product_form = CartAddProductForm
#     # context_object_form = 'cart_product_form'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = Product.objects.get(slug=self.kwargs['slug'])
#         return context


def get_product(request, id, slug):
    """Вывод конкретной модели"""
    product = get_object_or_404(Product, pk=id, slug=slug, availability=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'baton/single.html', {'product': product,
                                                 'cart_product_form': cart_product_form})


# class Shop(ListView):
#     model = Product
#     template_name = 'baton/shop.html'
#     context_object_name = 'products'
#     paginate_by = 1
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


def shop(request):
    """Получение всех моделей на странице shop"""
    products = Product.objects.filter(availability=True).select_related('category')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'baton/shop.html', {'products': products,
                                               'page_obj': page_obj})
