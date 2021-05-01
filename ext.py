def ext(s):
    l=len(s)
    if s[l-1] =="y" and s[l-2] =="p":
        print("the given file is python type")
    else:
        print("the given file is not a python file")
s=input("enter the file name: ")
ext(s)
