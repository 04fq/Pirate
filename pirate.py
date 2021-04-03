import requests
import urllib.request
from colorama import *
import random
import socket
import code_analysis as CA
from hashlib import *
from user_agent import generate_user_agent
import sys
import json
import threading
import time
from queue import Queue
import secrets
queue = Queue()
open_ports = []
r = requests.session()
print(Fore.LIGHTBLUE_EX + '''

  ██████╗ ██╗██████╗  █████╗ ████████╗███████╗   ██████╗ ██╗   ██╗    
  ██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝   ██╔══██╗╚██╗ ██╔╝    
  ██████╔╝██║██████╔╝███████║   ██║   █████╗     ██████╔╝ ╚████╔╝     
  ██╔═══╝ ██║██╔══██╗██╔══██║   ██║   ██╔══╝     ██╔═══╝   ╚██╔╝      
  ██║     ██║██║  ██║██║  ██║   ██║   ███████╗██╗██║        ██║       
  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝╚═╝        ╚═╝                                                                 
''')
print(Fore.MAGENTA + """
 [01] Password Compiling                      
 [02] Admin Panel BruteForce              
 [03] Hash Me
 [04] Site Cloner | Soon .....
 [05] Target IP Locator              
 [06] NumScan[@t8qu_] | Soon .....
 [07] Instagram Osint | Info       
 [08] Scan Web Exploit[PHP][@at9w]              
 [09] Port Scanner
 [10] Exit
""")
option = input(Fore.LIGHTYELLOW_EX + "[!] Select ? : ")
if option == '1':
    print(Fore.BLUE + '''
 [1] Random Passwords
 [2] Victim Information | Soon ......    
''')
    option1 = input(Fore.RED + "Select ? : ")
    if option1 == '1':
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"
        password_len = int(input(Fore.RED +"[?] Password Length : "))
        password_count = int(input(Fore.RED +"[?] Password Number : "))
        for x in range(0, password_count):
            password = ""
            for x in range(0, password_len):
                    password_char = random.choice(chars)
                    password = password + password_char
                    f = open("Password.txt", "a")
                    f.write(password + '\n')
                    f.close()

    elif option1 == '2':
        print(Fore.LIGHTBLUE_EX +"Soon")
