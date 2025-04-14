print("Hello from lesson 10")

score=input("give me your score") # default, it is a string
score=int(score) #converting this to a integer
if score> 90:
    print("you've gotten grade A")
elif score >= 80:
    print("you've gotten grade B")
elif score >= 70:
    print("you've gotten grade C")
elif score >= 60:
    print("you've gotten grade D")
else:
    print("you've gotten grade E")