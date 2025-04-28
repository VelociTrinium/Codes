text = input('The text you want to search in ->')
new_text = text.upper()

word = input('The word you want to search from the text->')
new_word = word.upper()
word_length = len(new_word)

occurrences = 0
start_index = 0
end_index = len(new_text)

if new_text.find(new_word) != -1:
    print(f"{word} has been found in the text")
else:
    print(f"{word} couldn't be found in the text")

while True:

    ans_0 = new_text.find(new_word, start_index, end_index)
    ans_1 = new_text.find(new_word + " ", start_index, end_index)
    ans_2 = new_text.find(new_word + ",", start_index, end_index)
    ans_3 = new_text.find(new_word + ";", start_index, end_index)
    ans_4 = new_text.find(new_word + ":", start_index, end_index)
    ans_5 = new_text.find(new_word + ".", start_index, end_index)
    ans_6 = new_text.find(new_word + "-", start_index, end_index)
    ans_7 = new_text.find(new_word + "_", start_index, end_index)
    

    if ans_0 != -1:
        start_index = ans_0 + word_length
        occurrences += 1

    elif ans_1 != -1:
        start_index = ans_1 + word_length
        occurrences += 1

    elif ans_2 != -1:
        start_index = ans_2 + word_length
        occurrences += 1

    elif ans_3 != -1:
        start_index = ans_3 + word_length
        occurrences += 1

    elif ans_4 != -1:
        start_index = ans_4 + word_length
        occurrences += 1

    elif ans_5 != -1:
        start_index = ans_5 + word_length
        occurrences += 1

    elif ans_6 != -1:
        start_index = ans_6 + word_length
        occurrences += 1
    
    elif ans_7 != -1:
        start_index = ans_7 + word_length
        occurrences += 1

    else:
        break

print(f'Number of times ( {word} ) has occurrences is = {occurrences}')
