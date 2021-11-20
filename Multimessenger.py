import os
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pyautogui import *
import requests

import smtplib
from email.MIMEBase import MIMEBase
from email import encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import getpass
import fbchat
import tweepy
import sys
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient



your_mode= confirm(text='Enter the Type of messenger you want to use',
                   title='Mode details:Multi Messenger',buttons=['FACEBOOK','SMS','TWITTER','GMAIL'])
if (your_mode == "FACEBOOK"):
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
    driver.find_element_by_xpath('//div[@class="_1mf _1mj"]').send_keys(message, Keys.ENTER)

    # This is where I entered the keys and Did Enter
    '''
    this is how it should look like

    Enter your username abdahi.oladejo.10
    Enter your Password 9ad3e22
    Enter your friend or Group Id100016740336536/
    Enter your text message here how are you doing
    '''
    
elif(your_mode == "SMS"):
    
    # Here i have used fast2sms api key , simply go on the site and get youre api key and replace authorization below.
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"NMDIIyBTmUsvRJpVRIWgMcDtCKsQQy4ExoKAi3epwIVr4v1UDD9hDBEqO5R4","message":"This is test message","language":"english","route":"q","numbers":"8287764290"}

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

elif(your_mode == "TWITTER"):

    
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET);
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET);
    print( "Enter your tweet\n");
    tweet=sys.stdin.read();
    status = tweepy.API(auth).update_status(status=tweet);
            
    exit_input = raw_input("To exit type EXIT, else press any key\n")

else:

    
    rec_adr = raw_input("Enter receiver's email\n")
    msg= MIMEMultipart()
    subj=raw_input("Subject:")
    msg['From']=your_adr
    msg['To']=rec_adr
    msg['Subject']=subj
            
    print ("Enter body of email")
    body=sys.stdin.read();
    
    msg.attach(MIMEText(body,'plain'))
    
    inp = raw_input("Do you want to attach any file? y/n")
    if(inp == 'y'):
            strings = raw_input("Enter file address\n")
            if(strings != ''):
                    attachment = open(strings,'rb')
                    part = MIMEBase('application','octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename = %s" % strings)
                    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(your_adr,pass_adr)
    text = msg.as_string()
    server.sendmail(your_adr,rec_adr,text)
    server.quit()





