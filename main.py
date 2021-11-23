import math
import sys


# Returns the information gain based on various parameters.
def information_gain(trues, falses, trues_with_a, falses_with_a, trues_with_b, falses_with_b):
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
    info_gain = shannon_entropy - entropy_total
    return info_gain


# Predicts the type of language each line of an example file is, using a decision tree.
def predict_language(the_hypothesis, the_examples):
    return


# Creates a decision tree based on an example file with the specified learning type, and outputs it to a specified file.
def train_data(example_file, file_out, learn_al):
    return


# Tries to open a particular file, and quits if the file does not exist or is in an incorrect format.
def try_file(file_try):
    file_split = file_try.split(".")
    if file_split[1] != "txt":
        print("The file", file_try, "is not a text file!")
        quit()
    try:
        f = open(file_try, "r")
        f.close()
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
            try_file(examples)
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
