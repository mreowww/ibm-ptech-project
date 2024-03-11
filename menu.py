import curses
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from time import sleep

def display_menu(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Define the menu options
    options = ["Identify From Description", "Custom"]
    selected_option = 0

    while True:
        # Clear the screen
        stdscr.clear()

        # Display the menu options
        for i, option in enumerate(options):
            if i == selected_option:
                stdscr.addstr(i, 0, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, f"  {option}")

        # Get user input
        key = stdscr.getch()

        # Process user input
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(options)
        elif key == ord('\n'):
            break

    # Return the selected option
    return selected_option
    print("ran")

# Run the menu
# selected_option = curses.wrapper(display_menu)

selected_option = 0

'''if selected_option == 0:
    model_id = ModelTypes.LLAMA_2_70B_CHAT
    parameters = {
    GenParams.MIN_NEW_TOKENS: 0,
    GenParams.MAX_NEW_TOKENS: 512,
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.REPETITION_PENALTY: 1
    }
    instruction = """"""
'''

if selected_option == 0:
    model_id = ModelTypes.GRANITE_13B_CHAT_V2
    parameters = {
    GenParams.MIN_NEW_TOKENS: 0,
    GenParams.MAX_NEW_TOKENS: 512,
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.REPETITION_PENALTY: 1
    } 
    instruction = """Determine what the user is trying to describe. Whether it be category of an object, movie/book contaning a character/actor or a description.
Input:What is an apple?
Output:fruit.
Input:What movie is about dinosaurs and has a character named Alan Grant?
Output:The movie you are trying to describe is Jurassic Park. The character Alan Grant is played by Sam Neill.
Input: Who is the main character in Breaking Bad? And I want to know how many seasons are there?
Output: The main character in Breaking Bad is Walter White, and there are 5 seasons of Breaking Bad. \n Breaking Bad is a crime drama television series created and produced by Vince Gilligan. It originally aired on AMC for five seasons, from January 20, 2008, to September 29, 2013. The show tells the story of Walter White, a struggling and depressed high school chemistry teacher diagnosed with stage-3 lung cancer."""
elif selected_option == 1:
    print("Custom option selected")
else:
    print("Invalid option selected")

