import requests 
from bs4 import BeautifulSoup
# Here,we're just importing both Beautiful Soup and the Requests library
res = requests.get('https://guidestarindia.org/List_of_NGOs.aspx')
#its a url that  I already determined is safe and legal to scrape from.
html_text = res.text
# Here we are taking the entire  text from the web page 
soup = BeautifulSoup(html_text,'html.parser')
# I use  the html parses to parse the url content and store it in a variable 
tablebody = soup.find('tbody')
# There I find table body in html
tablerow = tablebody.find_all('tr')
# Then I find the table row within the table body

print("--------List_of_NGOs---------")
for row in tablerow:
	cells = row.find_all('td')
	name = cells[0]
	gsn = cells[1]
	urls = cells[2]
	#I want to store the the data So,I loop throught the tablerow,and push them into a list
	ngo_names = name.text
	ngo_gsn = gsn.text
	ngo_url = urls.text
	#It writtens all the  contents such as names of  ngo and its gsn and the url under it

	print('------------------NGO--------------------')
	print('ngo_names: ',ngo_names)
	print('gsn:',ngo_gsn)
	print('urls:',ngo_url)
	#print function prints all the names of ngo,gsn and url under it 