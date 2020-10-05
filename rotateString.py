#rotate the second string starting from the 2 places in clockwise direction
def clockrotate(b):
    startstring=b[0:2]
    endstring=b[2:len(b)]
    clockconcatval=endstring + startstring
    return(clockconcatval)

#rotate the second string starting from the 2 places in anti-clockwise direction    
def anticlockrotate(b):
    startstring=b[0:len(b)-2]
    endstring=b[len(b)-2:len(b)]
    anticlockconcatval= endstring + startstring
    return(anticlockconcatval)

#Get all input values and provide output
def rotateString():
    print("Enter the number of test cases: ")
    try:
    	T=int(input())
    except Exception as e:
    	print("Enter a valid integer value")

    #Validate the input test case value range	
    while (T<1 or T>50):
                print("Only values from 1 to 50 are allowed. Please enter correct value: ")
                T=int(input())
    
    for i in range(1,T+1):
        print("Enter the first string: ")
        a=input()
        while (len(a)>100 or len(a)<1):
            print("Please enter a string with at least one character and below 100 characters: ")
            a=input()
        print("Enter the second string: ")
        b=input()
        while (len(b)>100 or len(b)<1):
            print("Please enter a string with at least one character and below 100 characters: ")
            b=input()

        #if string is below 3 characters in length    
        if(len(b)<3):
            if(a==b):
                print("1")
            else:
                print("0")
        #if string is more than 2 characters        
        elif(a==clockrotate(b) or a==anticlockrotate(b)):
            print("1")
        else:
            print("0")
rotateString()
