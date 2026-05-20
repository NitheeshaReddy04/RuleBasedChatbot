import datetime
import random

print("🤖 SmartBot: Hello! Type 'bye' to exit.")

jokes = [
    "Why do programmers hate bugs? Because they make life byte-sized misery!",
    "Why was the computer cold? It left its Windows open!",
    "Why do Python programmers love snakes? Because they don't bite errors!"
]

while True:
    user_input = input("You: ").lower()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        print("🤖 SmartBot: Hello there!")

    # Asking name
    elif "name" in user_input:
        print("🤖 SmartBot: I'm SmartBot.")

    # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"🤖 SmartBot: Current time is {current_time}")

    # Date
    elif "date" in user_input or "day" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"🤖 SmartBot: Today's date is {current_date}")

    # Mood
    elif "how are you" in user_input:
        print("🤖 SmartBot: I'm doing great!")

    # Joke
    elif "joke" in user_input or "funny" in user_input:
        print("🤖 SmartBot:", random.choice(jokes))

    # AI Questions
    elif "ai" in user_input:
        print("🤖 SmartBot: AI stands for Artificial Intelligence.")

    # Coding Questions
    elif "python" in user_input:
        print("🤖 SmartBot: Python is a powerful programming language.")

    # Help
    elif "help" in user_input:
        print("🤖 SmartBot: Ask me about AI, Python, jokes, time, or date.")

    # Exit
    elif "bye" in user_input or "exit" in user_input:
        print("🤖 SmartBot: Goodbye!")
        break

    # Unknown questions
    else:
        responses = [
            "Interesting question!",
            "I am still learning that.",
            "Can you ask differently?",
            "That's something I don't know yet."
        ]

        print("🤖 SmartBot:", random.choice(responses))