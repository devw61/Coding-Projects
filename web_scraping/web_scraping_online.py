from bs4 import BeautifulSoup
import requests
import datetime

while True:
    try:
        year = int(input("Enter the year: "))
        if year < 1950 or year > datetime.datetime.now().year:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid year between 1950 and 2024")

# get driver info 
website_request = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html').text 
_soup = BeautifulSoup(website_request, 'html.parser')
info = _soup.find_all('p', class_ = "f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px")
length = len(info)//5

#printing template
def print_result(): 
    max_name = max_org = 0
    for i in range(length):
        name = info[i*5+1].text[:-3]
        org = info[i*5+3].text
        if len(name) > max_name: max_name = len(name)
        if len(org) > max_org: max_org = len(org)
    
    for i in range(length):
        name = info[i*5+1].text[:-3]
        point = info[i*5+4].text
        org = info[i*5+3].text
        print(f"NAME: {name:<{max_name}} | ORG: {org:<{max_org}} | POINTS: {point}")

print_result()