elif option == '2':

    url = str(input("[?] Enter Website : "))
    if url.startswith('http'):
        url = url
    else:
        url = 'http://' + url
        if url.endswith('/'):
            url = url
        else:
            url = url + "/"

        # creat a list for all posiblity
    adminlist = [
            'admin/',
            'administrator/',
            'admin1/',
            'admin2/',
            'admin3/',
            'admin4/',
            'admin5/',
            'usuarios/',
            'usuario/',
            'administrator/',
            'moderator/',
            'webadmin/',
            'adminarea/',
            'bb-admin/',
            'adminLogin/',
            'admin_area/',
            'panel-administracion/',
            'instadmin/',
            'memberadmin/',
            'administratorlogin/',
            'adm/',
            'admin/account.php',
            'admin/index.php',
            'admin/login.php',
            'admin/admin.php',
            'admin/account.php',
            'admin_area/admin.php',
            'admin_area/login.php',
            'siteadmin/login.php',
            'siteadmin/index.php',
            'siteadmin/login.html',
            'admin/account.html',
            'admin/index.html',
            'admin/login.html',
            'admin/admin.html',
            'admin_area/index.php',
            'bb-admin/index.php',
            'bb-admin/login.php',
            'bb-admin/admin.php',
            'admin/home.php',
            'admin_area/login.html',
            'admin_area/index.html',
            'admin/controlpanel.php',
            'admin.php',
            'admincp/index.asp',
            'admincp/login.asp',
            'admincp/index.html',
            'admin/account.html',
            'adminpanel.html',
            'webadmin.html',
            'webadmin/index.html',
            'webadmin/admin.html',
            'webadmin/login.html',
            'admin/admin_login.html',
            'admin_login.html',
            'panel-administracion/login.html',
            'admin/cp.php',
            'cp.php',
            'administrator/index.php',
            'administrator/login.php',
            'nsw/admin/login.php',
            'webadmin/login.php',
            'admin/admin_login.php',
            'admin_login.php',
            'administrator/account.php',
            'administrator.php',
            'admin_area/admin.html',
            'pages/admin/admin-login.php',
            'admin/admin-login.php',
            'admin-login.php',
            'bb-admin/index.html',
            'bb-admin/login.html',
            'acceso.php',
            'bb-admin/admin.html',
            'admin/home.html',
            'login.php',
            'modelsearch/login.php',
            'moderator.php',
            'moderator/login.php',
            'moderator/admin.php',
            'account.php',
            'pages/admin/admin-login.html',
            'admin/admin-login.html',
            'admin-login.html',
            'controlpanel.php',
            'admincontrol.php',
            'admin/adminLogin.html',
            'adminLogin.html',
            'admin/adminLogin.html',
            'home.html',
            'rcjakar/admin/login.php',
            'adminarea/index.html',
            'adminarea/admin.html',
            'webadmin.php',
            'webadmin/index.php',
            'webadmin/admin.php',
            'admin/controlpanel.html',
            'admin.html',
            'admin/cp.html',
            'cp.html',
            'adminpanel.php',
            'moderator.html',
            'administrator/index.html',
            'administrator/login.html',
            'user.html',
            'administrator/account.html',
            'administrator.html',
            'login.html',
            'modelsearch/login.html',
            'moderator/login.html',
            'adminarea/login.html',
            'panel-administracion/index.html',
            'panel-administracion/admin.html',
            'modelsearch/index.html',
            'modelsearch/admin.html',
            'admincontrol/login.html',
            'adm/index.html',
            'adm.html',
            'moderator/admin.html',
            'user.php',
            'account.html',
            'controlpanel.html',
            'admincontrol.html',
            'panel-administracion/login.php',
            'wp-login.php',
            'adminLogin.php',
            'admin/adminLogin.php',
            'home.php',
            'admin.php',
            'adminarea/index.php',
            'adminarea/admin.php',
            'adminarea/login.php',
            'panel-administracion/index.php',
            'panel-administracion/admin.php',
            'modelsearch/index.php',
            'modelsearch/admin.php',
            'admincontrol/login.php',
            'adm/admloginuser.php',
            'admloginuser.php',
            'admin2.php',
            'admin2/login.php',
            'admin2/index.php',
            'usuarios/login.php',
            'adm/index.php',
            'adm.php',
            'affiliate.php',
            'adm_auth.php',
            'memberadmin.php',
            'administratorlogin.php',
            'admin/',
            'administrator/',
            'admin1/',
            'admin2/',
            'admin3/',
            'admin4/',
            'admin5/',
            'moderator/',
            'webadmin/',
            'adminarea/',
            'bb-admin/',
            'adminLogin/',
            'admin_area/',
            'panel-administracion/',
            'instadmin/',
            'memberadmin/',
            'administratorlogin/',
            'adm/',
            'account.asp',
            'admin/account.asp',
            'admin/index.asp',
            'admin/login.asp',
            'admin/admin.asp',
            'admin_area/admin.asp',
            'admin_area/login.asp',
            'admin/account.html',
            'admin/index.html',
            'admin/login.html',
            'admin/admin.html',
            'admin_area/admin.html',
            'admin_area/login.html',
            'admin_area/index.html',
            'admin_area/index.asp',
            'bb-admin/index.asp',
            'bb-admin/login.asp',
            'bb-admin/admin.asp',
            'bb-admin/index.html',
            'bb-admin/login.html',
            'bb-admin/admin.html',
            'admin/home.html',
            'admin/controlpanel.html',
            'admin.html',
            'admin/cp.html',
            'cp.html',
            'administrator/index.html',
            'administrator/login.html',
            'administrator/account.html',
            'administrator.html',
            'login.html',
            'modelsearch/login.html',
            'moderator.html',
            'moderator/login.html',
            'moderator/admin.html',
            'account.html',
            'controlpanel.html',
            'admincontrol.html',
            'admin_login.html',
            'panel-administracion/login.html',
            'admin/home.asp',
            'admin/controlpanel.asp',
            'admin.asp',
            'pages/admin/admin-login.asp',
            'admin/admin-login.asp',
            'admin-login.asp',
            'admin/cp.asp',
            'cp.asp',
            'administrator/account.asp',
            'administrator.asp',
            'acceso.asp',
            'login.asp',
            'modelsearch/login.asp',
            'moderator.asp',
            'moderator/login.asp',
            'administrator/login.asp',
            'moderator/admin.asp',
            'controlpanel.asp',
            'admin/account.html',
            'adminpanel.html',
            'webadmin.html',
            'pages/admin/admin-login.html',
            'admin/admin-login.html',
            'webadmin/index.html',
            'webadmin/admin.html',
            'webadmin/login.html',
            'user.asp',
            'user.html',
            'admincp/index.asp',
            'admincp/login.asp',
            'admincp/index.html',
            'admin/adminLogin.html',
            'adminLogin.html',
            'admin/adminLogin.html',
            'home.html',
            'adminarea/index.html',
            'adminarea/admin.html',
            'adminarea/login.html',
            'panel-administracion/index.html',
            'panel-administracion/admin.html',
            'modelsearch/index.html',
            'modelsearch/admin.html',
            'admin/admin_login.html',
            'admincontrol/login.html',
            'adm/index.html',
            'adm.html',
            'admincontrol.asp',
            'admin/account.asp',
            'adminpanel.asp',
            'webadmin.asp',
            'webadmin/index.asp',
            'webadmin/admin.asp',
            'webadmin/login.asp',
            'admin/admin_login.asp',
            'admin_login.asp',
            'panel-administracion/login.asp',
            'adminLogin.asp',
            'admin/adminLogin.asp',
            'home.asp',
            'admin.asp',
            'adminarea/index.asp',
            'adminarea/admin.asp',
            'adminarea/login.asp',
            'admin-login.html',
            'panel-administracion/index.asp',
            'dvwa',
            'panel-administracion/admin.asp',
            'modelsearch/index.asp',
            'modelsearch/admin.asp',
            'administrator/index.asp',
            'admincontrol/login.asp',
            'adm/admloginuser.asp',
            'admloginuser.asp',
            'admin2.asp',
            'admin2/login.asp',
            'admin2/index.asp',
            'adm/index.asp',
            'adm.asp',
            'affiliate.asp',
            'adm_auth.asp',
            'memberadmin.asp',
            'administratorlogin.asp',
            'siteadmin/login.asp',
            'siteadmin/index.asp',
            'siteadmin/login.html',
            'admin/',
            'administrator/',
            'admin1/',
            'admin2/',
            'admin3/',
            'admin4/',
            'admin5/',
            'usuarios/',
            'usuario/',
            'administrator/',
            'moderator/',
            'webadmin/',
            'adminarea/',
            'bb-admin/',
            'adminLogin/',
            'admin_area/',
            'panel-administracion/',
            'instadmin/',
            'memberadmin/',
            'administratorlogin/',
            'adm/',
            'admin/account.cfm',
            'admin/index.cfm',
            'admin/login.cfm',
            'admin/admin.cfm',
            'admin/account.cfm',
            'admin_area/admin.cfm',
            'admin_area/login.cfm',
            'siteadmin/login.cfm',
            'siteadmin/index.cfm',
            'siteadmin/login.html',
            'admin/account.html',
            'admin/index.html',
            'admin/login.html',
            'admin/admin.html',
            'admin_area/index.cfm',
            'bb-admin/index.cfm',
            'bb-admin/login.cfm',
            'bb-admin/admin.cfm',
            'admin/home.cfm',
            'admin_area/login.html',
            'admin_area/index.html',
            'admin/controlpanel.cfm',
            'admin.cfm',
            'admincp/index.asp',
            'admincp/login.asp',
            'admincp/index.html',
            'admin/account.html',
            'adminpanel.html',
            'webadmin.html',
            'webadmin/index.html',
            'webadmin/admin.html',
            'webadmin/login.html',
            'admin/admin_login.html',
            'admin_login.html',
            'panel-administracion/login.html',
            'admin/cp.cfm',
            'cp.cfm',
            'administrator/index.cfm',
            'administrator/login.cfm',
            'nsw/admin/login.cfm',
            'webadmin/login.cfm',
            'admin/admin_login.cfm',
            'admin_login.cfm',
            'administrator/account.cfm',
            'administrator.cfm',
            'admin_area/admin.html',
            'pages/admin/admin-login.cfm',
            'admin/admin-login.cfm',
            'admin-login.cfm',
            'bb-admin/index.html',
            'bb-admin/login.html',
            'bb-admin/admin.html',
            'admin/home.html',
            'login.cfm',
            'modelsearch/login.cfm',
            'moderator.cfm',
            'moderator/login.cfm',
            'moderator/admin.cfm',
            'account.cfm',
            'pages/admin/admin-login.html',
            'admin/admin-login.html',
            'admin-login.html',
            'controlpanel.cfm',
            'admincontrol.cfm',
            'admin/adminLogin.html',
            'acceso.cfm',
            'adminLogin.html',
            'admin/adminLogin.html',
            'home.html',
            'rcjakar/admin/login.cfm',
            'adminarea/index.html',
            'adminarea/admin.html',
            'webadmin.cfm',
            'webadmin/index.cfm',
            'webadmin/admin.cfm',
            'admin/controlpanel.html',
            'admin.html',
            'admin/cp.html',
            'cp.html',
            'adminpanel.cfm',
            'moderator.html',
            'administrator/index.html',
            'administrator/login.html',
            'user.html',
            'administrator/account.html',
            'administrator.html',
            'login.html',
            'modelsearch/login.html',
            'moderator/login.html',
            'adminarea/login.html',
            'panel-administracion/index.html',
            'panel-administracion/admin.html',
            'modelsearch/index.html',
            'modelsearch/admin.html',
            'admincontrol/login.html',
            'adm/index.html',
            'adm.html',
            'moderator/admin.html',
            'user.cfm',
            'account.html',
            'controlpanel.html',
            'admincontrol.html',
            'panel-administracion/login.cfm',
            'wp-login.cfm',
            'adminLogin.cfm',
            'admin/adminLogin.cfm',
            'home.cfm',
            'admin.cfm',
            'adminarea/index.cfm',
            'adminarea/admin.cfm',
            'adminarea/login.cfm',
            'panel-administracion/index.cfm',
            'panel-administracion/admin.cfm',
            'modelsearch/index.cfm',
            'modelsearch/admin.cfm',
            'admincontrol/login.cfm',
            'adm/admloginuser.cfm',
            'admloginuser.cfm',
            'admin2.cfm',
            'admin2/login.cfm',
            'admin2/index.cfm',
            'usuarios/login.cfm',
            'adm/index.cfm',
            'adm.cfm',
            'affiliate.cfm',
            'adm_auth.cfm',
            'memberadmin.cfm',
            'administratorlogin.cfm',
            'admin/',
            'administrator/',
            'admin1/',
            'admin2/',
            'admin3/',
            'admin4/',
            'admin5/',
            'usuarios/',
            'usuario/',
            'administrator/',
            'moderator/',
            'webadmin/',
            'adminarea/',
            'bb-admin/',
            'adminLogin/',
            'admin_area/',
            'panel-administracion/',
            'instadmin/',
            'memberadmin/',
            'administratorlogin/',
            'adm/',
            'admin/account.js',
            'admin/index.js',
            'admin/login.js',
            'admin/admin.js',
            'admin/account.js',
            'admin_area/admin.js',
            'admin_area/login.js',
            'siteadmin/login.js',
            'siteadmin/index.js',
            'siteadmin/login.html',
            'admin/account.html',
            'admin/index.html',
            'admin/login.html',
            'admin/admin.html',
            'admin_area/index.js',
            'bb-admin/index.js',
            'bb-admin/login.js',
            'bb-admin/admin.js',
            'admin/home.js',
            'admin_area/login.html',
            'admin_area/index.html',
            'admin/controlpanel.js',
            'admin.js',
            'admincp/index.asp',
            'admincp/login.asp',
            'admincp/index.html',
            'admin/account.html',
            'adminpanel.html',
            'webadmin.html',
            'webadmin/index.html',
            'webadmin/admin.html',
            'webadmin/login.html',
            'admin/admin_login.html',
            'admin_login.html',
            'panel-administracion/login.html',
            'admin/cp.js',
            'cp.js',
            'administrator/index.js',
            'administrator/login.js',
            'nsw/admin/login.js',
            'webadmin/login.js',
            'admin/admin_login.js',
            'admin_login.js',
            'administrator/account.js',
            'administrator.js',
            'admin_area/admin.html',
            'pages/admin/admin-login.js',
            'admin/admin-login.js',
            'admin-login.js',
            'bb-admin/index.html',
            'bb-admin/login.html',
            'bb-admin/admin.html',
            'admin/home.html',
            'login.js',
            'modelsearch/login.js',
            'moderator.js',
            'moderator/login.js',
            'moderator/admin.js',
            'account.js',
            'pages/admin/admin-login.html',
            'admin/admin-login.html',
            'admin-login.html',
            'controlpanel.js',
            'admincontrol.js',
            'admin/adminLogin.html',
            'adminLogin.html',
            'admin/adminLogin.html',
            'home.html',
            'rcjakar/admin/login.js',
            'adminarea/index.html',
            'adminarea/admin.html',
            'webadmin.js',
            'webadmin/index.js',
            'acceso.js',
            'webadmin/admin.js',
            'admin/controlpanel.html',
            'admin.html',
            'admin/cp.html',
            'cp.html',
            'adminpanel.js',
            'moderator.html',
            'administrator/index.html',
            'administrator/login.html',
            'user.html',
            'administrator/account.html',
            'administrator.html',
            'login.html',
            'modelsearch/login.html',
            'moderator/login.html',
            'adminarea/login.html',
            'panel-administracion/index.html',
            'panel-administracion/admin.html',
            'modelsearch/index.html',
            'modelsearch/admin.html',
            'admincontrol/login.html',
            'adm/index.html',
            'adm.html',
            'moderator/admin.html',
            'user.js',
            'account.html',
            'controlpanel.html',
            'admincontrol.html',
            'panel-administracion/login.js',
            'wp-login.js',
            'adminLogin.js',
            'admin/adminLogin.js',
            'home.js',
            'admin.js',
            'adminarea/index.js',
            'adminarea/admin.js',
            'adminarea/login.js',
            'panel-administracion/index.js',
            'panel-administracion/admin.js',
            'modelsearch/index.js',
            'modelsearch/admin.js',
            'admincontrol/login.js',
            'adm/admloginuser.js',
            'admloginuser.js',
            'admin2.js',
            'admin2/login.js',
            'admin2/index.js',
            'usuarios/login.js',
            'adm/index.js',
            'adm.js',
            'affiliate.js',
            'adm_auth.js',
            'memberadmin.js',
            'administratorlogin.js',
            'admin/',
            'administrator/',
            'admin1/',
            'admin2/',
            'admin3/',
            'admin4/',
            'admin5/',
            'usuarios/',
            'usuario/',
            'administrator/',
            'moderator/',
            'webadmin/',
            'adminarea/',
            'bb-admin/',
            'adminLogin/',
            'admin_area/',
            'panel-administracion/',
            'instadmin/',
            'memberadmin/',
            'administratorlogin/',
            'adm/',
            'admin/account.cgi',
            'admin/index.cgi',
            'admin/login.cgi',
            'admin/admin.cgi',
            'admin/account.cgi',
            'admin_area/admin.cgi',
            'admin_area/login.cgi',
            'siteadmin/login.cgi',
            'siteadmin/index.cgi',
            'siteadmin/login.html',
            'admin/account.html',
            'phpmyadmin',
            'admin/index.html',
            'admin/login.html',
            'admin/admin.html',
            'admin_area/index.cgi',
            'bb-admin/index.cgi',
            'bb-admin/login.cgi',
            'bb-admin/admin.cgi',
            'admin/home.cgi',
            'admin_area/login.html',
            'admin_area/index.html',
            'admin/controlpanel.cgi',
            'admin.cgi',
            'admincp/index.asp',
            'admincp/login.asp',
            'admincp/index.html',
            'admin/account.html',
            'adminpanel.html',
            'webadmin.html',
            'webadmin/index.html',
            'webadmin/admin.html',
            'webadmin/login.html',
            'admin/admin_login.html',
            'admin_login.html',
            'panel-administracion/login.html',
            'admin/cp.cgi',
            'cp.cgi',
            'administrator/index.cgi',
            'administrator/login.cgi',
            'nsw/admin/login.cgi',
            'webadmin/login.cgi',
            'admin/admin_login.cgi',
            'admin_login.cgi',
            'administrator/account.cgi',
            'administrator.cgi',
            'admin_area/admin.html',
            'pages/admin/admin-login.cgi',
            'admin/admin-login.cgi',
            'admin-login.cgi',
            'bb-admin/index.html',
            'bb-admin/login.html',
            'bb-admin/admin.html',
            'admin/home.html',
            'login.cgi',
            'modelsearch/login.cgi',
            'moderator.cgi',
            'moderator/login.cgi',
            'moderator/admin.cgi',
            'account.cgi',
            'pages/admin/admin-login.html',
            'admin/admin-login.html',
            'admin-login.html',
            'controlpanel.cgi',
            'admincontrol.cgi',
            'admin/adminLogin.html',
            'adminLogin.html',
            'admin/adminLogin.html',
            'home.html',
            'rcjakar/admin/login.cgi',
            'adminarea/index.html',
            'adminarea/admin.html',
            'webadmin.cgi',
            'webadmin/index.cgi',
            'acceso.cgi',
            'webadmin/admin.cgi',
            'admin/controlpanel.html',
            'admin.html',
            'admin/cp.html',
            'cp.html',
            'adminpanel.cgi',
            'moderator.html',
            'administrator/index.html',
            'administrator/login.html',
            'user.html',
            'administrator/account.html',
            'administrator.html',
            'login.html',
            'modelsearch/login.html',
            'moderator/login.html',
            'adminarea/login.html',
            'panel-administracion/index.html',
            'panel-administracion/admin.html',
            'modelsearch/index.html',
            'modelsearch/admin.html',
            'admincontrol/login.html',
            'adm/index.html',
            'adm.html',
            'moderator/admin.html',
            'user.cgi',
            'account.html',
            'controlpanel.html',
            'admincontrol.html',
            'panel-administracion/login.cgi',
            'wp-login.cgi',
            'adminLogin.cgi',
            'admin/adminLogin.cgi',
            'home.cgi',
            'admin.cgi',
            'adminarea/index.cgi',
            'adminarea/admin.cgi',
            'adminarea/login.cgi',
            'panel-administracion/index.cgi',
            'panel-administracion/admin.cgi',
            'modelsearch/index.cgi',
            'modelsearch/admin.cgi',
            'admincontrol/login.cgi',
            'adm/admloginuser.cgi',
            'admloginuser.cgi',
            'admin2.cgi',
            'admin2/login.cgi',
            'admin2/index.cgi',
            'usuarios/login.cgi',
            'adm/index.cgi',
            'adm.cgi',
            'affiliate.cgi',
            'adm_auth.cgi',
            'memberadmin.cgi',
            'administratorlogin.cgi',
            'admin/',
            'administrator/',
            'admin1/',
            'admin2/',
            'admin3/',
            'admin4/',
            'admin5/',
            'usuarios/',
            'usuario/',
            'administrator/',
            'moderator/',
            'webadmin/',
            'adminarea/',
            'bb-admin/',
            'adminLogin/',
            'admin_area/',
            'panel-administracion/',
            'instadmin/',
            'memberadmin/',
            'administratorlogin/',
            'adm/',
            'siteadmin/login.html',
            'admin/account.html',
            'admin/index.html',
            'admin/login.html',
            'admin/admin.html',
            'admin_area/login.html',
            'admin_area/index.html',
            'admincp/index.asp',
            'admincp/login.asp',
            'admincp/index.html',
            'admin/account.html',
            'adminpanel.html',
            'webadmin.html',
            'webadmin/index.html',
            'webadmin/admin.html',
            'webadmin/login.html',
            'admin/admin_login.html',
            'admin_login.html',
            'panel-administracion/login.html',
            'admin_area/admin.html',
            'bb-admin/index.html',
            'bb-admin/login.html',
            'bb-admin/admin.html',
            'admin/home.html',
            'pages/admin/admin-login.html',
            'admin/admin-login.html',
            'admin-login.html',
            'admin/adminLogin.html',
            'adminLogin.html',
            'admin/adminLogin.html',
            'home.html',
            'adminarea/index.html',
            'adminarea/admin.html',
            'admin/controlpanel.html',
            'admin.html',
            'admin/cp.html',
            'cp.html',
            'moderator.html',
            'administrator/index.html',
            'administrator/login.html',
            'user.html',
            'administrator/account.html',
            'administrator.html',
            'login.html',
            'modelsearch/login.html',
            'moderator/login.html',
            'adminarea/login.html',
            'panel-administracion/index.html',
            'panel-administracion/admin.html',
            'modelsearch/index.html',
            'modelsearch/admin.html',
            'admincontrol/login.html',
            'adm/index.html',
            'adm.html',
            'moderator/admin.html',
            'account.html',
            'controlpanel.html',
            'admincontrol.html',
            'wordpress',
            'btslab'
        ]
    print(Fore.BLUE +"[*] Trying : \n\n")
    # make a loop for the trying to find the link
    for i in adminlist:
        url_try = url + i
        try:
            openurl = urllib.request.urlopen(url_try)
            print("")
            print(Fore.GREEn +"[+] Found Something : " + openurl)
            print("")
        except:
            print(Fore.LIGHTRED_EX +"[!] Nothing Found : " + url_try)
