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
# todo: add more comments
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
        menuOptions[menuSelection][1]()

    # By design the exit_menu function runs before the while loop breaks.
    return None


# todo: add comments
def display_menu(mOpts):
    print(page_header('Main Menu'))
    for l in range(1,len(mOpts)):
        print('  {0}) {1}'.format(l, mOpts[l][0]))
    print('  {0}) {1}'.format(0, mOpts[0][0]))
    return None


def exit_menu():
    return 'end while'


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
def average_scores():
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


def get_test_scores(sList):
    print(page_header('Average Test Scores'))
    print('Please enter each test score. After the last score is accepted')
    print('press the [Enter] key.  The average will then be displayed.')
    while True:
        tmpScore = input('  Enter score: ')
        if len(tmpScore) == 0:
            verifyLast = input('Finished entering scores? (y)es/no\n >>> ')
            if verifyLast.lower() in ['','y','yes']:
                break
            else:
                continue
        if tmpScore.isdigit():
            sList.append(float(tmpScore))
        else:
            try:
                sList.append(float(tmpScore))
            except:
                print('Error: Invalid entry.  Only Real numbers accepted.')
                continue
    return None

def calc_average(sum, count, precision=2):
    avg = round(sum / count, precision)
    if sum % count == 0:
        avg = int(avg)
    return avg


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(count, avg):
    #
    print(page_header('Average Test Scores'))
    print('You entered {0} scores.'.format(count))
    print('The average score is: {0}'.format(avg))
    print('\n\n')
    return None

main()