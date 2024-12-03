from django.shortcuts import render
from . models import test_Details 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from .models import test_Details, test_Vehicle_Profile
from .serializer import UserDetailsSerializer
# Create your views here.


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(sel, request):
        content = {'message':'Hello, World'}
        return Response(content)


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
    email = request.data.get('email_address')
    password = request.data.get('user_password')
    try:
        user = test_Details.objects.get(email_address=email)
        if check_password(password, user.user_password):
            refresh = RefreshToken.for_user(user)
            return Response({"message": "Login successful!", 
                "user": {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email_address": user.email_address
                    },
                "refresh":str(refresh),
                "access": str(refresh.access_token)
            }, status=200)
        else:
            return Response({"error":"Invalid Password"}, status=401)
    except test_Details.DoesNotExist:
        return Response({"error": "User does not exist"}, status=400)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def hello(request):
    user = request.user
    print(request.headers.get('Authorization'))
    print(request.user)
    if user.is_authenticated:  # Check if the user is authenticated
        print(f"Authenticated User: {user}")
        return Response({"message": "Hello World"}, status=200)
    else:
        return Response({"error": "User not authenticated"}, status=403)


@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def vehicle_profile(request):
    user = request.user_id
    print(f"User: {request.user}, Auth: {request.auth}")
    if request.method == 'POST':
        data = request.data
        test_Vehicle_Profile.objects.create(
            user=user,
            mirror_angle=data['mirror_angle'],
            seat_height=data['seat_height'],
            seat_angle=data['seat_angle'],
            ambient_color=data['ambient_color']
        )
        return Response({"meesage": "Vehicle profile created successfully "}, status=201)
    
    elif request.method == 'PUT':
        try:
            profile = test_Vehicle_Profile.objects.get(user=user)
            data = request.data
            profile.mirror_angle = data['mirror_angle']
            profile.seat_height = data['seat_height']
            profile.seat_angle = data['seat_angle']
            profile.ambient_color = data['ambient_color']
            profile.save()
            return Response({"message": "Vehicle profile updated successfully"}, status=200)
        except test_Vehicle_Profile.DoesNotExist:
            return Response({"error":"Vehicle profile does not exist"}, status=404)