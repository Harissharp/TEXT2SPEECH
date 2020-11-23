#importing and setting up
import pyttsx3
import csv
engine = pyttsx3.init()
#importing and setting up ^


engine.say("hi,i'm a calculator enter your 1st number")#having th e program say it then after make it readable
engine.runAndWait()
num1=input("hi,i'm a calculator enter your 1st number: ")#collecting the 1st number
num1=float(num1)

engine.say("What operation would you like to do?")#asking what operation
engine.runAndWait()
oper=input("What operation would you like to do?(* , + , -, /) :")

engine.say("enter the second number")#asking for second num
engine.runAndWait()
num2=input("enter the second number:")
num2=float(num2)#converting after

#depending on what operation it will do that one
if oper=="*":
    ans=num1*num2
if oper=="+":
    ans=num1+num2
if oper=="-":
    ans=num1-num2
if oper=="/":
    ans=num1/num2
#prints answer and says it
print(ans)
engine.say(ans)
engine.runAndWait



