

def mcd(fraction):
    myList = fraction.split("/")
    divisors_0 = [x for x in range(1,int(int(myList[0])/2)+1) if int(myList[0])%x==0]
    divisors_1 = [x for x in range(1,int(int(myList[1])/2)+1) if int(myList[1])%x==0]
    divisors_0.append(int(myList[0]))
    divisors_1.append(int(myList[1]))
    for i in divisors_0[::-1]:
        if i in divisors_1:
            myList = [str(int(int(myList[0])/i)),str(int(int(myList[1])/i))]
            return  '/'.join(myList)
    


def main():
    while True:
        try:
            fraction = input("Give a fraction: ")
            if int(fraction.split('/')[1])== 0:
                print("You gave zero as denominator,please try again!")
                continue
            else:
                break
        except:
            print("Your input is not a fraction,please try again!")
            continue    
        
        
    print("The answer is:",mcd(fraction))






main() 
