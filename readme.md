# Rusty Bot: Your Companion for Enhanced Rust Gameplay

## Overview

Rusty Bot is a Python-based tool designed to connect with the Rust game through the official Rust+ API and Companion App. As a hobby project turned essential in-game utility, Rusty Bot offers Rust players real-time data and interactive capabilities, enhancing the overall gameplay experience without compromising the game's integrity or fair play.

## Understanding Rust+

Rust+ is an official companion app for the survival game Rust, developed by Facepunch Studios. It facilitates out-of-game interactions by allowing players to receive alerts about in-game events, control devices within their bases, and communicate with teammates. The Rust+ API provides a gateway for external applications like Rusty Bot to interact with the game's server, enriching the player's experience with additional layers of interaction and control.

## Features of Rusty Bot

Rusty Bot leverages the Rust+ API to introduce a series of functionalities aimed at making the Rust gaming experience more immersive and manageable:

- **Real-Time Notifications:** Players can receive instant notifications for specific events happening within the game, such as attacks on their bases or significant in-game occurrences.
- **In-Game Chat Commands:** Through simple commands entered into the in-game chat, players can engage with Rusty Bot to perform tasks like querying current game states or setting reminders, all designed to enhance strategic gameplay.
- **Automated Responses and Actions:** Rusty Bot can execute predefined actions based on specific game events or player commands, helping to manage routine tasks or alerts efficiently.

Rusty Bot stands out for its simplicity, effectiveness, and the practical value it brings to the Rust gameplay. It's a testament to what can be achieved with a passion for gaming and a bit of coding knowledge.



## Project Setup

Follow these steps to set up the project on your local machine:

1. **Install Python**

   If you haven't installed Python yet, download it from the official Python website: https://www.python.org/downloads/

2. **Navigate to the Project's Directory**

   Open Terminal or Command Prompt and navigate to your project's directory using `cd` command.

3. **Create a Virtual Environment**

   Use the following command to create a virtual environment in your project's directory:
   ```shell
   python -m venv .env
   ```
   This command creates a virtual environment named ".env".

4. **Activate the Virtual Environment**

   After you've created a virtual environment, you need to activate it.

   On Windows:
   ```shell
   .\\.env\\Scripts\\activate
   ```
   On MacOS / Linux:
    ```shell
   source .env/bin/activate
    ```

5. **Upgrade pip**

   Once the virtual environment is activated, you can upgrade pip using the following command:
   ```shell
   python -m pip install --upgrade pip
   ```
   
6. **Install Required Libraries**

   Now navigate back to your project directory and install the required libraries using `requirements.txt` file. Use the following command:
   ```shell
   python -m pip install -r requirements.txt
   ```
   Make sure that your project directory contains the `requirements.txt` file listing all the necessary libraries.

7. **Modify libraries**

    Now navigate to the `lib` directory inside `.env` and look for the rust_marker.py file located in `rustplus/structures/'rust_marker.py'`.
    Open the file and search for the property `name`.
    Under the property `name` you need to add the following lines of code:
    ```python
    @name.setter # Modified by Mike Vermeer
    def name(self, value: str):
        self._name = value
    ```

    Note: This is a temporary thing for now. You need to do this every time you create a new virtual environment or update the libraries.


8. **Run the Project**

   Now you can run the project using the following command:
   ```shell
   python main.py
   ```

9. **Deactivate the Virtual Environment**

   When you're done working, you can deactivate the virtual environment by simply typing `deactivate` into the terminal.
