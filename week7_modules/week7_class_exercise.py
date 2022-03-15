import bs4
import os
import sys
import requests
import shutil
import re
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


if __name__ == '__main__':

    req = Request("https://www.cphbusiness.dk/")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    print(links)


   