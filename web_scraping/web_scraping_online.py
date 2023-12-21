from bs4 import BeautifulSoup
import requests


#get points info 
points_request = requests.get('https://www.formula1.com/en/results.html/2023/drivers.html').text #the website
points_soup = BeautifulSoup(points_request, 'lxml')
# first_names = points_soup.find_all('span', class_ = "hide-for-tablet")
last_names = points_soup.find_all('span', class_ = "hide-for-mobile")
points = points_soup.find_all('td', class_ = "dark bold")
orgs = points_soup.find_all('a', class_ = "grey semi-bold uppercase ArchiveLink")
length = len(orgs)   

#get date info
date_request = requests.get("https://www.formula1.com/en/latest/article.formula-1-update-on-the-2023-calendar.4pTQzihtKTiegogmNX5XrP.html").text
date_soup = BeautifulSoup(date_request, 'lxml')
date_date = date_soup.find_all('td', class_ = "center")
race_dates = []

#printing template
def print_result(length): # need to change if want input
    body = ""
    for i in range(length) :
        # first_name = first_names[i].text
        last_name = last_names[i].text
        point = points[i].text
        org = orgs[i].text.split(" ", 2)
        if len(org) > 1:
            org = org[0] + " " + org[1]
        else:
            org = org[0]

        body += (f"""NAME: {last_name} | ORG: {org} | POINTS: {point}
""")
        print(f"NAME: {last_name} | ORG: {org} | POINTS: {point}")
    return body

def month_to_num(date):
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }
    month = date.strip()[:3].lower()
    try:
        return months[month]
    except:
        return 0


for i in range(3,len(date_date) - 3,3):
    race_dates += date_date[i].text.split(" ")
    
# user error possibilities / run
while 1:
    user_input_length = input("how many places do you want to see(enter=all): ")    
    if user_input_length == '':
        print_result(length)
        quit()
    elif int(user_input_length) > length :
        print(f"max length is {length}, try again")
        user_input_length
    elif int(user_input_length) <= 0 :
        print("must be positive number")
        user_input_length
    else :
        length = int(user_input_length)
        print_result(length)
        quit()