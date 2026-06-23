import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="Enter your api key")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)

history = []

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gemini Chatbot")
        self.root.geometry("700x700")

        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            width=80,
            height=30,
            state="disabled"
        )
        self.chat_area.pack(pady=10)

        self.entry_msg = tk.StringVar()

        self.entry_box = tk.Entry(
            root,
            textvariable=self.entry_msg,
            width=60
        )
        self.entry_box.pack(side=tk.LEFT, padx=10, pady=10)
        self.entry_box.bind("<Return>", self.send_msg)

        self.send_button = tk.Button(
            root,
            text="Send",
            command=self.send_msg
        )
        self.send_button.pack(side=tk.RIGHT, padx=10)

    def send_msg(self, event=None):
        msg = self.entry_msg.get()

        if not msg:
            return

        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"You: {msg}\n")
        self.chat_area.config(state="disabled")

        self.entry_msg.set("")

        try:
            global history

            chat_session = model.start_chat(history=history)
            response = chat_session.send_message(msg)

            bot_reply = response.text

            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")
            self.chat_area.config(state="disabled")

            history.append({"role": "user", "parts": [msg]})
            history.append({"role": "model", "parts": [bot_reply]})

        except Exception as e:
            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, f"Error: {e}\n")
            self.chat_area.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
