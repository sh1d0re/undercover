welcomemsg="┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃   ╭──╮   ┃   ╻ ╻ ┏┓╻ ┏━╮ ┏━╸ ┏┓  ┏━╸ ┏━┓ ╻ ╻ ┏━╸ ┏┓             ┃\n┃    ╭─╯   ┃   ┃ ┃ ┃┃┃ ┃ ┃ ┣━╸ ┣┻┓ ┃   ┃ ┃ ┃┏┛ ┣━╸ ┣┻┓            ┃\n┃    .     ┃   ┗━┛ ╹┗┛ ┗━╯ ┗━╸ ╹ ╹ ┗━╸ ┗━┛ ┗┛  ┗━╸ ╹ ╹            ┃\n┡━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩\n│                     PROGRAMMER : Sh1d0re                        │\n│                        LICENSE : GPL-v3                         │\n│                       LANGUAGE : Python                         │\n└────────────────────────────────┴────────────────────────────────┘"
print(welcomemsg)
def importMsgs(status,prompt:str):
    for i in range(10-len(str(prompt))):prompt=" "+prompt
    if "error" in status:
        print("    "+prompt+" Module ┠╴\x1b[31mERROR\x1b[39;49m\n──────────────────────┸────────────────────────────────────────────\n\x1b[31m"+str(e)+"\x1b[0m")
        if "." in status:print("──────────────────────┰────────────────────────────────────────────")
        else:
            print("───────────────────────────────────────────────────────────────────\n\x1b[31;1mProgram aborted due to error. Try contacting the github repo if you see no solution.\x1b[0m\n")
            quit()
    elif "success" in status:
        if "." in status:print("    "+prompt+" Module ┖╴\x1b[32mSUCCESS\x1b[39;49m")
        else:print("    "+prompt+" Module ┠╴\x1b[32mSUCCESS\x1b[39;49m")
print("━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[ 1: LOADING    PyP ] ┃ \x1b[31mEnter \x1b[31;1mControl&C\x1b[0m\x1b[31m To Abort. Leave To Proceed.\x1b[0m")
try:import random
except Exception as e: importMsgs("error","Random")
importMsgs("success","Random")
try:import string
except Exception as e: importMsgs("error","String")
importMsgs("success","String")
try:from models.model import terminology
except Exception as e: importMsgs("error","Model")
importMsgs("success.","Model")
print("━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[ 2: UNDERCOVER     ] ┃ Run \x1b[0;1m/help\x1b[0m Or Read \x1b[0;1mREADME.md\x1b[0m For Info.")
print("──────────────────────┸────────────────────────────────────────────\n[ Rank ] is the position and hierarchy you are in:\n 1 : ")
def undercover(rank,intellegence,officiality,gender,maturity,text):
    text=text.split()
    for _ in range(len(text)):
        for wordsBlock in range(len(terminology)):
            for alternativesBlock in range(len(terminology[wordsBlock])):
                for ranklevelBlock in range(len(terminology[wordsBlock][alternativesBlock])-1):
                    if text[_] == terminology[wordsBlock][alternativesBlock][ranklevelBlock+1]:
                        for i in range(len(terminology[wordsBlock])):
                            if int(rank) <= int(terminology[wordsBlock][i][0]):
                                text[_]=terminology[wordsBlock][i][random.randint(1,len(terminology[wordsBlock][i])-1)]
    
    for i in range(len(text)):text[i]=text[i]+" "
    text=''.join(text)
    if officiality >= 3:
        text=list(text)
        for i in range(len(string.ascii_lowercase)):
            if text[0][0] == string.ascii_lowercase[i]:text[0]=string.ascii_uppercase[i]+text[0][1:]
        text=''.join(text)
    if intellegence >= 2:
        for i in list('aeiou'):text=text.replace(" a "+i," an "+i)
        for i in list('bcdfghjklmnpqrstvwxyz'):text=text.replace(" an "+i," a "+i)
    if intellegence == 1:
        for i in list('aeiou'):text=text.replace(" an "+i," a "+i)
        for i in list('bcdfghjklmnpqrstvwxyz'):text=text.replace(" a "+i," an "+i)
    if officiality >= 4:
        for i in range(len(string.ascii_lowercase)):text=text.replace(str(". "+string.ascii_lowercase[i]),str(". "+string.ascii_uppercase[i]))
    if officiality >= 2:
        text.replace(" i "," I ")
    if intellegence >= 3:
        omissions=[["youre","dont","cant","its","musnt","aint","shouldnt",""],["you're","don't","can't","it's","musn't","ain't","shouldn't","aren't",""],["you are","do not","can not","it is","must not","ain't","should not",""]]
    return(text)
print(undercover(int(input("           Enter Rank ┃ ")),int(input("   Enter Intellegence ┃ ")),int(input("    Enter Officiality ┃ ")),"","",input("           Enter Text ┃ ")))
