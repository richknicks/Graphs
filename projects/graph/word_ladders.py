import util from Queue
 
 # Build our graph
 ## Could filter our workd list by length
 ## rememeber to lower case stuff

 # filtered_word_list = filter()
 # for word in word_list:
myfile

word_set = set()


def get_neighbors(start_word):
    neighbors[]
 # for every letter in the word, 
    for letter_index in range(len(start_word)):
 ## swap out a letter in the alphabet
    for letter in string.ascii_lowercase:
        word_list = list(start_word)
        word_list[word_letter]= letter
 ### if the result is in our words list, it's a neighbor! 















def word_ladders(start_word, end_word)
    q=Queue

    visted = set()

    q.enqueue([start_word])

    while q.size() > 0:

        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visted:
            visted.add(current_word)

            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                q.enqueue(new_path)
