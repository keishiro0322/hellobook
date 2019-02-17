from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages #メッセージライブラリ

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog

from .forms import BlogForm

# Create your views here.

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs" #テンプレートに渡される変数を変える
    paginate_by = 3

    def get_queryset(self):
        queryset = Blog.objects.order_by('-posted_date')

        return queryset

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")
    template_name = "blog/blog_create_form.html"

    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update_form.html"

    login_url = '/login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新されました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)
