from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Event, Register  # Importando os modelos Event e Register
from django.core.serializers import serialize
from .forms import EventForm, RegisterForm  # Importando os formulários EventForm e RegisterForm

# Função de visualização principal que renderiza a lista de eventos
def main(request):
    return render(request, 'events/list.html')

# Função para retornar todos os eventos como JSON
def get_events(request):
    events = list(Event.objects.all().values())
    return JsonResponse(events, safe=False)

# Função para visualizar um evento específico e suas inscrições
def get_event(request, id):
    event = get_object_or_404(Event, pk=id)
    registrations = Register.objects.filter(event=event)
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST
        form = RegisterForm(request.POST)
        if form.is_valid():  # Verifica se o formulário é válido
            register = form.save(commit=False)
            register.event = event  # Atribui o evento ao registro
            register.save()  # Salva o registro no banco de dados
            return redirect('/api/events/view/{id}'.format(id=id))  # Redireciona para a página de visualização do evento
    else:
        form = RegisterForm()
    labels = {
        'event': event,
        'form': form,
        'registrations':registrations
    }
    return render(request, 'events/view.html', labels)  # Renderiza a página de visualização do evento

# Função para atualizar um evento existente
def update_event(request, id):
    event = get_object_or_404(Event, pk=id)
    form = EventForm(instance=event)
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST
        form = EventForm(request.POST, instance=event)
        if form.is_valid():  # Verifica se o formulário é válido
            event.save()  # Salva as alterações do evento
            return redirect('/')  # Redireciona de volta para a página principal
    else:
        return render(request, 'events/update.html', {'form':form})  # Renderiza o formulário de atualização do evento

# Função para criar um novo evento
def create_event(request):
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST
        form = EventForm(request.POST)
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo evento no banco de dados
            return redirect('/')  # Redireciona de volta para a página principal após o cadastro do evento
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})  # Renderiza o formulário de criação de evento

# Função para excluir um evento
def delete_event(request, id):
    event = get_object_or_404(Event, pk=id)
    event.delete()  # Exclui o evento do banco de dados
    return redirect('/')  # Redireciona de volta para a página principal