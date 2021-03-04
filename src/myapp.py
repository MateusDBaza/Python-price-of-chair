import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-isaac-ergonomic-office-chair-black/p3575108")
content = request.content 


soup = BeautifulSoup(content,"html.parser")
element = soup.find("p", {"class": "price price--large"})
# < p class ="price price--large" > £279.00 < / p >
string_price = element.text.strip()# "£279.00"
price_without_string = string_price[1:] 
price = float(price_without_string)
if price < 299:
    print("Buy the chair!")
    print("The current price is {}".format(string_price))
elif price == 279:
    print("You can check other places")
else:
    print("It's too spensive, don't buy!")


