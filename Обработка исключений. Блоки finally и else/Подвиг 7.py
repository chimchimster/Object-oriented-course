def get_loss(w1, w2, w3, w4):
    try:
        x = w1 // w2
    except ZeroDivisionError:
        return 'деление на ноль'
    else:
        return 10 * x - 5 * w2 * w3 + w4

