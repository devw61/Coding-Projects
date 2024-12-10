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
        print(f"Please enter a valid year between 1950 and {datetime.datetime.now().year}")

# get driver info 
website_request = requests.get(f'https://www.formula1.com/en/results.html/{year}/drivers.html').text 
_soup = BeautifulSoup(website_request, 'html.parser')
info = _soup.find_all('p', class_ = "f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-none f1-text__micro text-fs-15px")
length = len(info)//5

if length == 0 and year == datetime.datetime.now().year:
    print(f"The {datetime.datetime.now().year} season has not started yet.")
    exit()
elif length == 0:
    print(f"No results found for {year}.")
    exit()

#printing template
def print_result(): 
    names = [info[i*5+1].text[:-3] for i in range(length)]
    orgs = [info[i*5+3].text for i in range(length)]
    max_name = max(len(name) for name in names)
    max_org = max(len(org) for org in orgs)
    
    for i in range(length):
        name = names[i]
        point = info[i*5+4].text
        org = orgs[i]
        print(f"NAME: {name:<{max_name}} | ORG: {org:<{max_org}} | POINTS: {point}")

print_result()