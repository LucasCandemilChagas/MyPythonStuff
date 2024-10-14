from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import cairosvg

from PIL import Image

import requests
import bs4
import re

import os
import sys

tipo_img = ""
num_img_baixada = 0
list_img = []
is_svg = False
driver = None


# metodo que deixa mais limpo o terminal
def limpar_console():
    print(os.name)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    print("Download de Imagens")
    print("1 - Download")
    print("2 - Sair")


def inicia_browser(browser: str):
    if re.match(browser.lower(), "chrome"):
        driver = webdriver.Chrome(
            service=ServiceChrome(executable_path=ChromeDriverManager().install())
        )
    elif re.match(browser.lower(), "firefox"):
        driver = webdriver.Firefox()
    elif re.match(browser.lower(), "edge"):
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    elif re.match(browser.lower(), "safari"):
        driver = webdriver.Safari()
    # elif re.match(browser.lower(), 'opera'):
    #    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        print("Navegador não encontrado!")
        return None

    return driver


def verifica_svg(svg):
    if re.search(".png|.jpg", svg):
        return False
    return True


def converte_svg_para_png(svg, nova_img):
    cairosvg.svg2png(url=svg, write_to=nova_img)


def transforma_svgsrc_link(svg_src):
    svg_link = "https://pt.wikipedia.org" + svg_src
    return svg_link


def verificacao_https(link):
    if re.match("https://", link):
        return True
    else:
        return False


def print_titulo_imgs(list):

    print("Imagens Disponiveis: ")
    for ind, i in enumerate(list):
        for barra in re.finditer(r"/", i["src"]):
            # print(barra.span())
            pass
        px = re.search("px-", i["src"])
        if px is not None:
            print(f"    {ind+1} - {i['src'][px.span()[1]:]}")
            # print(f"    {ind+1} - {i['src']}")
        else:
            list_str = str(i["src"]).split("/")
            name_img = list_str[len(list_str) - 1]
            if re.search(".png|.jpg|.svg", name_img):
                print(f"    {ind+1} - {name_img}")

def verifica_img(list):
    if len(list) == 0:
        print("Nenhuma imagem encontrada!")
        return False
    return True


def criacao_img(nome_arquivo, img_link: requests.models.Response):
    nome_arquivo += tipo_img
    print(nome_arquivo)
    print(tipo_img)
    with open(nome_arquivo, "wb") as f:
        f.write(img_link.content)
        print("Download Concluido!")


def validacao_indice(indice):
    if (indice >= 1 and indice < len(list_img)) or indice == -1:
        return True
    return False


def verifica_saida(indice):
    try:
        if int(indice) == -1:
            sys.exit(1)
    except ValueError:
        pass


def digitar_navegador_nome():
    while True:
        nav = input("Insira o nome do seu navegador: ")

        driver_ = inicia_browser(nav)

        if driver_ is not None:
            break

    return driver_


while True:

    #driver = digitar_navegador_nome()

    #print(driver)

    menu()
    
    while True:
        try:
            op = int(input("Opção: "))
            if op < 1 or op > 2:
                print("Opção inválida!")
            else:
                break
        except ValueError:
            print("Opção inválida!")
        
            

    try:
        if op == 1:
            while True:
                print("Para sair digite -1")

                link = input("Insira o link do site: ")

                limpar_console()

                verifica_saida(link)

                if verificacao_https(link):
                    break
                else:
                    print("Link Invalido!")

            verifica_saida(link)

            resultado = requests.get(link)

            soup = bs4.BeautifulSoup(resultado.text, "lxml")

            list_img = soup.select("img")

            list_img_fig = soup.select("figure")

            while verifica_img(list_img):
                limpar_console()
                
                print_titulo_imgs(list_img)
                
                while True:
                    try:
                        print("Para sair digite -1")
                        indice = int(
                            input(f"Insira um numero de 1 a {len(list_img)}: ")
                        )
                        if validacao_indice(indice):
                            raise ValueError
                    except ValueError:
                        print("Invalido!")
                    except NameError:
                        indice = -1

                    verifica_saida(indice)

                    limpar_console()

                    src = str(list_img[indice - 1]["src"])

                    tipo_img = src[len(src) - 4 :]

                    if not verifica_svg(src) and not verificacao_https(src):
                        src = "https:" + src
                    else:
                        src = transforma_svgsrc_link(src)
                        is_svg = True

                    img_link = requests.get(src)

                    nome_arquivo = input("Digite um nome para a sua imagem: ")

                    if not is_svg:
                        criacao_img(nome_arquivo, img_link)
                        nome_arquivo+=tipo_img
                    else:
                        nome_arquivo += ".png"
                        converte_svg_para_png(src, nome_arquivo)

                    with Image.open(nome_arquivo) as imagem:
                        imagem.show()

                    indice = 0

                    break

        elif op == 2:
            break
        
    except NameError:
        limpar_console()
        pass
