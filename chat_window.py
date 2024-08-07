import sys
import os
from groq import Groq
from PyQt5.QtWidgets import (
    QMainWindow, QTextEdit, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QLabel,
    QComboBox
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Chat App")
        self.setGeometry(100, 100, 600, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.left_panel = QWidget(self)
        self.left_layout = QVBoxLayout()
        self.left_panel.setLayout(self.left_layout)

        self.left_layout.setContentsMargins(10, 10, 10, 10)
        self.left_layout.setSpacing(10)

        self.model_label = QLabel("Select Model:", self)
        self.left_layout.addWidget(self.model_label)

        self.model_selector = QComboBox(self)
        self.model_selector.addItems(["llama3-8b-8192", "llama3-70b-8192", "gemma2-9b-it"]) 
        self.left_layout.addWidget(self.model_selector)

        self.content_label = QLabel("Input Content:", self)
        self.left_layout.addWidget(self.content_label)

        self.content_input = QTextEdit(self)
        self.content_input.setPlaceholderText("Enter content here...")
        self.content_input.setMinimumSize(200, 200)  
        self.left_layout.addWidget(self.content_input)

        self.left_layout.addStretch()
        self.main_layout.addWidget(self.left_panel)

        self.chat_widget = QWidget(self)
        self.chat_layout = QVBoxLayout()
        self.chat_widget.setLayout(self.chat_layout)

        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_layout.addWidget(self.chat_display)

        self.input_field = QLineEdit(self)
        self.chat_layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.chat_layout.addWidget(self.send_button)

        self.main_layout.addWidget(self.chat_widget, stretch=1)

        self.input_field.returnPressed.connect(self.send_message)

        groq_api_key = os.environ.get('GROQ_API_KEY')
        if groq_api_key is None:
            raise KeyError("Environment variable 'GROQ_API_KEY' is not set.")
        self.client = Groq(api_key=groq_api_key)

    def send_message(self):
        user_message = self.input_field.text()
        if not user_message:
            QMessageBox.warning(self, "Warning", "Please enter a message.")
            return

        self.chat_display.append(f'<span style="color: green;">You: {user_message}</span>')
        self.input_field.clear()

        try:
            model = self.model_selector.currentText()  
            content = self.content_input.toPlainText()  
            response = self.get_groq_ai_response(user_message, model, content)
            self.chat_display.append(f"AI: {response}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to get response: {e}")

    def get_groq_ai_response(self, prompt, model, content):

        combined_prompt = f"{content}\n\nUser Question: {prompt}"

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "user", "content": combined_prompt},
                ],
                model=model,  
            )
            return chat_completion.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

