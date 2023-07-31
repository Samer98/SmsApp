
import re


def get_words_next_to_dollar(input_string):
    # Using regular expression to find all words next to '$'
    words_next_to_dollar = re.findall(r'\$(\w+)', input_string)

    return words_next_to_dollar


def replace_all(body_message, replacement_values):
    for key, value in replacement_values.items():
        value = str(value)
        body_message = body_message.replace(key, value)
        # print(body_message)
    return body_message
