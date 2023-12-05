test = ["AGTC", "ARTGGCCC"]

def gc_counter(string:str):
    """Count the number of characters in a string"""

    GC_prop = 0
    for i in string:
        if i == 'G' or i == 'C':
            GC_prop += 1

    return GC_prop / len(string)


def sliding_window(n, test_string):
    """Create a sliding window of size n"""

    for i in range(0, len(test_string) - n + 1, 1):
        print(gc_counter(test_string[i:i+n]))

sliding_window(2, test[1])
