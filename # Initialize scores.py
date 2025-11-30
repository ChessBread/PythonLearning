# Initialize scores
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# Q1) Dawn or Dusk as numbers
q1 = int(input("Q1) Do you prefer:\n1) Dawn\n2) Dusk\n"))

if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

# Q2) How do you want to be remembered
q2 = int(input("""Q2) When I’m dead, I want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold
"""))

if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print("Please enter a number from 1 to 4.")

# Q3) Favorite instrument
q3 = int(input("""Q3) Which kind of instrument most pleases your ear?
1) Violin
2) Trumpet
3) Piano
4) Drum
"""))

if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

# Print final scores
print("\nFinal Scores:")
print("Gryffindor:", Gryffindor)
print("Ravenclaw:", Ravenclaw)
print("Hufflepuff:", Hufflepuff)
print("Slytherin:", Slytherin)