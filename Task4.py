"""
Task: Implement a simple chatbot that can respond to user input with predefined answers.
This is a simple implementation of a chatbot that responds to user input with predefined answers.
Author: Rathnayaka Pathiranage Sunera Dilnath
Student ID: CA/JU1/26435
Date: 2025-07-12

"""

import random


def simple_chatbot():

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