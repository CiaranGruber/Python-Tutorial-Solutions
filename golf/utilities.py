"""
Contains a set of utilities used in many programs

Utilities. 16/04/2020 - Created by Ciaran Gruber
"""


def get_max_length(item_list: list) -> int:
    """Get the max length item in a list"""
    max_value = -float('inf')
    for item in item_list:
        if len(str(item)) > max_value:
            max_value = len(str(item))
    return max_value


def get_integer(prompt: str, error_prompt: str, limits_prompt: str, min_num: int = -float('inf'),
                max_num: int = float('inf')) -> int:
    """Get an integer from the user within limits and with error checking"""
    while True:
        try:
            integer = int(input(prompt))
            if max_num >= integer >= min_num:
                return integer
            print(limits_prompt)
        except ValueError:
            print(error_prompt)


def display_menu(menu_title: str, menu_options: list, prompt: str, error_prompt: str, limits_prompt: str) -> int:
    """Display a menu with specific prompts and title"""
    print(menu_title)
    for i, menu_option in enumerate(menu_options):
        print(str(i + 1) + ".", menu_option)
    menu_choice = get_integer(prompt, error_prompt, limits_prompt, 1, len(menu_options))
    return menu_choice
