# Gemini Chatbot (Tkinter + Google Gemini API)

A simple AI chatbot desktop application built using **Python**, **Tkinter**, and **Google Gemini API**. The application provides a user-friendly graphical interface where users can chat with Google's Gemini AI model in real time.

## Features

* Clean and simple GUI using Tkinter
* Real-time conversation with Gemini AI
* Maintains chat history during the session
* Scrollable chat window
* Send messages using Enter key or Send button
* Easy to customize and extend

## Technologies Used

* Python 3.x
* Tkinter
* Google Generative AI (Gemini API)

## Project Structure

```text
gemini-chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install google-generativeai
```

or

```bash
pip install -r requirements.txt
```

## Configure Gemini API Key

Replace the API key in the code:

```python
genai.configure(api_key="YOUR_API_KEY")
```

You can get your API key from:

https://aistudio.google.com/app/apikey

## Run the Application

```bash
python chatbot.py
```

## How It Works

1. User enters a message.
2. Message is sent to Gemini AI.
3. Gemini generates a response.
4. Response is displayed in the chat window.
5. Conversation history is preserved for context.

## Screenshots

Add screenshots of your chatbot here.

## Future Improvements

* Dark Mode
* Chat Export to TXT/PDF
* Voice Input
* Voice Output (Text-to-Speech)
* Multiple Gemini Models
* Save Chat History

## Requirements

```text
google-generativeai
```

## License

This project is open-source and available under the MIT License.

## Author

Developed by Sowdagar Thabasum


<img width="600" height="534" alt="WhatsApp Image 2026-06-22 at 6 12 34 PM" src="https://github.com/user-attachments/assets/715d4dfd-1a34-40da-a9b9-fc9cbd10cbcf" />

<img width="600" height="512" alt="WhatsApp Image 2026-06-22 at 6 13 02 PM" src="https://github.com/user-attachments/assets/e451f2cb-2b43-4f34-a0eb-a69fbfa58423" />

