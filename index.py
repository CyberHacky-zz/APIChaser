#!/usr/bin/env python3

import requests 
import urllib.request
import json                                # To use request package in current program 
import sys
import os
import csv
import webbrowser 
from urllib.parse import urlparse



#Title print

chaserlogo = ('''
 █████╗ ██████╗ ██╗   █████╗ ██╗  ██╗ █████╗  ██████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║  ██╔══██╗██║  ██║██╔══██╗██╔════╝██╔════ ██╔══██╗
███████║██████╔╝██║  ██║  ╚═╝███████║███████║╚█████╗ █████╗  ██████╔╝
██╔══██║██╔═══╝ ██║  ██║  ██╗██╔══██║██╔══██║ ╚═══██╗██╔══╝  ██╔══██╗
██║  ██║██║     ██║  ╚█████╔╝██║  ██║██║  ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[!] This Tool Must Run As ROOT [!]         Created By : SecFirm Team\n\n''')

#https://reqres.in/api/users?page=2

def getapi():
    print(chaserlogo)  
getapi()    

# Provide Custom Browser headers
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

#dropapi = input("[+] Drop API Here : ") 
dropapi = ("https://reqres.in/api/users?page=2")
os.system('clear')
print (chaserlogo)
def menu():
    #print (chaserlogo)
    print ("""
   {1}--URL HEADER Response
   {2}--Request Response
   {3}--Request Body
   {4}--OWASP Top 10
   {0}--Exit
 """)
    choice = input("CHASER~# ")
    if choice == "1":
        urlheaderresponse()
    elif choice == "2":
        requestselect()
    elif choice == "3":
        requestbody()
    elif choice == "4":
        owaspmenu()
    elif choice == "0":
        print("Thanks for Using API CHASER")
        os.system('clear'), sys.exit()
    elif choice == "":
        
        print(chaserlogo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        menu()
    else:
        print(chaserlogo)
        menu()

def requestselect():
    #print (chaserlogo)
    print("\n")
    print(" Identify API Requeste Response HERE :  \n")
    print ("""
   {1}--GET
   {2}--POST
   {3}--PUT
   {4}--DELETE
   {5}--HEAD
   {6}--OPTIONS
   {0}--Back to Menu
   {99}-Exit
 """)
    choice = input("CHASER~# ")
    if choice == "1":
        getresponse()
    elif choice == "2":
        postresponse()
    elif choice == "3":
        putresponse()
    elif choice == "4":
        deleteresponse()
    elif choice == "5":
        headresponse()
    elif choice == "6":
        optionresponse()
    elif choice == "0":
        print(chaserlogo)
        menu()
    elif choice == "99":
        print("Thanks for Using API CHASER")
        os.system('clear'), sys.exit()
    elif choice == "":
        #print(chaserlogo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        requestselect()
    else:
        print(chaserlogo)
        menu()

def getresponse():
    test = requests.get(dropapi, allow_redirects=False)
    print("[+] API URL : " + test.url)                              # Print API Response Code
    print("[+] Response Status : " + str(test.status_code))
    bestapi = requests.get(dropapi).json()                      # Get API response and genrate global variable
    content = json.dumps(bestapi, indent = 4)
    print("[+] Response Data : \n")
    print(content)
    requestselect()


def headresponse():
    r = requests.head(dropapi)
    print("[+] HEAD Response : \n")
    print(r.headers)
    requestselect()


def deleteresponse():
    r = requests.delete(dropapi, allow_redirects=False)
    print("[+] DELETE Response : \n")
    print(r)
    requestselect()

def postresponse():

    print("Enter Post API URL : Example : https://example.org/post")
    getdata = input("Drop POST URL :  ")
    response = requests.post(getdata, allow_redirects=False, json={'key':'value'})
    get_post_res = response.json()
    bestresponse = json.dumps(get_post_res, indent = 4)
    print("[+] Response Status : " + str(response.status_code))
    print("[+] Response Data : \n")
    print(bestresponse)
    requestselect()


def putresponse():

    print("Enter PUT API URL : Example : https://example.org/put")
    getputdata = input("Drop PUT URL :  ")
    response = requests.put(getputdata, allow_redirects=False, json={'key':'value'})
    get_put_res = response.json()
    best_putresponse = json.dumps(get_put_res, indent = 4)
    print("[+] Response Status : " + str(response.status_code))
    print("[+] Response Data : \n")
    print(best_putresponse)
    requestselect()

def optionresponse():

    print("OPTION Method helps to identiy which request method accept API URL \n")
    optiondata = requests.options(dropapi, allow_redirects=False )
    print("[+] API URL Options Methods : " + optiondata.headers['Access-Control-Allow-Methods'])
    
    requestselect()




# Main Menu Functions

def urlheaderresponse():
    
    print("Enter URL  : Example [https://www.google.com/]")
    geturl = input("[+] Drop URL : ")
    responsecode = requests.head(geturl)
    url = urllib.request.urlopen(geturl)
    header = url.info()
    print("[+] URL Response Status : " + str(responsecode.status_code))
    print("[+] HEADER Response Data : \n")
    print(header.as_string())    
    menu()


def requestbody():
    testbody = webbrowser.open_new_tab(dropapi)
    print("\n")
    print(testbody)

    menu()

def owaspmenu():

    #print (chaserlogo)
    print("\n")
    print(" API OWASP Top 10 Security  :  \n")
    print ("""
   {1}--2019 — Broken object level authorization
   {2}--2019 — Broken authentication
   {3}--2019 — Excessive data exposure
   {4}--2019 — Lack of resources and rate limiting
   {5}--2019 — Broken function level authorization
   {6}--2019 — Mass assignment
   {7}--2019 — Security misconfiguration
   {8}--2019 — Injection
   {9}--2019 — Improper assets management
   {10}--2019 — Insufficient logging and monitoring
   {0}--Back to Menu
   {99}-Exit
 """)
    choice = input("CHASER~# ")
    if choice == "1":
        brokenobject()
    elif choice == "2":
        brokenauth()
    elif choice == "3":
        dataexpo()
    elif choice == "4":
        lackofresource()
    elif choice == "5":
        brokenfunction()
    elif choice == "6":
        massassignment()
    elif choice == "7":
        securitymis()
    elif choice == "8":
        injection()
    elif choice == "9":
        improperassets()
    elif choice == "10":
        insufficientlogmon()
    elif choice == "0":
        print(chaserlogo)
        menu()
    elif choice == "99":
        print("Thanks for Using API CHASER")
        os.system('clear'), sys.exit()
    elif choice == "":
        #print(chaserlogo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        owaspmenu()
    else:
        print(chaserlogo)
        menu()
    
    #OWASP TOP 10 | 8 : Injection perfom here

def injection():
        
        print("\n")
        url = input("[+] Drop API URL : ")
        url = url.strip()
        req = requests.get(url)
        responsecode = requests.head(url)
        print("[+] URL Response Status : " + str(responsecode.status_code))
        print("[+] API OWASP TOP 10 | 2019 — Injection : Report : \n")
   
        try:
            protection_xss = req.headers['X-XSS-Protection']

            if protection_xss != '1; mode = block':
                print ('X-XSS-Protection not set properly, it may be possible:', protection_xss)
        
        except:
            print ('X-XSS-Protection not set, it may be possible')
      
        try:
            options_content_type = req.headers['X-Content-Type-Options']
            
            if options_content_type != 'nosniff':
                print ('X-Content-Type-Options not set properly:', options_content_type)
        except:
            print ('X-Content-Type-Options not set')
            
        try:
            transport_security = req.headers['Strict-Transport-Security']
        except:
            print ('HSTS header not set properly, Man in the middle attacks is possible')
      
        try:
            content_security = req.headers['Content-Security-Policy']
            print ('Content-Security-Policy set:', content_security)
        except:
            print ('Content-Security-Policy missing')

        owaspmenu()

#Calling main menu here so program run        
menu()