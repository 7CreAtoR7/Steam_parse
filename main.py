import requests
from bs4 import BeautifulSoup

# this code parses HTML Tags from Steam
# you can put it in a HTML IDE and see the result
link = input('Insert game link: ')  # remember to remove the first 2 lines before pasting the html code


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    return r.text


def get_link(html):
    a = []
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('div', class_='apphub_AppName')
    photo = soup.find_all('a', attrs={"class": "highlight_screenshot_link", "href": True})
    logo = soup.find('div',
                     class_='game_header_image_ctn')
    description = soup.find('div', class_="game_description_snippet")
    rating_div = soup.find('span', class_='game_review_summary positive')
    rating_div.string.replace_with('Customer reviews: ' + rating_div.string)
    genre = soup.find('div', class_='glance_tags popular_tags').find_all('a', class_='app_tag')

    linkk = link

    price = soup.find('div', class_='discount_original_price')
    if price is None:
        price = soup.find('div', class_='game_purchase_price price')
    game_info = soup.find('div', id='game_area_description')
    system = soup.find('div', class_='game_area_sys_req_leftCol')
    metacritic = soup.find('div', class_='score high')
    if metacritic is None:
        metacritic = ''
    age = soup.find('div', class_='shared_game_rating')
    if age is None:
        age = ''

    print()
    for n in name:
        print('<span style="font-size: 18pt;"><strong>' + n + '</strong></span>')

    print(logo)
    for p in price:
        print(
            '<div class="discount_original_price" style="font-size: 18pt;"><strong>Price in Steam: </strong>' + '<span style="color: #ff0000;"><strong>' + p + '</strong></div>')
    print('<p><a href="' + linkk + '">' + linkk + '</a></p>' + '<br>')
    for rat in rating_div:
        b = rat.split(':')
    print('<span class="game_review_summary positive"><strong>' + b[0] + ':' + '</strong>' + str(
        b[1]) + '</span>' + '<br>')

    for i in metacritic:
        print('<span><strong>Rating on Metacritic:</strong> ' + i.strip() + '</span>' + '<br>')
    for w in genre:
        a.append(w.text.strip())
    print('<span><strong>Genre: </strong>', end='')
    for ress in a:
        print(ress + ', ', end='')
    print('</span>' + '<br>' + '<br>')

    for o in description:
        print('<strong>' + o + '</strong><br>')

    for item in photo:
        print('<img src="' + item['href'] + '" alt="" width="300" height="225" />\n')

    for g in game_info:
        print('<strong>' + str(g) + '</strong>')

    print(system)
    print(age)


get_link(get_html(str(link)))
