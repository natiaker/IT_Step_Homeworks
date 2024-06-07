from django.contrib.auth import logout
from django.db.models import Q
from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, RegistrationForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        query = request.GET.get('post_query')

        if query:
            posts = Post.objects.filter(Q(title__icontains=query))
        else:
            posts = Post.objects.all()

        return render(request, self.template_name, {'posts': posts})


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post_details'


class AddPostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'
    login_url = '/login'
    permission_required = 'blog.add_post'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user

        return super().form_valid(form)

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('blog:homepage')


class RemovePostView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:homepage')
    template_name = 'author_confirm_delete.html'
    login_url = '/login'
    permission_required = 'blog.delete_post'

    def test_func(self) -> bool | None:
        post = self.get_object()
        return self.request.user == post.author or self.request.user.has_perm(self.permission_required)

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('blog:homepage')


class UserLoginView(UserPassesTestMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('blog:homepage')

    def test_func(self) -> bool | None:
        return not self.request.user.is_authenticated

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('blog:homepage')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('blog:login')


class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'
    success_url = '/login'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()

        return super().form_valid(form)






