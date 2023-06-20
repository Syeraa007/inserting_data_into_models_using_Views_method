from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
# Create your views here.
def insert_topic(request):
    Tname=input('Enter Topic Name : ')
    TO=Topic.objects.get_or_create(topic_name=Tname)[0]
    TO.save()
    return HttpResponse('Topic is inserted')

def insert_webpage(request):
    Tname=input('Enter Topic Name : ')
    TO=Topic.objects.get_or_create(topic_name=Tname)[0]
    TO.save()
    Name=input('Enter name : ')
    Url=input('Enter URL : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)[0]
    WO.save()
    return HttpResponse('Webpage is inserted')

def insert_access_record(request):
    Tname=input('Enter Topic Name : ')
    TO=Topic.objects.get_or_create(topic_name=Tname)[0]
    TO.save()
    Name=input('Enter name : ')
    Url=input('Enter URL : ')
    Date=input('Enter date : ')
    Author=input('Enter author : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=Name,url=Url)[0]
    WO.save()
    ARO=AccessRecord.objects.get_or_create(name=WO,date=Date,author=Author)[0]
    ARO.save()
    return HttpResponse('Access Record is inserted')
