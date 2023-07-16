from .serializers import JogosSerializers
from rest_framework import generics
from .models import Jogos


# Listar e Criar os Jogos
class JogosAPIView(generics.ListCreateAPIView):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializers

# Atulaizar, trazer um jogo e deletar um jogo
class JogoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializers
    
