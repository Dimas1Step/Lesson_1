import sqlite3
from bs4 import BeautifulSoup
import requests

def create_db():
    connection = sqlite3.connect('wiki.db', 5)
    cursor = connection.cursor()
    print(connection)

    cursor.execute(
        'Create table website table (name TXT)'
    )
    connection.commit()
    connection.close()

def add_site(url):
    connection = sqlite3.connect('wiki.db', 5)
    cursor = connection.cursor()
    connection.execute('insert into sites (url) Values (?)', (url,))
    connection.commit()
    connection.close()

def clear_db():
    connection = sqlite3.connect('wiki.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM SITE')
    sites = cursor.fetchall()
    connection.close()
    return [site[0] for site in sites]

def search(query):
    sites = get_sites()
    search_results = []
    for site in sites:
        frequency = count_occurrences(site, query)
        search_results.append((site, frequency))

    