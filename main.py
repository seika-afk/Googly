import pandas as pd  
import pyfiglet
from InquirerPy import inquirer
import random
import datetime  
import os

log_dir = os.path.expanduser("~/.googly")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "logs.txt")


allqns = pd.read_csv("~/wonderland/wonders/googly/data/google_lcs.csv")

#range 0-5.91
pyfiglet.Figlet("big")
f=pyfiglet.figlet_format("Googly",font="mini")
print(f)

num_qns=inquirer.select(
        message="Choose Number of Questions :",
        choices=["> 2" , "> 3", "> 5"]


        ).execute()

if num_qns=="> 2":
    num_qns=2
elif num_qns=="> 3":
    num_qns=3
else:
    num_qns=5

solved=[]
for i in range(num_qns):
    num=random.randint(0,864)
    qn=allqns.iloc[num].to_dict()
    print(f"> Question : {qn['ID']}  \n {qn['Title']}")
    
    print(">> Difficulty : ",qn['Difficulty'])
    solved.append([qn['Title'],qn['ID']])
    print("---------------------------------------")
    input("> Enter to Next ")

with open(log_path,'a') as f:
    f.write(str(datetime.datetime.now())+str(solved)+"\n")

print("> Good work buddy :) !!")

