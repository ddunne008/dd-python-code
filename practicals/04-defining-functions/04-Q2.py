def no_uppercase_letters(**A):
    upper = sum(1 for char in A if 'A' <= char <= 'Z')


def no_lowercase_letters(**a):
    lower = sum(1 for char in a if 'a' <= char <= 'z')


text = (input("Enter a word: "))
    upper, no_uppercase_letters(text)
