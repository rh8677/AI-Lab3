import math
import sys


# Performs adaboost based on training an example file with 5 attributes
def adaboost(file_exam):
    gain_list = []
    file_opened = open(file_exam, encoding="utf8")
    english = 0
    dutch = 0
    english_c_is = 0
    english_i_is = 0
    dutch_c_is = 0
    dutch_i_is = 0
    english_c_len = 0
    english_i_len = 0
    dutch_c_len = 0
    dutch_i_len = 0
    english_c_ui = 0
    english_i_ui = 0
    dutch_c_ui = 0
    dutch_i_ui = 0
    english_c_oo = 0
    english_i_oo = 0
    dutch_c_oo = 0
    dutch_i_oo = 0
    english_c_q = 0
    english_i_q = 0
    dutch_c_q = 0
    dutch_i_q = 0

    for line in file_opened:
        content_split = line.split("|")
        language = content_split[0].strip()
        if language == "en":
            english += 1
        else:
            dutch += 1
        sentence = content_split[1].split(" ")
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence is "de", then we guess that the sentence is dutch
            if word == "de":
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_is += 1
            else:
                dutch_c_is += 1
        else:
            if language == "en":
                english_i_is += 1
            else:
                dutch_i_is += 1
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence is longer than 11 chars, then we guess that the sentence is dutch
            if len(word) >= 12:
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_len += 1
            else:
                dutch_c_len += 1
        else:
            if language == "en":
                english_i_len += 1
            else:
                dutch_i_len += 1
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence contains the chars "ui" together, then we guess that the sentence is dutch
            if "ui" in word:
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_ui += 1
            else:
                dutch_c_ui += 1
        else:
            if language == "en":
                english_i_ui += 1
            else:
                dutch_i_ui += 1
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence contains the chars "oo" together, then we guess that the sentence is dutch
            if "oo" in word:
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_oo += 1
            else:
                dutch_c_oo += 1
        else:
            if language == "en":
                english_i_oo += 1
            else:
                dutch_i_oo += 1
        the_guess = "nl"
        for word in sentence:

            # If a word in the sentence contains the char 'Q' or 'q', then we guess that the sentence is english
            if 'Q' in word or 'q' in word:
                the_guess = "en"
        if the_guess == language:
            if language == "en":
                english_c_q += 1
            else:
                dutch_c_q += 1
        else:
            if language == "en":
                english_i_q += 1
            else:
                dutch_i_q += 1
    file_opened.close()
    gain_is = info_gain(english, dutch, english_c_is, english_i_is, dutch_c_is, dutch_i_is)
    gain_list.append(gain_is)
    gain_len = info_gain(english, dutch, english_c_len, english_i_len, dutch_c_len, dutch_i_len)
    gain_list.append(gain_len)
    gain_ui = info_gain(english, dutch, english_c_ui, english_i_ui, dutch_c_ui, dutch_i_ui)
    gain_list.append(gain_ui)
    gain_oo = info_gain(english, dutch, english_c_oo, english_i_oo, dutch_c_oo, dutch_i_oo)
    gain_list.append(gain_oo)
    gain_q = info_gain(english, dutch, english_c_q, english_i_q, dutch_c_q, dutch_i_q)
    gain_list.append(gain_q)
    return gain_list


