import random
hand = random.randint(0, 1)
goal = input("Choose one of these hands, left or right: ").upper()
if hand == 0:
    hand = "RIGHT"
else:
    hand = "LEFT"

match goal:
    case "LEFT":
        if hand == "LEFT":
            print("You Win")
        else:
            print(f"You Lose. {hand.lower}")
    case "RIGHT":
        if hand == "RIGHT":
            print("You Win")
        else:
            print(f"You Lose. {hand.lower}")
    case _:
        print("Invalid Input!")
