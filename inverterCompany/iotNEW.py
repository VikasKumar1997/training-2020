systemintegrator='vikas kumar'
class inverter:
    def __init__(s):
        s.model=input("enter your model number:-")
        s.battery=input("enter your battery capacity:-")
        s.current=input("enter your output current:-")
        s.operatingVoltage=input("enter your operating voltage:-")
    def powerRating(s):
        s.power=s.current*s.operatingVoltage
class solar:
    pass
class solar_panel:
    pass
class gridon:
    def sell(s):
        s.gain=s.current/100
class pcu(inverter,solar):
    #super(pcu,s).__init__()
    pass
class gti(inverter,solar,gridon):
    #super(gti,s).__init__()
    pass
class regalia(inverter,solar):
    #super(regalia,s).__init__()
    pass
class icruze(inverter):
    #super(icruze,s).__init__()
    pass
class consumer:
    def __init__(s):
        s.name=input("enter your name:-")
        ch=int(input("1. pcu\n2. gti\n3. zelio\n\nAdd your choice:-"))
        if ch==1:
            obp=pcu()
        elif ch==2:
            obg=gti()
        elif ch==3:
            obz=zelio()
class Integrater(consumer):
    def __init__(s):
        ch=int(input("1. pcu\n2. gti\n3. icruze\n4. regalia\n\nAdd your choice:-"))
        if ch==1:
            obp=pcu()
        elif ch==2:
            obg=gti()
        elif ch==3:
            obi=icruze()
        elif ch==4:
            obr=regalia()
def main():
    ch=int(input("1. consumer\n2. integrator\n\nSelect your type:-"))
    if ch==1:
        obj=consumer()
    elif ch==2:
        obj=intergrater()
main()
            
    
