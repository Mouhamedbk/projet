ZONE_PLAN_MINI = (-200, 160)  # Coin inférieur gauche de la zone d'affichage du plan
ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
POINT_AFFICHAGE_ANNONCES = (-200, 365)  # Point d'origine de l'affichage des annonces
POINT_AFFICHAGE_INVENTAIRE = (220, 100)  # Point d'origine de l'affichage de l'inventaire

# Les valeurs ci-dessous définissent les couleurs des cases du plan
COULEUR_CASES = 'white'
COULEUR_COULOIR = 'white'
COULEUR_MUR = 'grey'
COULEUR_OBJECTIF = 'yellow'
COULEUR_PORTE = 'orange'
COULEUR_OBJET = 'green'
COULEUR_VUE = 'wheat'
COULEURS = [COULEUR_COULOIR, COULEUR_MUR, COULEUR_OBJECTIF, COULEUR_PORTE, COULEUR_OBJET, COULEUR_VUE]
COULEUR_EXTERIEUR = 'white'
COULEUR_CASE ="red"
TAILLE_CASE = 20

# Couleur et dimension du personnage
COULEUR_PERSONNAGE = 'red'
RATIO_PERSONNAGE = 0.9  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0, 1)  # Porte d'entrée du château

# Désignation des fichiers de données à utiliser
fichier_questions = 'dico_portes.txt'
fichier_objets = 'dico_objets.txt'

