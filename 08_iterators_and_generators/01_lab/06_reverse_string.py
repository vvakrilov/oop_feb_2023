def reverse_text(string):
    for i in reversed(string):
        yield i


for char in reverse_text("step"):
    print(char, end='')
