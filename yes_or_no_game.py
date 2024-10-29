
print("Welcome to my game!!!\n")
print("This is a quiz game. Are you ready to play this game?")

output = input(" Y or N\n")
if output == 'Y' or output == 'y':
    print("\nYour game has started now\n")
    finish = 0;
    print(" currently your score is 0. If your answer is correct you will give 1 marks for each correct answer")
    while (finish == 0):
        point = 0
        #first question
        question1 = print("\n\nWho is the Prime Minister of India ?")
        print("A. Narendra Modi")
        print("B. Rajendra Prasad")
        print("C. Indira Gandhi")
        print("D. Aditya Nath")
        
        ans = input();
        if ans == 'A' or ans == 'a':
            print("Correct Answer")
            point = point+1
            print("your point is : ",point);
        else:
            print("Wrong Answer")

    
        #Second question
        question1 = print("\n\nWhat is the National Flower of India ?")
        print("A. Lily")
        print("B. Rose")
        print("C. Lotus")
        print("D. other")
        ans = input();
        if ans == 'C' or ans == 'c':
            print("Correct Answer")
            point = point+1
            print("your point is : ",point);
        else:
            print("Wrong Answer")
            
            
        #Third question
        question1 = print("\n\nWho is the Persident of India ?")
        print("A. Narendra Modi")
        print("B. Rajendra Prasad")
        print("C. Indira Gandhi")
        print("D. Droupadi Murmu")
        ans = input();
        if ans == 'D' or ans == 'd':
            print("Correct Answer")
            point = point+1
            print("your point is : ",point);
        else:
            print("Wrong Answer")
    
    
        #Fourth question
        question1 = print("\n\nwhat is the national bird of India ?")
        print("A. Parrot")
        print("B. Peacock")
        print("C. Crow")
        print("D. Owl")
        ans = input();
        if ans == 'B' or ans == 'b':
            print("Correct Answer")
            point = point+1
            print("your point is : ",point);
        else:
            print("Wrong Answer")
    
    
        #Fifth question
        question1 = print("\n\nWho is the Chief Minister of Delhi ?")
        print("A. Narendra Modi")
        print("B. Rajendra Prasad")
        print("C. Arvind Kejriwal")
        print("D. Aditya Nath")
        ans = input();
        if ans == 'C' or ans == 'c':
            print("Correct Answer")
            point = point+1
            print("your point is : ",point);
        else:
            print("Wrong Answer")

    
    
        print("your game is over!")
        print("your total mark is : ",point);
        print("Thanks for Playing.")
        finish = 1;
    
else:
    print("good bye")
    finish = 1;

    
    # TODO: write code...

