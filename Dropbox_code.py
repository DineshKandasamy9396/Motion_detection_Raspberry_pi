import os
from subprocess import call
i=1
while i==1:
    path="/home/pi/"
    def upload_files():
        global c
        c=1
        global b
        b=0
        if  not os.path.exists(path):
            return
        dir_list = os.listdir(path)
        for file_name in dir_list:
         if ".jpg" in file_name:
                if c==1:
              #call notification
                    from twilio.rest import TwilioRestClient #twilio user account credentials allows this program to access the account for call or message  service
                    account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" #user sid
                    auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" # user authentication
                    client = TwilioRestClient(account_sid, auth_token) #
                    call = client.calls.create(to="+917896451230",  from_="+12015286683", 
                    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient") #url access service opted for, either call or msg (here it is call)
                    print call.sid
                    c=0
                if b<5:
                    photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/"+file_name +" "+file_name  #local_storage 
                    os.system(photofile)
                    os.remove("/home/pi/"+file_name)
                b=b+1
                if b>5:
                    os.remove("/home/pi/"+file_name)

 if __name__ == "__main__":
      upload_files()
