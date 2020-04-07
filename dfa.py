def get_char(text, pos):
    if pos < 0 or pos >= len(text):
        return None
    c = text[pos]
    if '0' <= c <= '9':
        return "int"
    elif c is ".":
        return "dot"


def scan(text, transitions, accepts, start):
    pos = 0
    state = start
    matched = None
    while True:
        c = get_char(text, pos)
        if state in transitions and c in transitions[state]:
            state = transitions[state][c]
            pos += 1
            if state in accepts:
                matched = {"lexeme": text[:pos],
                           "token": accepts[state],
                           }
        else:
            return matched


transitions = {"s0": {"dot": "s1", "int": "s2"},
               "s1": {"int": "s3"},
               "s2": {"int": "s2", "dot": "s4"},
               "s3": {"int": "s3"},
               "s4": {"int": "s3"},
               }

accepts = {
    "s3": "FLOAT_TOKEN",
    "s4": "FLOAT_TOKEN",
}

for test in ['12.456', '6789.', '.66998', '1234', '.']:
    m = scan(test, transitions, accepts, 's0')
    print("Testing '{}'\nResult: {}\n".format(test, m))

# I think You were going easy on us :)
print("""
⊂_ヽ
　 ＼＼ (p2017182)
　　 ＼( ͡° ͜ʖ ͡°)
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
ノ )　　Lﾉ
(_／
""")
