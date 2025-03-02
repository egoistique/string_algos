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


def kmp_search(pattern, text):
    """
    Реализация алгоритма Кнута-Морриса-Пратта для поиска вхождений подстроки pattern в строку text.
    """
    # Шаг 1: Построение массива граней для шаблона
    bpm = prefix_border_array(pattern)
    m = len(pattern)
    n = len(text)

    # Шаг 2: Основной цикл по тексту
    k = 0  # Индекс в шаблоне
    for i in range(n):
        # Продвигаем указатель k, если символы не совпадают
        while k and pattern[k] != text[i]:
            k = bpm[k - 1]

        # Если символы совпадают, продолжаем сравнение
        if pattern[k] == text[i]:
            k += 1

        # Если нашли полное вхождение
        if k == m:
            print(f"Вхождение с позиции {i - m + 1}")
            k = bpm[k - 1]  # Сдвигаем указатель, используя информацию из массива граней


# Тест
if __name__ == "__main__":
    print("test1")
    pattern = "ab"
    text = "abcabcab"
    kmp_search(pattern, text)

    print("test2")
    pattern = "abacab"
    text = "abacabcabacab"
    kmp_search(pattern, text)