# Creates a decision tree based on training an example file with 5 attributes
def decision_tree(file_exam):
    gain_list = []
    file_opened = open(file_exam, encoding="utf8")
    english = 0
    dutch = 0
    english_c_is = 0
    english_i_is = 0
    dutch_c_is = 0
    dutch_i_is = 0
    english_c_len = 0
    english_i_len = 0
    dutch_c_len = 0
    dutch_i_len = 0
    english_c_ui = 0
    english_i_ui = 0
    dutch_c_ui = 0
    dutch_i_ui = 0
    english_c_oo = 0
    english_i_oo = 0
    dutch_c_oo = 0
    dutch_i_oo = 0
    english_c_q = 0
    english_i_q = 0
    dutch_c_q = 0
    dutch_i_q = 0

    for line in file_opened:
        content_split = line.split("|")
        language = content_split[0].strip()
        if language == "en":
            english += 1
        else:
            dutch += 1
        sentence = content_split[1].split(" ")
        the_guess = "nl"
        for word in sentence:

            # If a word in the sentence is "de", then we guess that the sentence is english
            if word == "de":
                the_guess = "en"
        if the_guess == language:
            if language == "en":
                english_c_is += 1
            else:
                dutch_c_is += 1
        else:
            if language == "en":
                english_i_is += 1
            else:
                dutch_i_is += 1
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence is longer than 14 chars, then we guess that the sentence is dutch
            if len(word) >= 12:
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_len += 1
            else:
                dutch_c_len += 1
        else:
            if language == "en":
                english_i_len += 1
            else:
                dutch_i_len += 1
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence contains the chars "ui" together, then we guess that the sentence is dutch
            if "ui" in word:
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_ui += 1
            else:
                dutch_c_ui += 1
        else:
            if language == "en":
                english_i_ui += 1
            else:
                dutch_i_ui += 1
        the_guess = "en"
        for word in sentence:

            # If a word in the sentence contains the chars "oo" together, then we guess that the sentence is dutch
            if "oo" in word:
                the_guess = "nl"
        if the_guess == language:
            if language == "en":
                english_c_oo += 1
            else:
                dutch_c_oo += 1
        else:
            if language == "en":
                english_i_oo += 1
            else:
                dutch_i_oo += 1
        the_guess = "nl"
        for word in sentence:

            # If a word in the sentence contains the char 'Q' or 'q', then we guess that the sentence is english
            if 'Q' in word or 'q' in word:
                the_guess = "en"
        if the_guess == language:
            if language == "en":
                english_c_q += 1
            else:
                dutch_c_q += 1
        else:
            if language == "en":
                english_i_q += 1
            else:
                dutch_i_q += 1
    file_opened.close()
    gain_is = info_gain(english, dutch, english_c_is, english_i_is, dutch_c_is, dutch_i_is)
    gain_list.append(gain_is)
    gain_len = info_gain(english, dutch, english_c_len, english_i_len, dutch_c_len, dutch_i_len)
    gain_list.append(gain_len)
    gain_ui = info_gain(english, dutch, english_c_ui, english_i_ui, dutch_c_ui, dutch_i_ui)
    gain_list.append(gain_ui)
    gain_oo = info_gain(english, dutch, english_c_oo, english_i_oo, dutch_c_oo, dutch_i_oo)
    gain_list.append(gain_oo)
    gain_q = info_gain(english, dutch, english_c_q, english_i_q, dutch_c_q, dutch_i_q)
    gain_list.append(gain_q)
    return gain_list


# Returns the information gain based on various parameters.
def info_gain(trues, falses, trues_with_a, falses_with_a, trues_with_b, falses_with_b):
    total_things = trues + falses
    total_trues = trues_with_a + trues_with_b
    total_falses = falses_with_a + falses_with_b
    total_a = trues_with_a + falses_with_a
    total_b = trues_with_b + falses_with_b
    probability_true = trues / total_things
    probability_false = falses / total_things
    entropy_trues = (-(trues_with_a / total_trues) * math.log(trues_with_a / total_trues, 2)) + \
                    (-(trues_with_b / total_trues) * math.log(trues_with_b / total_trues, 2))
    entropy_falses = (-(falses_with_a / total_falses) * math.log(falses_with_a / total_falses, 2)) + \
                     (-(falses_with_b / total_falses) * math.log(falses_with_b / total_falses, 2))
    entropy_total = (probability_true * entropy_trues) + (probability_false * entropy_falses)
    shannon_entropy = -((total_a / total_things) * math.log(total_a / total_things, 2)) - \
                      ((total_b / total_things) * math.log(total_b / total_things, 2))
    information_gain = shannon_entropy - entropy_total
    return information_gain


