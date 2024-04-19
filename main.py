# Undercover
import random,string
from models.model import terminology
    
def uc_script(intellegence,officiality,age,gender,maturity,text):
    text=text.split()
    for _ in range(len(text)):
        for wordsblock in range(len(terminology)):
            for alternativesblock in range(len(terminology[wordsblock])):
                for intellegencelevelblock in range(len(terminology[wordsblock][alternativesblock])-1):
                    if text[_] == terminology[wordsblock][alternativesblock][intellegencelevelblock+1]:
                        for i in range(len(terminology[wordsblock])):
                            if int(intellegence) <= int(terminology[wordsblock][i][0]):
                                text[_]=terminology[wordsblock][i][random.randint(1,len(terminology[wordsblock][i])-1)]
    '''for _ in range(len(text)):
        for wordsblock in range(len(maturity)):
            for alternativesblock in range(len(maturity[wordsblock])):
                for maturitylevelblock in range(len(maturity[wordsblock][alternativesblock])-1):
                    if text[_] == maturity[wordsblock][alternativesblock][maturitylevelblock+1]:
                        for i in range(len(maturity[wordsblock])):
                            if int(maturity) <= int(maturity[wordsblock][i][0]):
                                text[_]=maturity[wordsblock][i][random.randint(1,len(maturity[wordsblock][i])-1)]'''
    for i in range(len(text)):text[i]=text[i]+" "
    if officiality >= 3:
        for i in range(len(string.ascii_lowercase)):
            if text[0][0] == string.ascii_lowercase[i]:text[0]=string.ascii_uppercase[i]+text[0][1:]
    text=''.join(text)
    if officiality >= 4:
        for i in range(len(string.ascii_lowercase)):text=text.replace(str(". "+string.ascii_lowercase[i]),str(". "+string.ascii_uppercase[i]))
    return(text)
print(uc_script(int(input("   Enter Intellegence ┃ ")),1,"","","",input("           Enter Text ┃ ")))#input("            Enter Age ┃ "),input("         Enter Gender ┃ "),input("       Enter Nativity ┃ "))
