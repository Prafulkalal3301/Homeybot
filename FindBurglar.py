from time import sleep
import smtplib,ssl
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders 
import cv2

import Clearup as c
import time
import numpy as np
import random
import string
import os




from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
img_counter=0
account_sid = 'AC----f2-------cc-------' 
auth_token = '6---------890---819------' 
client = Client(account_sid, auth_token) 








def DetectBurglar():
    global img_name
    i=0
    img_counter=0
    cap = cv2.VideoCapture(0)
    frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    print(frame1.shape)
    while cap.isOpened():
        
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            
            
            (x, y, w, h) = cv2.boundingRect(contour)
            

            if cv2.contourArea(contour) < 500:
                continue
            

            
            if(i<50):

                
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite('Images/'+img_name, frame1)
                print("{} Caught".format(img_name))
              
            
                
                m='Some activity has been found. Check your mail'
                client = Client(account_sid, auth_token) 
                time.sleep(2) 
                message = client.messages.create(
                #media_url='https://C:/Users/hp/Downloads/Weqw/Images/img_name',
      
                              from_='whatsapp:+14-------',  
                              body=m,      
                              to='whatsapp:+91---------' 
                          ) 
 
                
                i+=10
                img_counter += 1
                
                imname="{}".format(img_name)
                
                toaddr = 'receivergmail'      # To id 
                me = 'yourgmail'          # your id
                subject = "Alert"+str(i)              # Subject
  
                msg = MIMEMultipart()  
                msg['Subject'] = subject  
                msg['From'] = me  
                msg['To'] = toaddr  
                msg.preamble = "test "   
                #msg.attach(MIMEText(text))  
              
                part = MIMEBase('application', "octet-stream")  
                part.set_payload(open("Images/"+img_name, "rb").read())  
                encoders.encode_base64(part)  
                part.add_header('Content-Disposition', 'attachment; filename="image.jpg"')   # File name and format name
                msg.attach(part)  
              
                try:  
                   s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
                   s.ehlo()  
                   s.starttls()  
                   s.ehlo()  
                   s.login(user = 'yourgmail@gmail.com', password ='yourgmailpassword' )  # User id & password
                   #s.send_message(msg)  
                   s.sendmail(me, toaddr, msg.as_string())  
                   s.quit()  
                #except:  
                #   print ("Error: unable to send email")    
                except SMTPException as error:  
                      print ("Error")                # Exception
               
                c.remove_img('Images/',imname)
            
            
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
            
        #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        
        image = cv2.resize(frame1, (1280,720))
        out.write(image)
        cv2.imshow("feed", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(40) == 27:
            break
    
          
    cv2.destroyAllWindows()
    cap.release()
    out.release()



