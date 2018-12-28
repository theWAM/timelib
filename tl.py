# timelibWAM Functions        12.26.18                                      =
# © Woody Allen Montilus 2018                                            =
#                                                                        =
# ========================================================================

import sys
import email
import smtplib
import imaplib
import time as t
import tkinter as tk
from timelibWAM import tx
from tkinter import ttk
from pathlib import Path    
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# = Best Setup ======================
# Copy and paste this bad boy:
#
# from timelibWAM import *
#
#       try:
#           s = tl.start() 
#
#           *your code*
#
#           tl.send_frame_end()
#       
#       except Exception as e:
#           tl.error_alert()
#
# ===================================

# = start() =========================
# ===================================
# Begins run timer
#
# After importing timelibWAM, use this function to start the timer
# save the time returned in a variable, like s:
#
#           s = tl.start()
#
# You'll use that variable later!
# ===================================
def start():
    start = t.time()
    return start

# = print_end() =====================
# ===================================
# Ends run timer
#
# If you don't want any pop ups or texts, you can print
# the run time using this function:
#
#           tl.print_end(s)
#                        ^
#                        |
# the variable from start() 
# ===================================
def print_end(start):
    # Logs end time
    end = t.time()

    # Calculates difference aka run time
    diff = end - start
    print()
    print("Execution Time: "+ str(diff))

    # Returns value calculated
    return diff

# = frame_end(start) ================
# ===================================
# Ends run timer
#
# Use if you just want a popup to let you know the run time
#
#           tl.frame_end(s)
#                        ^
#                        |
# the variable from start() 
# ===================================
def frame_end(start):

    # Runs print_end and extracts run time difference
    diff = print_end(start)

    # Draws frame detailing run time
    popup = tk.Tk()
    popup.title("Program Completed")

    ttk.Label(popup, text = "Hey! " + str(Path(sys.argv[0]).name) + " is done.\n\n Execution Time: " + str(diff), font = "System 16 bold").grid()

    # Draws buttons OK and Destroy Everything
    btn_frame = ttk.Frame(popup)
    btn_frame.grid()
    
    # OK destroys popup frame
    ttk.Button(btn_frame, text = "OK", command = popup.destroy).grid(row=0, column=0)
    
    #Destroy Everything shuts down entire program
    ttk.Button(btn_frame, text = "Destroy Everything", command = quit).grid(row=0, column=1)

# = send_end(start) =================
# ===================================
# Ends run timer
#
# Use if you just want a text 
#
#           tl.send_end(s)
#                        ^
#                        |
# the variable from start() 
# ===================================
def send_end(start):
    
    # Logs into gmail using provided email/password
    addy = "runtimeemail@gmail.com"
    pwd = "f=yq9rp}t$`47T@2YPv5tTj;`8H/'$:#eRTvrbK,syWL8RzfH@r=w<"
    s = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
    s.starttls()
    s.login(addy, pwd)

    # Logs end time and returns run time
    diff = print_end(start)

    # Reads document created by mail_ready and sends message to contact given
    f = open("timelibContactDoc.txt","r")
    contact = f.read()
    message = "............................\n Hey! \n" 
    message = message + str(Path(sys.argv[0]).name) 
    message = message + " is done.\n\n Execution Time: " + str(diff) + " seconds"

    msg = MIMEMultipart()

    msg['From'] = addy
    msg['To'] = contact

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)

    return diff

# = send_frame_end(start) ===========
# ===================================
# Ends run timer
#
# Use if you want a popup and a text 
#
#           tl.send_frame_end(s)
#                             ^
#                             |
# the variable from start() ---
#
# ===================================
def send_frame_end(start):
    diff = send_end(start)

    # Draws frame detailing run time
    popup = tk.Tk()
    popup.title("Program Completed")

    ttk.Label(popup, text = "Hey! " + str(Path(sys.argv[0]).name) + " is done!\n\n Execution Time: " + str(diff), font = "System 16 bold").grid()

    # Draws buttons OK and Destroy Everything
    btn_frame = ttk.Frame(popup)
    btn_frame.grid()
    
    # OK destroys popup frame
    ttk.Button(btn_frame, text = "OK", command = popup.destroy).grid(row=0, column=0)
    
    #Destroy Everything shuts down entire program
    ttk.Button(btn_frame, text = "Destroy Everything", command = quit).grid(row=0, column=1)

# = frame_alert() ===================
# ===================================
# Alerts user
#
# Use if you just want a popup error message
#
#       try:
#           s = tl.start() 
#
#           your code
#
#           tl.one_of_our_ending_functions()
#       
#       except Exception as e: <--------
#           tl.frame_alert()            |
#                                       |
#       Screens for any errors types ---
#
# ===================================
def frame_alert():

    # Draws frame detailing run time
    popup = tk.Tk()
    popup.title("Program Completed")

    ttk.Label(popup, text = "Hey! \n One or more errors were found in " + str(Path(sys.argv[0]).name), font = "System 16 bold").grid()

    # Draws buttons OK and Destroy Everything
    btn_frame = ttk.Frame(popup)
    btn_frame.grid()
    
    # OK destroys popup frame
    ttk.Button(btn_frame, text = "I'll check it out", command = popup.destroy).grid(row=0, column=0)
    
    #Destroy Everything shuts down entire program
    ttk.Button(btn_frame, text = "Destroy Everything", command = quit).grid(row=0, column=1)

