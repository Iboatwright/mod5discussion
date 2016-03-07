# average_test_scores_calculator.py
# Exercises selected: Lab 6.5 - Average Test Scores
# Name of program: Average Test Scores Calculator
# Description of program: This program calculates the average test
#   score based on a set of scores input by the user. Then it displays
#   the average of the scores and prompts to enter another set of
#   scores/repeat the program.
#
# Ivan Boatwright
# March 7, 2016

def main():
    # Menu control options passed to the menu function.  A list with each
    #   entry a tuple of [0] the display text and [1] the function to call.
    #   Menu numbers start at 1), option 0) defaults to Exit.
    customMenuOptions = [('Average Test Scores', average_scores)]

    # Displays the intro to user.
    fluffy_intro()

    # Call the menu loop program.  The menu options are: 1) Average Test
    #   Scores and 0) Exit the program.
    main_menu(customMenuOptions)

    # End main.
    return None


# Section Block: Misc Output ------------------------------------------------>

# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print(page_header('Average Test Scores'))
    print('Welcome! This program requests a list of test scores, calculates\n'
          'the average and then displays the results.\n')


# Returns a string used to identify a new part(i.e. page) of the program.
def page_header(title):
    return '{0}\n{1:^40}\n{0}'.format('='*40,title)


# Section Block: Menu ------------------------------------------------------->

# main_menu prints a list of options for the user to select from.  The user
#   enters the desired option's number and the function paired with that
#   option is then executed.  If that option is 0 the while loop is terminated
#   and control returns to the calling function.  Otherwise after the selected
#   function is finished main menu is displayed again.
def main_menu(customMenuOptions):
    # Menu control options. A list with each entry a tuple of
    #   [0] the display text and [1] the function to call.
    menuOptions = [('Exit',exit_menu)]  # Set default menu options.
    menuOptions.extend(customMenuOptions)  # Add custom menu options.
    MENU_COUNT = len(menuOptions)

    # Initialize the loop control variable.
    menuSelection = True

    # While menuSelection does not equal 0 (the default exit option.)
    while menuSelection != 0:
        display_menu(menuOptions)
        # Calls the input request/validation function and converts the return
        #   value into an integer.  The number of menu elements is prepended
        #   to the input request and used as part of the validation testing.
        menuSelection = int(get_valid_inputs([[str(MENU_COUNT) +
                                              ' menu options', 'selection']]))

        # Use the validated user input to select the function reference and
        #   execute the function with the trailing ().
        menuSelection = menuOptions[menuSelection][1]()

    # By design the exit_menu function runs before the while loop breaks.
    return None


# Prints the menu header and menu options to stdout.  The menuOptions list
#   is the parameter and used to generate the option strings.
def display_menu(mOpts):
    print(page_header('Main Menu'))
    # This loops through the list starting at [1] and prints [0] (Exit)
    #   at the end.
    for l in range(1,len(mOpts)):
        print('  {0}) {1}'.format(l, mOpts[l][0]))
    print('  {0}) {1}'.format(0, mOpts[0][0]))
    return None


# Sets the loop control variable to 0 which ends the while loop.
def exit_menu():
    # "Until we meet again, farewell."
    print("\nJusqu'à ce que nous nous reverrons, adieu.")
    return 0


# Section Block: Input Validation ------------------------------------------->

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
    return input('  >>> ')


# test_value uses the testCondition to select the proper test.
# It returns True or False to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition[1:] == ' menu options':
        # The number of menu items is prepended to the test condition string.
        #   testCondition[1:] strips the first character and then does the
        #   string comparison.
        # If (the number of menu items) is greater than int(testItem) and
        #   int(testItem) is greater than or equal to zero, True is
        #   returned.  If int(testItem) creates an error or fails the other
        #   logic tests, False is returned.
        try:
            if int(testItem) >= 0 and int(testCondition[:1]) > int(testItem):
                return True
            else:
                return False
        except:
            return False
    else:
        return None


# Section Block: Average Test Scores ---------------------------------------->

# This is the primary Average Test Scores function.  When control is returned
#   to the main menu this function and all of it's variables pass out of scope
#   If Average Test Scores is repeated the variables are effectively reset.
def average_scores():
    # Local variables Dict.
    scores = {
        'sCount': 1,
        'sList': [],
        'sSum': 0,
        'sAvg': 0.0,
    }

    get_test_scores(scores['sList'])
    scores['sSum'] = sum(scores['sList'])
    scores['sCount'] = len(scores['sList'])
    scores['sAvg'] = calc_average(scores['sSum'],scores['sCount'])

    display_results(scores['sCount'],scores['sAvg'])
    return None


# Uses a list by reference to store the requested values.  When the user enters
#   a blank entry the loop verifies if all scores are entered.  If not the user
#   can continue entering scores, otherwise control is returned to
#   average_scores.  Each entry is validated before being stored in sList.
def get_test_scores(sList):
    print(page_header('Average Test Scores'))
    print('Please enter each test score. After the last score is accepted')
    print('press the [Enter] key.  The average will then be displayed.')
    while True:
        tmpScore = input('  Enter score: ')
        # A length of 0 means input returned '', an empty string. i.e. the user
        #   pressed [Enter].
        if len(tmpScore) == 0:
            verifyLast = input('Finished entering scores? (y)es/no\n >>> ')
            # By checking for '' here the user is spared having to type
            #   y or yes and can just hit [Enter] again.
            if verifyLast.lower() in ['','y','yes']:
                # Break will end the while True loop immediately.
                break
            else:
                # Continue skips the rest of the code in the while loop and
                #   initiates another iteration.
                continue
        if tmpScore.isdigit():
            sList.append(float(tmpScore))
        else:
            # If tmpScore cannot be converted to a float this catches the
            #   error message and instead executes the except clause.
            try:
                sList.append(float(tmpScore))
            except:
                print('Error: Invalid entry.  Only Real numbers accepted.')
                continue
    return None


# Calculates the average of two numbers and return the value.  Optionally
#   specify how many decimal places are returned.  If there is no fractional
#   component, the value is converted to an integer and returned.
def calc_average(sum, count, precision=2):
    avg = round(sum / count, precision)
    if sum % count == 0:
        avg = int(avg)
    return avg


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(count, avg):
    print(page_header('Average Test Scores'))
    print('You entered {0} scores.'.format(count))
    print('The average score is: {0}'.format(avg))
    print('\n\n')
    return None


# Start the program
main()