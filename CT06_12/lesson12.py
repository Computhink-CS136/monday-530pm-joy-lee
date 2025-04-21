   #inside the loop
    # order = order + answer + ", "
    # answer = input("what is your order?")
#outside the loop
# print("you have ordered these items. do enjoy your meal!")
# print(order)




import random
for count in range(10):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    #what is 3 + 5?
    question = "what is" + str(number1) + " + " + str(number2) +"?"
    answer = int(input (question))
    hidden_answer = number1 + number2
    while not answer == hidden_answer:
       print("wrong! try again!")
    answer = input(question)
    answer = int(answer) #convert to a number
else:
    print("you are correct!")

