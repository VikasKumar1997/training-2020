class solar:
    def panelType():
        print("\n\n   These type of solar inverter have panel to get chareg up\n   They cannot store power for backup\n   But they can sell it")
    def batteryType():
        print("\n\nThese type of solar inverter can store battery backup after get charged")
    def normalSolar():
        print("\n\nThese type of solar inverter can get charged by solar panel no storage for battery backup")
class nonSolar:
    def non_solar():
        print("\n\nThese type of inverter are our home inverter which run on battery")
class inverter(solar,nonSolar):
    def __init__(s):
        print("  There are two types of solar inverter")
        print("\n1. inverter with solar panel\n2. Inverter with battery")
    def findPowerrating(s):
        current=float(input("enter current:-"))
        operatingvoltage=float(input("enter voltage:-"))
def main():
    print("     WELCOME TO IOT INVERTER COMPANY     ")
    object=inverter
    while True:
        print("\n1. solar inverter\n2. non-solar\n3. Exit from company")
        choice=int(input("Enter your choice:-"))
        if choice==1:
            print("\n\nsolar inverters are:-\n1.   PCI\n2.   GTI\n3.   Reaglia")
            choose=int(input("Choose one of the inverter type from them:-"))
            if choose==1:
                object.batteryType()
            if choose==2:
                object.panelType()
            if choose==3:
                object.normalSolar()
        elif choice==2:
            object.non_solar()
            print("\n\nTwo varieties are available\n   1. Zelio\n   2. iCruze")
        elif choice==3:
            break
        else:
            print("enter valid choice")
main()
        