'''import turtle
from CONFIGS import *

turtle.tracer(0)

def dessiner_carre(x, y, taille, couleur):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    for _ in range(4):
        turtle.forward(taille)
        turtle.left(90)
    turtle.end_fill()

def charger_grille_depuis_fichier(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        return [[int(cellule) for cellule in ligne.strip().split(',')] for ligne in lignes]

def dessiner_grille(grille, taille_case):
    ecran = turtle.Screen()
    ecran.setup(width=len(grille[0]) * taille_case + 200, height=len(grille) * taille_case)

    for i in range(len(grille)):
        for j in range(len(grille[0])):
            x = j * taille_case - (len(grille[0]) * taille_case) / 2 + taille_case/2
            y = (len(grille) - i - 1) * taille_case - (len(grille) * taille_case) / 2 + taille_case/2
            dessiner_carre(x, y, taille_case, COULEURS[grille[i][j]])

    ecran.update()
    return ecran

def dessiner_annonce():
    turtle.penup()
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("lightgreen")
    for _ in range(2):
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()

def dessiner_inventaire():
    turtle.penup()
    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("lightblue")
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()

def move_up(grid):
    global square_size, player_position
    new_y = player_position[0] + 1
    if new_y < len(grid) and (grid[new_y][player_position[1]] == 0):
        player_position = (new_y, player_position[1])
        update_player(grid)
    elif new_y < len(grid) and grid[new_y][player_position[1]] == 3:  # Si la case est une porte
        detecter_porte(new_y, player_position[1])
    elif new_y < len(grid) and grid[new_y][player_position[1]] == 4:  # Si la case est un objet
        detecter_objet(new_y, player_position[1])

def move_down(grid):
    global square_size, player_position
    new_y = player_position[0] - 1
    if new_y >= 0 and (grid[new_y][player_position[1]] == 0):
        player_position = (new_y, player_position[1])
        update_player(grid)
    elif new_y >= 0 and grid[new_y][player_position[1]] == 3:  # Si la case est une porte
        detecter_porte(new_y, player_position[1])
    elif new_y >= 0 and grid[new_y][player_position[1]] == 4:  # Si la case est un objet
        detecter_objet(new_y, player_position[1])

def move_left(grid):
    global square_size, player_position
    new_x = player_position[1] - 1
    if new_x >= 0 and (grid[player_position[0]][new_x] == 0):
        player_position = (player_position[0], new_x)
        update_player(grid)
    elif new_x >= 0 and grid[player_position[0]][new_x] == 3:  # Si la case est une porte
        detecter_porte(player_position[0], new_x)
    elif new_x >= 0 and grid[player_position[0]][new_x] == 4:  # Si la case est un objet
        detecter_objet(player_position[0], new_x)

def move_right(grid):
    global square_size, player_position
    new_x = player_position[1] + 1
    if new_x < len(grid[0]) and (grid[player_position[0]][new_x] == 0):
        player_position = (player_position[0], new_x)
        update_player(grid)
    elif new_x < len(grid[0]) and grid[player_position[0]][new_x] == 3:  # Si la case est une porte
        detecter_porte(player_position[0], new_x)
    elif new_x < len(grid[0]) and grid[player_position[0]][new_x] == 4:  # Si la case est un objet
        detecter_objet(player_position[0], new_x)

# def detecter_porte(x, y):
#     print("Vous êtes devant une porte à la position :", x, y)
#     if repondre_question():  # Si la réponse est correcte
#         print("Vous avez répondu correctement. Vous pouvez franchir la porte.")
#         move_through_door()
#     else:
#         print("Vous n'avez pas répondu correctement à la question. Vous ne pouvez pas franchir la porte.")

def move_through_door():
    global player_position
    # Vous pouvez personnaliser cette fonction en fonction de la logique de votre jeu
    # Ici, je déplace le joueur vers le haut pour simuler le passage par la porte
    player_position = (player_position[0] + 1, player_position[1])
    update_player(grille)

def detecter_objet(x, y):
    global grille
    grille[x][y] = 0  # Mettre à jour la grille pour indiquer que la case est désormais vide
    dessiner_carre((y * TAILLE_CASE - (len(grille[0]) * TAILLE_CASE) / 2 + TAILLE_CASE/2),
                   ((len(grille) - x - 1) * TAILLE_CASE - (len(grille) * TAILLE_CASE) / 2 + TAILLE_CASE/2),
                   TAILLE_CASE, "white")  # Redessiner la case en blanc
    print("Vous avez trouvé un objet à la position :", x, y)


def detecter_porte(x, y):
    global grille
    print("Vous êtes devant une porte à la position :", x, y)
    question_posee = False
    with open("dico_portes.txt", "r") as file:
        for line in file:
            line = line.strip()
            coordinates, question_and_answer = eval(line)
            porte_x, porte_y = coordinates
            if porte_x == x and porte_y == y:
                question, reponse_attendue = question_and_answer
                question_posee = True
                if repondre_question(question, reponse_attendue):
                    print("Vous avez répondu correctement. ")
                    grille[x][y] = 0  # Mettre à jour la grille pour indiquer que la case est désormais vide
                    dessiner_carre((y * TAILLE_CASE - (len(grille[0]) * TAILLE_CASE) / 2 + TAILLE_CASE/2),
                                   ((len(grille) - x - 1) * TAILLE_CASE - (len(grille) * TAILLE_CASE) / 2 + TAILLE_CASE/2),
                                   TAILLE_CASE, "white")  # Redessiner la case en blanc
                    move_through_door()
                else:
                    print("Vous n'avez pas répondu correctement à la question. Vous ne pouvez pas franchir la porte.")
                break
    if not question_posee:
        print("Il n'y a pas de question associée à cette porte.")


def repondre_question(question, reponse_attendue):
    # Poser la question au joueur
    reponse = input(question + " ")
    # Vérifier si la réponse est correcte
    if reponse.lower() == reponse_attendue.lower():
        print("Bonne réponse !")
        return True
    else:
        print("Mauvaise réponse.")
        return False



def update_player(grid):
    global player_turtle, player_position, square_size
    square_size = TAILLE_CASE
    x = player_position[1] * square_size - (len(grid[0]) * square_size) / 2 + square_size/2
    y = (len(grid) - player_position[0] - 1) * square_size - (len(grid) * square_size) / 2 + square_size/2
    player_turtle.clear()
    player_turtle.penup()
    player_turtle.goto(x, y)
    player_turtle.pendown()
    player_turtle.begin_fill()
    player_turtle.fillcolor(COULEUR_PERSONNAGE)
    for _ in range(4):
        player_turtle.forward(square_size)
        player_turtle.left(90)
    player_turtle.end_fill()

# Charger la grille depuis le fichier
grille = charger_grille_depuis_fichier("plan_chateau.txt")
TAILLE_CASE = 20  # Définir la taille de la case ici
player_position = POSITION_DEPART

# Initialiser le joueur
player_turtle = turtle.Turtle()
player_turtle.speed(0)

# Variable pour suivre si un objet a été trouvé
objet_trouve = False

# Dessiner la grille et le joueur
dessiner_grille(grille, TAILLE_CASE)
dessiner_annonce()
dessiner_inventaire()
update_player(grille)

# Configurer les touches pour les déplacements
turtle.listen()
turtle.onkey(lambda: move_up(grille), "Up")
turtle.onkey(lambda: move_down(grille), "Down")
turtle.onkey(lambda: move_left(grille), "Left")
turtle.onkey(lambda: move_right(grille), "Right")

while True:
    if objet_trouve:
        break

    turtle.update()

turtle.done()
'''