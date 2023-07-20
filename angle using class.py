import math
class area():
    a=int(input('Enter the value of a:'))
    b=int(input('Enter the value of b:'))
    def rect(self):
        print('\n\t\tRECTANGLE')
        area_rect=self.a*self.b
        print('\tArea of Rectangle is :',area_rect)
        return
    def sq(self):
        print('\n\t\tSQUARE')
        area_sq=self.a*self.a
        print('\tArea of Square is :',area_sq)
        return
    def cir(self):
        print('\n\t\tCIRCLE')
        area_cir=3.14*self.a*self.a
        print('\tArea of Circle is :',area_cir)
        return
    def tri(self):
        print('\n\t\tTRIANGLE')
        area_tri=(1/2)*self.a*self.b
        print('\tArea of Triangle is :',area_tri)
        return
area_obj=area()
area_obj.rect()
area_obj.sq()
area_obj.cir()
area_obj.tri()


