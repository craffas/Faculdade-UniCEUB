def mdc (oi, hello):
    if hello == 0:
        return  oi
    else:
        return mdc(hello, oi % hello)
print(mdc(1, 1))
