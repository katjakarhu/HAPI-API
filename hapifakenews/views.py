# Create your views here.
from urllib.parse import urlparse

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from hapifakenews.models import FakeSite
from hapifakenews.serializers import FakeSiteSerializer

class FakeNewsMixin(object):
    # This is the fake news site data we have in the DB
    serializer_class = FakeSiteSerializer
    queryset = FakeSite.objects.all()   


class FakeNewsListVersion1ViewSet(FakeNewsMixin, generics.ListAPIView):
    pass


class FakeNewsRetrieveVersion1View(FakeNewsMixin, generics.RetrieveAPIView):
    print("jkfldjklfjfklfjdlak!!!!!!!!!!!!!!!!")
    print(len(FakeNewsMixin.queryset))
    
    def retrieve(self, request, *args, **kwargs):
        print("jkfldjklfjfklfjdlak!!!!!!!!!!!!!!!!?????????????????????")
        return Response()
   

class FakeNewsList(generics.ListAPIView):
    # This is the fake news site data we have in the DB
    queryset = FakeSite.objects.all()

    serializer_class = FakeSiteSerializer

    # Here we construct a JSON response
    def list(self, request, *args, **kwargs):
        # Check if the domain is classified as a fake news site in out db
        # If it is, return the data from DB, else return None
        def am_i_fake(url):

            if url.startswith("http") is False:
                url = "http://" + url

            parsed_uri = urlparse(url)
            domain = parsed_uri.netloc.lower()
            path = parsed_uri.path.lower()
            # Let's remove unnecessary crap so that the actual domain is all that's left
            while domain.count('.') > 1:
                domain = domain.partition('.')[2]
           
            if domain == "twitter.com" or domain == 'facebook.com':
                split_path = path.split("/")
                domain = domain + '/' + split_path[1]
        
            matching_site_queryset = self.queryset.filter(site__icontains=url)

            if len(matching_site_queryset) > 0:
                return matching_site_queryset
            else:
                return None

        # HTTP GET parameters are here
        query_dict = self.request.query_params
        query_keys = query_dict.keys()
        if len(query_keys) != 1:
            return None
    
        query_filters = []
        custom_filters = []

        # We want to go through all the URL -parameters
        url_param_list = query_dict.getlist("url")

        json_response = {"response":[]}

        for url_param in url_param_list:
            fake_data = am_i_fake(url_param)
                       
            # Site is not fake, woohoo!
            if fake_data is None:
                source = ""
                source_url = ""
                foo = "false"
            else: # It's a fake!
                foo = "true"
                source = fake_data.all()[0].sourcename
                source_url = fake_data.all()[0].sourceurl
            json_response['response'].append({"url":url_param,"sourceUrl":source_url, "source":source, "isFake":foo})

        return Response(json_response)

    
    
