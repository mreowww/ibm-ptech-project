from flask import Flask, request, render_template
import os
from ibm_watson_machine_learning.foundation_models import Model
import colors
import menu
from dotenv import load_dotenv
import re

app = Flask(__name__)

# Get the credentials & project id
load_dotenv()
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": os.getenv("APIKEY")
}
project_id = os.getenv("PROJECT_ID")

# Load the model
model = Model(
    model_id=menu.model_id, 
    params=menu.parameters,
    credentials=credentials,
    project_id=project_id)

history = "" # Initialize the history

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global history
    if request.method == 'POST':
        prompt = request.form['prompt']
        # Generate the response
        response = model.generate_text(prompt=menu.instruction + history + "Input: " + prompt + "\nOutput:")
        # Add the prompt and response to the history string
        history += "Input: " + prompt + "\nOutput: " + response + "\n"
    
    # Check if history is empty or only contains "Input:" and "Output:" prompts
    stripped_history = re.sub(r'(Input:|Output:|\s)', '', history)
    if stripped_history == '':
        messages = None
    else:
        # Split the history string into a list of messages at each "Input:" and "Output:" prompt
        messages = re.split(r'(?=Input:|Output:)', history)
    
    return render_template('chat.html', messages=messages)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=5000)