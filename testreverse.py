from main import reverse


def test_r():
    test_data = ((42, None),
                 (['a','b','c'], None),
                 ("",""),
                 ('aba','aba'),
                 ('a','a'),
                 ('abcd','dcba'))
    for inp_s, correct_out in test_data:
        try:
            out_s = reverse(inp_s)
        except TypeError as E:
            if correct_out is None:
                continue
            if type(inp_s) == str:
                print(f"0шибка! Не удалось вычеслить reverse({inp_s}). 0шибка: {E}")
                return False
        except Exception as E:
            print(f"0шибка! Не удалось вычеслить reverse({inp_s}). 0шибка: {E}")
            return False
        else:
            if out_s != correct_out:
                print(f"0шибка! reverse({inp_s}) вернула {out_s} вместо {correct_out}.")
                return False
    print("Все тесты прошли успешно")
    return True


test_r()