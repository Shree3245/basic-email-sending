import smtplib


fromaddr = ''
toaddrs  = ''
msg = 'Spam email Test'  

username = ''
password = ''

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()