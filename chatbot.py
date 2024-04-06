import tkinter as tk
from tkinter import messagebox
import mysql.connector
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import gradio as gr

# Download NLTK data (you only need to do this once)
nltk.download('punkt')
nltk.download('stopwords')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
porter = PorterStemmer()

def preprocess_command(command):
    # Tokenize the command
    tokens = word_tokenize(command)
    
    # Remove stopwords
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Stem the tokens
    stemmed_tokens = [porter.stem(word) for word in filtered_tokens]
    
    # Join the stemmed tokens back into a command string
    preprocessed_command = ' '.join(stemmed_tokens)
    
    return preprocessed_command

def fetch_data(name):
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nalini2004",
            database="employee"
        )
        
        # Execute SQL query
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee_data")
        
        # Fetch data
        result = cursor.fetchall()
        
        if result:
            # Display fetched data
            messagebox.showinfo("Query Result", f"Data:\n{result}")
        else:
            messagebox.showinfo("Query Result", "No data found.")
        
        # Close database connection
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error executing SQL query: {e}")

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=fetch_data, inputs="textbox", outputs="textbox", title="Greeting Interface", description="Enter your name and click submit to get a greeting message.")
    
if __name__ == "__main__":
    demo.launch()