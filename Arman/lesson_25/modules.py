def check_hidden(input_style):
    """Function checks input field hidden"""
    if "display: none;" in input_style:
        return "Hide/Show input field hidden"
    else:
        return "Hide/Show input field show"
