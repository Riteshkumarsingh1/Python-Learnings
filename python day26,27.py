# create a python program that greets the user by good morning sir  using time module

# import time
# current_time = time.localtime()
# hour = current_time.tm_hour
# if (hour<12):
#     print("Good Morning Sir")
# else:
#     if(hour<18):
#         print("Good Afternoon Sir")
#     else:
#         print("Good Evening Sir")







# KBC   : CREATE A PROGRAM CAPABLE OF DISPLAYING QUESTIONS TO THE USER LIKE KBC

# use list data type to store the questions and their correct answers
# display the final amount the person is taking home after playing the game 



kbc_ques = [
    ("What is the capital of India?",
    ("A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"),
    "B",
    1000),
    
    ("Who is the Prime Minister of India?",
    ("A) Rahul Gandhi", "B) Narendra Modi", "C) Amit Shah", "D) Manmohan Singh"),
    "B",
    2000),
    
    ("Who is the Chief Minister of Uttar Pradesh?",
    ("A) Mayawati", "B) Akhilesh Yadav", "C) Yogi Adityanath", "D) Mulayam Singh Yadav"),
    "C",
    3000),
    
    ("Who is the Chief Minister of Maharashtra?",
    ("A) Uddhav Thackeray", "B) Devendra Fadnavis", "C) Eknath Shinde", "D) Sharad Pawar"),     "C",
    5000),
    
    ("Which is the largest planet in our solar system?",
    ("A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"),
    "C",
    10000),
    
    ("Who wrote the Indian national anthem?",
    ("A) Bankim Chandra Chatterjee", "B) Rabindranath Tagore", "C) Sarojini Naidu", "D) Subhash Chandra Bose"),
    "B",
    20000),
    
    ("What is the national animal of India?",
    ("A) Lion", "B) Elephant", "C) Tiger", "D) Peacock"),
    "C",
    40000),
    
    ("Which is the longest river in India?",
    ("A) Ganga", "B) Yamuna", "C) Brahmaputra", "D) Godavari"),
    "A",
    80000),
    
    ("Who is known as the 'Iron Man of India'?",
    ("A) Jawaharlal Nehru", "B) Sardar Vallabhbhai Patel", "C) B.R. Ambedkar", "D) Mahatma Gandhi"),
    "B",
    160000),
    
    ("Which company developed the Python programming language?",
    ("A) Microsoft", "B) Google", "C) CWI", "D) Apple"),
    "C",
    320000)
]
def kbc_game():
    print("="*50)
    print("WELCOME TO KBC!")
    print("="*50)
    
    # List of questions (question, options tuple, correct answer, prize)
    kbc_questions = [
        ("What is the capital of India?",
         ("A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"),
         "B", 1000),
        ("Who is the Prime Minister of India?",
         ("A) Rahul Gandhi", "B) Narendra Modi", "C) Amit Shah", "D) Manmohan Singh"),
         "B", 2000),
        ("Who is the Chief Minister of Uttar Pradesh?",
         ("A) Mayawati", "B) Akhilesh Yadav", "C) Yogi Adityanath", "D) Mulayam Singh Yadav"),
         "C", 3000),
        ("Who is the Chief Minister of Maharashtra?",
         ("A) Uddhav Thackeray", "B) Devendra Fadnavis", "C) Eknath Shinde", "D) Sharad Pawar"),
         "C", 5000),
    ]
    
    total_prize = 0
    ques_no = 1
    
    for q_data in kbc_questions:
        question, options, correct_ans, prize = q_data
        print(f"\nQuestion no: {ques_no} for Rs. {prize}")
        print(question)
        for opt in options:
            print(opt)
        
        user_ip = input("\nYour answer (A/B/C/D) or 'QUIT' to stop: ").strip().upper()
        
        if user_ip == "QUIT":
            print(f"You quit the game. You take home Rs. {total_prize}")
            break
        
        if user_ip == correct_ans:
            print(f"✅ Correct! You won Rs. {prize}")
            total_prize = prize   # in KBC, prize becomes current level amount (not add)
            ques_no += 1
            
            if ques_no <= len(kbc_questions):
                cont = input("Do you want to continue? (y/n): ").strip().lower()
                if cont != 'y':
                    print(f"You decided to stop. You take home Rs. {total_prize}")
                    break
        else:
            print(f"❌ Wrong answer! Correct answer was {correct_ans}.")
            # Simple penalty: if crossed question 2, get 1000 else 0
            if ques_no >= 3:
                total_prize = 1000
            else:
                total_prize = 0
            print(f"You go home with Rs. {total_prize}")
            break
    else:
        # This else runs if for loop completes without break (all questions correct)
        print(f"\n🏆 Congratulations! All answers correct!")
        print(f"🏆 You take home Rs. {total_prize}")
    
    print("\n" + "="*50)
    print(f"Final Amount: Rs. {total_prize}")
    print("Thanks for playing KBC!")
    print("="*50)

if __name__ == "__main__":
    kbc_game()
            
            
            
            
            
#             Summary – Flow of Program



# Initialize list of questions.

# Show rules.

# Loop through each question.

# Display question, options, prize.

# Get user input.

# If quit → exit with current prize.

# If correct → update prize, ask to continue.

# If wrong → show answer, apply penalty, exit.

# If all questions correct → grand prize.

# Print final amount.







