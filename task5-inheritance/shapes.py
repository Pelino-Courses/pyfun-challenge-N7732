import math
class shape:
    def __init__(self,side,area):
        self.side=side
        self.area=area
class Circle(shape):
    def __init__(self,side,area):
        super().__init__(side,area)
        pass
    def calcularate_area(self):
        """This allow user to get the area of circle through the approrpriate formula below"""
        self.radius=int(input("Enter Radius in cm: "))
        self.p=math.pi
        self.area=self.p*self.radius**2
        return self.area
    def permeter(self):
        """This perform calculation of permeter """
        permete=2*self.p*self.radius
        return permete
    def shape_fugure(self):
        """This function describe the shape of circle"""
        return "Shape of circle is round\n" 
    def __str__(self):
        return f"{self.shape_fugure()}\nArea of circle:{self.area}cm²\n its permeter :{self.permeter()}"    
class Triangle(shape):
    def __init__(self,side,area):
        super().__init__(side,area)
        pass
    def shape_fugure(self):
        """This describe the figure of Triangle"""
        return f"Triangle Has Three side!\n"
    def calculate_area(self):
        """This perform The arae of the Triangle by using this formula below
        here we enter the sides of this figure"""
        self.B=int(input("Enter base in cm:"))
        self.h=int(input("Enter Height in cm:"))
        Area=2*self.B*self.h
        return f"area of Triangle is {Area}cm²\n"
    def permeter(self):
        """Here it's perform permeter of Triangle
        and it require to enter the hypotenuse"""
        Hpy=int(input("Enter Hypotenuse in cm: "))
        permete=Hpy+self.B+self.h
        return f"Permetre of Triangle:{permete}cm"
    def __str__(self):
        return f"{self.shape_fugure()}\nArea of T"
class Rectangle(shape):
    def __init__(self,side,area):
        super().__init__(side,area)
        pass
    def shape_fugure(self):
        """This describe the shape of Rectangle"""
        return "Rectangle have two equal width and two equal Length\n "
    def calculate_area(self):
        """This perform Area of Rectangle 
        By entering the sides both width and length of Rectangle"""
        self.W=int(input("Enter width in cm:"))
        self.L=int(input("Enter Length in cm:"))
        Area=self.W*self.L
        return f"Area of Triangle is {Area}cm²\n"
    def permeter(self):
        """This perform Permeter of triangle """
        permeter=2*self.W+2*self.L
        return f"Permeter :{permeter}cm"
def main():
    print("Choce:\n1.circle\n2.Triangle\n3.Rectangle")
    chose=int(input("Enter your choice:"))
    if chose==1:
        a=Circle(0,0)
        a.calcularate_area()
        print(a)
    elif chose==2:
        b=Triangle(0,0)
        b.calculate_area()
        b.permeter()
        print(b)
    elif chose==3:
        c=Rectangle(0,0)
        c.calculate_area()
        print(c)
    else:
        print("Invalid option")
if __name__=="__main__": 
    main()
    
