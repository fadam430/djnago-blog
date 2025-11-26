from django.shortcuts import render, get_object_or_404 # type: ignore
from django.views import generic # type: ignore
from .models import Post
#from .models import Event

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/index.html'
    paginate_by = 6
    
def post_detail(request, slug):
    """
    Renders the detail view of a blog post identified by its slug.
    
    **Content**
    
    ``post_detail``
        an instance of model : `blog.pot`
        
    **Template**
    
    :template:`blog/post_detail.html`
    """
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by('-created_on')
    comment_count = post.comments.filter(approved=True).count()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_count': comment_count}) 








# class EventList(generic.ListView):
#     model = Event
#     template_name = "index.html"
#     paginate_by = 12



# def event_detail(request, event_id):
#     """
#     Renders the detail view of an event identified by its ID.
    
#     **Content**
    
#     ``event_detail``
#         an instance of model : `blog.event`
        
#     **Template**
    
#     :template:`blog/event_detail.html`
#     """
    
#     # Assuming there's an Event model similar to Post

#     queryset = Event.objects.all()
#     event = get_object_or_404(queryset, id=event_id)
#     return render(request, 'events/event_detail.html', {'event': event})