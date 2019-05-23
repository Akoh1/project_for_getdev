from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from api.forms import UserSignUpForm, AdminSignUpForm, BookForm
from api.models import Users, NormalUSer, Books
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .decorators import admin_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('book_list')
    return render(request, 'api/index.html')


class UserSignUpView(CreateView):
    model = Users
    form_class = UserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'regular user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('book_list')


class AdminSignUpView(CreateView):
    model = Users
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'regular user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('book_list')


@login_required
@admin_required
def book_create(request, template_name='books/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form': form})


def book_list(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books/book_list.html', context)


@login_required
@admin_required
def book_update(request, book_id, template_name='books/book_form.html'):
    book = get_object_or_404(Books, pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form': form})


@login_required
@admin_required
def rate(request, rate_id):
    book = get_object_or_404(Books, pk=rate_id)
    if request.session.get('has_rated', False):
        mssg = messages.warning(request, "You've already voted!")
        # return HttpResponse("You've already rated.")
        return HttpResponseRedirect(reverse('book_list', args=(mssg)))

    try:
        book.rating += 1
        book.save()
    except (KeyError, Books.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'books/book_list.html', {
            # 'question': question,
            'error_message': "Books dont exist.",
        })

    request.session['has_rated'] = True
    return HttpResponseRedirect(reverse('book_list'))


@login_required
@admin_required
def book_delete(request, book_id, template_name='books/book_delete.html'):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object': book})
