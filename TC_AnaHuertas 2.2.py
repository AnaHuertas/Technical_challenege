#with string interpolation!!!!!!!!!
import os
import random
reciever = 'Maggie'
sender = 'Gloria'
timeframelist=['before the next working day','in the next few hours','during today']#declare the list where the posible options for time are contained
os.system('cls')
print(f'Now you´ll choose the expected time that will take to answer the email:\n1- {timeframelist[0]}\n2- {timeframelist[1]}\n3- {timeframelist[2]}\nIf you want it to be randomly selected just press any other buttom\n')
jj=input('Select one option\n')
if jj=="1"or jj=="2"or jj=="3":
    j=int(jj)-1
else:
    print('The time frame will be randomly seleted.')
    j=random.randint(0,2)
timeframe=timeframelist[j]
email1 = ['Hello ','! we will answer ',' This is ']
email=email1
print(f'Hello {reciever}! we will answer {timeframe} This is {sender}')
print(f'{email[0]}{reciever}{email[1]}{timeframe}{email[2]}{sender}')