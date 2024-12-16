liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = get_int_value("combien de longeur ?")
    d = input("Quelle est la date (YYYY-MM-DD) ? ")
    liste.append((a, b, c, d))

def get_cmd():
    '''Menu d'affichage avec un numéro qui donne une  commande'''
    print("Menu :")
    print("1 -> ajout d'une performance")
    print("2 -> ajout d'un individu")
    print("3 ->jout d'une nouvelle nage")
    print("4 -> liste toutes les performances")
    print("5 -> liste les performances d'un nageur")
    print("6 -> liste tous les nageurs pratiquants une nage")
    print("7 -> sauvegarde les données utilisateurs")
    print("8 -> charge les données utilisateurs")
    print("0 -> quitter le logiciel")
    msg = get_int_value("Choisir une option")
    return msg

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  nage   |  longueur |  date")
    print("--------------------------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:8} | {elt[3]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print("Performances de ", tmp)
    print("  nage   |  longueur |  date")
    print("--------------------")
    for elt in liste:
        if elt[0]== tmp:
            print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:8} | {elt[3]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quel nage ? ")
    print("Nage ", tmp)
    print(" Nageur     |  longueur |  date")
    print("------------------------")
    for elt in liste:
        if elt[1]== tmp:
            print(f" {elt[0]:11}|  {elt[2]:8}")

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    else:
        return True

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        tmp = line.split(',')
        liste.append(tuple(tmp))
    fichier.close()

def get_int_value():
    while True:
        try:
            msg = int(input("Valeur ? "))
            return msg
        except:
            print("Indiquez bien une valeur numérique")
print('le nombre est ', get_int_value())

isAlive = True
while isAlive:
    commande = get_cmd()

    if commande == 'ajout':
        cmd_ajout(liste)
        continue
   
    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == 'nageur':
        cmd_nageur(liste)
        continue

    if commande == 'nage':
        cmd_nage(liste)
        continue

    if commande == 'save':
        cmd_save(liste, 'save.csv')
        continue

    if commande == 'load':
        cmd_load(liste, 'save.csv')
        continue

    if commande == 'exit':
        isAlive = cmd_exit(liste)
        continue
    
    if commande == 1:
        cmd_ajout(liste)
    elif commande == 2:
        cmd_ajout(liste)
    elif commande == 3:
        cmd_ajout(liste)
    elif commande == 4:
        cmd_liste(liste)
    elif commande == 5:
        cmd_nageur(liste)
    elif commande == 6:
        cmd_nage(liste)
    elif commande == 7:
        cmd_save(liste, 'save.csv')
    elif commande == 8:
        cmd_load(liste, 'save.csv')
    elif commande == 0:
        isAlive = cmd_exit(liste)
    else:
        print("Option invalide.")


    print(f"Commande {commande} inconnue")