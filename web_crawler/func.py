import requests
from lxml import etree
from bs4 import BeautifulSoup

def gvm():
  url = "https://www.gvm.com.tw/category/money"

  headers = {
    'authority': 'www.gvm.com.tw',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '__lt__cid=26b73da8-3476-4f81-a28d-26e2951d0507; AviviD_uuid=3d65a30b-9cb6-4607-b350-280a775303ae; webuserid=a07d55b2-ecca-65d1-f32a-71c7dfd34068; AviviD_sw_version=1.0.868.210701; _fbp=fb.2.1659939297101.2085150820; _itg=m6v0kl06se3pa9k8tdc4nfnf2o; user_cookie=d9f6c1eb-1e6c-5661-93a1-bfaf0d82e87a; _tk_tags_frck=["tech","financial_innovation","financial_investment"]; _tk_tags_frck_pr={"tech":43,"financial_innovation":77,"financial_investment":0}; _ss_pp_id=0147408b37fa45e06931654531364932; AviviD_token_retake=0; AviviD_refresh_uuid_status=2; csrf_cookie_name=e8527e8cb6b4a69f0845bb984a1e4074; ci_session=fnro1rmro4bjfa2j3ilrioppn3ndjp2n; __lt__sid=9e735b18-d759d48b; _gid=GA1.3.1482054890.1660103968; _gac_UA-3027687-2=1.1660103968.Cj0KCQjw852XBhC6ARIsAJsFPN0CR_Jk4T0LQyKACHUyBolBqU_8v4LkfNtObgLSgM5fv-iOozoyufwaAvQWEALw_wcB; _gat=1; __gpi=UID=0000086309f3ec2b:T=1659939297:RT=1660103968:S=ALNI_MahxIADdhreXAukkrbUzp_Br7_lUw; _ga_KKZ7H0YQTB=GS1.1.1660103968.2.0.1660103968.60; _ga=GA1.1.1191973167.1659939296; __gads=ID=f17b8cf0c866388b:T=1659939297:S=ALNI_MaDXUKJKMJBMG7X-sIIJRSkqEFjFQ; _clck=f9mbnc|1|f3w|0; _td=e4070a6d-3dc1-40f6-8f65-c3b152b18d5a; _clsk=1wieka|1660103970211|1|1|e.clarity.ms/collect; AviviD_already_exist=1; AviviD_show_sub=1; csrf_cookie_name=e8527e8cb6b4a69f0845bb984a1e4074',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
  }

  response = requests.request("GET", url, headers=headers)

  content = response.content.decode()
  html = etree.HTML(content)
  #
  blocks = html.xpath('//*[@id="article_list"]/div[2]/div')

  res = []
  for block in blocks:
    res_dict = {}
    res_dict['title'] = block.xpath('./div[1]/a/@title')[0]
    res_dict['a_href'] = block.xpath('./div[1]/a/@href')[0]
    res_dict['img_src'] = block.xpath('./div[1]/a/img/@data-original')[0]
    res_dict['sub_text'] = block.xpath('./div[2]/a[2]/p/text()')[0]
    res.append(res_dict)
    break
  return res

def food():
  import requests

  url = "https://ihappy.tw/restaurant"

  host = "https://ihappy.tw"

  headers = {
    'authority': 'ihappy.tw',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_gid=GA1.2.1511205782.1660105834; _gat_gtag_UA_168934439_5=1; _ga_8ZZ0C3Y52B=GS1.1.1660105834.1.0.1660105834.60; _ga=GA1.1.481169533.1660105834; __gads=ID=92894a07fc3b0a29-229d75daf3d400c3:T=1660105834:RT=1660105834:S=ALNI_MbkPboVlpY5QlybKAyZeUFHuzakyA; __gpi=UID=00000875611cdcef:T=1660105834:RT=1660105834:S=ALNI_MZgmfqGUurTY5OOMHM1t2X5gM-KVw; _fbp=fb.1.1660105834586.160215769',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
  }

  response = requests.request("GET", url, headers=headers)

  # blocks = html.xpath('//div[@class="events"]')
  soup = BeautifulSoup(response.text, "html.parser")
  soup.encoding = 'utf-8'
  blocks = soup.find_all('div', class_="events")

  res = []
  counter = 0

  for block in blocks:
    if counter == 10:
      break
    res_dict = {}
    h2 = block.find('h2')
    a = h2.find('a')
    img = block.find('img')
    sub_text = block.find('div', class_="idescc")
    res_dict['title'] = h2.text
    res_dict['a_href'] = host + a['href']
    res_dict['img_src'] = host + img['src']
    res_dict['sub_text'] = sub_text.text
    res.append(res_dict)
    counter += 1

  return res

