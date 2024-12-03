from django.shortcuts import render
from . models import test_Details 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from .models import test_Details
from .serializer import UserDetailsSerializer
# Create your views here.

def user_list(request):
    users = test_Details.objects.all()
    return render(request, 'user_list.html', {'users':users})

@api_view(['POST'])
def signup(request):
    serializer = UserDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email_user')
    password = request.data.get('user_password')

    try:
        user = test_Details.objects.get(email_address=email)
        if check_password(password, user.user_password):
            return Response({"message": "Login successful!", "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email_address": user.email_address
            }}, status=200)
        else:
            return Response({"error":"Invalid Password"}, status=401)
    except test_Details.DoesNotExist:
        return Response({"error": "User does not exist"}, status=400)