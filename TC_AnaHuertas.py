import random #so random values can be generated
import os #so the screen can be clean
import pyperclip #so the email can be copied in the clipboard
timestimation=['before the next working day','in the next few hours','during today']#declare the list where the posible options for time are contained
#declare the array with the standard emails sections
message=[['Hello','\n\nThank you for reaching out. We recieved your message and will do our best to get back to you','\nIf you need help immediately, please call us, or see if our Help Center could be helpfull.\n\nHave a beautiful evening!\n\nRegards,'],
    ['Hi','\n\nThanks so much for your email! This auto-reply is just to let you know...\n\nWe recieved your email and will get back to you with a human response','\n\nFor general questions, check out our Help Center, it might help.\nIf you need help immediately, please give us a call.\n\nWe look forward to chatting soon!\n\nCheers,'],
    ['Hi','\n\nThanks for getting in touch. We are working on your request and will come back to you','\n\nDo you know that we have a Help Center for walkthroughs and answers to FAQs?\nPlease give us a call if you need immediate help.\n\nCan´t wait to connect with you personally!\n\nRegards,']]
os.system('cls')#this cleans the screen
reciever=input('Who will recieve this email?\n').capitalize() #in this case Maggie #it will write the first letter of the name in capital letter
reciever+=','
os.system('cls')
sender=input('Who will sign this email?\n').capitalize() #in this case Gloria
os.system('cls')
print(('Now you´ll choose the expected time that will take to answer the email:\n1- Before the next working day\n2- In the next few hours\n3- During today\nIf you want it to be randomly selected just press any other buttom\n'))
jj=input('Select one option\n')
if jj=="1"or jj=="2"or jj=="3":
    j=int(jj)-1
else:
    print('The time frame will be randomly seleted.')
    j=random.randint(0,2)
a=timestimation[j]
a+='.'
os.system('cls')
print('This is the final step.\nYou need to select the standard email that you want to use. You´ll be offered 3 different options.\n')
for i in range(len(message)):
    print("Option ",i+1)
    print(message[i][0],reciever,message[i][1],a,message[i][2])
    print(sender)
    print('\n\n')
kk=input('Select option 1, 2 or 3. If you want it to be selected randomly just press any other buttom.\n')
if kk=="1"or kk=="2"or kk=="3":
    k=int(kk)-1
else:
    print('The time frame will be randomly seleted.')
    k=random.randint(0,2)
os.system('cls')
print(message[k][0],reciever,message[k][1],a,message[k][2])
print(sender)
le=message[k][0]+' '+reciever+message[k][1]+a+message[k][2]+'\n'+sender
pyperclip.copy(le)
fin=input("The email has been copied on the clipboard")