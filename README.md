# The Random Sequence Word Finder

This is a program that when run, tries to find the input word in a sequence of completely random numbers

Imagine a string of random numbers, then imagine each was assigned to a letter e.g. a = 0, b = 1, z = 25

This way, we may eventually find the numbers (letters) in the exact order as the input word

### Known Bugs: ###
> Some threads may not finish before the found flag is activated, allowing messages to show after the completion message

### Usage: ###
> `python3 randomsequencewordfinder.py <word> -t <threads> -l <logfile>`

### Running Example: ###
![Image Example](https://github.com/TacticalAxis/RandomSequenceWordFinder/blob/master/example.PNG)
