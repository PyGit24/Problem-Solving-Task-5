# TV Class inherting TVClass - Base class; LedTV class; PlasmaTV class

# TV Base Class
class Tv_Base():
    def __init__(self,brand,channel,price,inches,onoff,volume,reset):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.onoff = onoff
        self.volume = volume
        reset = reset

# Constructor
        def basetv(self):
            print("Default Channel is: 1")
            print("Default Volume is : 50")

        def volum(self):
            self.volume=50
            while volume < 0 :
                print(" Volume can't be below zero")
                while volume > 100:
                    print(" Volume can't be above 100")
                else:
                    print("The set volume is:", volume)
        def chanl(self):
            self.channel
            for channel in range(1,50):
                while channel > 50 :
                    print(" Channel is: ", channel)
                else:
                    print("The current channel is:", channel)

        def rest(self):
            self.reset
            set.self.channel=1
            set.self.volume=50
            
        def status(self):
            print("Panasonic at channel:8")
            print("Panasonic set volume is: 75")


class LedTV(Tv_Base):
    def __init__(self):
        super().__init__(self, brand, channel,price,inches,onoff,volume,reset)
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.onoff = onoff
        self.volume = volume
        reset = reset
        screen_thickness = "20mm"
        energy_usage = "5 Star"
        life_span = "6 Years"
        refresh_rate = "60 - 120 Hz"
        functional = "Viewing Angle 15degrees upward or downward or around 40 degrees from left to right"
        back_light = "Yes"
        display_details = " "
    def letv(self):
        print(screen_thickness)
        print(energy_usage)
        print(life_span)
        print(refresh_rate)
        print(functional)
        print(back_light)
        print(display_details)

class PlasmaTv(Tv_Base):
    def __init__(self):
        screen_thick = "6cm"
        energy_usag = "3 Star"
        life_pan = "11 Years"
        refres_rate = "60 Hz"
        functiona = "Viewing Angle 15degrees upward or downward or around 40 degrees from left to right"
        back_lit = "Yes"
        display_detail = " "
    def ptv(self):
        print(screen_thick)
        print(energy_usag)
        print(life_pan)
        print(refres_rate)
        print(functiona)
        print(back_lit)
        print(display_detail)
TV= Tv_Base("panasonic",2,15000,30,"on",50,"no")
test=PlasmaTv
test.ptv

