# Example usage
sequence = 'ATCTGACGCGCGCCGC'

def find_freq(seq):
    # Initialize a dictionary to store the frequency of each character
    freq_dict = {}

    # Go through each character in the sequence
    for char in seq:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Print the frequency results
    print("Frequencies:")
    for char, count in freq_dict.items():
        print(f"{char}: {count / len(seq):.4f}")

find_freq(sequence)







