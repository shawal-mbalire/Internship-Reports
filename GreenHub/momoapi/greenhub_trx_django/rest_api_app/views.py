from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_api_app.models import MyUser
from rest_api_app.serializers import MyUserSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def my_user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = MyUser.objects.all()
        serializer = MyUserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)