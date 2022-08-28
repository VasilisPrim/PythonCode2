



def fibo(N):
    i=0
    j=1
    myList = [i,j]
    while myList[i]+myList[j]<=N:
        myList.append(myList[i]+myList[j])
        i+=1
        j+=1
    print(myList) #Το έβαλα για να φαίνεται η λίστα με τους αριθμούς fibonacci μαζί με τους πρώτους             
    return [x  for x in myList  if (0 not in [x%i for i in range(2,int(x/2)+1)]) and x not in [0,1]]
         #Επιστρέφει τους πρώτους αριθμούς απο τη δοθείσα λίστα.   
        
    


def main():
    while True:
        try:
            number = int(input("Give an integer: "))
            print(fibo(number))
            break
        except:
            print("This is not an integer!")



    
main()
