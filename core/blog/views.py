from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView, RedirectView, ListView, DetailView
# Create your views here.
def fbv_view(request):
    return render(request,'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='ali'
        return context

class RedirectToGoogle(RedirectView):
    url = 'https://google.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk = kwargs['pk'])
        print(post.content)
        return super().get_redirect_url(*args, **kwargs)

class PostListView(ListView):
    # We can use queryset var here instead of def get_queryset for custom queries!
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    # Because we don't inherit below code ordering will overwrite!
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(DetailView):
    model = Post