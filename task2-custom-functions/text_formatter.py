def format_text(text,prefix="",suffix="",capitalize=False,max_length=None):
    """ format text
    parameter definition
    text(str) : input text must be string
    prifix(str): prexif must be string
    suffix(str): suffix must be string
    captilize(bool): Starting letter must be string then captilize when boolean is false
    max_length(int): length of the text must be integer 
    """


    if capitalize:
        text = text.capitalize()
        text = list(text)
        finall_text = ''.join(text for text in text[:max_length+1])
        return f"{prefix} {finall_text} {suffix}"
    else:
        text = list(text)
        finall_text = ''.join(text for text in text[:max_length+1])
        return f"{prefix} {finall_text} {suffix}"

text=str(input("Enter Text :"))
prefix=str(input("Enter prefix :"))
suffix=str(input("Enter suffix : "))
max_length = int(input("Lenght to test: "))
capitalize_option = input("Capitalize? True/False: ").capitalize()
print(format_text(text, prefix, suffix, capitalize_option, max_length))



