from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldAPI(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        return Response({'hello': 'world'})


class ByByWorldAPI(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        return Response({'by': 'by world'})
