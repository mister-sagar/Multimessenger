import os
from pyautogui import *

import pywhatkit

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from pyautogui import * 

import requests


import getpass
import tweepy
import sys

import smtplib,ssl


your_mode= confirm(text='Enter the Type of messenger you want to use',title='Mode details:Multi Messenger',buttons=['FACEBOOK','SMS','TWITTER','GMAIL','WHATSAPP'])
if (your_mode == "FACEBOOK"):
    try:
        usernam=str(input('Enter your username: '))
        password=str(input('Enter your Password: '))
        frndId = str(input('Enter your friend or Group Id: '))
        message = str(input('Enter your text message here: '))
        #this is where i open a new window
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #this is where i open facebook
        driver.get ('https://www.facebook.com/')
        # this is where i start entering my username and password.
        driver.find_element_by_id("email").send_keys(usernam)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_name("login").click() # I click login button
        # login process done I am now on facebook
        sleep(1)
        # i start navigating to message and click on the friend i wanna messsage
        mesgAdd='https://www.facebook.com/messages/t/'
        mesgLink=mesgAdd+frndId
        driver.get(mesgLink)
        sleep (1)
        #This is Where I clicked the Send Message '
        driver.find_element_by_xpath('//div[@class="_1mf _1mj"]').send_keys(message,
        Keys.ENTER)
        # This is where I entered the keys and Did Enter
    except NoSuchElementException as exc:
        print(exc) # and/or other actions to recover 
        

elif(your_mode == "SMS"):
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {"authorization":"API KEY","message":"This is test message","language":"english","route":"q","numbers":"your mobile no."}
    headers = {
    'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    {
    "return": True,
    "request_id": "lwdtp7cjyqxvfe9",
    "message": [
    "Message sent successfully"
    ]
    }
    
elif(your_mode == "WHATSAPP"):
    mob_no= int(input('enter  no.'))
    message=input('enter message')
    time = [int(x) for x in input("time").split(",")]
    pywhatkit.sendwhatmsg(f'+91{mob_no}', message, time[0], time[1])
    
elif(your_mode == "TWITTER"):
    
    try:
        # personal details
        consumer_key ="_"
        consumer_secret ="_"
        access_token ="_"
        access_token_secret ="_"

        # authentication of consumer key and secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # authentication of access token and secret
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth) 

        # update the status
        status=input('enter the status you want to set')
        api.update_status(status)
        print('status set on twitter')
    except:
        print('an error occured')
        
else:
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "_"  # Enter your address
        receiver_email = "_"  # Enter receiver address
        password = '_'
        sub=input('enter the subject')
        mes=input('enter the message')
        args=(sub,mes)
        message = """\
        Subject: {0}

        {1}""".format(*args)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        print('an error occured')
