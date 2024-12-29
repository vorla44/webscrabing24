#huom. tässä luetaan ladatulta sivulta, jos haluat ajankohtaisen tiedon , nettisivu pitää päivittää

import requests  #lukee sivun tekstinä
import selectorlib  # valitsee sivulta

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# headers lisätään, ellei scrape muuten toimi (kopioitiin UDEMYn ohjeista). Auttaa myös, jos sivu ei hyväksy scriptejä

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS) # headers jos tehtiin lisäys
    source = response.text   #lukee tekstin
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml") #Extractor on class, extract.yaml tehdään itse
    #extract.yaml ilmoittaa mitä kohtaa haetaan
    value = extractor.extract(source)["tours"] # key extract.yaml:ssä, voi olla mikä vaan
    return value

if __name__ == "__main__":
    #print(scrape(URL)) voi kokeilla ennen alla olevaa
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