elif option == '3':
        texter = input(Fore.LIGHTYELLOW_EX +'[#] Enter Text To Encrypt It : ')
        print(Fore.LIGHTBLUE_EX +"""
 [01] SHA1           
 [02] MD5                
 [03] SHA384         
 [04] SHA3_512       
 [05] SHA224         
 [06] SHA512         
 [07] SHA256""")
        option1000 = input(Fore.LIGHTMAGENTA_EX +'[!] Select ? : ')
        if option1000 == '1':
            sha1er = sha1(texter.encode()).hexdigest()
            print(sha1er)
        if option1000 == '2':
                scripter = md5(texter.encode()).hexdigest()
                print(scripter)
        if option1000 == '3':
                scripter = sha384(texter.encode()).hexdigest()
                print(scripter)
        if option1000 == '4':
                scripter = sha3_512(texter.encode()).hexdigest()
                print(scripter)
        if option1000 == '5':
                scripter = sha224(texter.encode()).hexdigest()
                print(scripter)
        if option1000 == '6':
                scripter = sha512(texter.encode()).hexdigest()
                print(scripter)
        if option1000 == '7':
                scripter = sha256(texter.encode()).hexdigest()
                print(scripter)
elif option == '4':
    print('Soon')
    exit()
elif option == '5':
    tarip = input(Fore.LIGHTGREEN_EX +"[$] Target IP : ")
    IP = requests.get("https://get.geojs.io/v1/ip.json")
    loc = requests.get("https://get.geojs.io/v1/ip/geo/" + tarip + ".json")
    loc2 = loc.json()
    print(Fore.LIGHTBLUE_EX +"[!] Target Country : " + loc2["country"])
    print(Fore.LIGHTBLUE_EX +"[!] Target Time Zone : " + loc2["timezone"])
    print(Fore.LIGHTBLUE_EX +"[!] Target Longitude Location : " + loc2["longitude"])
    print(Fore.LIGHTBLUE_EX +"[!] Target Latitude Location : " + loc2["latitude"])
