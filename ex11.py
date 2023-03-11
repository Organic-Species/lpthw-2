print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Can you solve this issue? 3 + 12", end=' ')
equation = input()
if equation == 15:
    print ('Correct')
elif equation != 0:
    print ("Sorry, That's wrong")