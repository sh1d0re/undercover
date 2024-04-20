# Undercover
import random,string
from models.model import terminology
    
def uc_script(rank,intellegence,age,gender,maturity,text):
    text=text.split()
    for _ in range(len(text)):
        for wordsBlock in range(len(terminology)):
            for alternativesBlock in range(len(terminology[wordsBlock])):
                for ranklevelBlock in range(len(terminology[wordsBlock][alternativesBlock])-1):
                    if text[_] == terminology[wordsBlock][alternativesBlock][ranklevelBlock+1]:
                        for i in range(len(terminology[wordsBlock])):
                            if int(rank) <= int(terminology[wordsBlock][i][0]):
                                text[_]=terminology[wordsBlock][i][random.randint(1,len(terminology[wordsBlock][i])-1)]
    '''for _ in range(len(text)):
        for wordsBlock in range(len(maturity)):
            for alternativesBlock in range(len(maturity[wordsBlock])):
                for maturitylevelblock in range(len(maturity[wordsBlock][alternativesBlock])-1):
                    if text[_] == maturity[wordsBlock][alternativesBlock][maturitylevelblock+1]:
                        for i in range(len(maturity[wordsBlock])):
                            if int(maturity) <= int(maturity[wordsBlock][i][0]):
                                text[_]=maturity[wordsBlock][i][random.randint(1,len(maturity[wordsBlock][i])-1)]'''
    for i in range(len(text)):text[i]=text[i]+" "
    text=''.join(text)
    if intellegence >= 3:
        for i in range(len(string.ascii_lowercase)):
            if list(text)[0][0] == string.ascii_lowercase[i]:text[0]=string.ascii_uppercase[i]+text[0][1:]
    if intellegence >= 2:
        for i in list('aeiou'):text=text.replace(" a "+i," an "+i)
        for i in list('bcdfghjklmnpqrstvwxyz'):text=text.replace(" an "+i," a "+i)
    if intellegence == 1:
        for i in list('aeiou'):text=text.replace(" an "+i," a "+i)
        for i in list('bcdfghjklmnpqrstvwxyz'):text=text.replace(" a "+i," an "+i)
    if intellegence >= 4:
        for i in range(len(string.ascii_lowercase)):text=text.replace(str(". "+string.ascii_lowercase[i]),str(". "+string.ascii_uppercase[i]))
    return(text)
print(uc_script(int(input("           Enter Rank ┃ ")),int(input("   Enter Intellegence ┃ ")),"","","",input("           Enter Text ┃ ")))#input("            Enter Age ┃ "),input("         Enter Gender ┃ "),input("       Enter Nativity ┃ "))
