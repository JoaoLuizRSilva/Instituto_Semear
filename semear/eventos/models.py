from django.db import models

# Definindo o modelo Event
class Event(models.Model):
    # Campo para armazenar o título do evento com no máximo 255 caracteres
    title = models.CharField(max_length=255)
    # Campo para armazenar o local do evento com no máximo 255 caracteres
    local = models.CharField(max_length=255)
    # Campo para armazenar a data e hora do evento
    schedule = models.DateTimeField()
    # Campo para armazenar a descrição do evento (texto longo)
    description = models.TextField()

# Definindo o modelo Register
class Register(models.Model):
    # Campo para armazenar o nome do participante com no máximo 255 caracteres
    name = models.CharField(max_length=255)
    # Campo para armazenar o email do participante (com validação de formato de email)
    email = models.EmailField()
    # Campo para armazenar o evento associado ao registro
    # ForeignKey é usado para estabelecer uma relação muitos-para-um
    # on_delete=models.CASCADE especifica que se um evento for excluído, todos os registros associados a ele serão excluídos também
    # null=True permite que esse campo seja opcional (ou seja, pode ser nulo)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)