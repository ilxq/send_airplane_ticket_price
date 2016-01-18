# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:35:49 2015

@author: sherryup
"""
import urllib2
from bs4 import BeautifulSoup
url = "http://touch.qunar.com/h5/flight/flightlist?startCity=%E6%A1%82%E6%9E%97&destCity=%E8%A5%BF%E5%AE%89&startDate=2016-02-12&backDate=&flightType=oneWay"
response = urllib2.urlopen(url)
cont= response.read()
soup=BeautifulSoup(cont,"lxml")
for item in soup.select('.today-item'):
    t=item.select('span')[0].text

    import smtplib  
    from email.mime.text import MIMEText  # 引入smtplib和MIMEText

    host = 'smtp.163.com' 
    port = 25 
    sender = 'imlixiaofan@163.com' 
    pwd = 'xxxxxxxxxxxx'  
    receiver = 'imlixiaofan@163.com' 
    body= '2016-02-12:Guilin To Xian:' + t 

    msg = MIMEText(body, 'html') 
    msg['subject'] = 'Qunaer--air ticket price' 
    msg['from'] = sender  
    msg['to'] = receiver  

    s = smtplib.SMTP(host, port)  
    s.login(sender, pwd)  
    s.sendmail(sender, receiver, msg.as_string())  


    print 'DONE!'  


