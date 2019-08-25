import speech_recognition as sr
import webbrowser as wb
import re #regex
from googlesearch import search
#library for web scrapping
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


def speechToText():
    print("Tell Me The Song u want Lyrics For:(I will try!!!)")
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
        query = listener.recognize_google(audio)
    print("Very Good !!, you said :",query)

    return query

def createSearchQuery(query):
    searchText = re.sub('[" "]','+',query)  #also i could had use re.sub('\s','+',string)
    url = "https://search.azlyrics.com/search.php?q="
    return url+searchText

def webScrapper(query):

    uClient = uReq(query)
    page_html = uClient.read() #here i get a non formatted raw text of html code
    uClient.close()
    page_soup = soup(page_html, "html.parser") # with this  i got a structured html code
    return(page_soup)

def urlScrapper(page_soup):
    container = page_soup.findAll("div", {"class": "panel"})[0] #later i can make class searcher more robost.
    urls = []
    for link in page_soup.findAll('a'):
        temp = link.get('href')
        if(re.findall("^https",temp)):
         urls.append(temp)

    return urls

def getLyrics(url):
    page_soup = webScrapper(url)
    container = page_soup.findAll("div",{"class": "col-xs-12 col-lg-8 text-center"})
    innerContainer = container[0].findAll("div")
    lyrics = innerContainer[6].get_text()

    return lyrics


print("welcome To LyricsDownloader By Akshit Goel :")
flag = False
try:
    textualQuery = speechToText()
    searchQuery = createSearchQuery(textualQuery)
    wholePage = webScrapper(searchQuery)
    # print(wholePage.prettify())
    urls_list = urlScrapper(wholePage)
    print(urls_list[0])
    lyrics = getLyrics(urls_list[0])
    flag =True
except:
    print("Sorry No Result Found For Your Query")

if flag:
    print(lyrics)
    print("===================================================")
    flag = input("Want to save your file: [y/n] :")
    if flag=='y':
        name = input("input name for your file :")
        f = open(name+".txt","w+")
        f.write(lyrics)
        f.close