# = error_alert() ===================
# ===================================
# Alerts user
#
# Use if you want a popup and text for errors
#
#       try:
#           s = tl.start() 
#
#           your code
#
#           tl.one_of_our_ending_functions()
#       
#       except Exception as e: <--------
#           tl.error_alert()            |
#                                       |
#       Screens for any errors types ---
#
# ===================================
def error_alert():
    # Logs into gmail using provided email/password
    addy = "runtimeemail@gmail.com"
    pwd = "f=yq9rp}t$`47T@2YPv5tTj;`8H/'$:#eRTvrbK,syWL8RzfH@r=w<"
    s = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
    s.starttls()
    s.login(addy, pwd)

    # Reads document created by mail_ready and sends message to contact given
    f = open("timelibContactDoc.txt","r")
    contact = f.read()
    message = "............................\n Hey! \n" 
    message = message + "One or more errors were found in " + str(Path(sys.argv[0]).name) 

    msg = MIMEMultipart()

    msg['From'] = addy
    msg['To'] = contact

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)

    frame_alert()


# Module specific functions ==============================
# ========================================================

# Draws Provider List popup
def pvd_lst():
    ATT = "@txt.att.net"
    TMOBILE = "@tmomail.net"
    VERIZON ="@vtext.com"
    SPRINT = "@messaging.sprintpcs.com"
    VGMOBILE = "@vmobl.com"
    METROPCS = "@mymetropcs.com"

    pop = tk.Tk()
    pop.title("Provider List")

    ttk.Label(pop, text = "Provider List", font = "System 14 bold").grid(padx = 10, pady = 10)

    ttk.Label(pop, text = "Copy recipient provider and paste after their #").grid(padx = 10, pady = 10)

    labels_frame = ttk.Frame(pop)
    labels_frame.grid(padx = 10, pady = 10)

    ttk.Label(labels_frame, text = "AT&T:").grid(row = 0, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "T-Mobile:").grid(row = 1, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "Verizon:").grid(row = 2, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "Sprint:").grid(row = 3, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "Virgin Mobile:").grid(row = 4, column = 0, padx= 10)
    ttk.Label(labels_frame, text = "MetroPCS:").grid(row = 5, column = 0, padx= 10)

    ttk.Label(labels_frame, text = ATT).grid(row = 0, column = 1)
    ttk.Label(labels_frame, text = TMOBILE).grid(row = 1, column = 1)
    ttk.Label(labels_frame, text = VERIZON).grid(row = 2, column = 1)
    ttk.Label(labels_frame, text = SPRINT).grid(row = 3, column = 1)
    ttk.Label(labels_frame, text = VGMOBILE).grid(row = 4, column = 1)
    ttk.Label(labels_frame, text = METROPCS).grid(row = 5, column = 1)

    ttk.Button(pop, text = "OK", command = pop.destroy).grid()

    pop.mainloop()

# Draws Error popup
def error():
    error = tk.Tk()
    error.title("ERROR")

    er_frame = ttk.Frame(error)
    er_frame.grid(padx=20, pady=10)
    popup.geometry("+450+250")

    label = ttk.Label(pop_frame, text = "Uh oh! Something went wrong! Try again!")
    label.grid()

    b1_frame = ttk.Frame(pop_frame)
    b1_frame.grid(pady = 10)
    b1 = ttk.Button(pop_frame, text = "OK", default = "active", command = popup.destroy)
    b1.grid()

def doc_bool():
    try:
        f = open("timelibContactDoc.txt","r")
        return True
    except FileNotFoundError:
        return False

# Destroy's frame
def click_cancel():
    print("User pressed cancel")
    self.destroy()
    quit()

# When enter is pressed, mail_ready from timelibex is run
def send_request(event):

    print("Making send request...")

    try:
        # Signs into email using mail_ready function from timelibex
        tx.mail_ready(e_to.get())

    except Exception as e:
        error()

        print("...Request completed")

    # Closes window after info is gathered
    self.destroy()

# ========================================================
# ========================================================


# If the contact document has yet to be created,
# draw entry frame to accept it
if doc_bool() == False:

    # Draws info gathering frame =====================================================================

    self = tk.Tk()
    self.grid()
    self.geometry("+250+150")
    self.title("TextEm!")

    spacer_frame = ttk.Frame(self)
    spacer_frame.grid(pady=10)

    # Space for the entirety of the frame
    body_frame = ttk.Frame(self)
    body_frame.grid(padx=20, pady=10)

    # Space for header material
    header_div = ttk.Frame(body_frame)
    header_div.grid()

    # Draws labels in header
    ttk.Label(header_div, text = "RunTimeText (Gmail supported only)", font = "System 16 bold").grid()
    ttk.Label(header_div, text = "Enter phone#@provideraddress (i.e. 1234567890@txt.att.net)").grid()
    ttk.Label(header_div, text = "Click Provider List for provider specific addresses").grid()

    # Space for upcoming label and entry slot
    to_div = ttk.Frame(body_frame)
    to_div.grid()

    # Draws label
    ttk.Label(to_div, text = "Your # address:").grid(row = 3, column = 0, padx = 10, pady = 15)

    #Entry space - pressing enter runs mail_ready from timelibex
    e_to = ttk.Entry(to_div)
    e_to.grid(row = 3, column = 1, padx = 10, pady = 15)
    e_to.bind("<Return>", send_request)

    # Space for upcoming button
    btns = ttk.Frame(body_frame)
    btns.grid(padx=10, pady=10)

    # Draws Provider List button
    ttk.Button(btns, text = "Provider List", command = pvd_lst).grid()

    # Cancel button and Exit button run click_cancel function
    self.protocol("WM_DELETE_WINDOW", click_cancel)
    ttk.Button(btns, text = "Cancel", command = click_cancel).grid()
    #==================================================================================================

# Else, if contact document exists, just run user program
else:
    print("Information needed is already in system")