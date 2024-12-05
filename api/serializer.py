from rest_framework import serializers
from.models import programmer, Student

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        # fields = ['fullname', 'nickname', 'age', 'is_active']
        fields= '__all__' #se especifica los campos que se quiere mostrar en la serialización.  


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # especifica los campos que se quiere most
        