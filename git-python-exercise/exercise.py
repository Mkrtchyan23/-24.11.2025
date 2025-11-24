def analyze_number(n):
    """Возвращает словарь с информацией о числе: знак и чётность."""
    if n > 0:
        sign = "positive"
    else:
        sign = "non-positive"

    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    return {"value": n, "sign": sign, "parity": parity}

if __name__ == "__main__":
    sample = 6
    info = analyze_number(sample)
    print("Input:", sample)
    print("Info:", info)