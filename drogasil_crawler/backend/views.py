from django.shortcuts import render
# from rest_framework import renderers, response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import requests
import json

# Create your views here.
URL_SEARCH = 'https://www.drogasil.com.br/search?w='

# def scrape_data(request, query):
#     if request.method == 'POST':
#         r = requests.post(URL_SEARCH+str(query))
#         print(r.text)
#         soup = BeautifulSoup(,'lxml')


# @csrf_exempt
@api_view(['GET','POST'])
def home(request, format=None):
    if request.method == 'GET':
        content = {"products":""}
        return Response(content)
        return render(request, 'home.html')

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # content = body['content']
        req_content = requests.get(URL_SEARCH+str(body_unicode)).text
        # print(req_content)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(body_unicode)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<')
        soup = BeautifulSoup(req_content, 'html.parser')
        print('_______________________SOUP PRETTIFY________________________________')
        # print(soup.prettify())class="rd-col-8 rd-col-sm-4"
        # todos_links = soup.find_all("div", attrs={"class":"rd-col-8 rd-col-sm-4"})
        # todos_links = soup.find_all("div", attrs={"class": "TwoColumnsstyles__SecondColumnStyles-sc-1lryd20-1 hEcJif rd-col-13"})
        # todos_links = soup.find_all("div", attrs={"class": "SearchProductsstyles__SearchProductsStyles-sc-1kesk16-0 iyYAwe"})
        # for element in todos_links:
        #     print(element)
        #     print('\n')
        todos_produtos = soup.find("div", attrs={"class": "SearchProductsstyles__SearchProductsStyles-sc-1kesk16-0 iyYAwe"}).find_all("div", attrs={"class": "rd-col-8 rd-col-sm-4"})
        for produto in todos_produtos:
            print(produto)
            print('\n')
        print('**********************************************************************************')
        print(len(todos_produtos))
        # print(todos_links)
        # print(soup)        
        # soup2 = BeautifulSoup(todos_links, 'lxml')
        # print(soup2.prettify())
        # print(todos_links)
        # r = requests.post(URL_SEARCH+str(query))
        # print(r.text)
        # resultado = r.text
        # soup = BeautifulSoup(resultado,'lxml')
        return Response({"products":str(todos_produtos)})
        # return HttpResponse('<html><body>'+str(todos_links)+'</body></html>')

        