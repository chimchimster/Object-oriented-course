class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        if '-' in args[0][0] and args[0][1:].isdigit():
            return int(args[0])
        if args[0].isdigit():
            return int(args[0])
        return None




dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)