#!/usr/bin/python
# -*- coding: utf-8 -*-
# Useragent
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Useragent

import os, sys, time, random
from time import sleep
from requests import *
from bs4 import BeautifulSoup as bs

info = """
Nama        : Useragent
Versi       : 3.0 (Update: 12 Juli 2020, 1:00 AM)
Tanggal     : 01 Januari 2019
Author      : Nedi Senja
Tujuan      : Memilih agen pengguna
              menggunakan whatismybrowser
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;43;90;1m[          Useragent, My Github: @stepbystepexe          ]\033[0m"""

logo = """\033[0;36;3m░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[0;77;1m_______                __
\033[0;36;3m░░█░░░█░█▀▀▀▀░█▀▀▀▀░█▀▀▀▄░░\033[0;77;1m___/ _ |___ ____ ___  / /_
\033[0;36;3m░░█░░░█░▀▀▀▀█░█▀▀▀▀░█▀▀▀▄░░\033[0;77;1m__/ __ / _ `/ -_) _ \/ __/
\033[0;36;3m░░▀▀▀▀▀░▀▀▀▀▀░▀▀▀▀▀░▀░░░▀░░\033[0;77;1m_/_/ |_\_, /\__/_//_/\__/  _
\033[0;36;3m░░░░░░░░░░░░░░░░░░░░░░░░░░░      \033[0;77;1m/___/               (_)
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    o = [' .   ',' ..  ',' ... ']
    for i in o:
        print('\r\033[0m[\033[0;34m●\033[0m] Sedang menghubungkan'+i,end=''),;sys.stdout.flush();time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def pr():
        r = get('https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country=US').text
        return r.split()

def crawler():
        os.system('clear')
        os.system('clear')
        os.system('reset')
        sleep(1)
        print()
        print(logo)
        print(example)
        print()
        write("\033[0m[ \033[32mINFO \033[0m] \033[3mSaya tidak real kalo code program saya ini ditiru")
        write("         Seburuk apaun itu tolong hargai karya milik orang\033[0m\n\n")
        n = int(input('\033[0m[\033[41;77;1m Jumlah \033[0m] '))
        print()
        loads()
        prokk = pr()
        prok = random.choice(prokk)
        print(f'\n\033[0m[\033[92;1m#\033[0m] Terhubung ke proxy:\033[77;1m {prok}')
        sleep(3)
        userA = []
        try:
                        r = get('https://developers.whatismybrowser.com/useragents/explore/',proxies={'https':'https://'+prok}).text
                        b = bs(r,'html.parser')
                        for i in b.find('ul',{'id':'listing-by-field-name'}).find_all('ul'):
                                if len(userA) == n:
                                        break
                                else:
                                        for a in i.find_all('a'):
                                                if len(userA) == n:
                                                        break
                                                else:
                                                        url = 'https://developers.whatismybrowser.com'+a.get('href')
                                                        rr = get(url,proxies={'https':'https://'+prok}).text
                                                        bb = bs(rr,'html.parser')
                                                        for ua in bb.find_all('td',{'class','useragent'}):
                                                                if len(userA) == n:
                                                                        break
                                                                else:
                                                                        userA.append(ua.text)
                                                                        print('\rMengumpulkan: ',len(userA),end='',flush=True)
                                                                        time.sleep(0.01)
        except KeyboardInterrupt:
                pass
        except exceptions.ProxyError or exceptions.SSLError:
                print('\n\033[0m[\033[91;1m!\033[0m] \033[77;1mProxy Error, segarkan kembali\n')
                sys.exit(1)
        if len(userA) != 0:
                f = open('useragents.txt','w')
                for ua in userA:
                        f.write(ua+'\n')
                print(f'\n\Selesai {len(userA)} Agen pengguna tersimpan (useragents.txt)\n')
                sys.exit(1)

if __name__=='__main__':
        os.system('clear')
        os.system('clear')
        os.system('reset')
        sleep(1)
        print()
        print(logo)
        print(example)
        print()
        print("\033[0m[\033[96;2;1m1\033[0m] \033[1;77mPilih Agen Pengguna")
        print()
        print("\033[0m[\033[93;1m&\033[0m] LISENSI")
        print("\033[0m[\033[94;1m#\033[0m] Informasi")
        print("\033[0m[\033[92;1m*\033[0m] Perbarui")
        print("\033[0m[\033[91;1m-\033[0m] Keluar")
        print()
        option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
        if option.strip() in '1 pilih'.split():
            write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
            sleep(1)
            crawler()
        elif option.strip() in '& 2 lisensi'.split():
            print()
            os.system('nano LICENSE')
            print()
            restart()
        elif option.strip() in '# 3 info'.split():
            os.system('clear')
            print(example)
            os.system('toilet -f smslant User')
            print(info)
            sleep(1)
            print()
            input('[ Tekan Enter ]')
            restart()
        elif option.strip() in '* 4 perbarui'.split():
            print()
            os.system('git pull origin master')
            print()
            input('\033[0m[ \033[32mTekan Enter \033[0m]')
            restart()
        elif option.strip() in '- 0 keluar'.split():
            print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
            print()
            sys.exit(1)
        else:
            print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
            print()
            sleep(1)
            restart()