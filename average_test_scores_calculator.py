# average_test_scores_calculator.py
# Exercises selected: Lab 6.5 - Average Test Scores
# Name of program: Average Test Scores Calculator
# Description of program: This program calculates the average test
#   score based on a set of scores input by the user. Then it displays
#   the average of the scores and prompts to enter another set of
#   scores/repeat the program.
#
# Ivan Boatwright
# March x, 2016

def main():
    # Displays the intro to user.
    fluffy_intro()

    # Call the menu loop program.  The menu options are: 1) Average Test
    #   Scores and 2) Exit the program.
    main_menu()

    # End main.
    return None


# reset_vars takes the mainVars dict by reference and sets/resets the
#   program variables.
def reset_vars(mainVars):
    mainVars['menuOptions'] = {'averageScores','exit'}
    mainVars['scores'] = {}
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('\nWelcome to the Average Test Scores program.\n'
          'This program requests a list of test scores, calculates\n'
          'the average and then displays the results.\n')


def main_menu():
    # Menu control options dict.
    MENU_OPTIONS = {1: average_scores,0: exit_menu}

    # Initialize the program variables.
    # reset_vars(mainVars)

    menuSelection = int(display_menu())

    while menuSelection in [1, 0]:
        MENU_OPTIONS[menuSelection]

    return None


def display_menu():
    print('Main Menu\n 1) Average Test Scores\n 0) Exit')
    return get_valid_inputs(['menu option', 'selection.'])


# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestsList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop.
        untestedInput = prompt_user_for_input(request[1])

        # If test_value returns True, Not converts it to False and the While
        #   Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #   prompted to enter a valid value.
        while (not test_value(request[0], untestedInput)):

            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module.
    # With only a single test run in this program, only the first value
    #   in userInputs is returned.
    return userInputs[0]


# prompt_user_for_item is passed a String to print to screen as part of a user
#   prompt.  Then returns it to the calling module.
def prompt_user_for_input(promptTerm):
    # promptTerm is a local variable to hold the value passed from the
    #   calling module.
    print('Please enter your {}.'.format(promptTerm))
    return input('  >> ')


# test_value uses the testCondition to select the proper test.
# It returns True or False to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition == 'menu option':
        # If float(testItem) is greater than or equal to zero True is
        #  returned.  If float(testItem) creates an error or is less than
        #  zero False is returned.
        try:
            if int(testItem) == (0 or 1):
                return True
            else:
                return False
        except:
            return False
    else:
        return None


def average_scores():
    menuSelection = 1
    return menuSelection

def exit_menu():
    return 'end while'



# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(mCosts):
    #
    return None
