# PROJECT TO SCRAPE BOOKS HAVING A 3 STAR RATING

import requests
import bs4
# URL OF FORMAT  https://books.toscrape.com/catalogue/page-1.html
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# go through page 1 to 50

#res = requests.get(base_url.format('1'))

# make soup
#soup = bs4.BeautifulSoup(res.text,'lxml')
#grab the product info of books on url
#grab_page1 =soup.select(".product_pod")


#function to grab title of 3 star
def title_grab(page_grab):

	for book in page_grab:
		rating_check = book.select(".star-rating.Three")
		if rating_check:
			print(book.select('a')[1]['title'])
			#for item in book.select('a'):
			#
			#		print(item['title'])
			#	except:
			#		pass

		
if __name__ == '__main__':
	#
	page_num = 1
	while page_num <=50:

		res = requests.get(base_url.format(page_num))
		soup = bs4.BeautifulSoup(res.text,'lxml')
		grab_page1 =soup.select(".product_pod")
		title_grab(grab_page1)####	NEED TO ADJUST LOOP VARIABLE
		page_num+=1