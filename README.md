# AI Chat Groq

This is a simple AI Chat application built using PyQt5 and Groq API. The application allows users to select an AI model, input content, and chat with the AI.

## Features

- Select from multiple AI models.
- Input custom content for the chat.
- Send and receive messages in a chat interface.

## Requirements
- Python 3.x
- PyQt5
- Groq API Key, you can get free here: https://console.groq.com/keys

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/KrzysztofW02/AI-Chat-Groq.git
    cd AI-Chat-Groq
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Set the Groq API Key as an environment variable:
    ```bash
    set GROQ_API_KEY=your_groq_api_key
    ```
## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Select an AI model from the dropdown.
3. Input custom content for the chat.
4. Type your message and click "Send" to chat with the AI.

## File Structure

- `main.py`: Entry point of the application.
- `chat_window.py`: Contains the main window and chat functionalities.
- `requirements.txt`: List of required Python packages.
