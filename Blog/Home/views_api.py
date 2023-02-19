from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class Login(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message']  = 'Something went wrong'
        try:
            data= request.data
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            if data.get('password') is None:
                response['messsage'] = 'key passwor not found'
                raise Exception('key password not found')
            
            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user is None:
                response['message'] = 'invalid username'
                raise Exception('invalid username')
            user_obj = authenticate(username = data.get('password') , password = data.get('password'))
            if user_obj:
                response['status']=200
                response['message']= 'Welcome'
            else:
                response['message']= 'invalid password'
                raise Exception('invalid password')
            
        except Exception as e:
            print(e)

        return Response(response)
    
Login = Login.as_view()


class Register(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message']  = 'Something went wrong'
        try:
            data= request.data
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            if data.get('password') is None:
                response['messsage'] = 'key passwor not found'
                raise Exception('key password not found')
            
            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user:
                response['message'] = 'username already taken'
                raise Exception('username already taken')
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'User created'
            response['status'] = 200
        except Exception as e:
            print(e)
Register = Register.as_view()


            