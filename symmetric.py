


#Προσπάθησα να λύσω την άσκηση με δύο τρόπους ψάχνοντας να βρω τον πιο
#αποδοτικό.Επίσης έβαλα και μια έτοιμη συνάρτηση για να λύσω το θέμα του τονισμού.

import unicodedata



def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def check():
    myword = input("Give a word :").upper().strip()
    no_Accents = remove_accents(myword)
    char = ""
    for i in list(no_Accents)[::-1]:
        char = char+i

    if  no_Accents== char:
        print("Is palindrome")
    else:
        print("No palindrome")


        

def check2():
    myword = input("Give a word :").upper().strip()
    no_Accents = remove_accents(myword)
    i=0
    j=len(myword)-1
    check = True
    while i<=j:
        if list(no_Accents)[i]== list(no_Accents)[j]:
            i+=1
            j-=1
            continue
        else:
            print("No palindrome")
            check=False
            break
        
    if check==True:
        print("Is palindrome")
    
    
    



check()
