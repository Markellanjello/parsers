import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
url = ("http://www.yaroslavl.vybory.izbirkom.ru/region/region/yaroslavl?action=show&root=1&tvd=27620001114195&vrn"
				"=27620001114190&region=76&global=&sub_region=76&prver=0&pronetvd=0&cuiknum=null&type=220")
response = requests.get(url, headers=headers)
html_content = BeautifulSoup(response.text, "html.parser")
# print(html_content)
def get_head():
	head = html_content.find_all("th", class_="text-center")
	for z in range(0, len(head), 8):
		head_text = [(head[z + y].text).replace("	", "").replace("\n", "").replace("\r", "") for y in range(8)]
		yield head_text