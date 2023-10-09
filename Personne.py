class personne:
    def __init__(self,nom,prenom,age):
        self.__nom
        self.__prenom
        self.__age
    def se_presenter(self):
        return("mon nom est",self.__nom,"mon prenom est",self.__prenom,"mon age est",self.__age)
        p1=personne("ali","ahmed",22)
        print (p1.se_presenter())
