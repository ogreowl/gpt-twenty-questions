import openai
import time
import random

openai.api_key = "Insert your OpenAI API Key;"

# A list of 60 potential people
people_list = [
    "Harry Potter", "Superman", "Zeus", "Winston Churchill", "Abraham Lincoln",
    "Steve Jobs", "Elon Musk", "Sherlock Holmes", "Aristotle", "Cleopatra",
    "Robin Hood", "Lady Gaga", "Luke Skywalker", "Marilyn Monroe", "Albert Einstein",
    "Beyonce", "Mickey Mouse", "William Shakespeare", "Barack Obama", "Madonna",
    "Lionel Messi", "Adele", "Muhammad Ali", "Julius Caesar", "Nelson Mandela",
    "Mahatma Gandhi", "Marie Curie", "Isaac Newton", "Galileo Galilei", "Leonardo da Vinci",
    "Bill Gates", "Michael Jordan", "Beethoven", "Mozart", "Frida Kahlo",
    "Vincent van Gogh", "Pele", "Oprah Winfrey", "Rosa Parks", "Queen Elizabeth II",
    "Martin Luther King Jr.", "Charlie Chaplin", "Bob Marley", "Bruce Lee", "Buddha",
    "Mao Zedong", "Pablo Picasso", "Sigmund Freud", "J.K. Rowling", "Joan of Arc",
    "Osama bin Laden", "Mother Teresa", "John F. Kennedy", "Anne Frank", "Plato",
    "Michael Jackson", "John Lennon", "Darth Vader", "James Bond", "Spider-Man"
]

# Randomly pick a person from the list
person = random.choice(people_list)
print(person)

print("Welcome to twenty-questions! ChatGPT is thinking of a person -- can you guess who?")
time.sleep(1)


def chat_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message


time.sleep(1)

i = 0
while i < 20:
    question = input(f"Question {i + 1}: ")
    question_prompt = f"You are playing 20 questions. The person that you chose is '{person}'. Someone asks you: '{question}' about your person: '{person}'. Answer that question with a 'Yes' or 'No'."
    answer = chat_bot(question_prompt)
    print(answer)
    
    guess_now = input("Would you like to guess the person now? (yes/no): ").strip().lower()
    
    if guess_now == 'yes':
        guess = input("Who do you think ChatGPT is thinking of? ")

        # Validate the guess
        check_guess_prompt = f"The chosen person was '{person}'. Did the player correctly guess '{guess}'?"
        response = chat_bot(check_guess_prompt)

        if "Yes" in response:
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Incorrect guess. You lose a turn. Continue guessing or asking questions.")
            i += 1  # Increment by one more to simulate the loss of a turn
    else:
        i += 1

if i == 20:
    print(f"Sorry, you've run out of questions! The correct answer was {person}. Better luck next time!")
