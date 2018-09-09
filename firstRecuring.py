

def rc(str):
    rec = {}

    for ch in str:
        rec[ch] = rec.setdefault(ch, 0)
        if rec[ch] != 1:
            rec[ch] = 1
        else:
            return ch


if __name__ == "__main__":
    print(rc("ACDBCBA"))
