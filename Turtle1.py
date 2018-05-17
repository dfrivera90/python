# -*- coding:utf-8 -*-
import turtle
def main():
    window = turtle.Screen()
    daniel = turtle.Turtle()

    make_rectangle(daniel)

    turtle.mainloop()

def make_rectangle(daniel):
    lenght = int(input('Tamaño de Lado: '))

    for i in range(4):
        make_line(daniel, lenght)

def make_line(daniel, lenght):
    daniel.forward(lenght)
    daniel.left(90)

if __name__ == '__main__':
    main()
