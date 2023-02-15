import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('justkiddingboat@gmail.com','just123kidding')
smtpObj.sendmail("justkiddingboat@gmail.com","michael.byrne@vice.com","go to bed!")
smtpObj.quit()
