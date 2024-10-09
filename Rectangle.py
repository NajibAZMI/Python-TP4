from  Point import Point
import math
class Rectangle:
            def __init__(self ,hg,bd): 
                           self.__hg=hg
                           self.__bd=bd
            def Hauteur(self):
                      return (self.__hg.getY()-self.__bd.getY())
            def Largeur(self):
                      return (self.__bd.getX()-self.__hg.getX())
            def Perimetre(self):
                      return (2*(self.Hauteur()+self.Largeur()))
            def Surface(self):
                      return (self.Hauteur()*self.Largeur())
            def Diagonal(self):
                      return math.sqrt(pow(self.__bd.getX()-self.__hg.getX(),2)+pow(self.__bd.getY()-self.__hg.getY(),2))
            def Appartenance(P,self):
                    if( P.getX()<=self.__bd.getX() and
                        P.getX()>=self.__hg.getX() and
                        P.getY()<=self.__hg.getY() and 
                        P.getY()>=self.__bd.getY()):
                            return True
                    else:
                            return False
            def Deplacer(self,P):
                    self.__hg.setX(P.getX())
                    self.__hg.setY(P.getY())
                    self.__bd.setX(self.__bd.getX()+P.getX())
                    self.__bd.setY(self.__bd.getY()+P.getY())
               