import string


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


word_set = set()
# Read all words from file and add them to the set
with open("projects/graph/words.txt") as f:
    for line in f:
        word = line.strip()  # remove new lines
        word_set.add(word)

# Build our graph

## rememeber to lower case stuff

# filtered_word_list = filter()
# for word in word_list:

letters = list(string.ascii_lowercase)


def get_neighbors(word):
    neighbors = []
    string_word = list(word)  # ['w', 'o', 'r', 'd']
    for i in range(len(string_word)):  ## Could filter our word list by length
        for letter in letters:  # for every letter in the alphabet
            temp_word = list(string_word)  # Make a copy that we can munge

            temp_word[i] = letter
            w = "".join(temp_word)  # Turn it back into a string
            if w == word:  # Words are not their own neighbors
                continue
            if w in word_set:
                neighbors.append(w)

    return neighbors


### if the result is in our words list, it's a neighbor!

# BFS
def word_ladders(start_word, end_word):
    q = Queue()

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
                new_path = list(current_path)
                new_path.append(neighbor)
                q.enqueue(new_path)
        return None


print(word_ladders("hit", "cog"))
