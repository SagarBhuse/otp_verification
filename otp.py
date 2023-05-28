import tkinter as tk
import smtplib
import random


otp = str(random.randint(200000,999999))

smtp_server = "smtp.gmail.com"
port = 587  
sender_email = "sagarbhuse18@gmail.com"
password = "dqulnfwhvbdlghmx"
receiver_email = ""

def send_email():
    global otp, receiver_email

    receiver_email = email_entry.get()
    message = f"Subject: OTP Verification\n\n OTP is {otp}"
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def verify_otp():
    user_input = otp_entry.get()
    if user_input == otp:
        result_label.config(text="OTP verified")
    else:
        result_label.config(text="OTP Not verified")

root = tk.Tk()
root.title("OTP_verified_Py")
root.iconbitmap(r'password__1__IAq_icon.ico')
root.geometry("300x200")

email_label = tk.Label(root, text="Enter your email:",bg="black",fg="white")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

send_button = tk.Button(root, text="Send OTP", command=send_email,bg="green",fg="white")
send_button.pack()

otp_label = tk.Label(root, text="Enter OTP:",bg="red",fg="black")
otp_label.pack()

otp_entry = tk.Entry(root)
otp_entry.pack()

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp,bg="green",fg="white")
verify_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()