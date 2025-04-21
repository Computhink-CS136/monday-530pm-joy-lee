order = ""
answer = input("what is your order?")
while not answer == "end":
    order = order + answer + ", "
    answer = input("what is your order?")
print("you have ordered these items. do enjoy your meal!")
print(order)