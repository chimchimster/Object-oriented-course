lst_in = "1 -5.6 True abc 0 23.56 hello".split()


def sort_int_float(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

lst_out = list(map(lambda x: sort_int_float(x), lst_in))
print(lst_out)