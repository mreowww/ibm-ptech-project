import os
from ibm_watson_machine_learning.foundation_models import Model
import colors
import menu
from dotenv import load_dotenv

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal

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


# Main loop
while True:
    prompt = "Input: " + input(colors.gray + "\nEnter your prompt (or 'q' to quit):" + colors.reset) + "\n"
    if prompt == 'Input: q' + "\n":
        os.system('cls')  # clear the terminal
        exit(0)

    # Generate the response
    response = model.generate_text(prompt=menu.instruction + history + prompt + "Output:")

    # Add the response to the history and print it
    history += prompt + response + "\n"
    print(colors.green + response + colors.reset)