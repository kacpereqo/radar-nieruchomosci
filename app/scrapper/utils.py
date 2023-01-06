def extract_numbers_from_string(string: str) -> str:
    string = string.replace(',', '.')
    return "".join([i for i in string if i in '0123456789.'])
