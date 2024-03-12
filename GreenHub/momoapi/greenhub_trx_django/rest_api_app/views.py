from rest_framework import permissions, viewsets
from rest_api_app.models import MyUser, Transfer, Collection
from rest_api_app.serializers import MyUserSerializer, TransferSerializer, CollectionSerializer

class MyUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-date_joined')
    serializer_class = MyUserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TransferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Transfers to be viewed or edited.
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # permission_classes = [permissions.IsAuthenticated]

    
class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Transfers to be viewed or edited.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    # permission_classes = [permissions.IsAuthenticated]