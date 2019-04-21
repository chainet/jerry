import random, sys, time
point = 0
for i in range(1,11):
    num_a = random.randint(1,11)
    num_b = random.randint(1,11)
    print(num_a, " + ", num_b, " = ")
    answer = int(input(" "))
    if answer == 0:
        print("Wait,WHAT?! You can't write a 0 here! Th-This answer can't be 0! Is that some bug or...")
        time.sleep(3)
        print("Seems this game has lot of bugs, give me a second to fix the bugs. of course, you can do next topic")
        continue
    if answer > 20:
        print("Hmmmm...I remember that the answer can not > 20...Am I mistaken?")
        time.sleep(1)
        print("Anyway it's false")
        continue
    if num_a + num_b == answer:
        print ("corect!")
        point += 1
    else:
        print ("false")
print("Finish!")
time.sleep(1.5)
if point < 4:
    print("Sorry, you got", point, "point, but I think you can do better.")
elif point > 8:
    print("congratulation! You got", point, "point! You're better than I think!")
else:
    print("Well done! You got", point, "point!")