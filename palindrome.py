import math
n=str(input("please enter a positive integer: "))#input
mir=len(n)/2
mir=math.floor(mir)
def palindrome(num):
        if (num>=0 and num[0]==num[len(num)] and num.is_integer()):
            for i in range(1,mir):
                    if num[i]==num[len(num)-i]:
                        print("processing:...")
                        i+=i
                        print ("Yeah "+num+" is a palindrome")
                    else:
                        print "Meh..."+num+" isn't a palindrome"
        else:
            print(num+" isn't a palindrome, or maybe not a positive integer")
            palindrome(n)