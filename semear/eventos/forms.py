from django import forms
from .models import Event, Register

# Formulário para eventos
class EventForm(forms.ModelForm):
    # Metaclasse para associar o modelo e os campos do formulário
    class Meta:
        model = Event
        fields = '__all__'

    # Campo personalizado para o horário do evento
    schedule = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

# Formulário para registro
class RegisterForm(forms.ModelForm):
    # Metaclasse para associar o modelo e os campos do formulário
    class Meta:
        model = Register
        fields = ['name', 'email']