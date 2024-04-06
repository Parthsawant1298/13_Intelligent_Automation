import gradio as gr
import google.generativeai as genai

# Configure the Generative AI with your API key
genai.configure(api_key="AIzaSyDoR10wPWSnCCLXHZWWrlrAg7XCXFzzpx8")  # Replace "YOUR_API_KEY" with your actual API key

# Create a GenerativeModel instance
model = genai.GenerativeModel(model_name="gemini-pro")

# Define the chat_with_gemini function to interact with the Generative AI
def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text  # Extract the generated text from the response object

def chatbot_response(user_input):
    if user_input.lower() in ["quit", "exit", "bye"]:
        return "Goodbye!"
    response = chat_with_gemini(user_input)
    return response

inputs = gr.Textbox(lines=2, label="You")
output = gr.Textbox(label="Chatbot")

gr.Interface(fn=chatbot_response, inputs=inputs, outputs=output).launch()
