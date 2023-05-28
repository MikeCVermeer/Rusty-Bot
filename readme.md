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
   python -m pip install --upgrade pip

6. **Install Required Libraries**

   Now navigate back to your project directory and install the required libraries using `requirements.txt` file. Use the following command:
   ```shell
   python -m pip install -r requirements.txt
   ```
   Make sure that your project directory contains the `requirements.txt` file listing all the necessary libraries.


7. **Run the Project**

   Now you can run the project using the following command:
   ```shell
   python main.py
   ```

8. **Deactivate the Virtual Environment**

   When you're done working, you can deactivate the virtual environment by simply typing `deactivate` into the terminal.