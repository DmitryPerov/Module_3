def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        if first != 0:           # если последняя цифра в числе не 0,
            return first         # то возвращаем его
        else:                    # если последняя цифра в числе - 0, то его возвращать нельзя,т.к.произведение всегда будет 0.
            return 1             # в этом случае возвращаем 1
    else:
        result = first * get_multiplied_digits(int(str_number[1:]))
    return result

result = get_multiplied_digits(40203)
print (result)

result = get_multiplied_digits(402030000)
print (result)
