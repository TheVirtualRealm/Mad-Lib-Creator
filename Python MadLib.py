import random as r

person_1 = input("Person: ")
place_1 = input("Place: ")
thing_1 = input("Thing: ")
person_2 = input("Person: ")
person_3 = input("Person: ")
place_2 = input("Place:")
creapy_person = input("Creapy Person: ")
verb_1 = input("Verb: ")
place_3 = input("Place: ")
place_4 = input("Place: ")
place_5 = input("Place: ")
place_Outside_1 = input("Place Outside: ")
place_Outside_2 = input("Place Outside: ")
family_Member_1 = input("Family Member: ")
family_Member_2 = input("Family Member: ")
body_part = input("Body Part: ")


Story1 = (person_1 + " heard a noise coming from the " + place_1 + ". While on the way to check it out a " +
          thing_1 + "came flying from the" + place_2 + "and hitting me in the " + body_part)
Story2 = (person_1 + " heard a noise coming from the " + place_1 + ". While on the way to check it out a " +
          thing_1 + "came flying from the" + place_2 + "and hitting me in the " + body_part)
Story3 = (person_1 + " heard a noise coming from the " + place_1 + ". While on the way to check it out a " +
          thing_1 + "came flying from the" + place_2 + "and hitting me in the " + body_part)

randomNumber = r.randint(1, 3)

if randomNumber <=1:
    print(Story1)
elif randomNumber <=2:
    print(Story2)
else:
    print(Story3)