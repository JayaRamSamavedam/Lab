a=True
while(a):
    
    s=input("Enter a string: ")
    c1="1. convert the input string to upper case"
    c2="2. convert the input string to lower case"
    c3="3. Check whether all the characters of input are in upper case"
    c4="4. Check whether all the characters of input are in lower case"
    c5="""5. Replace the string "INTELLIgence" by "Neural Networks"."""
    c6="""6. check whether the given string  starts with "T"."""
    c7="""7. check whether the given string ends with "e"."""
    c8="8. convert the first letter to upper case"
    c9="9. covert the upper case string to lower case and lower case to upper case and vice versa"
    print(c1+"\n"+c2+"\n"+c3+"\n"+c4+"\n"+c5+"\n"+c6+"\n"+c7+"\n"+c8+"\n"+c9+"\n10. Exit\n----------------------------------------------------------------\n")
    ip=int(input("choose any option: "))
    f={1:s.upper(),2:s.lower(),3:s.isupper(),4:s.lower(),5:func5(),6:True if s[0]=="T" else False,7:True if s[len(s)-1]=="e" else False,8:s[0].upper()+s[1:],9:s.swapcase()}    
    
    