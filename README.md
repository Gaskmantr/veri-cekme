# IMDb Top 250 Veri Çekme
IMDb Top 250 listesinden verilen rating üzerindeki filmleri listeler. Yapılan hiç bir şeyden sorumlu değilim 

## Gerekli Paketler
* `requests` - Web sayfasına istek göndermek için
* `bs4` - Web sayfasındaki verileri seçmek için

## Kullanım
1. Gerekli paketleri kur

```
pip install requests bs4
```
2. Çalıştır

Rating parametresi komut satırından ya da program çalışırken girilebilir.
```
python imdb.py [rating]
  ```

### Örnek kullanım:

```
$ python imdb.py 
Raitingi giriniz:9
Filmin ismi: 1.      Esaretin Bedeli(1994) Filmin ratingi: 9.2 
Filmin ismi: 2.      Godfather(1972) Filmin ratingi: 9.1 
$ python imdb.py 9
Filmin ismi: 1.      Esaretin Bedeli(1994) Filmin ratingi: 9.2 
Filmin ismi: 2.      Godfather(1972) Filmin ratingi: 9.1 
```
