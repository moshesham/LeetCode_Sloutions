    # Init counter dictionary
    counter = {}

    # Iterate through integers
    for arrInt in arr:
        
        # Increment counter
        if arrInt in counter.keys():
            counter[arrInt] += 1
        else:
            counter[arrInt] = 1

    # Convert dictionary keys (unique values in arr) to set
    counterKeys = set(counter.keys())
    # Convert dictionary values (frequency values in arr) to set
    counterValues = set(counter.values())

    # Check if any values have the same number of occurences 
    if len(counterKeys) == len(counterValues):
        return True
    else:
        return False