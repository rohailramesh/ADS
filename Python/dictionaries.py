# Creating a dictionary to keep a count letter frequency in a given string

def letter_freq(str_input):
    count_dict = {}
    # This is the quicker way without using if/else condition
    for char in str_input:
        count_dict[char] = 1 + count_dict.get(char, 0)
    
    # printing the dict key and value
    for char, count_val in count_dict.items():
        print(char, count_val)
        

str_input = "yesterday"
letter_freq(str_input)



def letter_freq(str_input):
    count_dict = {}
    # This is the another way using if/else condition
    for char in str_input:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1 
    
    # printing the dict key and value
    for char, count_val in count_dict.items():
        print(char, count_val)
        

str_input_2 = "yesterday"
letter_freq(str_input_2)