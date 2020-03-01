# with string interpolation
import os
import random
import pyperclip

os.system('cls')  # this cleans the screen
# in this case Maggie #it will write the first letter of the name in capital letter
reciever = input('Who will recieve this email?\n').capitalize()

os.system('cls')
# in this case Gloria
sender = input('Who will sign this email?\n').capitalize()

# declare the list where the posible options for time are contained
timeframelist = ['before the next working day',
                 'in the next few hours', 'during today']

os.system('cls')
print(
    f'Now you´ll choose the expected time that will take to answer the email:\n1- {timeframelist[0]}\n2- {timeframelist[1]}\n3- {timeframelist[2]}\nIf you want it to be randomly selected just press any other buttom\n')
jj = input('Select one option\n')

# this loop select the time option according with the user selection.
if jj == "1"or jj == "2"or jj == "3":
    j = int(jj)-1
else:  # if the user didn't choose 1,2 or 3 it will be randomly selected
    print('The time frame will be randomly seleted.')
    j = random.randint(0, 2)

timeframe = timeframelist[j]

# emailarray is an array containing 3vectors. Each vector is a different option of standar email
emailarray = [['Hello', 'Thank you for reaching out. We recieved your message and will do our best to get back to you', 'If you need help immediately, please call us, or see if our Help Center could be helpfull.\n\nHave a beautiful evening!\n\nRegards,'],
              ['Hi', 'Thanks so much for your email! This auto-reply is just to let you know...\n\nWe recieved your email and will get back to you with a human response',
                  'For general questions, check out our Help Center, it might help.\nIf you need help immediately, please give us a call.\n\nI look forward to chatting soon!\n\nCheers,'],
              ['Hello', 'Thanks for getting in touch. We are working on your request and will come back to you', 'Have you taken a look in our fantastic Help Center? It has plenty of walkthroughs and answers to FAQs.\nPlease give us a call if you need immediate help.\n\nCan´t wait to connect with you personally!\n\nRegards,']]

os.system('cls')
print('This is the final step.\nYou need to select the standard email that you want to use. You´ll be offered 3 different options.\n')

# this loop shows to the user how the 3possible email would look like
for i in range(len(emailarray)):
    print(f'Option {i+1}')
    email = emailarray[i]
    print(
        f'{email[0]} {reciever},\n\n{email[1]} {timeframe}.\n\n{email[2]}\n{sender}')
    print('\n')

kk = input('Select option 1, 2 or 3. If you want it to be selected randomly just press any other buttom.\n')

if kk == "1"or kk == "2"or kk == "3":
    k = int(kk)-1
else:  # if the user didn't choose 1,2 or 3 it will be randomly selected
    print('The time frame will be randomly seleted.')
    k = random.randint(0, 2)

email = emailarray[k]

os.system('cls')
print('This is the selected version for the response:\n')
# this shows in the screen the selected version of the email
print(
    f'{email[0]} {reciever},\n\n{email[1]} {timeframe}.\n\n{email[2]}\n{sender}')
print('\n')

# this copy the email on the computer clipboard soit can be pasted wherever
pyperclip.copy(
    f'{email[0]} {reciever},\n\n{email[1]} {timeframe}.\n\n{email[2]}\n{sender}')

# stops the program until enter is press so the user can read the information
fin = input("The email has been copied on the clipboard")
