import email
import smtplib
import imaplib
import time as t
import tkinter as tk
from tkinter import ttk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Logs into provided gmail and logs contact address in txt file
class mail_ready():

    def __init__(self, to):

        # Provided email information
        addy = "runtimeemail@gmail.com"
        pwd = "f=yq9rp}t$`47T@2YPv5tTj;`8H/'$:#eRTvrbK,syWL8RzfH@r=w<"
        
        # Extracts info given by original entry box
        self.to = to

        # email related libraries' material, word for word
        s = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
        s.starttls()

        try:

            # Attempting to log into default email
            s.login(addy, pwd)

            print("Email successfully authenticated...")

            print("Writing contact document...")

            # Creating and writing entry material in txt file
            f = open("timelibContactDoc.txt","w+")
            f.write(self.to)
            f.close()

            print("...Document successfully written")
	            
        except Exception as e:

            # If attempt to log in fails, user is alerted via popup
            print("Failed email authentication")
	            
            priv = tk.Tk()
            priv.title("ERROR")

            ttk.Label(priv, text = "We had a problem accessing our email. Please try again at a later time").grid()
            ttk.Button(priv, text = "OK", command = priv.destroy).grid()

            priv.mainloop()