def travel():
  import requests

  url = "https://okgo.tw/discount_type.html?tp=A"
  host = "https://okgo.tw"


  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=rso0ioquanu13jjljyrfv52d; __AntiXsrfToken=90876a52953849cb93e37222a1c1102a; _ga=GA1.2.1335212486.1660191917; _gid=GA1.2.1556081774.1660191917; _gat=1; __gpi=UID=0000087c60ee5dd2:T=1660191917:RT=1660191917:S=ALNI_MbfNwiEkGbmZpbqh91HeE6k3XKjGA; __gads=ID=c95e5cc295128ce1-221782ff8ad500f3:T=1660191917:RT=1660191918:S=ALNI_MZKgFEzeggy37kCegMQY0EIZ0gIFw',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  soup = BeautifulSoup(response.text, "html.parser")
  soup.encoding = 'utf-8'
  blocks = soup.find('div', class_="sec3").find_all('li')

  res = []
  counter = 0
  for block in blocks:
    if counter == 10:
      break
    res_dict = {}

    span = block.find('span', class_="td2")
    a = block.find('a')
    img = block.find('img')
    td4 = block.find('td', class_="td4")
    res_dict['title'] = span.text
    res_dict['a_href'] = host + '/' + a['href'].split('/')[1]
    if not 'http' in img['src']:
      res_dict['img_src'] = host + '/' + img['src'].replace('../', '')
    else:
      res_dict['img_src'] = img['src']
    res_dict['sub_text'] = td4.text
    res.append(res_dict)
    counter += 1
  return res

def long(city):
  url = f"https://www.104.com.tw/jobs/search/?keyword={city}工讀生"
  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__auc=dc9ef8181825d6a49384daa6b18; _gcl_au=1.1.1980393030.1659424623; luauid=31321061; bprofile_history=%5B%7B%22key%22%3A%221a2x6bj96b%22%2C%22custName%22%3A%22SHOPLINE%20Technology%20Corp.%2C%20L%22%7D%5D; cust_same_ab=1; lup=31321061.4702989186930.4623532291991.1.4640712161167; lunp=4623532291991; TS016ab800=01180e452dafb7bc8db5308eae5eb0552e24b1175096183e5e6b6d0f9a50d164aaa17958a1c0e049d8e2f6e628871603b88419e51c92c43283c6c7410920ed0cfdfa0f0ac7e942bb2e73d362e3a4dc5e65594a454e; ALGO_EXP_6019=B; ALGO_EXP_12509=E; __asc=33e2391b1828b1f723fd861f6df; _ga_WYQPBGBV8Z=GS1.1.1660191470.5.0.1660191470.60; _ga_FJWMQR9J2K=GS1.1.1660191470.5.0.1660191470.60; _ga_W9X1GB1SVR=GS1.1.1660191470.5.0.1660191470.60; _ga=GA1.3.986727618.1659424623; _gid=GA1.3.1379412925.1660191470; _dc_gtm_UA-15276226-1=1',
    'Referer': 'https://www.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  soup = BeautifulSoup(response.text, "html.parser")
  soup.encoding = 'utf-8'
  blocks = soup.find_all('article')

  res = []
  counter = 0

  for block in blocks:
    if counter == 10:
      break
    res_dict = {}
    a = block.find('a', class_="js-job-link")
    p = block.find('p', class_="job-list-item__info")
    try:
      res_dict['title'] = a.text
      res_dict['a_href'] = 'https://' + a['href'].replace('//', '')
      res_dict['sub_text'] = p.text
      res_dict['img_src'] = 'https://static.104.com.tw/104main/mobile/img/brand/app_icon.svg'
    except:
      pass
    res.append(res_dict)
    counter += 1
  return res

def short(city):
  url = f"https://www.104.com.tw/jobs/search/?keyword={city}兼職"
  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__auc=dc9ef8181825d6a49384daa6b18; _gcl_au=1.1.1980393030.1659424623; luauid=31321061; bprofile_history=%5B%7B%22key%22%3A%221a2x6bj96b%22%2C%22custName%22%3A%22SHOPLINE%20Technology%20Corp.%2C%20L%22%7D%5D; cust_same_ab=1; lup=31321061.4702989186930.4623532291991.1.4640712161167; lunp=4623532291991; TS016ab800=01180e452dafb7bc8db5308eae5eb0552e24b1175096183e5e6b6d0f9a50d164aaa17958a1c0e049d8e2f6e628871603b88419e51c92c43283c6c7410920ed0cfdfa0f0ac7e942bb2e73d362e3a4dc5e65594a454e; ALGO_EXP_6019=B; ALGO_EXP_12509=E; __asc=33e2391b1828b1f723fd861f6df; _ga_WYQPBGBV8Z=GS1.1.1660191470.5.0.1660191470.60; _ga_FJWMQR9J2K=GS1.1.1660191470.5.0.1660191470.60; _ga_W9X1GB1SVR=GS1.1.1660191470.5.0.1660191470.60; _ga=GA1.3.986727618.1659424623; _gid=GA1.3.1379412925.1660191470; _dc_gtm_UA-15276226-1=1',
    'Referer': 'https://www.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  soup = BeautifulSoup(response.text, "html.parser")
  soup.encoding = 'utf-8'
  blocks = soup.find_all('article')

  res = []
  counter = 0

  for block in blocks:
    if counter == 10:
      break
    res_dict = {}
    a = block.find('a', class_="js-job-link")
    p = block.find('p', class_="job-list-item__info")
    try:
      res_dict['title'] = a.text
      res_dict['a_href'] = 'https://' + a['href'].replace('//', '')
      res_dict['sub_text'] = p.text
      res_dict['img_src'] = 'https://static.104.com.tw/104main/mobile/img/brand/app_icon.svg'
    except:
      pass
    res.append(res_dict)
    counter += 1
  return res
