from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from hapisentiment.models import SentimentData
from hapisentiment.serializers import SentimentDataSerializer


class SentimentList(generics.ListAPIView):
    queryset = SentimentData.objects.all()
    serializer_class = SentimentDataSerializer

    def list(self, request, *args, **kwargs):
        query_dict = self.request.query_params
        query_keys = query_dict.keys()
        if len(query_keys) != 1:
            return None

        urlParamList = query_dict.getlist("url")
        jsonDicts = {"response":[]}
        jsonDicts['response'].append({"url":"url", "containsHateSpeech":""})

        return Response(jsonDicts)