from typing import Any

import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36"}
url = "http://www.altai-rep.vybory.izbirkom.ru/region/region/altai-rep?action=show&root=0&tvd=4044008246253&vrn=4044008246249&region=2&global=&sub_region=2&prver=0&pronetvd=null&vibid=4044008246249&type=221"
response = requests.get(url, headers=headers)
html_content = BeautifulSoup(response.text, "html.parser")
print(html_content)
block = html_content.find("table", class_="candidates-221-2")
data = block.find_all("td")
head = block.find_all("th")
z = []
for i in head:
	z.append(i.text.replace("	", "").replace("\n", "").replace("\r", ""))
z.pop(-4)
l = 7
print(z, len(z))
for i in data:
	z = i.text
for z in range(0, len(data), l):
	print([data[z + y].text for y in range(l)])
# delete = html_content.find("th", class_="text-center")
# l = len(head) - 1
# for m in head:
# 	q = m.text
# 	print(q)
# for i in data:
# 	z = i.text
# for z in range(0, len(data), l):
# 	print([data[z + y].text for y in range(l)])
