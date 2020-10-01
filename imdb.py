import sys
import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"
response = requests.get(url)

html = response.content

soup = BeautifulSoup(html,"html.parser")

if len(sys.argv) > 1:
    min_rating = float(sys.argv[1]) 
else:
    min_rating = float(input("Raitingi giriniz:"))

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler =  soup.find_all("td",{"class":"ratingColumn imdbRating"})

for baslik,rating in zip(basliklar,ratingler):

    baslik=baslik.text
    rating=rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if (float(rating) > min_rating):
        print("Filmin ismi: {} Filmin ratingi: {} ".format(baslik,rating))