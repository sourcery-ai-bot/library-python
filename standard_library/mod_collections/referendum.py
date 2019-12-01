""" Uses a more complex defaultdict example """

from collections import defaultdict
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

ALPHABET = 'a'
BASE_URL = 'https://www.bbc.co.uk/news/politics/eu_referendum/results/local/'
results = defaultdict(list)
leave_votes, remain_votes = 0, 0

for letter in ALPHABET:
    page_response = requests.get(f"{BASE_URL}{letter}", timeout=5)
    print(f"{BASE_URL}{letter}{': '}{page_response.status_code}")
    if page_response:
        page_content = BeautifulSoup(page_response.content, "html.parser")
        areas = page_content.find_all('div', attrs={'class': 'eu-ref-result-bar'})
        for area in areas:
            results['area_name'].append(area.find('h3').getText())
            results['leave_votes'].append(area.find_all('div',
                {'class': 'eu-ref-result-bar__votes'})
                [0].string.strip().split('\n')[0].strip()
            )
            results['remain_votes'].append(area.find_all('div',
                {'class': 'eu-ref-result-bar__votes'})
                [1].string.strip().split('\n')[0].strip()
            )
            results['turnout'].append(area.find(
                'div', {'class': 'eu-ref-result-bar__turnout'})
                .getText().replace('Turnout: ', '')
            )
            leave_votes = sum(Decimal(num.replace(',', '')) for num in results['leave_votes'])
            remain_votes = sum(Decimal(num.replace(',', '')) for num in results['remain_votes'])
    else:
        continue

print(results)
print(f"{leave_votes:,}, {remain_votes:,}")
