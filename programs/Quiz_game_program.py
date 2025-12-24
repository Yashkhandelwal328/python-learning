Questions = (("Which animal lays the largest single egg in the world?"),
             ("Which continent is the only one to have land in all four hemispheres (North, South, East, and West)?"),
             ("Which human body part is the only one that is fully grown from the moment of birth?"),
             ("What is a group of pandas officially called?"),
             ("Which of these spices is the rarest and most expensive spice in the world by weight?")
             )

Options = (("A) Great White Shark","B) Elephant","C) Ostrich","D) Whale Shark"),
           ("A) Asia","B) Australia","C) Africa",'D) South America'),
           ("A) Nose","B) Heart","C) Teeth","D) Eyes"),
           ("A) A Clan","B) An Embarrassment","C) A Tower","D) A Fluff"),
           ("A) Cardamom","B) Vanilla","C) Saffron","D) Cinnamon"))
           

Answers = ('C',
           'C',
           'D',
           'B',
           'C'
           )

Guesses = []
score = 0 

for i, question in enumerate(Questions): 
    print("-----------------------------------------------------------------------------------------")
    print(f"{i+1}. {question}")
    
    
    for option in Options[i]:
        print(option)
        
    Guess = input("Enter your Answer (A,B,C,D): ").upper()
    
    
    Guesses.append(Guess) 
    
    
    if Guess == Answers[i]: 
        print("Your answer is correct! 🎉")
        score += 1
    else:
        print(f"You are wrong 😔. The correct answer was {Answers[i]}")

print("-----------------------------------------------------------------------------------------")
print("QUIZ COMPLETE!")
print(f"Your final score is: {score} out of {len(Questions)} ({round((score/len(Questions))*100, 2)}%)")