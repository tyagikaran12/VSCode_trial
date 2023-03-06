import random

Q1 = "Who is Karan Tyagi?" \
     "A.Boy " \
     "B.Girl"
Q2 ="Where does Karan Tyagi live?" \
    "A.Holambi Kalan " \
    "B.Khera Khurd"
Q3 = "Who is Prime Minister of India?" \
     "A.Narendra Modi " \
     "B.Rahul Gandhi"
Q4 = "In which  country Ganga located?" \
     "A.Bnagladesh " \
     "B.India"
Questions = [[Q1,"A",10000],[Q2,"A",50000],[Q3,"A",75000],[Q4,"B",100000]]
random.shuffle(Questions)


reward = 0
for q,answer,amount in Questions:
    print(q)
    o1 = input("Enter your option here: ")
    if o1 == answer:
        print("You won")
        reward+=amount
        print(amount)
        print("Do you want to continue?"
              "A.Yes "
              "B.No")
        choice = input("Enter your choice here: ")
        if choice != "A":
            break
    else:
        print("Do you want to take help of your partner?"
              "A. Yes "
              "B. No ")
        choice_2 = input("Enter your choice for partner here: ")
        if choice_2 == "A":

            partner_choice = input("Enter audience choice here: ")
            if partner_choice == answer:
                print("You won")
                print(amount)
                reward+=amount
            else:
                break
        else:
            print("You lose")
            print(reward)
            break
print("Total amount you won= " + str(reward))