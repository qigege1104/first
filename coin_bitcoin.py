import urllib.request
import urllib.parse
import urllib.error
import json
import jsonpath
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://block.cc/api/v1/coin/tickers?coin=bitcoin&exchange=&symbol=&page=0&size=100'
#url = 'https://block.cc/api/v1/coin/tickers?coin=bitcoin&exchange=&symbol=$page=0$size=100'
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request)
hjson = response.read().decode('utf-8')
print(hjson)
unicodestr = json.loads(hjson)#把JSON形式的字符串转换成python形式的Unicode字符串
#print(unicodestr)
# print (unicodestr.keys())
# print(unicodestr['code'])
# print(unicodestr['message'])
# print(unicodestr['data'])
#print(unicodestr['data']['tickers'])
lists = unicodestr['data']['tickers']
#print(lists)
mum = len(lists)
print(mum)
for list in lists:
    print( '交易所：',list['exchange_display_name'])
    print('交易量：',list['volume'])
    print('交易量（%）：','%.3f' %(list['percent']))
    print('----------------------------------------')
print(mum)
