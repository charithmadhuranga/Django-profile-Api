from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from profile_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """Hello APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a post request"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """hello viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'viewsets have list,create,retrieve,update,partial_update',
            'give functionality to the app with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """get specific object"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partially update an object"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})




