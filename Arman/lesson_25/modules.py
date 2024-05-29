def check_hidden(input_style):
    """Function checks input field hidden"""
    hidden_style = "display: none;"
    if hidden_style in input_style:
        return "Hide/Show input field hidden"
    else:
        return "Hide/Show input field show"
