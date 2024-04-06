import gradio as gr
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nalini2004",
    database="employee"
)

def execute_query(query):
    try:
        # Execute SQL query
        cursor = conn.cursor()
        cursor.execute(query)
        
        # Fetch data
        result = cursor.fetchall()
        
        if result:
            # Return fetched data
            return result
        else:
            return "No data found."
        
        # Close database connection
        cursor.close()
    except Exception as e:
        return f"Error executing SQL query: {e}"

def process_command(command):
    if command.strip().lower() == "retrieve john doe data":
        query = "SELECT * FROM employee_data WHERE name = 'John Doe'"
        return execute_query(query)
    elif command.strip().lower() == "hi":  # Fixed indentation here
        query = "SELECT * FROM employee_data WHERE name ='Jane Smith'"
        return execute_query(query)
    else:
        return "Command not recognized."

def chatbot(command):
    response = process_command(command)
    return response

chatbot_interface = gr.Interface(fn=chatbot, inputs="textbox", outputs="textbox", title="Chatbot", description="Type 'retrieve John Doe data' to fetch data for John Doe or 'hi' to fetch data with salary 50000.00.")
chatbot_interface.launch()
