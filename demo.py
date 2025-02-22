class shape:
    def __init__(self,a,b=None,c=None):
        if(b==None and c==None):
            self.r=a
            print(f"Area of the circle: {3.14*self.r*self.r}")
        elif(b==None):
            self.len=a
            self.bre=c
            print(f"Area of the rectangle: {self.len*self.bre}")
        else:
            self.l=a
            self.b=b
            self.h=c
            print(f"Area of the cube: {self.l*self.b*self.h}")
ob1=shape(5,6,7)
ob2=shape(5,8)
ob3=shape(5)