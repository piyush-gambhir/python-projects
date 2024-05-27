# importing libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver







quit()
product_title = bs(requests.get(reviews_url).content, 'lxml').title.text.replace(
    'Amazon.in:Customer reviews: ', '')

# number_pages = page_count(reviews_url)
number_pages = 501
product_review_list = []

for i in range(298, number_pages + 1):
    if (i < 298):
        reviews_page_url = reviews_url + '?pageNumber={}'.format(i)
        print('Scraping page {} of {}'.format(i, number_pages))
        request = requests.get(reviews_page_url)
        # time.sleep(10)
        soup = bs(request.text, 'lxml')
        print(soup)
        for review in reviews:
            review_dict = {
                'Product Title': product_title,
                'Review Title': review.find('a', {'data-hook': 'review-title'}).text.strip(),
                'Rating': review.find('i', {'data-hook': 'review-star-rating'}).text,
                'Review Body': review.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
#                 print(review_dict)
            product_review_list.append(review_dict)
    else:
        reviews_page_url = reviews_url + '?pageNumber={}'.format(i)
        print('Scraping page {} of {}'.format(i, number_pages))
        request = requests.get(reviews_page_url)
        # time.sleep(10)
        soup = bs(request.text, 'lxml')
        reviews = soup.findAll('div', {'data-hook': 'review'})
        for review in reviews:
            review_dict = {
                'Product Title': product_title,
                'Review Title': review.find('span', {'data-hook': 'review-title'}).text.strip(),
                'Rating': review.find('i', {'data-hook': 'cmps-review-star-rating'}).text,
                'Review Body': review.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
#                 print(review_dict)
            product_review_list.append(review_dict)
return product_review_list
