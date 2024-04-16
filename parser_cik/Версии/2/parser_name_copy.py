from typing import Any

import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36"}
url = input("URL : ")
response = requests.get(url, headers=headers)
html_content = BeautifulSoup(response.text, "html.parser")

head = ["№ п/п", "ФИО кандидата", "Дата рождения кандидата", "Субьект выдвижения", "Номер округа", "Выдвижение",	"Регистрация", "Избрание"]
lens = html_content.find_all("a", class_="page-link")
x = 0
for i in lens:
  x += 1
def get_data():
	for count in range(x + 2):
		sleep(5)
		url_local = url + f"&number={count}"
		response = requests.get(url_local, headers=headers)
		html_content = BeautifulSoup(response.text, "html.parser")
		block = html_content.find("div", class_="table-responsive")
		data = block.find_all("td")
		for i in data:
			z = i.text
		for z in range(0, len(data), 9):
			yield [data[z + y].text for y in range(9)]

