# Voice Assistant

This Python script serves as a basic voice assistant that performs Google searches based on user input. It utilizes the following libraries:

- **speech_recognition**: Used for recognizing speech input from the user.
- **pyttsx3**: Utilized for converting text to speech, enabling the assistant to provide audible responses.
- **webbrowser**: Employed to open web browser windows and perform Google searches.

## Functionality

The script performs the following tasks:

1. Initializes the Text-to-Speech engine.
2. Defines functions for speaking text and listening to user input.
3. Greets the user with a predefined message.
4. Listens for the user's response.
5. Upon hearing "hello" from the user, prompts the user for their query.
6. Performs a Google search using the user's query and opens the results in the default web browser.
7. Asks the user if they need any further assistance.
8. If the user requests additional searches, the assistant continues to listen and perform searches accordingly.
9. Terminates the conversation when the user indicates they have no further queries.

## Usage

To use the voice assistant, simply execute the Python script. Ensure that the required libraries (`speech_recognition`, `pyttsx3`) are installed in your Python environment.

## Note

This is a basic implementation of a voice assistant and may require further customization or refinement for specific use cases. Feel free to modify and expand upon the script as needed.
