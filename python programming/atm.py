code=int(input("enter the code '1'for entry:"))
if code==1:
    print("come in:")
    language=input("choose the language:")
    if language=="english" or language=="hindi":
        service=input("choose the service:")
        if service=="withdraw" or service=="case":
            x=int(input("enter the amount:"))
            security=int(input("enter the your security number="))
            if security==9:
             print("take you amount:")
else:
    print("something went wrong:")
            
             