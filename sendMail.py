import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()
conn.login('rushab.bayas@gmail.com', '123rbs456')
conn.sendmail('rushab.bayas@gmail.com', 'vrushab.bayas@gmail.com',
              'Subject:My first email sending script\n\nDeal Vrushab,\n\nI am proud of you ,You are doing well. \n\n keep it up\n\n Thank you,\n\nVrushab Bayas')
conn.quit()
