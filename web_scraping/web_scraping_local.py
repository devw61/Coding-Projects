from bs4 import BeautifulSoup

with open('web_scraping_web.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')
    course_cards = soup.find_all('div', class_='card') #need the underscore
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}') #remember f strings so you can inpliment variables