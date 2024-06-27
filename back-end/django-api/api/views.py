import qrcode
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from . serializers import ListCustomUserSerializer, CustomUserSerializer, CustomTokenObtainPairSerializer, ListItemsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from api.models import CustomUser, Item
from . pagination import CustomPagination


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUserSerializer
    queryset = CustomUser.objects.all()


class ListItemApiView(ListAPIView):
    serializer_class = ListItemsSerializer
    queryset = Item.objects.all()
    pagination_class = CustomPagination
    # limit the number of requests per user to 5 in 1 minute
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'brand']
    ordering_fields = ['price']
    search_fields = ['title', 'brand']
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60)) 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Item.objects.all()
        # Filter by price greater than
        # price = self.request.query_params.get('price', None)

        # price_gt = queryset.filter(price__gt=10000)
        # brand = queryset.filter(brand='MANDARINA DUCK')

        # # return combined queryset
        # return price_gt.intersection(brand)
        # if price is not None:
        #     queryset = queryset.filter(price__gte=price)
        return queryset
    

class DetailItemApiView(RetrieveAPIView):
    serializer_class = ListItemsSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'


class QRCodeApiView(APIView):

    def get(self, request, *args, **kwargs):
        data = "https://www.apgiiit.com"  # Replace with your data

        qr = qrcode.make(data, version=1, box_size=10)  # Optional parameters
        
        # save qg code image in a new media folder
        qr.save('media/qrcode.png')
        return Response({'message': 'This is a QR code API view'})
    




