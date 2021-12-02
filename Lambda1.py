#training for  functions , call and print them 

def getName(item):
    
    listItem=list(item) # makes a list , puts the Name and put insite a list 
    print(listItem)
    return listItem
  
def printName(item2) :
    count=0
    for i in item2:
        print(i,end='-') 
        if i==" ":
          count+=1
                 
    
def lengthName(lengy):    
    print("\nThe length of  your name  is  : " ,len(lengy))
    
  
item=str(input("Enter a name :"))
printName(getName(item))
lengthName(item)



  # print(len(value))
    # return(value)

#====================================================================

#trainig for  Lambda  

# x=lambda x:x+2
# print(x(4))


# x=int(input("Enter a number to Multiple  :"))
# numbers=lambda y:[( "hello",i*x) for i in range (1,6)]


# print(numbers(x))






# inputNumberA=int(input("Enter a number to be calculated "))
# inputNumberB=int(input("Enter a number to be calculated "))
# inputNumber=lambda  x:inputNumberA*inputNumberB
# print(inputNumber(inputNumber))






