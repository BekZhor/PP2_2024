def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into a list of words

    reversed_sentence = " ".join(words[::-1])

    return reversed_sentence

input_sentence = "We are ready"
print(reverse_words(input_sentence)) 

