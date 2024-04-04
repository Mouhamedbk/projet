import turtle
from CONFIGS import *

import tkinter as tk
from tkinter import simpledialog


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

def poser_question(question):
    root = tk.Tk()
    root.withdraw()
    answer = simpledialog.askstring("Question", question)
    return answer

def charger_grille_depuis_fichier(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        return [[int(cellule) for cellule in ligne.strip().split(',')] for ligne in lignes]

def dessiner_grille(grille, taille_case):
    ecran = turtle.Screen()
    ecran.setup(width=len(grille[0]) * taille_case + 200, height=len(grille) * taille_case)

    for i in range(len(grille)):
        for j in range(len(grille[0])):
            x = j * taille_case - (len(grille[0]) * taille_case) / 2 + taille_case / 2
            y = (len(grille) - i - 1) * taille_case - (len(grille) * taille_case) / 2 + taille_case / 2
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

def dessiner_inventaire(inventaire):
    turtle.penup()
    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)
    turtle.pendown()
    turtle.begin_fill()
    # turtle.fillcolor("lightblue")
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(POINT_AFFICHAGE_INVENTAIRE[0] + 10, POINT_AFFICHAGE_INVENTAIRE[1] - 20)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Inventaire:", font=("Arial", 12, "normal"))
    y_offset = 0
    for objet in inventaire:
        turtle.penup()
        turtle.goto(POINT_AFFICHAGE_INVENTAIRE[0] + 10, POINT_AFFICHAGE_INVENTAIRE[1] - 40 - y_offset)
        turtle.pendown()
        turtle.write(f"- Objet trouvé à la position : {objet}", font=("Arial", 10, "normal"))
        y_offset += 20

def move_up(grid):
    global square_size, player_position, inventaire
    new_y = player_position[0] + 1
    if new_y < len(grid) and (grid[new_y][player_position[1]] == 0):
        player_position = (new_y, player_position[1])
        update_player(grid)
    elif new_y < len(grid) and grid[new_y][player_position[1]] == 3:  # Si la case est une porte
        detecter_porte(new_y, player_position[1])
    elif new_y < len(grid) and grid[new_y][player_position[1]] == 4:  # Si la case est un objet
        detecter_objet(new_y, player_position[1])

def move_down(grid):
    global square_size, player_position, inventaire
    new_y = player_position[0] - 1
    if new_y >= 0 and (grid[new_y][player_position[1]] == 0):
        player_position = (new_y, player_position[1])
        update_player(grid)
    elif new_y >= 0 and grid[new_y][player_position[1]] == 3:  # Si la case est une porte
        detecter_porte(new_y, player_position[1])
    elif new_y >= 0 and grid[new_y][player_position[1]] == 4:  # Si la case est un objet
        detecter_objet(new_y, player_position[1])

def move_left(grid):
    global square_size, player_position, inventaire
    new_x = player_position[1] - 1
    if new_x >= 0 and (grid[player_position[0]][new_x] == 0):
        player_position = (player_position[0], new_x)
        update_player(grid)
    elif new_x >= 0 and grid[player_position[0]][new_x] == 3:  # Si la case est une porte
        detecter_porte(player_position[0], new_x)
    elif new_x >= 0 and grid[player_position[0]][new_x] == 4:  # Si la case est un objet
        detecter_objet(player_position[0], new_x)

def move_right(grid):
    global square_size, player_position, inventaire
    new_x = player_position[1] + 1
    if new_x < len(grid[0]) and (grid[player_position[0]][new_x] == 0):
        player_position = (player_position[0], new_x)
        update_player(grid)
    elif new_x < len(grid[0]) and grid[player_position[0]][new_x] == 3:  # Si la case est une porte
        detecter_porte(player_position[0], new_x)
    elif new_x < len(grid[0]) and grid[player_position[0]][new_x] == 4:  # Si la case est un objet
        detecter_objet(player_position[0], new_x)

def detecter_objet(x, y):
    global grille, inventaire
    grille[x][y] = 0
    inventaire.append((x, y))
    dessiner_carre((y * TAILLE_CASE - (len(grille[0]) * TAILLE_CASE) / 2 + TAILLE_CASE / 2),
                   ((len(grille) - x - 1) * TAILLE_CASE - (len(grille) * TAILLE_CASE) / 2 + TAILLE_CASE / 2),
                   TAILLE_CASE, "white")
    print("Vous avez trouvé un objet à la position :", x, y)
    print("L'objet a été ajouté à votre inventaire.")
    dessiner_inventaire(inventaire)  # Mettre à jour l'affichage de l'inventaire


def detecter_porte(x, y):
    global grille, inventaire
    print("Vous êtes devant une porte à la position :", x, y)
    question_posee = False
    with open("dico_portes.txt", "r") as file:
        for line in file:
            question_posee = False  # Réinitialisation à False à chaque itération
            line = line.strip()
            coordinates, question_and_answer = eval(line)
            porte_x, porte_y = coordinates
            if porte_x == x and porte_y == y:
                question, reponse_attendue = question_and_answer
                question_posee = True
                reponse = poser_question(question)
                if reponse and reponse.lower() == reponse_attendue.lower():
                    print("Vous avez répondu correctement. ")
                    grille[x][y] = 0
                    dessiner_carre((y * TAILLE_CASE - (len(grille[0]) * TAILLE_CASE) / 2 + TAILLE_CASE / 2),
                                   ((len(grille) - x - 1) * TAILLE_CASE - (
                                               len(grille) * TAILLE_CASE) / 2 + TAILLE_CASE / 2),
                                   TAILLE_CASE, "white")
                    return True  # Sortir de la fonction après le passage de la porte
                else:
                    print("Vous n'avez pas répondu correctement à la question. Vous ne pouvez pas franchir la porte.")
                    # Vous pouvez ajouter d'autres actions à effectuer en cas de mauvaise réponse ici

    if not question_posee:
        print("Il n'y a pas de question associée à cette porte.")

def update_player(grid):
    global player_turtle, player_position, square_size
    square_size = TAILLE_CASE
    x = player_position[1] * square_size - (len(grid[0]) * square_size) / 2 + square_size / 2
    y = (len(grid) - player_position[0] - 1) * square_size - (len(grid) * square_size) / 2 + square_size / 2
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

grille = charger_grille_depuis_fichier("plan_chateau.txt")
TAILLE_CASE = 20
player_position = POSITION_DEPART
inventaire = []  # Initialisation de l'inventaire

player_turtle = turtle.Turtle()
player_turtle.speed(0)

dessiner_grille(grille, TAILLE_CASE)
# dessiner_annonce()
dessiner_inventaire(inventaire)
update_player(grille)

turtle.listen()
turtle.onkey(lambda: move_up(grille), "Down")
turtle.onkey(lambda: move_down(grille), "Up")
turtle.onkey(lambda: move_left(grille), "Left")
turtle.onkey(lambda: move_right(grille), "Right")

while True:
    turtle.update()

turtle.done()
