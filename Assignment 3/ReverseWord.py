import collections

def reverse_words(input):
    reverse = collections.deque()

    input = input.split(' ') # identify words
    for i in input:
        reverse.appendleft(i) # append from the left, going backwards
    
    return " ".join(reverse) 


def main():
    print(reverse_words("Uber Career Prep"))
    # Output: Prep Career Uber

    print(reverse_words("Emma lives in Brooklyn, New York."))
    # Output: York. New Brooklyn, in lives Emma

main()