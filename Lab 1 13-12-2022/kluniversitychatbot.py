def courses(a):
    print(" the courses that you have to study are ")
    a1="OS\nCNS"
    a2="AIDS\nSE"
    a3="AIDS\nSE"
    a4="OS\nCNS"
    a5="SE"
    a6="OS\n CNS"
    a7="DAA"
    x = {'1': a1, '2': a2, '3': a3, '4': a4, '5': a5, '6': a6, '7': a7}
    print("\n",x[a])


def Certification(a):
    print("\n The Global certifications you have to do are:\n")
    a1="1.Junica Junos\n"\
        "2.Red hat EX-183"\
        "\n3.AWS -Cloud Practitioner"
    a2="1.PCAP\n" \
       "2.Red Hat EX-183\n" \
       "3.AWS -Cloud Practitioner"
    a3="1.PCAP\n" \
       "2.Red hat EX-183\n" \
       "3.AWS-cloud practioner"
    a4="1.Juniper Junica Junos\n" \
       "2.Red hat EX-183\n" \
       "3.AWS-cloud practioner"
    a5="1.AZ-204\n"
    a7="1. Code chef Data structure exam\n"
    a6="1. Juniper Junica Junos\n"
    x={ '1':a1,'2':a2,'3':a3,'4':a4,'5':a5,'6':a6,'7':a7}
    print(x[a])
def ab(x):
    print("1.Courses\n2.Certifications")
    print(" may i Know what you want to know ??")
    f=int(input())
    if(f==1):
        courses(x)
    else:
        Certification(x)
def printSpecialistaion():
    f="1.Cloud and Edge Computing\n2.Artificial intelligence\n3.Data Science\n" \
      "4.Cyber Security\n5.Devops\n6.IOT\n7.GUX"
    print(f)
    p()
    x=str(input("enter the specialisation number... "))
    ab(x)
def p():
    print("....................................................")


print("Welcome to K L DEEMED TO BE UNIVERSITY")
x=str(input("may i  know your name ??"))
print("hello "+x)
a=True
while(a):
    print(x+" may i know what specialisation did you belongs to ??")
    printSpecialistaion()


    print("Thank you "+x+" hoping that your query has resolved....")
    p()
    t=int(input("enter 1 to resolve the more queries\n0 to exit"))
    if(t==0):
        a=False
