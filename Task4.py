"""
Task: Implement a simple chatbot that can respond to user input with predefined answers.
This is a simple implementation of a chatbot that responds to user input with predefined answers.
Author: Rathnayaka Pathiranage Sunera Dilnath
Student ID: CA/JU1/26435
Date: 2025-07-12

"""

import random


def simple_chatbot(user_input):

    user_input = user_input.lower().strip()
    

    greet =  ["hello", "hi", "hey","good morning", "good evening"]
    how_are_you = ["how are you", "how are you doing", "how's it going"]
    farewell = ["bye", "goodbye", "see you later", "take care", "see you soon", "exit  "]

    if user_input in greet:
        return random.choice([

            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! How can I help you?",
            "Good morning! What brings you here today?",
        ])
    
    elif user_input in how_are_you:
        return random.choice([

            "I'm doing well... thanks for asking!",
            "All good here! How about you?",
            "I'm great...ready to assist you!",

        ])
    
    elif user_input in farewell:
        return random.choice([

            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Looking forward to our next chat!",
            "Take care! Until next time!",

        ])
    
    elif  user_input in ["what is your name", "who are you", "tell me about yourself"]:
        return random.choice([
            "I am a simple chatbot created to assist you.",
            "I'm your friendly chatbot, here to help!",
            "I am a chatbot designed to answer your questions.",
        ])
    
    elif user_input in ["what can you do", "what are your capabilities", "tell me your features"]:
        return random.choice([
            "I can answer your questions, provide information, and engage in simple conversations.",
            "I can assist you with various queries and provide predefined responses.",
            "I am here to help you with basic information and casual conversation.",
        ])
    
    elif user_input in ["Thank you", "thanks", "thank you very much"]:
        return random.choice([
            "You're welcome! If you have more questions, feel free to ask.",
            "No problem! I'm here to help.",
            "Glad I could assist you!",
        ])
    
    else:
        return random.choice([
            "I'm not sure how to respond to that. Can you ask something else?",
            "I don't have an answer for that, but I'm here to help with other questions.",
            "That's interesting! Can you tell me more or ask something else?",
        ])
    

def main():
    print("Welcome to simple chatbot!")
    print("Type your message below (type 'exit' to quit):")

    while True:
        user_message = input ("You: ")
        response = simple_chatbot(user_message)
        print(f"Chatbot:", response)

        if user_message.lower() in ["exit", "bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break


main()