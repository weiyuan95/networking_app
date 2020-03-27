def generate_headers(num_headers):
    char_counter = 64
    header_text = ""
    headers = {}

    for i in range(num_headers):
        char_counter += 1

        if char_counter > 90:
            header_text += "A"
            char_counter = 65
        else:
            header_text = header_text[:-1] + chr(char_counter)

        headers[header_text] = "ABCKJHDSAKUFGKNIUHNFKWJNEFIKJNDSKHIKIOSEUHFKSNDBKJUSBDFJKHSBDFGJKBHSDGFJUYH"

        headers = {
            'status': 200,
            'content-type': r'text/html; charset=ISO-8859-1',
            'p3p': r'CP="This is not a P3P policy! See g.co/p3phelp for more info."',
            'server': r'gws',
            'x-xss-protection': r'0',
            'x-frame-options': r'SAMEORIGIN',
            'set-cookie': r'A'*200,
            'set-cookie': r'A'*200,
            'alt-svc': r'quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,h3-T050=":443"; ma=2592000',
            'accept-ranges': r'none',
            'vary': r'Accept-Encoding',
        }

    return headers

if __name__ == "__main__":
    print(generate_headers())