# import urllib.request
#
# opener = urllib.request.build_opener()
# response = opener.open('https://httpbin.org/get')
# print(response.read())


import requests

# response = requests.get('https://httpbin.org/get')         ГІРШЕ
# print(response.text)

# response = requests.post('https://httpbin.org/post', data='Hello from Python', headers={'Title': 'Test title'})    КРАЩЕ
# print(response.text)

# response = requests.get('https://coinmarketcap.com/')
# text = response.text
# parse = text.split('<span>')
#
# result = []
#
# for item in parse:
#     if item.startswith('$'):
#         for value in item.split('</span>'):
#             if value.startswith('$') and value[1].isdigit():
#                 result.append(value)
#
# bitcoin = result[0]
# print(bitcoin)

from bs4 import BeautifulSoup

response = requests.get('https://coinmarketcap.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('table')
    for value in soup_list:
        all_td = value.find_all('td')
        print(all_td[3].find('span').text)