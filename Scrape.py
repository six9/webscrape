from bs4 import BeautifulSoup
import requests

thelink = 'http://mohe.gov.lk/index.php/en/scholaships/scholarships-for-local-students'
responce = requests.get(thelink)

responce.status_code
thecontent = BeautifulSoup(responce.content,"html.parser")

thecontent.find_all('strong',class_='scholaship')


