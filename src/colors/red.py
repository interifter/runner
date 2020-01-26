
def ride():
    return "I'm the red rider!"

def write():
    return "I'm red. I don't write..."

def mix(color=None):
    if not color:
        return " you tried to mix with the wrong color, bro."
    return f"I don't want to mix with {color.mix()}"