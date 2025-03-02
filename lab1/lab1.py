def prefix_border_array(s):
    """
    Вычисляет массив граней префиксов.
    """
    n = len(s)
    bp = [0] * n

    for i in range(1, n):
        bp_right = bp[i - 1]
        while bp_right > 0 and s[i] != s[bp_right]:
            bp_right = bp[bp_right - 1]

        if s[i] == s[bp_right]:
            bp[i] = bp_right + 1
        else:
            bp[i] = 0

    return bp


# Тесты
if __name__ == "__main__":
    test_cases = [
        ("abacaba", [0, 0, 1, 0, 1, 2, 3]),
        ("aaaaaa", [0, 1, 2, 3, 4, 5]),
        ("abcabc", [0, 0, 0, 1, 2, 3]),
        ("aabaaab", [0, 1, 0, 1, 2, 2, 3]),
        ("banana", [0, 0, 0, 0, 0, 0])  # Исправленный ожидаемый результат
    ]

    for s, expected in test_cases:
        result = prefix_border_array(s)
        print(f"s = '{s}'\nResult:   {result}\nExpected: {expected}\n")
        assert result == expected, f"Ошибка на тесте: {s}"
