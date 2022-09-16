from cgitb import text
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
import pprint

# PARA PEGAR OS ELEMENTOS <SPAN> É NECESSÁRIO USAR UMA FERRAMENTA QUE TRAGA RENDERIZACAO JS
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Create your views here.
URL_SEARCH = 'https://www.drogasil.com.br/search?w='

CLASSE_FRAME_LISTAGEM = "SearchProductsstyles__SearchProductsStyles-sc-1kesk16-0 iyYAwe"
CLASSE_CARD_PRODUTOS = "rd-col-8 rd-col-sm-4"
LINK_COMPRA = "LinkNextstyles__LinkNextStyles-t73o01-0 cpRdBZ LinkNext" # ACESSAR O ATRIBUTO href
MARCA_PRODUTO = "product-brand"
INFORMACOES_EXTRAR = "aditional-info" # INFORMACOES EXTRAS COMO PESO DA EMBALAGEM
AVALIACAO_PRODUTO = "TrustVoxRatingStarsstyles__RatingValuesStyles-sc-11ews35-1 biOkhp"
VALOR_AVALIACAO_PRODUTO = "TrustVoxRatingStarsstyles__RatingValuesStyles-sc-11ews35-1 jKLwc"
# pp = pprint.PrettyPrinter(indent=4)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
# @csrf_exempt

@api_view(['GET','POST'])
def home(request, format=None):
    
    if request.method == 'GET':
        content = {"products":""}
        return Response(content)
    
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        driver = webdriver.Chrome(options = options)
        driver.get(URL_SEARCH+str(body_unicode))
        page = driver.page_source
        # body = json.loads(body_unicode)
        # content = body['content']
        # req_content = requests.get(URL_SEARCH+str(body_unicode)).text
        # print(req_content)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(body_unicode)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<')
        soup = BeautifulSoup(page, 'lxml')
        
        """ PARA OS PRECOS EM COMBO DE PROMOCAO"""
        #class="price price-final"
        
        print('_______________________SOUP PRETTIFY________________________________')
        todos_produtos = soup.find("div", attrs={"class": CLASSE_FRAME_LISTAGEM}).find_all("div", attrs={"class": CLASSE_CARD_PRODUTOS})
        parsed_products = []
        for produto in todos_produtos:
            payload = {}
            dados = produto.find("div", attrs={"class":"ProductCardstyles__ProductCardStyle-iu9am6-4 dheFWb false null"})
            # print(dados)
            # dados = produto.find_all("a")
            # descricao = produto.find("a", attrs={"class":"LinkNextstyles__LinkNextStyles-t73o01-0 cpRdBZ LinkNext"})
            descricao = produto.find("a")["title"]
            print(descricao)
            payload["descricao"] = descricao
            # print(descricao.title)
            # attrs={"class":"price-number"}
            """, attrs={"class":"price price-final"}"""
            preco = produto.find("span", attrs={"class":"price-number"})
            # print(preco)
            # print(preco.text)
            payload["valor"] = preco.text
            # for element in preco:
            #     element = preco.find
            #     payload["valor"] = element.text
            #     print(payload["valor"])
            # print(produto.text)
            # print(produto.prettify())
            # print(produto.find("div", attrs={"class":"product-brand"}))
            marca = produto.find("div", attrs={"class":"product-brand"})
            try:
                payload["marca"] = marca.text
            except AttributeError:
                payload["marca"] = 'sem marca definida'
            # if len(preco) > 1:
            #     for element in preco[1]:
            #         payload["valores"]["combo"] = element.text
            #         print(element.text)
            # else:
            #     for element in preco[0]:
            #         produto["valores"]["individual"] = element.text
            #         print(element.text)
            # print(preco.prettify())
            # print(preco.html.contents[0])
            # print(preco)
            # print(produto)

            # payload["marca"] = [marca]
            # payload["valores"] = [valores]
            # payload.append(produto, preco)
            print(payload)
            parsed_products.append(payload)

        print('**********************************************************************************')
        print(len(todos_produtos))
        
        return Response({
            "products":parsed_products
        })

        #"query":str(body_unicode), 