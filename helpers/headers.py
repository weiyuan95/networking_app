def generate_headers():
    char_counter = 64
    header_text = ""
    headers = {}

    for i in range(1000):
        char_counter += 1

        if char_counter > 90:
            header_text += "A"
            char_counter = 65
        else:
            header_text = header_text[:-1] + chr(char_counter)

        headers[header_text] = "ABCKJHDSAKUFGKNIUHNFKWJNEFIKJNDSKHIKIOSEUHFKSNDBKJUSBDFJKHSBDFGJKBHSDGFJUYH"

    return headers

if __name__ == "__main__":
    print(generate_headers())