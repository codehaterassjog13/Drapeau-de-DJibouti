import turtle

# Initialiser la fenêtre de dessin
window = turtle.Screen()
window.title("Drapeau de Djibouti")
window.bgcolor("#808080")

# Créer un stylo pour dessiner
pen = turtle.Turtle()
pen.speed(2)
pen.up()

# Dessiner le rectangle bleu
pen.goto(-300, 250)
pen.down()
pen.color("#00AEEF")
pen.begin_fill()
for _ in range(2):
    pen.forward(300)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
pen.end_fill()

# Dessiner un rectangle vert

pen.goto(-300, 150)
pen.down()
pen.color("#7cfc00")
pen.begin_fill()
for _ in range(2):
    pen.forward(300)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
pen.end_fill()

#Dessiner la partie blanc

pen.goto(-300, 250)
pen.down()
pen.color("#ffffff")
pen.begin_fill()
pen.right(57)
pen.forward(120)
pen.right(66)
pen.forward(120)
pen.right(147)
pen.forward(200)
pen.right(90)
pen.end_fill()


# Dessiner l'étoile rouge
pen.up()
pen.goto(-290, 152.5)
pen.down()
pen.color("red")
pen.begin_fill()
for _ in range(5):
    pen.forward(30)
    pen.right(144)
pen.end_fill()

#tracer le poteau
pen.up()
pen.goto(-300, 49)
pen.down()
pen.color("#696969")
pen.begin_fill()
for _ in range(2):
    pen.forward(30)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
pen.end_fill()

# Écrire du texte à côté du carré
pen.color("White")
pen.up()
pen.goto(-50, -50)
pen.down()
pen.write("Joyeuse 46ème fête d'independance !", align="left", font=("Roboto", 14, "bold"))


#Copyright
pen.color("Yellow")
pen.up()
pen.goto(150, -250)
pen.down()
pen.write("Write by Hamoud", align="left", font=("Roboto", 14, "bold"))

# Cacher le stylo
pen.hideturtle()

# Terminer le programme
turtle.done()
