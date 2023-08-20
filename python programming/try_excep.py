try:
    n=int(input("n="))
    for i in range(1,5):
        print(n*i)
except:
    #print(e)
    print("invalid input")
    print("exceptional handling")
    
finally:
    print("shivay")