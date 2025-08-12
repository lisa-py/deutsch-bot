# A list of dictionaries to hold our vocabulary to keep the related data together!

word_bank = [
    {
        "question": "Hello", 
        "answer": "Hallo"
    },
    {
        "question": "Goodbye",
        "answer": "Auf Wiedersehen"
    },
    {
        "question": "Thank you", 
        "answer": "Danke"
    },
    {
        "question": "Yes",
        "answer": "Ja"
    },
    {
        "question": "No",
        "answer": "Nein"
    },
    {
        "question": "The man",
        "answer": "Der Mann"
    },
    {
        "question": "The woman",
        "answer": "Die Frau"
    },
    {
        "question": "A man",
        "answer": "Ein Mann"
    },
    {
        "question":"A woman",
        "answer": "Eine Frau"
    },
    {   
        "question": "Coffee",
        "answer": "Kaffee"
    },
    {
        "question": "Tea",
        "answer": "Tee"
    },
    {
        "question": "Water",
        "answer": "Wasser"
    },
    {  
        "question": "Bread",
        "answer": "Brot"
    },
    {   
        "question": "and",
        "answer": "und"
    },
    {        
        "question": "Please",
        "answer": "Bitte"
    },
    {   
        "question": "or",
        "answer": "oder"
    },
    {    
        "question": "Wine",
        "answer": "Wein"
    },
    {        
        "question": "Beer",
        "answer": "Bier"
    },
    {        
        "question": "Milk",
        "answer": "Milch"
    },
    {        
        "question": "Cat",
        "answer": "Katze"
    },
    {        
        "question": "Dog",
        "answer": "Hund"
    }
]

#Setting up game variables to keep track of the score and the flow of the game
score = 0

print("--- Hallo from Dein Deutsch-Bot! ---")
print("Ready to challenge your linguistic drivers?\n")
print("Decrypt the following English data-strings. PROCEED, and try not to disappoint my circuits.\n")
print("EXIT- This message will not self-destruct, but your pride might if you fail.") #to quit the game
print("Your quest begins now!\n")

#A loop through word_bank to ask questions and check answers
for qa_pair in word_bank:
    english_word = qa_pair["question"]
    german_word = qa_pair["answer"]

    user_answer = input(f"Can your linguistic drivers decrypt '{english_word}' to German? ")

    if user_answer.lower() == german_word.lower():
        print("Gut Gemacht! Your circuits are functioning well.\n")
        score +=1
    else:
        print(f"Not Quite! The correct answer is '{german_word}'.\n")


#Calculating score and win percentage

total_questions= len(word_bank)

win_percentage = (score/total_questions)*100.0

print("--- Quest Completed! ---")
print("Calculating your performance...\n")
print(f"Gems Collected {score} out of {total_questions}.")

#formatting the float to 2 decimal places for a cleaner look.
print(f"Your win percentage is {win_percentage:.2f}%.")

if win_percentage >= 70:
    print("You have successfully decrypted the linguistic drivers! Your circuits are intact.")  
elif win_percentage >= 100:
    print("You are a linguistic genius! Your circuits are in perfect condition.")
else:
    print("Your circuits might need some recalibration. Better luck next time!")            
print("Thank you for playing! Auf Wiedersehen!")  # Goodbye message
print("--- End of Transmission ---")