from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, authentication
from rest_framework.decorators import APIView, api_view, throttle_classes
from rest_framework.response import Response
from  catalog.serializers import ArtistSerializer, UserSerializer, AlbumSerializer
from rest_framework.throttling import UserRateThrottle
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from catalog.models import Artist, Album
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

# Function Based View
@api_view(['POST', 'GET'])
@throttle_classes([OncePerDayUserThrottle])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': 'Got some data!'})
    return Response({'message': 'Hello, World!'})


# Class Based View
# class ArtistView(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     throttle_classes = [OncePerDayUserThrottle]

#     def get(self, request):
#         artists = Artist.objects.all()
#         return Response(artists)

#     def post(self, request):
#         return Response({'data': request.data})


# Generic Based View(creating new artist, listing out all artists)
class ArtistGenericView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset =Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# artists/<pk>
# retrive the object by id, update the object by id, delete object by id
class ArtistDetailGenericView(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              GenericAPIView):
    
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArtistView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]


class ArtistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer