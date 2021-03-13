# IDLE (Python 3.8.0)

# lists of terms

import random
from copy import deepcopy as copy_of
from shodule_for_lists_of_terms import *

print()
print('Note: a character that represents a list of characters that typically --but not necessarily--')
print('represent phonemes can be --for ex.-- a V that represents a primary list of vowels, v that')
print('represents a secondary list of vowels, C that represents a primary list of consonants, c that')
print('represents a secondary list of consonants and g that represents a list of consonant glides, etc.')
print('As for the characters in a list they should be entered with a space between them. This is so that')
print('someone can use the comma as a character if they want and so that each individual character that is')
print('meant to be used can be more easily parsed.')
print()
characteral_dictionary = {}
another_character_and_lict_of_characters = 'yes'
while another_character_and_lict_of_characters == 'yes':
    print('What is the character that represents a list of characters?')
    print()
    user_input = input('Enter: ')
    print()
    character = copy_of(user_input)
    print('What is the list of characters?')
    user_input = user_input_handling_function_ninth()
    lict_of_characters = copy_of(user_input)
    characteral_dictionary[character] = []
    characteral_dictionary[character].extend(copy_of(lict_of_characters))
    print('Is there another character that represents another list of characters? (yes or no).')
    user_input = user_input_handling_function_third()
    if user_input == 'yes':
        another_character_and_lict_of_characters = 'yes'
    else:
        another_character_and_lict_of_characters = 'no'

print('Note: a form consists of a sequence of the characters that represent the lists of characters. For')
print('example: CgVvc, VCVc or VC.')
print()
termal_dictionary = {}
another_form = 'yes'
while another_form == 'yes':
    print('What is the form?')
    user_input = user_input_handling_function_second(characteral_dictionary)
    form = copy_of(user_input)
    lict = []
    for character in form:
        lict.append(characteral_dictionary[character])
    termal_lict = termal_generator(lict)
    termal_dictionary[form] = []
    termal_dictionary[form].extend(copy_of(termal_lict))
    termal_dictionary['r' + form] = []
    termal_dictionary['r' + form].extend(copy_of(termal_lict))
    random.shuffle(termal_dictionary['r' + form])
    print('Is there another form? (yes or no).')
    user_input = user_input_handling_function_third()
    if user_input == 'yes':
        another_form = 'yes'
    else:
        another_form = 'no'

print('There is', len(termal_dictionary), 'lists of terms with the forms:')
print()
for form in termal_dictionary:
    print(form)
print('Note: r means random. Each list is automatically randomized. You\'re welcome. ;)')
print()

print('Do you want to modify all or some of the terms in a list? (yes or no).')
user_input = user_input_handling_function_third()

