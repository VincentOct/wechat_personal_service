import requests
from bs4 import BeautifulSoup

# obj_bookname = '了不起的盖茨比'
# obj_bookname = input('Enter a bookname.\n')
checkout_status = ['可借', ]
bookbase_status = ['学府城书库', '东校区中文图书库', '南山书院书库', '草堂移动书库']

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'catalog.lib.xauat.edu.cn',
    'Referer': 'http://catalog.lib.xauat.edu.cn/opac/search.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
                  '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

url = 'http://catalog.lib.xauat.edu.cn/opac/openlink.php'


def get_book_index(bookname):
    data = {
        'strSearchType': 'title',
        'match_flag': 'forward',
        'historyCount': '1',
        'strText': bookname,
        'doctype': 'ALL',
        'with_ebook': 'on',
        'displaypg': '20',
        'showmode': 'list',
        'sort': 'CATA_DATE',
        'orderby': 'desc',
        'location': 'ALL',
    }
    try:
        response = requests.get(url, headers=headers, params=data, timeout=30)
        response.raise_for_status()
        response.encoding = 'uft-8'
        return response.text
    except requests.RequestException as e:
        print('Something Wrong Happended.')
        print(e)
        return None


def parse_html(_html):
    if _html:
        soup = BeautifulSoup(_html, 'lxml')
        books = soup.select('#search_book_list li')
        book_result = []
        for book in books:
            book_info = {
                'title': book.select_one('h3 a').string,
                'url_number': book.select_one('h3 a').attrs['href'][-10:]
            }
            book_result.append(book_info)
        return book_result


def get_book_detail(book_info):
    ajax_url = 'http://catalog.lib.xauat.edu.cn/opac/ajax_item.php?marc_no={}'.format(book_info['url_number'])
    try:
        response = requests.get(ajax_url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = 'uft-8'
        soup = BeautifulSoup(response.text, 'lxml')
        book_trs = soup.select('tr.whitetext')
        book_info['status'] = []
        for book_tr in book_trs:
            if book_tr.contents[9].get_text(strip=True) in checkout_status:
                if book_tr.contents[7].get_text(strip=True) not in bookbase_status:
                    book_info['status'].append(book_tr.get_text('||', strip=True))
        return book_info
    except requests.RequestException as e:
        print('Something Wrong Happended.')
        print(e)
        return None


def add_book_status(info_list):
    if info_list:
        for i in range(len(info_list)):
            info_list[i] = get_book_detail(info_list[i])
        return info_list


def result_to_string(aresult):
    result_string = []
    none_status_book = 0
    for i in range(len(aresult)):
        item = aresult[i]
        if item['status']:
            status = '\n'.join(item['status']) + '\n--------------'
            single_string = '[Bookname]: {name}\n[Unique number]: {uni_number}\n[Book status]:\n{status}' \
                .format(name=item['title'], uni_number=item['url_number'], status=status)
            result_string.append(single_string)
        else:
            none_status_book += 1
    content_1 = '\n'.join(result_string)
    content_2 = '\nAnd there are {} book(s) have no status information.'.format(none_status_book)
    content_0 = content_1 + content_2 if content_2 else content_1
    return content_0


def book_main(abookname):
    html = get_book_index(abookname)
    raw_result = parse_html(html)
    result = add_book_status(raw_result)
    final_string = result_to_string(result)
    print(final_string[:450] + '...\n......')
    # send_bh_email(subject='[Vincent][{}]'.format(obj_bookname), content=final_string)
    return final_string

