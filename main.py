from bs4 import BeautifulSoup as b
import requests
from openpyxl import *


def parse_quotes():
    data = []
    page_number = 1
    
    while True:
        
        url = f'https://quotes.toscrape.com/page/{page_number}/'
        response = requests.get(url)
     
        soup = b(response.text, 'html.parser')
        quotes_blocks = soup.find_all('div', class_='quote')
    
        if not quotes_blocks:
            break
    
        for block in quotes_blocks:
            text = block.find('span', class_='text').get_text(strip=True)
            author = soup.find('small', class_='author').get_text(strip=True)
            
            data.append({
                'quote': text,
                'author': author
            })
        
        page_number += 1
    
    return data


    
if __name__ == '__main__':
    quotes_data = parse_quotes()
    workbook = Workbook()
    worksheet = workbook.active
    worksheet["A1"] = "Author"
    worksheet['B1'] = "Quote"
    for item in quotes_data:
        worksheet.append([
            item['author'],
            item['quote']
        ])
        
    
    workbook.save('result.xlsx')