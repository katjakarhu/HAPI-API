# Create your views here.
from urllib.parse import urlparse

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from hapifakenews.models import FakeSite
from hapifakenews.serializers import FakeSiteSerializer

class FakeNewsMixin(object):
    # This is the fake news site data we have in the DB
    serializer_class = FakeSiteSerializer
    queryset = FakeSite.objects.all()
    

class FakeNewsUrlCheckView(FakeNewsMixin, generics.RetrieveAPIView):
    lookup_fields = 'url'
  
    def get_object(self):
        def am_i_fake(url):
            if url.startswith("http") is False:
                url = "http://" + url

            parsed_uri = urlparse(url)
            domain = parsed_uri.netloc.lower()
            path = parsed_uri.path.lower()

            # Let's remove unnecessary crap so that the actual domain is all that's left
            while domain.count('.') > 1:
                domain = domain.partition('.')[2]

            # If the site is a twitter handle, let's add / and a username. Result:  domain/username
            if domain == "twitter.com" or domain == 'facebook.com':
                split_path = path.split("/")
                domain = domain + '/' + split_path[1]

            matching_site_queryset = self.queryset.filter(url__icontains=domain)

            return matching_site_queryset

        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)


        url_param = self.kwargs['url']
        print(url_param)

        filter ={}
        fake_data_queryset = am_i_fake(url_param)
                       
        obj = get_object_or_404(fake_data_queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    
class FakeNewsListVersion1ViewSet(FakeNewsMixin, generics.ListAPIView):
    pass


class FakeNewsRetrieveVersion1View(FakeNewsMixin, generics.RetrieveAPIView):
    pass

   


    
    
