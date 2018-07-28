import requests
from bs4 import BeautifulSoup

req = requests.get("http://selfcare.jtl.co.ke/")
page = BeautifulSoup(req.text, "html5lib")
data = page.find_all('td')[-3:]

print(r'Hey \n new line')

exp_date = data[0].get_text()
exp_date = ''.join(char for char in exp_date if char.isdigit())

print("You have {} remaining out of {}GB. Expiry date is {}".format(data[1].get_text(), exp_date ,data[2].get_text()))
