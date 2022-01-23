import json
import traceback
from aiohttp import http
import requests
import time
import random
import threading
import websocket
from websocket import WebSocketConnectionClosedException,WebSocketBadStatusException
from ssl import SSLCertVerificationError, SSLEOFError
from python_socks import ProxyConnectionError,ProxyTimeoutError,ProxyError
headers = {
    'authority': 'public.freeproxyapi.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'accept': 'application/octet-stream',
    'dnt': '1',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://freeproxyapi.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://freeproxyapi.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
}

data = '{"types":[],"levels":[],"countries":[],"type":"json","resultModel":"Mini"}'

response = requests.post('https://public.freeproxyapi.com/api/Download/Json', headers=headers, data=data)

channel = ''
nick = ['']
test_mode = True

def change_color():
    colors = ['red','yellow','blue','green','white','black','pink','purple','grey','cyan','camel','beige']
    return random.choice(colors)

def getDictKey_1(myDict, value):
    if value in myDict['socks4']:
        return 'socks4'
    if value in myDict['socks5']:
        return 'socks5'
    # if value in myDict['https']:
    #     return 'https'

def fuck():
    global api,channel,nick
    def shit():
        global i,proxy_dict
        try:
            ip = proxy_list.pop()
            ws = websocket.WebSocket()
            ws.connect('ws://146.56.135.157:6060',
                http_proxy_host=ip.split(':')[0], 
                http_proxy_port=ip.split(':')[1], 
                proxy_type=getDictKey_1(proxy_dict,ip))
            req = json.dumps({"cmd": "join", "channel": channel, "nick": '___' + ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 18)) + '___',
                                "password": '123456',})
            ws.send(req)
            time.sleep(0.5)
            ws.send(json.dumps({ 'cmd': 'changecolor', 'color': ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'],6))}))
            while True:
                if nick != ['']:
                    ws.send(json.dumps({'cmd': 'whisper', 'nick': random.choice(nick), "text": 
                    random.choices([
                                '$$\Huge\color{green}\colorbox{red}{傻}\Huge\color{red}\colorbox{green}{逼}\Huge\color{green}\colorbox{red}{傻}\Huge\color{red}\colorbox{green}{逼}$$',
                                '$$\Huge\color{red}\colorbox{green}{█▌▐█▌ ▐▀▀▄ ▄█▀▀█ ██▪ █▌▐█▌██ ▄▄▐▀▀▄█▌▐█▌ ▐▀▀▄ ▄█▀▀█ ██▪ █▌▐█▌██ ▄▄▐▀▀▄█▌▐█▌ ▐▀▀▄ ▄█▀▀█ ██▪ █▌▐█▌██ ▄▄▐▀▀▄█▌▐█▌ ▐▀▀▄ }$$',
                                '$$\Huge\color{red}\colorbox{green}{°▽°}\Huge\color{green}\colorbox{red}{°O°}\Huge\color{red}\colorbox{green}{°▽°}\Huge\color{green}\colorbox{red}{°O°}$$',
                                ],weights=[0,1,0])[0]}))
                    time.sleep(5)
                else:
                    ws.send(json.dumps({'cmd': 'chat', "text": 
                    random.choices([
                                '$$\Huge\color{green}\colorbox{red}{傻}\Huge\color{red}\colorbox{green}{逼}\Huge\color{green}\colorbox{red}{傻}\Huge\color{red}\colorbox{green}{逼}$$',
                                '$$\Huge\color{red}\colorbox{green}{█▌▐█▌ ▐▀▀▄ ▄█▀▀█ ██▪ █▌▐█▌██ ▄▄▐▀▀▄█▌▐█▌ ▐▀▀▄ ▄█▀▀█ ██▪ █▌▐█▌██ ▄▄▐▀▀▄█▌▐█▌ ▐▀▀▄ ▄█▀▀█ ██▪ █▌▐█▌██ ▄▄▐▀▀▄█▌▐█▌ ▐▀▀▄ }$$',
                                '$$\Huge\color{red}\colorbox{green}{°▽°}\Huge\color{green}\colorbox{red}{°O°}\Huge\color{red}\colorbox{green}{°▽°}\Huge\color{green}\colorbox{red}{°O°}$$',
                                ],weights=[0,1,0])[0]}))
                    time.sleep(5)
        except (ProxyConnectionError,ProxyTimeoutError,ProxyError,SSLEOFError,SSLCertVerificationError,ValueError,WebSocketBadStatusException,WebSocketConnectionClosedException,ConnectionResetError,ConnectionRefusedError):
            i = 0
            return
        except BrokenPipeError:
            i = 1
            return
    while True:
        shit()
        if i == 0:break
        time.sleep(3)

# def get_zuan():
#     url = random.choice(['https://api.shadiao.app/nmsl?level=min','https://api.shadiao.app/nmsl?level=max'])
#     text = requests.get(url,timeout=5).text
#     return json.loads(text)["data"]["text"]

def main():
    global proxy_list,proxy_dict,thread_count,success_count
    thread_list = []
    thread_count = 0
    success_count = 0
    proxy_lst = []
    lst = []

    def getproxy():
        d = {'Socks4':[],'Socks5':[],'Https':[]}
        response = json.loads(requests.post('https://public.freeproxyapi.com/api/Download/Json', headers=headers, data=data).text)
        for w in response:
            if w['Type'] in ['Socks4','Socks5','Https']:
                proxyip = w['Host'] + ':' + str(w['Port'])
                d[w['Type']].append(proxyip)
        return d
        
    m = getproxy()
    socks4_list1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
    socks4_list2 = requests.get('https://www.proxyscan.io/download?type=socks4').text.split('\n')
    socks4_list3 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4').text.split('\r\n')
    socks4_list4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text.split('\n')
#     socks4_list5 = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt').text.split('\n')
    socks4_list6 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt').text.split('\n')
    socks4_list7 = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt').text.split('\n')
    socks4_list8 = m['Socks4']
    socks4_list = list(set(socks4_list1 + socks4_list2 + socks4_list3 + socks4_list4 + socks4_list6 + socks4_list7 + socks4_list8))
    print(len(socks4_list))

    socks5_list1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
    socks5_list2 = requests.get('https://www.proxyscan.io/download?type=socks5').text.split('\n')
    socks5_list3 = requests.get('https://www.proxy-list.download/api/v1/get?type=socks5').text.split('\r\n')
    socks5_list4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text.split('\n')
    socks5_list5 = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt').text.split('\n')
    socks5_list6 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt').text.split('\n')
    socks5_list7 = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt').text.split('\n')
    socks5_list8 = m['Socks5']
    socks5_list = list(set(socks5_list1 + socks5_list2 + socks5_list3 + socks5_list4 + socks5_list5 + socks5_list6 + socks5_list7 + socks5_list8))
    print(len(socks5_list))

#     https_list1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
#     https_list2 = requests.get('https://www.proxyscan.io/download?type=https').text.split('\n')
#     https_list3 = requests.get('https://www.proxy-list.download/api/v1/get?type=https').text.split('\r\n')
# #    https_list4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text.split('\n')
#     https_list5 = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt').text.split('\n')
#     https_list6 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt').text.split('\n')
#     https_list7 = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/https.txt').text.split('\n')
#     https_list8 = m['Https']
#     https_list = list(set(https_list1 + https_list2 + https_list3 + https_list5 + https_list6 + https_list7 + https_list8))
#     print(len(https_list))

    proxy_dict = {'socks4':socks4_list,'socks5':socks5_list, }#'https':https_list}
    proxy_list = socks4_list + socks5_list # + https_list
    print(len(proxy_list))
    print(proxy_list[:10])
    print(proxy_list[-10:])
    
    def test():
        try:
            global thread_count,success_count
            ipp = proxy_list.pop()
            if ipp != '':
                ws = websocket.WebSocket()
                ws.connect('wss://hack.chat/chat-ws',
                    http_proxy_host=ipp.split(':')[0], 
                    http_proxy_port=ipp.split(':')[1], 
                    proxy_type=getDictKey_1(proxy_dict,ipp))
                ws.close()
                lst.append(ipp)
                thread_count -= 1
                success_count += 1
            else:
                thread_count -= 1

        except:
            thread_count -= 1
            pass
    

    if test_mode == True:
        for i in range(len(proxy_list)):
            t = threading.Thread(target=test)
            t.start()
            thread_list.append(t)
        for t in thread_list:
            thread_count += 1
            t.join()      
    else:
        for p in range(len(proxy_list)):
            t = threading.Thread(target=fuck)
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()

    if thread_count == 0:
        print(len(lst))
if __name__ == '__main__':
    main()
