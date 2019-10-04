from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView

from flowerv3.custom_error import CustomError
from flowerv3.custom_response import CustomResponse
from .models import Hoa
from .serializers import CreateHoaSerializer


class PostHoa(APIView):
    name = "post_hoa"
    """
    get:
    Return a list of all the existing novels.

    post:
    Create a new novel instance.
    """

    def post(self, request):
        serializer = CreateHoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(data=serializer.data, status=status.HTTP_200_OK)
        errors = CustomError(message="Bạn nhập định dạng không đúng ", code=2000)

        return CustomResponse(errors=errors, debug=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetHoa(APIView):
    name = "get_hoa"

    def get(self, request):
        hoas = Hoa.objects.all()
        serializer = CreateHoaSerializer(hoas, many=True)
        return CustomResponse(data=serializer.data, status=status.HTTP_200_OK)
