#with string interpolation!!!!!!!!!
import os
import random
import paperclip
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
emailarray = [['Hello','we will answer','This is'],
    ['lala','lele','lili'],
    ['mama','meme','mimi']]
os.system('cls')
print('This is the final step.\nYou need to select the standard email that you want to use. You´ll be offered 3 different options.\n')
for i in range(len(emailarray)):
    print(f'Option {i+1}')
    email=emailarray[i]
    print(f'{email[0]} {reciever},\n\n{email[1]} {timeframe}.\n\n{email[2]}\n{sender}')
    print('\n')
kk=input('Select option 1, 2 or 3. If you want it to be selected randomly just press any other buttom.\n')
if kk=="1"or kk=="2"or kk=="3":
    k=int(kk)-1
else:
    print('The time frame will be randomly seleted.')
    k=random.randint(0,2)
email=emailarray[k]
os.system('cls')
print(f'{email[0]} {reciever},\n\n{email[1]} {timeframe}.\n\n{email[2]}\n{sender}')
pyperclip.copy(f'{email[0]} {reciever},\n\n{email[1]} {timeframe}.\n\n{email[2]}\n{sender}')
fin=input("The email has been copied on the clipboard")
#print(f'Hello {reciever}! we will answer {timeframe} This is {sender}')
#print(f'{email[0]}{reciever}{email[1]}{timeframe}{email[2]}{sender}')