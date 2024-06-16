import tkinter as tk
from tkinter import scrolledtext

class RuleBasedChatbot:
    def __init__(self, master):
        self.master = master
        self.master.title("Rule-Based Chatbot")
        
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled', width=50, height=20)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.input_area = tk.Entry(master, width=40)
        self.input_area.grid(row=1, column=0, padx=10, pady=10)
        
        self.send_button = tk.Button(master, text="Send", command=self.get_response)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.display_message("Chatbot: Hi! How can I help you today?")
    
    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')
    
    def get_response(self):
        user_input = self.input_area.get().strip()
        if user_input:
            self.display_message(f"You: {user_input}")
            response = self.generate_response(user_input)
            self.display_message(f"Chatbot: {response}")
            self.input_area.delete(0, tk.END)
    
    def generate_response(self, user_input):
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input:
            return "Hello! How can I assist you today?"
        elif "how are you" in user_input:
            return "I'm a chatbot, so I don't have feelings, but thank you for asking!"
        elif "name" in user_input:
            return "I am a simple rule-based chatbot created to assist you."
        elif "weather" in user_input:
            return "I don't have real-time data, but you can check a weather website for current information."
        elif "bye" in user_input or "goodbye" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = RuleBasedChatbot(root)
    root.mainloop()
