import requests
import  bs4



five_star_titles = []

for i in range(1,51):
    url = f'http://books.toscrape.com/catalogue/category/books_1/page-{i}.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
   
    for book in books:
        if len(book.select('.star-rating.Five')) != 0:
            book_title = book.select('a')[1]['title']
            five_star_titles.append(book_title)

print(five_star_titles)