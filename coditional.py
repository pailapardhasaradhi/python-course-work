data={'prasanth@gmail.com': '12@',
      'dinesh@gmail.com':'789!',
      'sanjay@gmail.com' :'456#',
      }
      
email,pwd=input('enter the email and pwd:').split()
      
if  data.get(email)==pwd:
    print('login succesful')
else:
    print('invalid login')
