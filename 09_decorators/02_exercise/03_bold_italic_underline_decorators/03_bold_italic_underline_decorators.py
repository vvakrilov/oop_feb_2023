def make_bold(bold):
    def wrapper(*string):
        start = '<b>'
        end = '</b>'
        return f"{start}{bold(*string)}{end}"

    return wrapper


def make_italic(italic):
    def wrapper(*string):
        start = '<i>'
        end = '</i>'
        return f"{start}{italic(*string)}{end}"

    return wrapper


def make_underline(underline):
    def wrapper(*string):
        start = '<u>'
        end = '</u>'
        return f"{start}{underline(*string)}{end}"

    return wrapper


# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
#
# print(greet_all("Peter", "George"))
