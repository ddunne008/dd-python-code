def print_header(msg):
    """
    A docstring can be used for making code more understandable as it can provide a quick reference or description
    is uses triple quotes too
    Args:
    msg (str): The message to print

    Returns:
    None
    """
    print("*****", msg)

print(print_header.__doc__) # This can be used to print out what is in the docstring
