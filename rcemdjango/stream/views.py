from django.shortcuts import render, redirect

from stream.models import Message, Utilisateur

def index(request):
    latest_message_list = Message.objects.all().order_by('date')[:5]
    context = {'latest_message_list': latest_message_list}
    return render(request, 'stream/index.html', context)

def add_message(request):
    # Si la requete n'est pas un POST, rediriger au stream
    if request.method != 'POST':
        return redirect('/stream')

    message_content = request.POST.get('message', None)

    if message_content != None: # Si il y a bien un message, on l'enregistre
        user = Utilisateur.ghost_user()
        message_content = message_content.strip() # On enleve le whitespace du message
        message = Message.objects.create(auteur=user, texte=message_content)
        message.save()

    return redirect('/stream')
