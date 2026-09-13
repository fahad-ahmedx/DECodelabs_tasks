# Project 1: Rule-Based AI Chatbot
# DecodeLabs Artificial Intelligence Training

# Knowledge base: predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Nice to meet you.",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I'm a simple rule-based AI chatbot.",
    "who are you": "I am an AI chatbot created using Python.",
    "help": "You can greet me, ask my name, or ask how I am.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!"
}

# Exit commands
exit_commands = ["exit", "quit", "bye", "goodbye"]

print("=" * 50)
print("        RULE-BASED AI CHATBOT")
print("=" * 50)
print("Hello! I am your AI chatbot.")
print("Type 'exit', 'quit', 'bye', or 'goodbye' to stop.")
print()

# Continuous conversation loop
while True:

    # Take input from the user
    user_input = input("You: ")

    # Input sanitization:
    # Convert to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Check exit command
    if user_input in exit_commands:
        print("Bot: Goodbye! Have a great day!")
        break

    # Search for a matching response
    if user_input in responses:
        print("Bot:", responses[user_input])

    # Fallback response for unknown input
    else:
        print("Bot: Sorry, I don't understand that yet.")

print("Chatbot terminated.")