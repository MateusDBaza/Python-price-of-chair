import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-isaac-ergonomic-office-chair-black/p3575108")
content = request.content # variable for content of the page above

# chearch data using html.parser which is an build_in for html beautifulsoup content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("p", {"class": "price price--large"})# to find <p> tag which has atribute class="price price--large"
# < p class ="price price--large" > £279.00 < / p >
string_price = element.text.strip()# "£279.00"
price_without_string = string_price[1:] # will start from 279.0
price = float(price_without_string)
if price < 299:
    print("Buy the chair!")
    print("The current price is {}".format(string_price))
elif price == 279:
    print("You can check other places")
else:
    print("It's too spensive, don't buy!")
#print(element.text.strip())# strip() clean all the white space in the string

