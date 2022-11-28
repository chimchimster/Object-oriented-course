def summ_concat():
    x = None
    a, b = input().split()
    try:
        x = int(a) + int(b)
    except:
        try:
            x = float(a) + float(b)
        except:
            try:
                x = str(a) + str(b)
            except:
                pass
    finally:
        print(x)

summ_concat()
