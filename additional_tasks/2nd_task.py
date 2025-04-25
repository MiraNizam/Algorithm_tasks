def resdeland_answer(expression):
    # это на стек, всегда интересно
    s = expression.replace(' ', '')
    stack = []
    result = 0
    operator = 1
    i = 0
    n = len(s)

    while i < n:
        symbol = s[i]

        if symbol.isdigit():
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            result += operator * num
            operator = 1
            continue

        elif symbol in '+-':
            count_minus = 0
            while i < n and s[i] in '+-':
                if s[i] == '-':
                    count_minus += 1
                i += 1
            operator = -1 if count_minus % 2 == 1 else 1
            continue

        elif symbol == '(':
            stack.append(result)
            stack.append(operator)
            result = 0
            operator = 1
        elif symbol == ')':
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result
        i += 1

    return result


expression = input()
print(resdeland_answer(expression))