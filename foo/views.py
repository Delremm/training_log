from django.views import generic
from models import Entry, Massage
from django.db.models import get_model
from forms import PostForm, PostModelForm
from django.http import HttpResponseRedirect



class EntryView(generic.ListView):
    template_name = 'board/index.html'
    #model = get_model('foo', 'Massage')
    queryset = Massage.objects.order_by('-tree_id_attr')


class NewPostView(generic.CreateView):
    form_class = PostModelForm
    model = Massage
    template_name = 'board/new_post.html'

class PostDetailView(generic.DetailView):
    model = get_model('foo', 'Massage')
    template_name = 'board/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        self.object = self.get_object()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['branch'] = self.object.get_root().get_descendants(include_self=True)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        if 'save' in request.POST:
            form = PostForm(data=request.POST)
            if form.is_valid():
                post = Massage()
                post.title = form.cleaned_data['title']
                post.parent = self.object
                post.save()
                return HttpResponseRedirect('/board/%s/' % post.id)
            else:
                context['form'] = PostForm()
            return self.render_to_response(context)