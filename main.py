def reverse(s):
    if type(s) != str:
        raise TypeError(f"Ожидали тип str получили {type(s)}")
    return s[::-1]


if __name__ == '__main__':
    print( reverse("abc"))
