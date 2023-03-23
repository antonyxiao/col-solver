'''
Improvement: remove word from list after appending to results

Future:
branch from start word and end word until they meet
'''
import re

def one_letter(word, words, result, visited):
    x = []
    
    expressions = [''] * 4

    # regex expressions to match words that differ by one letter
    expressions[0] = r'\w*' + word[1:4]
    expressions[1] = r'' + word[0] + '\w*' + word[2:4]
    expressions[2] = r'' + word[0:2] + '\w*' + word[3]
    expressions[3] = r'' + word[0:3] + '\w*'
    
    for w in words:
        if w in visited: # Skip words that have already been processed
            continue
            
        for i in range(4):
            # match if the word is different by one letter
            match = re.fullmatch(expressions[i], w)
            
            if match: # Add the word to the list of one-letter different words
                x.append(w) # Mark the word as visited
                visited.add(w) # Break the loop as a match has been found
                break

    return x

def main():  
    while True:
        start = input('Enter start word: ')
        end = input('Enter end word: ')
        
        # Set to store all 4-letter words
        words = set()  
        
        # Read 4-letter word list from the file
        with open('words.txt') as f:
            for line in f.readlines():
                words.add(line.strip())          
        
        # Validate start and end words
        if start not in words:
            print('Invalid start word')
            continue
        if end not in words:
            print('Invalid end word')
            continue
            
        break
    
    # List to store the n-ary tree of words
    result = [start]
    # Set to store visited words
    visited = set([start])
    # List to store the parent indices of words in the result list
    indices = [0]
    # Index to traverse the result list
    i = 0
    
    # Build the n-ary tree until the end word is found
    while end not in result:
    
        # for info printing
        old_len = len(result)
        
        # Get children words from the current word and extend the result list
        result.extend(one_letter(result[i], words, result, visited))
        new_len = len(result)
        
        # info printing
        print(str(round((new_len/len(words))*100,2)) + '% [' + result[i] + ']', end=' -> ')

        if result[old_len:new_len]:
            print(result[old_len:new_len])
        else:
            print()
        
        # Append parent index for newly added words
        for ind in range(new_len - len(indices)):
            indices.append(i)
        
        # Move to the next word if the result list has more words
        if i < new_len - 1:
            i += 1
        # If the end word is not found and all words have been traversed, it's impossible
        elif i == new_len - 1:
            print('===IMPOSSIBLE===')
            break
    
    # Find the index of the end word in the result list
    result_ind_buf = result.index(end)
    
    # List to store the final list of solution words
    result_words = []
    
    # Build the solution list by tracing back the parent indices
    while result[result_ind_buf] != start:
        result_words.insert(0, result[result_ind_buf])
        result_ind_buf = indices[result_ind_buf]
        
    # Include the starting word in the solution list
    result_words.insert(0, start)
    
    # Print the solution list
    for i in range(len(result_words)):
        print(str(i) + ' ' + result_words[i])
        
main()
