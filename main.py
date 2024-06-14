try:
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
    try:from models.model import *
    except Exception as e: importMsgs("error","Model")
    importMsgs("success.","Model")
    print("━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[ 2: UNDERCOVER     ] ┃ Run \x1b[0;1m/help\x1b[0m Or Read \x1b[0;1mREADME.md\x1b[0m For Info.")
    print("──────────────────────┸────────────────────────────────────────────")
    def convert(formality,intellegence,officiality,gender,maturity,text):
        text=text.split()
        for _ in range(len(text)):
            for wordsBlock in range(len(terminology)):
                for alternativesBlock in range(len(terminology[wordsBlock])):
                    for formalitylevelBlock in range(len(terminology[wordsBlock][alternativesBlock])-1):
                        if text[_] == terminology[wordsBlock][alternativesBlock][formalitylevelBlock+1]:
                            for i in range(len(terminology[wordsBlock])):
                                if int(formality) <= int(terminology[wordsBlock][i][0]):
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
        if officiality <= 3:text.replace(" I "," i ")
        if officiality >= 3:text.replace(" i "," I ")
        if intellegence >= 3:
            omissions
        return(text)
    print(convert(
        int(input("[ Formality ] determines the position of the opponent:\n   1 : Includes high frequencies of slang seen in Close friends.\n   2 : Uses major frequencies of slangs seen in friends.\n   3 : Incompletely formal english seen on internet persona.\n   4 : Formal english. First meetings, real life relations, etc.\n   5 : Very formal english. Used against Higher-ups, emails.\n──────────────────────┰────────────────────────────────────────────\n      Enter Formality ┃ ")),
        int(input("──────────────────────┸────────────────────────────────────────────\n[ Intellegence ] determines the intellegence seen in the text:\n   1 : Uneducated english with wrong grammar.\n   2 : English with major grammar errors.\n   3 : English with minor mistakes and grammar errors.\n   4 : Grammar errors rarely seen in sentences.\n   5 : Strict, correct usage of english.\n──────────────────────┰────────────────────────────────────────────\n   Enter Intellegence ┃ ")),
        int(input("    Enter Officiality ┃ ")),
        "",
        "",
        input("           Enter Text ┃ ")))
except KeyboardInterrupt:print("\nProgram Aborted.")
except Exception as e:print("\nProgram Aborted due to error: "+e)
