from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import PostForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)


# Create your views here.
def fbv_view(request):
    return render(request, "index.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context


class RedirectToGoogle(RedirectView):
    url = "https://google.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post.content)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    # We can use queryset var here instead of def get_queryset for custom queries!
    # permission_required = "blog.view_post"
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"
    # Because we don't inherit below code ordering will overwrite!
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/posts/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    success_url = "/blog/posts/"
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    success_url = "/blog/posts/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/posts/"
