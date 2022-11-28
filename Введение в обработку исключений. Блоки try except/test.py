def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

res_1 = get_number('-5')
res_2 = get_number('5.78')
res_3 = get_number('8(912)000-000-00')
res_4 = get_number(True)
print(res_1, res_2, res_3, res_4, end=' ')