from bs4 import BeautifulSoup
import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


url = 'https://www.google.com/'

req = requests.get(url , headers)

soup = BeautifulSoup(req.content, 'html.parser')

print(soup.prettify())



# html_doc = """
#     <html><head><title>The Dormouse's story</title></head>
#     <body>
#     <p class="title"><b>The Dormouse's story</b></p>

#     <p class="story">Once upon a time there were three little sisters; and their names were
#     <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#     and they lived at the bottom of a well.</p>

#     <p class="story">...</p>
#     """

# soup = BeautifulSoup(html_doc , 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.name)
# print(soup.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.find_all('a'))
# print(soup.find(id="link3"))


# for link in soup.find_all('a'):
#     print(link.get('href'))
