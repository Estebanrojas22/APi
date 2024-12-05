from rest_framework import viewsets
from .serializer import ProgrammerSerializer, StudentSerializer
from .models import programmer, Student

# Create your views here.

class programmerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer  #se establece el serializer que se va a utilizar para serializar los datos.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  #se establece el serializer que se va a utilizar para serializar los datos.