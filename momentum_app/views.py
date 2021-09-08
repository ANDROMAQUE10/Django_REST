from django.shortcuts import render
from django.shortcuts import render
from django.http import request, JsonResponse, Http404
from .models import SP500, DJ30, Divs, Etf, Notes
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import DJ30Serializer, EtfSerializer, DivsSerializer, NotesSerializer, SP500Serializer
import os


class Momentum2SP500(APIView):

    def get(self, request):
        obj = SP500.objects.all().order_by('-momentum_12_2')
        serializer_obj = SP500Serializer(obj, many=True)
        return Response(serializer_obj.data)


class EpSP500(APIView):

    def get(self, request):
        obj = SP500.objects.all().order_by('-ep')
        serializer_obj = SP500Serializer(obj, many=True)
        return Response(serializer_obj.data)



class Momentum2DJ30(APIView):

    def get(self, request):
        obj = DJ30.objects.all().order_by('-momentum_12_2')
        serializer_obj = DJ30Serializer(obj, many=True)
        return Response(serializer_obj.data)


class EpDJ30(APIView):

    def get(self, request):
        obj = DJ30.objects.all().order_by('-ep')
        serializer_obj = DJ30Serializer(obj, many=True)
        return Response(serializer_obj.data)


class DetailDJ30(APIView):

    def get(self, request, symbol):
        try:
            obj = DJ30.objects.get(symbol=symbol)
            serializer_obj = DJ30Serializer(obj)
            return Response(serializer_obj.data)
        except:
            raise Http404


class DetailSP500(APIView):

    def get(self, request, symbol):
        try:
            obj = SP500.objects.get(symbol=symbol)
            serializer_obj = SP500Serializer(obj)
            return Response(serializer_obj.data)
        except:
            raise Http404

class ListEtf(APIView):

    def get(self, request):
        obj = Etf.objects.all().order_by('-momentum_12_1')
        serializer_obj = EtfSerializer(obj, many=True)
        return Response(serializer_obj.data)


class DetailEtf(APIView):

    def get(self, request, name):
        try:
            obj = Etf.objects.get(name=name)
            serializer_obj = EtfSerializer(obj)
            return Response(serializer_obj.data)
        except:
            raise Http404


class ListDivs(APIView):

    def get(self, request):
        obj = Divs.objects.all().order_by('-div_p')
        serializer_obj = DivsSerializer(obj, many=True)
        return Response(serializer_obj.data)


class ListNotes(APIView):

    def get(self, request):
        obj = Notes.objects.all().order_by('id')
        serializer_obj = NotesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    def post(self, request):
        data = request.data
        serializer_obj = NotesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)


class UpdateNotes(APIView):

    def delete(self, request, id):
        obj = Notes.objects.get(id=id)
        obj.delete()
        return Response({"response": "Note is successfully deleted"})


class Updatedj30(APIView):

    def post(self, request):
        if request:
            os.system("python manage.py runscript dj30_script")
            return Response({"response": "dj30 was updated"})
        else:
            return Response({"response": "Something wrong!"})

class Updatesp500(APIView):

    def post(self, request):
        if request:
            os.system("python manage.py runscript sp500_script")
            return Response({"response": "sp500 index was updated"})
        else:
            return Response({"response": "Something wrong!"})


class Updatedivs(APIView):

    def post(self, request):
        if request:
            os.system("python manage.py runscript divs_script")
            return Response({"response": "dividend index was updated"})
        else:
            return Response({"response": "Something wrong!"})


class Updateetf(APIView):

    def post(self, request):
        if request:
            os.system("python manage.py runscript etf_script")
            return Response({"response": "dividend index was updated"})
        else:
            return Response({"response": "Something wrong!"})
