# from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError;
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    @action(detail=True, methods=['get'])
    def retrieve_by_id(self, request, pk=None):
        recipe = self.get_object()
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

@api_view(['POST'])
def login(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Přihlášení proběhlo úspěšně'})
    else:
        return Response({'message': 'Neplatné jméno, nebo heslo'}, status=401)

@csrf_exempt
@api_view(['POST'])
def register(request):
    # the register logic
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if User.objects.filter(username=username).exists():
        return Response({'message': 'Toto jméno je již zabrané'}, status=status.HTTP_400_BAD_REQUEST)
    
    if password != password2:
        return Response({'message': 'Hesla se neshodují'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) < 5:
        return Response({'message': 'Heslo musí obsahovat alespoň 5 znaků'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({'message': 'Registrace proběhla úspěšně'})
    except IntegrityError:
        return Response({'message': 'objevil se Error při vytváření účtu'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ValidationError as e:
        return Response({'message': e.messages}, status=status.HTTP_400_BAD_REQUEST)

# udělat URL routy v urls.py