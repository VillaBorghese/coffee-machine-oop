#import
# import another_module
from turtle import Turtle, Screen
from prettytable import PrettyTable
#use
# print(another_module.another_variable)
#
# #turtle
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue4","aquamarine4")
# timmy.fd(100)
# #screen
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#prettytable
table = PrettyTable()
print(table)

table.field_names=["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "electric"],
    ["Bulbasaur","grass"],
    ["Riolu","fighting"],
    ["Charmander","fire"],
    ["Geodude","rock"],
])

print(table)
table.align="l"
print(table)