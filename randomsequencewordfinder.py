# Welcome to the Random Sequence Word Finder
# --- This is a program that when run, tries to find the input word in a sequence of completely random numbers
# --- Imagine a string of random numbers, then imagine each was assigned to a letter e.g. a = 0, b = 1, z = 25
# --- This way, we may eventually find the numbers (letters) in the exact order as the input word
# --- 
# --- Known Bugs:
# --- - Some threads may not finish before the found flag is activated, allowing messages to show after the 
# ---   completion message

import argparse
import random
import threading
import time

# setup commandline arguments
parser = argparse.ArgumentParser(description='Random Sequence Word Finder')
parser.add_argument('w', type=str, help='Word to be used')
parser.add_argument('-t', '--threads', default=3, help='number of threads to use', type=int)
parser.add_argument('-l', '--log', default='', help='log to file')

args = parser.parse_args()

# global variables
found = False
startTime = None
elapsedTime = None

word = args.w
logFile = args.log
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
log = []

# logging function
def printf(toPrint):
    print(toPrint)
    log.append(toPrint)

# main function
def start(assignedNumber:int):
    global found
    global word
    global letter
    global elapsedTime
    global startTime

    # variable assignment
    threadFound = False
    complete = []
    lastSequence = []
    numberSequence = []
    N = len(word) + 10
    tries = 0

    # main routine to find word
    while "".join(complete) != word:
        newNumber = random.randint(0, len(letter) - 1)
        if letter[newNumber] == list(word)[len(complete)]:
            complete.append(letter[newNumber])
        else:
            tries += 1
            if len(lastSequence) < len(complete):
                lastSequence = complete
                if not found:
                    printf("[Thread {}] Sequence: {}, Tries: {}".format(assignedNumber, "".join(complete), tries))
            complete = []
        numberSequence.append(newNumber + 1)
        if found:
            break
    
    # if the word was found but current thread
    if "".join(complete) == word:
        threadFound = True
        found = True
        elapsedTime = time.time() - startTime

    if threadFound:
        # get last N numbers/letters to show randomness
        numberSequenceSnapshot = numberSequence[-N:]

        numberSequenceSnapshotLetters = []
        for i in numberSequenceSnapshot:
            numberSequenceSnapshotLetters.append(letter[i - 1])
        
        printf("--- [Thread {}] found word \"{}\" in {} tries, which took {:.2f} seconds".format(assignedNumber, word, tries, elapsedTime))
        printf("--- [Thread {}] Number Sequence (Minus 10 Numbers): {}".format(assignedNumber, numberSequenceSnapshot))
        printf("--- [Thread {}] Letter Sequence (Minus 10 Letters): {}".format(assignedNumber, "".join(numberSequenceSnapshotLetters)))

# create/start threds
threads = []
for i in range(0, int(args.threads)):
    threads.append(threading.Thread(target=start, args=[i + 1]))

for t in threads:
    startTime = time.time()
    t.start()

for t in threads:
    t.join()

# print logfile
if logFile != '':
    printf("Writing Log File...")
    printf("Process Complete.")
    with open(logFile, 'w') as f:
        for line in log:
            f.write(line + "\n")