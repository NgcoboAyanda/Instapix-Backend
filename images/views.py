import openai
import environ
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Image
from .serializers import ImageSerializer

#environ
env = environ.Env()

#openai
openai.api_key = env('OPENAI_API_KEY')

# Create your views here.
class GenerateImagesView(APIView):    
    def post(self, request):
        prompt = request.data['prompt']
        resolution = request.data['resolution']
        number_of_images = request.data['nOfImages']
        res = openai.Image.create(
            prompt=prompt,
            n=number_of_images,
            size=resolution
        )
        images = res['data']
        image_list = []
        for image in images:
            image = Image.objects.create(prompt=prompt, number=number_of_images, url=image['url'], resolution=resolution)
            image_list.append(image)
        serializer = ImageSerializer(image_list, many=True)
        return Response(serializer.data)

class GetImageHistoryView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
