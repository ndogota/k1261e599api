from rest_framework import generics
from rest_framework import mixins

from .models import City
from .serializers import CitySerializer


class CityGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request, pk)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


