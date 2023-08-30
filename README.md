# gpt-twenty-questions

# 20 Questions with ChatGPT

## Overview

This Python script uses the OpenAI GPT-3 API to play a game of 20 Questions where the bot thinks of a person from a predefined list and the player attempts to guess who it is.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Install the required packages.

    ```bash
    pip install openai
    ```

## Prerequisites
1. Python 3.x
2. OpenAI API key
3. OpenAI Python package

## Description

This Python script is a 20 Questions game involving a list of 60 famous people, real and fictional. The program begins by importing the OpenAI library, setting an API key, and then initializing a list of potential people. This list contains diverse choices, such as "Harry Potter," "Mahatma Gandhi," and "Marilyn Monroe," among others. Once the list is ready, the program uses Python's random module to pick a person from that list. The game kicks off with a printed statement welcoming the player and a brief pause to build anticipation.

The main logic of the game is handled in a while loop that iterates up to 20 times, allowing the player to ask up to 20 questions. Within this loop, the player inputs a question, which is then processed using the OpenAI GPT-3 engine. To do so, the script makes use of the function chat_bot, which takes a prompt string and passes it to GPT-3's Davinci engine. The bot responds with either 'Yes' or 'No,' based on the characteristics or attributes of the selected person. After each question, the player has the opportunity to make a guess. If the guess is correct, the game ends, and if not, the loop counter is incremented by an extra turn as a penalty.

Additionally, after each question or guess, the player can decide whether they want to make a guess at who the person is. If they opt to guess and get it correct, a congratulatory message is displayed and the game ends. If the guess is incorrect, the player loses a turn. If all 20 questions are asked without a correct guess, the game announces that the player has run out of questions and reveals the correct answer. This makes for an engaging game of 20 Questions where the computer intelligently answers queries about a randomly selected person from a pre-defined list, all while offering the player the option to guess who the person is at each turn.
