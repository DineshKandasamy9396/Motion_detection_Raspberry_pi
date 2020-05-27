import os
from subprocess import call
i=1
from email import Encoders
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
USERNAME = "xxxxxxxxxxxx@gmail.com"
PASSWORD = "kngjgfcgj"
while i==1:
    path="/home/pi/"
    def sendMail(to, subject, text, files=[]):
        assert type(to)==list
        assert type(files)==list

        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = COMMASPACE.join(to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach( MIMEText(text) )
        for file in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(file,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(file))
            msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(USERNAME,PASSWORD)
        server.sendmail(USERNAME, to, msg.as_string())
        server.quit()
   def upload_files():
        global a
        a=[]
        global c
        c=1
        global e
        e=0
       global b
        b=0
        global d
        d=0
        if  not os.path.exists(path):
             return
        dir_list = os.listdir(path)
        for file_name in dir_list:
            if ".jpg" in file_name:
                if c==1:
                    from twilio.rest import TwilioRestClient
                    account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXX"
                    auth_token = "YYYYYYYYYYYYYYYYYYYYYYYYYYY"
                    client = TwilioRestClient(account_sid, auth_token)
                    call = client.calls.create(to="++7894561230",  
                           from_="+12015286683", 
                          url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
                    print call.sid
                    c=0
                if b<5:
                    a.append(file_name)
               if b==5:
                   sendMail( ["mnmnmnmnm@gmail.com"], "Intruder Photos","Kindly take appropriate action",a )
                    for i in range(5):
                        os.remove("/home/pi/"+a[i])
                b=b+1
                if b>5:
                     os.remove("/home/pi/"+file_name)
if __name__ == "__main__":
        upload_files()
       
