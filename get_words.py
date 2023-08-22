def get_words(s):
    words = []
    with open (f"corpus/{s}","r") as f:
        words=f.read().strip().split('\n')
    return words