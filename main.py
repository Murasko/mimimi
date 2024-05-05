def convert_text(user_input: str) -> str:
    text = user_input.lower()
    text_array = []
    is_lower = False
    for c in text:
        if is_lower:
            text_array.append(c)
            is_lower = False
        else:
            text_array.append(c.upper())
            is_lower = True
    new_text = ''.join(text_array)
    return new_text

if __name__ == "__main__":
    user_input = input("Input your string you want to convert: \n")
    print("")
    converted_text = convert_text(user_input)
    print(f"Here you go bro: \n{converted_text}")
    input("Press any key to close")