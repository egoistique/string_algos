def bad_character_heuristic(pattern):
    """Создаёт таблицу плохих символов."""
    bad_char = {char: -1 for char in set(pattern)}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char # Получаем таблицу в которой для каждого символа стоит последнее его вхождение в шаблон


def good_suffix_heuristic(pattern):
    """Создаёт таблицу сдвигов по хорошему суффиксу."""
    m = len(pattern)
    suffix = [-1] * m
    border = [0] * m

    j = m
    for i in range(m - 1, -1, -1):
        if i == m - 1 or pattern[i] != pattern[i + 1]:
            j = i + 1
        suffix[i] = j

    for i in range(m - 1):
        border[m - suffix[i]] = i + 1

    return border


def boyer_moore(text, pattern):
    """Поиск подстроки в строке с помощью алгоритма Бойера-Мура."""
    m, n = len(pattern), len(text)
    if m > n:
        return []

    bad_char = bad_character_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)

    positions = []
    s = 0  # Смещение шаблона относительно текста

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            positions.append(s)
            s += good_suffix[0] if good_suffix[0] > 0 else 1
        else:
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j] if good_suffix[j] > 0 else 1
            s += max(bad_char_shift, good_suffix_shift)

    return positions


def test_boyer_moore():
    text = "ABAAABCDABC"
    pattern1 = "ABC"
    pattern2 = "AA"
    pattern3 = "XYZ"

    text2 = "ABBABCABCCABCA"
    pattern4 = "CABCCAB"

    print(f"Тест 1: {boyer_moore(text, pattern1)}")
    print(f"Тест 2: {boyer_moore(text, pattern2)}")
    print(f"Тест 3: {boyer_moore(text, pattern3)}")

    assert boyer_moore(text, pattern1) == [4, 8], "Ошибка в тесте 1"
    assert boyer_moore(text, pattern2) == [2, 3], "Ошибка в тесте 2"
    assert boyer_moore(text, pattern3) == [], "Ошибка в тесте 3"

    print("Все тесты пройдены!")


test_boyer_moore()
