from datetime import datetime
class CompteBancaire:
           Nbr_Compte=0
           def __init__(self,numeroCompte,nom,solde):    
                   self.nom=nom
                   self.numeroCompte=numeroCompte
                   self.solde=solde
                   CompteBancaire.Nbr_Compte+=1

           def Versement(self,vers):
                    self.solde+=vers      
           def Retrait(self,vers):
                   if(self.solde>=vers):
                           self.solde-=vers
                           return f"Retrait réussi de {vers}. Solde restant : {self.solde}."

                   else:
                           return f"Retrait échoué, Solde insuffisant :{self.solde}" 
           def afficher(self):
                   return f"Nom : {self.nom} \n Numéro De Compte : {self.numeroCompte}  \n Solde : {self.solde} DH  \n Date :{datetime.now()}" 
           
           @staticmethod
           def nombreComptes( ):
                   return CompteBancaire.Nbr_Compte



compte1=CompteBancaire(12891,"NAJIB AZMI",1000.293)   
compte2=CompteBancaire(12891,"NAJIB AZMI",1000.293)    
compte3=CompteBancaire(12891,"NAJIB AZMI",1000.293)         
# print(compte1.afficher())
# print("############### Retrait de 100000 DH #################")
# print(compte1.Retrait(900000))  
# print(compte1.afficher())
# print("############### Versement de 90000 DH ###############")
# compte1.Versement(90000)
# #print(compte1.afficher())

print(CompteBancaire.Nbr_Compte)