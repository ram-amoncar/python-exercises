# KBC
import random

# First choice in answer tuple is always is the correct answer
que_n_ans = {
    "What is the output of 'print(2 ** 3)' ?": ("8", "6", "9", "5"),
    "How do you comment a single line in Python?": (
        "# Comment",
        "// Comment",
        "/* Comment */",
        "-- Comment",
    ),
    "What keyword is used to define a function in Python?": (
        "def",
        "func",
        "function",
        "define",
    ),
    "How do you create a empty set in Python?": (
        "set()",
        "{,}",
        "{}",
        "()",
    ),
    "How do you import a module in Python?": (
        "import module_name",
        "include module_name",
        "require module_name",
        "using module_name",
    ),
}

prize_money = (
    "Zero",
    "Five Thousand",
    "Fifty Thousand",
    "One Lakh",
    "Fifty Lakhs",
    "Seven Crore",
)
imo = 0


print("Welcome to Kaun Banega Crorepati (Python Version)")
for q, a in que_n_ans.items():
    shuffled_order = list(range(len(a)))
    random.shuffle(shuffled_order)
    win_index = shuffled_order.index(0)

    index = 1
    print(f"\nFor: {prize_money[imo + 1]} Rupees")
    print(q)
    for i in shuffled_order:
        print(f"\t{index}. {a[i]}", end="\t\t")
        if index % 2 == 0:
            print()  # printing newline
        index += 1
    usr_ans = int(input("Option: "))

    if win_index != usr_ans - 1:
        print("\nIncorrect Answer")
        print(f"Correct Answer was: {a[0]}")
        break
    else:
        print("\nCorrect Answer")
        imo += 1
        if imo == len(prize_money) - 1:
            break
        print(f"For: {prize_money[imo + 1]} Rupees")
        if input("Do you want to continue ? (y/n): ").lower() != "y":
            break


print(f"\nYou won: {prize_money[imo]} Rupees")
