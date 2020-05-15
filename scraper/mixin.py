import requests
from bs4 import BeautifulSoup


def get_websites_data(threshold=None, page=None):
    page = requests.get('https://websites.co.in/sitemap?page=%s'%str(page))
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup)
    data = []
    table = soup.find('table', attrs={'class': 'table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')

    th = table.find_all('th')
    th = [ele.text.strip() for ele in th]

    for row in rows[0:threshold]:
        cols = row.find_all('td')

        url = "https:" + row.find_all('td')[0].find('a').get("href")
        category = row.find_all('td')[1].contents[0]
        city = row.find_all('td')[2].contents[0]

        output = scrape_url(url)

        data.append({"url":url, "category": category, "city": city, "data": output})

    return data


def scrape_url(url=None):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')

    text = soup.find_all(text=True)

    set([t.parent.name for t in text])

    """{'label', 'h4', 'ol', '[document]', 'a', 'h1', 'noscript', 'span', 'header', 'ul', 'html',
        'section', 'article', 'em', 'meta', 'title', 'body', 'aside', 'footer', 'div', 'form', 'nav', 'p', 'head',
        'link', 'strong', 'h6', 'br', 'li', 'h3', 'h5', 'input', 'blockquote', 'main', 'script', 'figure'}"""

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    return output.replace("\n","")