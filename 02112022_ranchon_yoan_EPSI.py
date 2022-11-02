#                Exception


# while True:
#     try:
#         x=int(input("Identifiant: "))
#         break
#     except ValueError:
#         print("Entrée invalide")
#     finally:
#         print("Gardons le cap")

# try:
#     2/0
# except ZeroDivisionError:
#     pass

# div = input()
# try:
#     div=int(div)
#     if div==1:
#         raise ValueError()
# except ValueError:
#     print("Valeur saisie inutile, pas besoin de cet ordi")
# else:
#     print("Le resultat est", 7/div)



#           Boucles for

liste=range(20)
print(liste)

liste_1=[]
for x in liste:
    if x % 2 ==0:
        liste_1.append(x)
print(liste_1)

liste_2 = [x for x in liste if x % 2 == 0]  # -> rédaction avec compréhension
print(liste_2)

liste_3 = [str(x) for x in liste_2]
print(liste_3)

liste_4 = [x**2 for x in liste_2]
print(liste_4)

filtre_1 = [item for item in liste_2 if item]
print(filtre_1)


#           dictionnaire

nombres = range(20)
dict_for = {}
for n in nombres:
    if n%2==0:
        dict_for[n] = n**2
print(dict_for)

dict_for_2 = {n:n**2 for n in nombres if n%2==0}
print(dict_for_2)

equipe = {'Christiano': 'Juve', 'Hakimi': 'Dortmund', 'Kante': 'Chelsea'}
equipe_joueur = {equipe[key] for key in equipe}
print(equipe_joueur)

distance_m = {'v_1':100000, 'v_2':153000, 'v_3':700000}
distance_km = {i:j/1000 for (i,j) in distance_m.items()}
print(distance_km)

distance2_m = {'v_1':100000, 'v_2':153000, 'v_3':700000}
distance2_km = {i:j/1000 for (i,j) in distance2_m.items() if j/1000>1}
print(distance2_km)

import logging
logging.basicConfig(level=logging.INFO)
logging.debug('Message 1 fichier log')
logging.warning('Message 2 avertissement')
logging.info('Message 3 info')


#               fonction lambda

f_1 = lambda x,y:x*y
print(f_1(2,3))

d_1 = [[0], [2], [3], [10], [5]]
max_val = lambda x:max(x)
print(max_val(d_1))


#           class

class felins:
    famille = 'mammifères placentaires'
    ordre = 'carnivores'
    sous_ordre = 'féliformes'

    def mam_plac(self):
        """constructeur"""
        print(self.famille)

def main():
    tigre = felins()
    tigre.mam_plac()

if __name__ == '__main__':main()

class tigres(felins):
    """classe qui représente un tigre qui hérite de félins"""
    def __init__(self, type_felin, vitesse):
        self.type_felin = type_felin
        self.vitesse = vitesse

t_1 = tigres("tigre", "100km/h")
t_1.vitesse
t_1.famille

issubclass(felins, tigres)


#           setter / getter

class felins2:
    def __init__(self, type_félin="tigre", couleur="orange"):
        self.type_félin = type_félin
        self.couleur = couleur
    def def_couleur(self):
        return self.couleur
    def ch_couleur(self, valeur):
        self.couleur = valeur
    def def_type_félin(self):
        return self.type_félin
    def ch_type_félin(self, valeur):
        if valeur == "serpent":
            raise ValueError("Ca va la tête ?")
        self.type_félin = valeur

# code "pythonique"
# bonnes pratiques : éviter d'alourdir le code avec des getters et des setters
# quand vous voulez indiquer qu'un attribut est "non public" on utilise un _ ( covention pour avertir l'utilisateur)
# une classe sans méthode ne sert a rien , éviter d'avoir une liste vide comme attribut de classe


class person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        print('Getting name')
        return self._name
    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value
    def del_name(self):
        print('Deleting name')
        del self._name
    name= property(get_name, set_name, del_name, 'Name property')

p = person('Adam')
print(p.name)
p.name= 'Jhon'
del p.name


def Afficher_decorateur(function):
    def nouvelle_fonction(a, b):
        print('le résultat de cette opération avec {} et {}'.format(a,b))
        res = function(a,b)
        print('résultat: {}'.format(res))
        return res
    return nouvelle_fonction


@Afficher_decorateur
def soustraction(a,b):
    return a-b
soustraction(1,2)

@Afficher_decorateur
def addition(a,b):
    return a+b
addition(1,2)


def minuscule(fonc):
    def wrapper():
        texte = fonc()
        if not isinstance(texte, str):
            raise TypeError("Type non adapté")
        return texte.lower()
    return wrapper

@minuscule
def salut():
    return "Hello les amis"

salut()


def adresse_pro(fonc):
    def wrapper():
        texte = fonc()
        res = "".join([texte, "@entreprise.com"])
        return res
    return wrapper


# l'ordre des décorateurs est importante
@minuscule
@adresse_pro
def utilisateur():
    return "Tasnime"

utilisateur()