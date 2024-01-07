from django.shortcuts import render

from .models import Topics

# Create your views here.
def index(request):
    """The homepage for Learning Log. """
    return render(request, template_name='learning_logs/index.html')

def topics(request):
    topics = Topics.objects.all()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Show a single topic and all its entries."""
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
