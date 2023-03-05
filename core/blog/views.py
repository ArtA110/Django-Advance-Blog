from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView, RedirectView, ListView
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

class PostList(ListView):
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=True)