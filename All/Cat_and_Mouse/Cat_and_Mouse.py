def who_would_win(cat_a, mouse, cat_b):
    a, b = abs(cat_a - mouse), abs(cat_b - mouse)
    return "The mouse has escaped" if a == b else "Cat A" if a < b else "Cat B"