# Predicts the type of language each line of an example file is, using a decision tree.
def predict_language(the_hypothesis, the_examples):
    hypo_file = open(the_hypothesis, "r")
    exam_file = open(the_examples, "r")
    line_offset = []
    offset = 0
    for line in hypo_file:
        line_offset.append(offset)
        offset += len(line)
    for line in exam_file:
        sentence = line.split(" ")
        for word in sentence:
            if word == "de":
                print("nl")
                break
            elif len(word) >= 12:
                print("nl")
                break
            elif 'Q' in word or 'q' in word:
                print("en")
                break
            elif "oo" in word:
                print("nl")
                break
            elif "ui" in word:
                print("nl")
                break
            else:
                print("en")
                break


# Creates a decision tree based on an example file with the specified learning type, and outputs it to a specified file.
def train_data(example_file, file_out, learn_al):

    # Will run the decision tree algorithm and create the hypothesis file out of it
    if learn_al == "dt":
        file_to_write = open(file_out, "w")
        the_list = decision_tree(example_file)
        the_list_copy = the_list
        the_list_copy.sort()
        max_info = the_list_copy[-1]
        sec_info = the_list_copy[-2]
        thi_info = the_list_copy[-3]
        fou_info = the_list_copy[-4]
        print(the_list)
        if the_list[4] == max_info:
            file_to_write.write("q 1 6\n")
            if the_list[3] == sec_info:
                file_to_write.write("oo 2 3\n")
                if the_list[2] == thi_info:
                    file_to_write.write("ui 4 5\n")
                    file_to_write.write("en\n")
                    file_to_write.write("nl\n")
                    file_to_write.write("en\n")
                    if the_list[1] == fou_info:
                        file_to_write.write("len 7 8\n")
                        file_to_write.write("nl\n")
                        file_to_write.write("is 9 10\n")
                        file_to_write.write("en\n")
                        file_to_write.write("nl\n")

    # Will run adaboost and then create the hypothesis file out of it
    else:
        file_to_write = open(file_out, "w")
        the_list = adaboost(example_file)
        the_list_copy = the_list
        the_list_copy.sort()
        max_info = the_list_copy[-1]
        sec_info = the_list_copy[-2]
        thi_info = the_list_copy[-3]
        fou_info = the_list_copy[-4]
        print(the_list)
        if the_list[4] == max_info:
            file_to_write.write("q 1 6\n")
            if the_list[3] == sec_info:
                file_to_write.write("oo 2 3\n")
                if the_list[2] == thi_info:
                    file_to_write.write("ui 4 5\n")
                    file_to_write.write("en\n")
                    file_to_write.write("nl\n")
                    file_to_write.write("en\n")
                    if the_list[1] == fou_info:
                        file_to_write.write("len 7 8\n")
                        file_to_write.write("nl\n")
                        file_to_write.write("is 9 10\n")
                        file_to_write.write("en\n")
                        file_to_write.write("nl\n")


# Tries to open a particular file, and quits if the file does not exist or is in an incorrect format.
def try_file(file_try):
    file_split = file_try.split(".")
    if file_split[1] != "txt":
        print("The file", file_try, "is not a text file!")
        quit()
    try:
        file_unknown = open(file_try, "r")
        file_unknown.close()
    except FileNotFoundError:
        print("The file", file_try, "cannot be found.")
        quit()


# The main function takes in command-line arguments with error checking, and runs the appropriate algorithm.
if __name__ == '__main__':
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Incorrect amount of parameters")
        quit()
    if sys.argv[1] == "train":
        if len(sys.argv) != 5:
            print("Incorrect amount of parameters")
            quit()
        else:
            examples = sys.argv[2]
            hypothesis_out = sys.argv[3]
            learn_type = sys.argv[4]
            try:
                f = open(examples, "r")
                f.close()
            except FileNotFoundError:
                print("The file", examples, "cannot be found.")
                quit()
            if learn_type != "dt" and learn_type != "ada":
                print(learn_type, "is not a proper learning type.")
            train_data(examples, hypothesis_out, learn_type)
    elif sys.argv[1] == "predict":
        if len(sys.argv) != 4:
            print("Incorrect amount of parameters")
            quit()
        else:
            hypothesis = sys.argv[2]
            file = sys.argv[3]
            try_file(hypothesis)
            try_file(file)
            predict_language(hypothesis, file)
    else:
        print("Unknown command: " + sys.argv[1])