elif option == '6':
    print(Fore.LIGHTBLUE_EX +'Soon')
    exit()
elif option == '7':
    print(Fore.CYAN +"[!] Get Instagram  Info using ?")
    print(Fore.LIGHTCYAN_EX +"[1] Username             [2] sessionId")
    maop = input(Fore.LIGHTYELLOW_EX +"[?] Select ? : ")
    if maop == '1':
        username = input(Fore.LIGHTGREEN_EX +"[!] Enter Username : ")
        head = {
                'HOST': "www.instagram.com",
                'KeepAlive': 'True',
                'user-agent': generate_user_agent(),
                'Cookie': 'ig_did=B229D588-7641-44E0-8035-467C7BEC3282; ig_nrcb=1; mid=YGWX3wALAAFc7t0VgtJpoYSw1rEc; csrftoken=wn59xw8BMRIceNQOBzjqjhoTPhTXENBB; ds_user_id=11675767944; sessionid=11675767944%3Ao1hjlJiSGKw9vR%3A21; shbid=19303; shbts=1617412509.6840706; rur=FTW',
                'Accept': "*/*",
                'ContentType': "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "X-IG-App-ID": "936619743392459",
                "X-Instagram-AJAX": "missing",
                "X-CSRFToken": "wn59xw8BMRIceNQOBzjqjhoTPhTXENBB",
                "Accept-Language": "en-US,en;q=0.9"
            }
        cookie = secrets.token_hex(8) * 2
        url_id = f'https://www.instagram.com/{username}/?__a=1'
        req_id = r.get(url_id, headers=head).json()
        bio = str(req_id['graphql']['user']['biography'])
        url = str(req_id['graphql']['user']['external_url'])
        nam = str(req_id['graphql']['user']['full_name'])
        idd = str(req_id['graphql']['user']['id'])
        isp = str(req_id['graphql']['user']['is_private'])
        isv = str(req_id['graphql']['user']['is_verified'])
        pro = str(req_id['graphql']['user']['profile_pic_url'])
        print(Fore.LIGHTBLUE_EX +'''[$] Simple Info For {} 
[$] Name / {}
[$] Url / {}
[$] Bio / {}
[$] ID / {}
[$] Private ? / {}
[$] Verified ? / {}
[$] Profile Picture / {} 
'''.format(username,nam,url,bio,idd,isp,isv,pro))
    elif maop == '2':
        sessionid = input(Fore.LIGHTBLUE_EX +'[!] Enter Session ID : ')
        hydrated = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': generate_user_agent(),
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }
        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/accounts/access_tool/former_usernames?__a=1'
        response = requests.request("GET", url, data=data, headers=hydrated, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Users Since Account Created : " + str(info["data"]))
        hydrated2 = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/accounts/access_tool/former_phones?__a=1'
        response = requests.request("GET", url, data=data, headers=hydrated2, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Phone Numbers Since Account Created : " + str(info["data"]))
        hydrated3 = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/session/login_activity/?__a=1'
        response = requests.request("GET", url, data=data, headers=hydrated3, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Login Activity Since Account Created : " + str(info["data"]))
        hydrated4 = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/accounts/access_tool/former_emails?__a=1'
        response = requests.request("GET", url, data=data, headers=hydrated4, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Emails Activity Since Account Created : " + str(info["data"]))
        hydrated5 = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/emails/emails_sent/?__a=1'
        response = requests.request("GET", url, data=data, headers=hydrated5, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Last Activity : " + str(info["data"]))
        headers = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/accounts/access_tool/accounts_you_blocked?__a=1'
        response = requests.request("GET", url, data=data, headers=headers, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + '[-] Blocked Accounts :  ' + str(info["data"]))
        headers = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/accounts/access_tool/former_bio_texts?__a=1'
        response = requests.request("GET", url, data=data, headers=headers, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Bio Since Account Created : " + str(info["data"]))


        headers = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/accounts/access_tool/search_history?__a=1'
        response = requests.request("GET", url, data=data, headers=headers, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Search History :  " + str(info["data"]))

        headers = {'Host': 'www.instagram.com',
                   'Content-Type': 'application/json; charset=utf-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept': '*/*',
                   'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                   'Connection': 'close',
                   'X-IG-App-ID': '936619743392459',
                   'X-Requested-With': 'XMLHttpRequest',
                   'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
                   'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
                   'DNT': '1'
                   }

        cookies = {'sessionid': sessionid}
        data = ''
        url = 'https://www.instagram.com/download/request/?__a=1'
        response = requests.request("GET", url, data=data, headers=headers, cookies=cookies)
        info = json.loads(response.text)
        print(Fore.LIGHTBLUE_EX + "[-] Verified Email : " + str(info["email_hint"]))
elif option == '8':
    def read_all_file():
        file = open(sys.argv[1], 'r', encoding="utf8")
        file = file.read()
        return file
        # information about php code


    CA.info.GET_parameters(read_all_file())
    CA.info.POST_parameters(read_all_file())
    # scan SQL injection

    file = open(sys.argv[1], 'r', encoding="utf8")
    line_number = 0
    print(Fore.RED +'vulnerability found:\n')
    CA.search.SQLi(read_all_file())
    for line in file:
        CA.search.command_injection(line.strip('\n'), line_number)
        CA.search.LFI(line.strip('\n'), line_number)
        CA.search.XSS(line.strip('\n'), line_number)
        CA.search.SSRF(line.strip('\n'), line_number)
        CA.search.open_redirect(line.strip('\n'), line_number)
        CA.search.ID(line.strip('\n'), line_number)

        line_number = line_number + 1
##### Port Scanner For osama.a.m.y
elif option == '9':
        tarurl = input(Fore.LIGHTBLUE_EX +'[%] Enter Url (Ex : website.com): ')
        if tarurl == "":
         print(Fore.RED +'[!] No Url')
         time.sleep(3)
         exit()
        else:
         pass
        nport = input(Fore.LIGHTMAGENTA_EX +'[?] Range Of Ports :  '+ Style.RESET_ALL)
        if nport == "":
                nport = 1024
        else:
                nport = nport


        def getIP():
                global tarurl
                global hostIP
                try:
                        hostIP = socket.gethostbyname(tarurl)
                except socket.gaierror:
                        print('[!]')
                        what = input(
                                Fore.CYAN + '[#] [t] Try Again :  ' + Style.RESET_ALL)
                        if what == 't':
                                tarurl = input(
                                        Fore.CYAN + '[!] Enter Url (Ex : example.com):  ' + Style.RESET_ALL)
                                if tarurl == "":
                                        print(Fore.RED +'[!] No Url')
                                        time.sleep(3)
                                        exit()
                                else:
                                        tarurl = tarurl
                                        hostIP = socket.gethostbyname(tarurl)
                        elif what == "":
                                time.sleep(3)
                                exit()
                        else:
                                time.sleep(3)
                                exit()

                        return (hostIP)


        getIP()


        def portscan(port):
                global hostIP
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((hostIP, port))
                        return True
                except:
                        #print(Fore.LIGHTRED_EX + '[!] Error Port')
                        return False


        def fill(port_list):
                for port in port_list:
                        queue.put(port)


        def scan():
                while not queue.empty():
                        port = queue.get()
                        if portscan(port):
                                print(Fore.GREEN + f'[-] Port {port} is Opened' + Style.RESET_ALL)
                                open_ports.append(port)


        port_list = range(1, int(nport))
        fill(port_list)

        thread_list = []
        for t in range(int(100)):
                thread = threading.Thread(target=scan)
                thread_list.append(thread)

        for thread in thread_list:
                thread.start()

        for thread in thread_list:
                thread.join()
elif option == '10':
    print(Fore.LIGHTRED_EX +'Goodbye Baby ')
    exit()
