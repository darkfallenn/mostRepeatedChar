# This function locates the most repeated character within a sequence of characters.

def mostRepChar(arr):
    freq_map = {} 
    
    for char in arr: # Maps each character to its frequency
        if char in freq_map:
            freq_map[char] += 1 # Adds to frequency if already in map.
        else:
            freq_map[char] = 1 # Sets frequency to 1 if not in map.
            
    sorted_map = sorted(freq_map.items(), key = lambda tup: tup[1], reverse = True) 
    # Sorts the array by converting it into tuple key-value pairs.
    
    return sorted_map[0] # Returns the first (most repeated) element.