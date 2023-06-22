def reverse_words(input):
    stack, res = [], []
    input = input.split(' ') # identify words
    for i in input:
        stack.append(i) # append to stack
    while stack:
        res.append(stack.pop()) # add top of stack to res then pop
    return " ".join(res) 


def main():
    print(reverse_words("Uber Career Prep"))
    # Output: Prep Career Uber

    print(reverse_words("Emma lives in Brooklyn, New York."))
    # Output: York. New Brooklyn, in lives Emma

main()