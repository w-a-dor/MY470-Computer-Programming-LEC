def leading_substrings(s):
    """Take string s as input and return a list of all 
    the substrings that start from the beginning."""
    print(f"Received input: {s}, type: {type(s)}")  # Debugging line
    if not isinstance(s, str):  # Check if the input is not a string
        raise TypeError("Input must be a string")
    
    if s:  # If the string is non-empty
        return [s[:i+1] for i in range(len(s))]
    else:  # If the string is empty
        return []