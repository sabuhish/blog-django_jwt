from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from blog_app.models import *
from .serializers import *

class TestApiview(APIView):

    def get(self, *args, **kwargs):
        return JsonResponse({
            "message":"Api teste xosh gelmisiniz {}".format(
                self.request.user.get_full_name()
            )
        })
# bundan otur bir dene serilizer yaratmaliyiq
# bu post list view ucun nezerde tutulub
# modelu goturek, objects all ile
# serilizer import eliyirik
# serilizerin icine article_list atiriq, ve many ture edirik
class PostListApi(APIView):

    def get(self, *args, **kwargs):
        article_list =Article.objects.all()
        serializer = PostListSerializer(article_list, many=True)
        return JsonResponse({
            "data": serializer.data
        })
    
# json response ise