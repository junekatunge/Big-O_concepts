class Cookie:
    def __init__(self,color):
        self.color = color
        
    def get_color (self):
        return self.color
    
    def set_color (self,color):
        self.color = color
        
Cookie_A = Cookie("Yellow")
Cookie_B = Cookie ("Red")

Cookie_B.set_color("Purple")
Cookie_A.set_color("Green")

print ("She bought a", Cookie_A.get_color())
print ("He bought a",Cookie_B.get_color())

print("He returned and bought a",Cookie_B.get_color())
print("She also changed her cookie and bought",Cookie_A.get_color())