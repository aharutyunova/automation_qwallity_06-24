def same_text(input_text, button_text):
    """Function check request text and response button text are same"""
    if input_text == button_text.text:
        print("Text and button texts are same")
    else:
        print("Text and button texts are not same!")