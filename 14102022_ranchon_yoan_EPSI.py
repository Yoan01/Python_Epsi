# syntaxe  exercices "micro" projet

#  conversion
from dataclasses import replace
from operator import truediv
import random


x=float(1)
y=int(2.8)
z=complex(1)

print(x)
print(y)
print(z)

a=float(x)
b=int(x)
c=complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# exercice nb aléatoire entre 1 et 10

print(random.randrange(1,10))

print(""" fezfefze  
fezfezf
fzefze
""")  #triple quote pour un texte sur plusieurs lignes

# afficher la longueur de la chaine "lait"

print(len("lait"))

# j'ai une phrase je souhaite "detecter" un mot dans cette phrase mais afficher autre chose qu'un boolean

txt = "voila la phrase"

if ("la" in txt):
    print("trouvé")


# le "slicing"

p = "exemple"

print(p[2:4])

# afficher la position d'un caractère

i=0
while i < len(p):
    if (p[i]=="m"):
        print(i)
    
    i+=1

# si je peux afficher pl, au moins 2 solutions.. j'aimerais partir "a l'envers" de la chaine

print(p[-3:-1])


# test

print(bool("hello"))
print(bool(15))

# fonctions

def mafonction() :
    return True

print(mafonction())

# j'aimerai tester si un nombre est entier

m = 15

if ((m%1) == 0):
    print("entier")
else:
    print("pas entier")
#ou
print(isinstance(m,int))

x=float(1)
u=float(3.4)
z=float("6")
s=float("6.4")

(b,c) = (5,6)

def test():
    return 5,6

a = test()
b,c = test()

#acces à un tuple 
a[0]

a = (3) # tuple avec un seul element

print(type(a))

b=(3,)
print(type(b))

#recup l'element unique dans le tuple

c = b[0]
print(c)
#ou
d,=b
print(d)

#exercice 1 :  déclarer différents types de variables
prenom = "Pierre"
age = 20 
majeur = True
compte_en_banque = 20135.384
amis = ["Marie","Julien","Adrien"]
parents = ("Marc","Caroline")

#exercice 2 : corriger l'erreur

site_web = "google"
print(site_web)

#exercice 3: variable d'un type vers un autre, apres avoir declarer une variable afficher "le nombre est 17"

nombre = 17
print("le nombre est " + str(nombre))

#exercice 4: trouver la valeur de la variable, on veut printer la valeur que contien la variable a

a = 3
b = 6
a = b
b = 7

print(a) #pour 6

#exercice 5 : comment print une somme sans les additions

tab = [2,6,3]
print(sum(tab))

#ou 

a = 2
b = 6
c = 3
print(a,b,c, sep=" + ")

#exercice 6 : 

list1 = range(3)
list2 = range(5)
print(list(list2))

#exercice 7 :  verifier qu'une variable est bien d'un certain type

prenom = "Vincent"
if type(prenom)==str:
    print("la variable est une chaine de caractere")
else:
    print("la variable n'est pas une chaine de caractere")

nb = "22"

if type(nb)==int:
    print("la variable est un entier")
else:
    print("la variable n'est pas un entier")

#exercice 8: remplacer un mot par un autre dans la chaine "Salut les dev". Remplacer Salut par Bonsoir

txt = "Salut les dev, salut alors ca va"
print(txt)
txt2 = txt.replace("Salut","Bonsoir", 1)
print(txt2)

