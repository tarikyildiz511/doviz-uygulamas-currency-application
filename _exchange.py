import requests
import json


api_url = "https://api.exchangeratesapi.io/latest?base="



bozulan_doviz = input("bozulan döviz türü:")
alinan_doviz = input("alinan doviz turu :")
miktar =int(input(f"ne kadar{bozulan_doviz}bozdurmak istiyorsunuz"))

x = requests.get(api_url+bozulan_doviz)

x = json.loads(x.text)
print("1{0}={1}{2}".format(bozulan_doviz,x["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*x["rates"][alinan_doviz],alinan_doviz))







