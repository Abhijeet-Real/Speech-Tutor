
def resolve_topic(choice_mode, dropdown_value, custom_value):
    """
    Resolves which topic to use based on the input mode.
    This function is used by both the UI and backend to ensure consistent behavior.
    """
    return custom_value.strip() if choice_mode == "Enter custom topic" and custom_value else dropdown_value