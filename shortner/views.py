from .serializers import TinyURLSerialzier
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TinyURL
from django.http.response import HttpResponseRedirect
from .mixins import DefaultResponseMixin


class ShortURLView(DefaultResponseMixin, APIView):

    def get_object(self, url_hash):
        try:
            return TinyURL.objects.get(short_url_hash=url_hash)
        except TinyURL.DoesNotExist:
            raise Http404

    def get(self, request, url_hash):
        shortened_url = self.get_object(url_hash)
        return HttpResponseRedirect(redirect_to=shortened_url.original_url)

    def post(self, request):
        serializer = TinyURLSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.create_response(data=serializer.data)
        return self.create_response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


