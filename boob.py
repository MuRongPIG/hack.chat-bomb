import json
import requests
import time
import random
import threading
import websocket
from websocket import WebSocketConnectionClosedException,WebSocketBadStatusException
from ssl import SSLCertVerificationError, SSLEOFError
from python_socks import ProxyConnectionError,ProxyTimeoutError,ProxyError
channel = 'test'
nick = ['someone']
test_mode = True 

def change_color():
    colors = ['red','yellow','blue','green','white','black','pink','purple','grey','cyan','camel','beige']
    return random.choice(colors)

def fuck():
    global api,channel,nick
    def shit():
        global i
        try:
            ip = proxy_list.pop()
            ws = websocket.WebSocket()
            ws.connect('wss://hack.chat/chat-ws',
                http_proxy_host=ip.split(':')[0], 
                http_proxy_port=ip.split(':')[1], 
                proxy_type="socks4")
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
        except (ProxyConnectionError,ProxyTimeoutError,ProxyError,SSLEOFError,SSLCertVerificationError,ValueError,WebSocketBadStatusException,WebSocketConnectionClosedException):
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
    global proxy_list
    thread_list = []
    proxy_lst = []
    lst = []
    t1 = time.time()
    socks1_list = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
    socks2_list = requests.get('https://www.proxyscan.io/download?type=socks4').text.split('\n')
    socks3_list = requests.get('https://www.proxy-list.download/api/v1/get?type=socks4').text.split('\r\n')
    socks4_list = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text.split('\n')
    socks5_list = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt').text.split('\n')
    
    socks6_list = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt').text.split('\n')
    proxy_ist = list(set(socks1_list + socks2_list + socks3_list + socks4_list + socks5_list + socks6_list))
    response = json.loads(requests.post('https://public.freeproxyapi.com/api/Download/Json', headers=headers, data=data).text)
    print(len(response))
    for w in response:
        proxyip = w['Host'] + ':' + str(w['Port'])
        proxy_lst.append(proxyip)
    
    proxy_list = list(set(proxy_ist + proxy_lst))
    proxy_list.pop(-1)
    print(len(proxy_list))

    
    def test():
        try:
            ipp = proxy_list.pop()
            ws = websocket.WebSocket()
            ws.connect('wss://hack.chat/chat-ws',
                http_proxy_host=ipp.split(':')[0], 
                http_proxy_port=ipp.split(':')[1], 
                proxy_type="socks4")
            lst.append(ipp)
        except:
            pass
    

    if test_mode == True:
        for i in range(len(proxy_list)):
            t = threading.Thread(target=test)
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()      
    else:
        for p in range(len(proxy_list)):
            t = threading.Thread(target=fuck)
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()

    while True:
        if thread_list == []:
            print(len(lst))
if __name__ == '__main__':
    main()
