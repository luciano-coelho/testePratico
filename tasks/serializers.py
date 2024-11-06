from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Category

# Serializer para representar a categoria associada a uma tarefa
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Serializer para representar os usuários com username e id
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Serializer principal para a tarefa
class TaskSerializer(serializers.ModelSerializer):
    # Usando UserSerializer para `shared_with` para exibir `username` dos usuários
    shared_with = UserSerializer(many=True, read_only=True)
    # Serialização aninhada para `category` usando CategorySerializer
    category = CategorySerializer(read_only=True)
    # Campo adicional para receber o ID da categoria no payload
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True, required=False
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'completed', 'created_at', 
            'updated_at', 'user', 'category', 'category_id', 'shared_with'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

# Serializer para registrar um novo usuário
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
