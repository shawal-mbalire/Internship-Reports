from rest_framework import permissions, viewsets
from rest_api_app.models import MyUser, Transfer, Collection
from rest_api_app.serializers import MyUserSerializer, TransferSerializer, CollectionSerializer

from mtnmomoapi.collection import Collection
from mtnmomoapi.disbursement import Disbursement

class MyUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-date_joined')
    serializer_class = MyUserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TransferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Transfers to be viewed or created.
    """
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        client = Disbursement()
        response = client.transfer(
            amount        ="600", 
            phone_number  ="0966456787", 
            external_id   ="123456789", 
            payee_note    ="dd",      
            payer_message ="dd", 
            currency      ="EUR"
        )
        return super().create(request, *args, **kwargs)
    


    
class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Collections to be viewed or created.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        client = Collection()
        response = client.requestToPay(
            amount        ="600", 
            phone_number  ="0966456787", 
            external_id   ="123456789", 
            payee_note    ="dd", 
            payer_message ="dd", 
            currency      ="EUR"
        )
        return super().create(request, *args, **kwargs)