if user_input == 'yes':
    print('Do you want to remove terms with one or more unwanted characters from one or more of the lists? (yes')
    print('or no).')
    user_input = user_input_handling_function_third()

    if user_input == 'yes':
        print('Do you want to remove terms with one or more unwanted characters from ONE --not all-- of the lists?')
        print('(yes or no).')
        user_input = user_input_handling_function_third()

        if user_input == 'yes':
            more_terms_in_more_licts = 'yes'
            while more_terms_in_more_licts == 'yes':
                print('What is the form?')
                user_input = user_input_handling_function_fourth(termal_dictionary)
                form = copy_of(user_input)
                print('The characters or combination of characters that are part of terms that you want removed have to be')
                print('entered with spaces between them.')
                print()
                print('What are the characters?')
                user_input = user_input_handling_function_tenth(characteral_dictionary)
                unwanted_characters = copy_of(user_input)
                print('Your unwanted characters occupy a range of places in a term. Between and including the first and')
                print('not including the second places --for ex.-- or between and including the last and not including the')
                print('third-last places. When counting from the start of a term begin with 0. When counting from the end')
                print('of a term begin with -1. The first two places would be 0 and 1 so nothing on the left and 2 on the')
                print('right ( :2) will get the job done because 2 isn\'t included. The last two places would be -1 and -2')
                print('so -2 on the left and nothing on the right (-2: ) will get the job done because nothing isn\'t')
                print('included. The number on the left is included and the number on the right isn\'t included. Use the')
                print('keyword: None to represent nothing.')
                print()
                print('What is the first index?')
                user_input = user_input_handling_function_eighth()
                first_index = copy_of(user_input)
                print('What is the second index?')
                user_input = user_input_handling_function_eighth()
                second_index = copy_of(user_input)
                for term in termal_dictionary[form]:
                    if term[first_index:second_index] in unwanted_characters:
                        termal_dictionary[form].remove(term)
                print('Do you want to remove more terms with one or more unwanted characters from this list or another')
                print('one? (yes or no).')
                user_input = user_input_handling_function_third ()
                if user_input == 'yes':
                    more_terms_in_more_licts = 'yes'
                else:
                    more_terms_in_more_licts = 'no'

        print('Do you want to remove terms with one or more unwanted characters from ALL --not one-- of the lists?')
        print('(yes or no).')
        user_input = user_input_handling_function_third ()
        if user_input == 'yes':
            more_terms_in_all_licts = 'yes'
            while more_terms_in_all_licts == 'yes':
                print('The characters or combination of characters that are part of terms that you want removed have to be')
                print('entered with spaces between them.')
                print()
                print('What are the characters?')
                user_input = user_input_handling_function_tenth(characteral_dictionary)
                unwanted_characters = copy_of(user_input)
                print('Your unwanted characters occupy a range of places in a term. Between and including the first and')
                print('not including the second places --for ex-- or between and including the last and not including the')
                print('third-last places. When counting from the start of a term begin with 0. When counting from the end')
                print('of a term begin with -1. The first two places would be 0 and 1 so nothing on the left and 2 on the')
                print('right ( :2) will get the job done because 2 isn\'t included. The last two places would be -1 and -2')
                print('so -2 on the left and nothing on the right (-2: ) will get the job done because nothing isn\'t')
                print('included. The number on the left is included and the number on the right isn\'t included. Use the')
                print('keyword: None to represent nothing.')
                print()
                print('What is the first index?')
                user_input = user_input_handling_function_eighth()
                first_index = copy_of(user_input)
                print('What is the second index?')
                user_input = user_input_handling_function_eighth()
                second_index = copy_of(user_input)
                for form in termal_dictionary:
                    for term in termal_dictionary[form]:
                        if term[first_index:second_index] in unwanted_characters:
                            termal_dictionary[form].remove(term)
                print('Do you want to remove more terms with one or more unwanted characters from ALL of the lists? (yes')
                print('or no).')
                user_input = user_input_handling_function_third ()
                if user_input == 'yes':
                    more_terms_in_all_licts = 'yes'
                else:
                    more_terms_in_all_licts = 'no'

    print('Is there a set of lists that you want to add together? (yes or no).')
    print('Note: remember that lists are automatically randomized. So you don\'t need to add your random lists')
    print('together in addition to your sequential lists.') 
    user_input = user_input_handling_function_third()

    if user_input == 'yes':
        another_set_of_licts = 'yes'
        while another_set_of_licts == 'yes':
            form = ''
            lict = []
            another_lict = 'yes'
            while another_lict == 'yes':
                print('What is the form?')
                user_input = user_input_handling_function_fourth(termal_dictionary)
                form = form + user_input + '_'
                lict.extend(copy_of(termal_dictionary[user_input]))
                print('Is there another list that you want to add? (yes or no).')
                user_input = user_input_handling_function_third()
                if user_input == 'yes':
                    another_lict = 'yes'
                else:
                    another_lict = 'no'
            termal_dictionary[form] = []
            termal_dictionary[form].extend(copy_of(lict))
            termal_dictionary['r' + form] = []
            termal_dictionary['r' + form].extend(copy_of(lict))
            random.shuffle(termal_dictionary['r' + form])
            print('Is there another SET of lists that you want to add together? (yes or no).')
            user_input = user_input_handling_function_third()
            if user_input == 'yes':
                another_set_of_licts = 'yes'
            else:
                another_set_of_licts = 'no'

        print('There is', len(termal_dictionary), 'lists of terms with the forms:')
        print()
        for form in termal_dictionary:
            print(form)
        print()
                
print('Do you want to print a list so that you can inspect it? (yes or no).')
user_input = user_input_handling_function_third()
if user_input == 'yes':
    another_lict = 'yes'
    while another_lict == 'yes':
        print('What is the form?')
        user_input = user_input_handling_function_fourth(termal_dictionary)
        form = copy_of(user_input)
        print('Do you want your list displayed vertically? (yes or no).')
        user_input = user_input_handling_function_third()
        if user_input == 'yes':
            print_vertical_lict(termal_dictionary[form])
        else:        
            print_horizontal_lict(termal_dictionary[form])
        print('Do you want to print another list so that you can inspect it? (yes or no).')
        user_input = user_input_handling_function_third()
        if user_input == 'yes':
            another_lict = 'yes'
        else:
            another_lict = 'no'

print('Do you want to write / save your lists to files (.txt files)? (yes or no).')
user_input = user_input_handling_function_third()
if user_input == 'yes':
    for form in termal_dictionary:
        write_horizontal_lict(form, termal_dictionary[form])
    print('All done. Enjoy your lists of terms.')
else:
    print('WARNING: All the lists that you\'ve created will be lost if you don\'t save them. Are you sure that')
    print('you don\'t want to write / save them to files? (yes or no).')
    user_input = user_input_handling_function_third()
    if user_input == 'yes':
        print('Alrighty. Bye.')
    else:
        for form in termal_dictionary:
            write_horizontal_lict(form, termal_dictionary[form])
        print('All done. Enjoy your lists of terms.')
                       
