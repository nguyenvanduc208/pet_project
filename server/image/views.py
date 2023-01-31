from rest_framework.views import APIView
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class ImageView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request):
        data = request.data
        serializer = ImageSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)
