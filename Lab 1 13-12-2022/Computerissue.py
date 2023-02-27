def printfaqs():
    a="1.OVER HEATING\n2.Slow Hard Drive\n3.Battery Won’t Hold a Charge" \
      "4.Bad Keyboard\n5.Can’t Connect to Wireless Network"
    print(a)
    p()
    x=str(input("enter the query number... "))
    return x

def p():
    print("....................................................")

def solutionfaq(a):
    a1="Overheating\n"\
       "Symptom: Computer crashes, freezes\n"\
       "Solution: Clean out air vents, put filtered material over the inhalation vent, or update BIOS Overheating can rob your laptop of performance and often cause a host of hiccups, such as system crashes and freezing. Every computer generates lots of heat, but laptops are especially susceptible to overheating due to their small size and lack of ventilation.\n Excessive dust can clog air vents and deprive your system of cold air to cool off the CPU."
    a2="Symptom: Excessive program load times, slow file transfers \nSolution: Disk defragmentation \n Disorganized information on your hard drive can sap performance because the computer requires more time to sift through data fragments and bad sectors on the drive. \nThis problem can be cleared up easily (but not especially quickly; defragging can sometimes take hours) using the built-in Windows tool called Disk Defragmenter. \nYou can access this program through the Programs menu in the Accessories or System Tools folder.\n Simply click the Analyze button to see if your disk drive requires defragmenting, and then click Defragment to begin."
    a3="Symptom: Your notebook runs only a few minutes when unplugged\nSolution: Battery replacement\nOver their lifespans, lithium-ion batteries can lose the ability to hold a charge. After a few years, some batteries will last only a fraction of the rated runtime. Replacing a battery is relatively simple; most pop out from the bottom or back of the laptop.\nTop tip – Never run the laptop plugged in on a fully charged battery, it will do more harm to your battery in the long run."
    a4="Symptom: Missing or Loose Keys\nSolution: Replace keyboard\nKeyboards get the brunt of abuse on any laptop, either from typing or spilled coffee. As a result, keys can often become dislodged or worn out. Thankfully, laptop makers provide quick online guides for replacing keyboards on their support pages; simply type “keyboard replacement” into the search bar or check the manufacturer’s knowledge base"
    a5="Symptom: No Internet connection, frequent time-outs while Web browsing\nSolution: Make sure wireless is turned on, smarter software tools, make sure router is broadcasting network name (SSID)\nPart of taking your laptop everywhere on the go is expecting to be able to connect to any wireless network, whether in an airport, coffee shop, or hotel. But wireless networks, by their very nature, are finicky beasts. Some laptops come with an external button or switch, separate from the software settings, to enable wireless connectivity. \n" \
       "Always make sure this wireless toggle is switched on.\n Also make sure that the network you’re connecting to is broadcasting its network name or SSID."

    x={ '1':a1,'2':a2,'3':a3,'4':a4,'5':a5}
    print(x[a])
    p()


print("hello ")
a=True
while(a):
    p()
    print(" may i know whats your issue are you facing??")
    f=printfaqs()
    solutionfaq(f)
    print("Thank you  hoping that your query has resolved....")
    t=int(input("enter 1 to resolve the more issues\n0 to exit"))
    if(t==0):
        a=False
