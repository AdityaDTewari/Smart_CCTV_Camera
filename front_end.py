from tkinter import *
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
window = Tk()
window.title("GUI")
window.geometry('600x280')
title_frame = Frame(window).grid(row = 0, column = 0)
image_frame = Frame(window).grid(row = 1, column = 0)
webcam_frame = Frame(window).grid(row = 1, column = 0)
video_frame = Frame(window).grid(row = 1, column = 0)
#title_frame
label1 = Label(title_frame, text = "Smart CCTV for Weapons Detection", font=("Arial
Bold", 25))
label1.grid(row=0, columnspan=15)
label0 = Label(title_frame, text = "Welcome User", font=("Arial Bold", 10))
label0.grid(row=1, columnspan=15)
#email function
def sendemail():
email = '' #email address here
password = '' #password here
47
send_to_email = '' #email address here
subject = 'CAM - 01'
message = 'ALERT ALERT ALERT'
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
msg.attach(MIMEText (message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
#image button function
def clicked():
data = subprocess.Popen(['./darknet','detect', 'yolov3_custom.cfg',
'yolov3_custom_5000.weights', txt2.get()], stdout = subprocess.PIPE)
output = data.communicate()
encode = 'utf-8'
str = output[0].decode(encode)
#if (str.find(txt2.get()) > -1 ):
str2 = str.replace(txt2.get(),'filename')
if (str2.find('Knife') != -1 or str2.find('Handgun') != -1):
sendemail()
label4 = Label(image_frame, text = "Weapons have been detected and an
email has been sent", font=("Arial Bold", 10))
label4.grid(row=4, columnspan=15)
else:
label4 = Label(image_frame, text = "Weapons have not been detected",
font=("Arial Bold", 10))
48
label4.grid(row=4, columnspan=15)
#image_frame
label2 = Label(image_frame, text = "Image", font=("Arial Bold", 15))
label2.grid(row=2, column=0)
txt2 = Entry(image_frame, width=10)
txt2.grid(row=2, column=1)
btn2 = Button(image_frame, text = "Result", command=clicked)
btn2.grid(row=3, column=1)
#webcam button function
def pushed():
subprocess.Popen(['./darknet', 'detector', 'demo', 'coco.data', 'yolov3_custom.cfg',
'yolov3_custom_5000.weights'])
#webcam_frame
label4 = Label(image_frame, text = "Webcam", font=("Arial Bold", 15))
label4.grid(row=2, column=7)
btn4 = Button(image_frame, text = "Result", command=pushed)
btn4.grid(row=3, column=7)
#video button function
def pressed():
data2 = subprocess.Popen(['./darknet', 'detector', 'demo', 'coco.data',
'yolov3_custom.cfg', 'yolov3_custom_5000.weights', txt3.get()], stdout = subprocess.PIPE)
output2 = data.communicate()
print(output2)
49
if (output2.find('Knife') != -1 or output2.find('Handgun') != -1):
sendemail()
label4 = Label(image_frame, text = "Weapons have been detected and an
email has been sent", font=("Arial Bold", 10))
label4.grid(row=4, columnspan=15)
else:
label4 = Label(image_frame, text = "Weapons have not been detected",
font=("Arial Bold", 10))
label4.grid(row=4, columnspan=15)
#video_frame
label3 = Label(video_frame, text = "Video", font=("Arial", 15))
label3.grid(row=2, column=13)
txt3 = Entry(video_frame, width=10)
txt3.grid(row=2, column=14)
btn3 = Button(image_frame, text = "Result", command = pressed)
btn3.grid(row=3, column=14)
window.mainloop()