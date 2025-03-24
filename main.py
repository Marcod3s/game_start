# make 3 rooms, solutions to each

import Rooms as r
import character as ch

print ("Welcome to the quest of hawk tuah")
username = input("Enter your username: ")

character = ch.character(username, 20)


r.room1(character)

if character.health == 0:
  print("YOU DIED")
  exit()

r.room2(character)

if character.health == 0:
  print("YOU DIED")
  exit()

r.room3(character)

if character.health == 0:
  print("YOU DIED")
  exit()