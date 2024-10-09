class Rectangle:
           nombre_de_rectangles=0
           def __init__(self,longueur,largeur) :
                   self.longueur=longueur
                   self.largeur=largeur
                   Rectangle.nombre_de_rectangles+=1
           @staticmethod        
           def calculerPerimetre(a,b):
                   return 2*(a+b)   
           @staticmethod
           def calculerSurface(a,b):
                    return a*b
           
           def Perimetre(self):
                    return Rectangle.calculerPerimetre(self.longueur,self.largeur)         
           
           def Surface(self):
                    return Rectangle.calculerSurface(self.longueur,self.largeur)
           
           @staticmethod
           def nombreRectangles():
                    return Rectangle.nombre_de_rectangles
           
           def __str__(self):
                   return "Longueur :{} \n Largeur:{}".format(self.longueur,self.largeur)
           
Rect1=Rectangle(12,18)  
Rect2=Rectangle(2,8)
print(Rect1.nombre_de_rectangles)
       
 