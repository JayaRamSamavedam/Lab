def printfaqs():
    a="1.how to order the food??\n2.how to cancel the food order??\n3.how to track my order??" \
      "4.What if my order has not got on time??\n5.what if my order has not matched to delivered product??"
    print(a)
    p()
    x=str(input("enter the query number... "))
    return x

def p():
    print("....................................................")

def solutionfaq(a):
    a1="1.first open the smj app\n"\
        "2.search the beloved product in the search bar"\
        "\n3.select the product"\
        "\n4.below you will get two buttons $ BUY NOW $ and $ ADD TO CART$\n"\
        "5.if you want to buy only that click on the $ BUY NOW $ else click on the add to cart to buy more"
    a2="1.click on the profile\n" \
       "2.click on the orders placed\n" \
       "3.click on the cancel the order button"
    a3="1.click on the profile click on the orders placed\n" \
       "2.click on the specific order you want to track\n" \
       "3.You can able to see the status of the order"
    a4="SMJ delever the order with in the 1 hour of time\n" \
       "if you order is not recieved on the time you can complaint in the complaint box which is in the profile send the order number" \
       "our team will refund the amount in 1 working day"
    a5="SMJ delever the order very acurately if your order has mismatched just place a complaint \n" \
       " in the complaint box which is in the profile send the order number our team will come to resolve the problem"

    x={ '1':a1,'2':a2,'3':a3,'4':a4,'5':a5}
    print(x[a])
    p()

print("Welcome to SMJ")
x=str(input("please enter your name??"))
print("hello "+x)
a=True
while(a):
    p()
    print(x+" may i know whats your doubt in you mind??")
    f=printfaqs()
    solutionfaq(f)
    print("Thank you "+x+" hoping that your query has resolved....")
    t=int(input("enter 1 to resolve the more queries\n0 to exit"))
    if(t==0):
        a=False
