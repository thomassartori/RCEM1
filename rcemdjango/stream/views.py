from django.shortcuts import render

from stream.models import Message

def index(request):
    latest_message_list = Message.objects.all().order_by('date')[:5]
    context = {'latest_message_list': latest_message_list}
    return render(request, 'stream/index.html', context)
