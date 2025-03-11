def gorner2mod(s, m, q):
    """Вычисляет хеш строки s по схеме Горнера по модулю q при x = 2."""
    res = 0
    for i in range(m):
        res = (res * 2 + ord(s[i])) % q  # ord() для преобразования символа в число
    return res


def karp_rabin(text, pattern, q=101):
    """Алгоритм Карпа-Рабина для поиска подстроки."""
    m, n = len(pattern), len(text)
    if m > n:
        return []

    p2m = 1  # 2^(m-1) mod q
    for _ in range(m - 1):
        p2m = (p2m * 2) % q

    hp = gorner2mod(pattern, m, q)  # Хеш образца
    ht = gorner2mod(text[:m], m, q)  # Хеш первой подстроки текста

    positions = []
    for j in range(n - m + 1):
        if ht == hp:
            if text[j:j + m] == pattern:
                positions.append(j)  # Совпадение найдено

        if j < n - m:
            ht = ((ht - p2m * ord(text[j])) * 2 + ord(text[j + m])) % q
            if ht < 0:
                ht += q  # Коррекция отрицательного значения

    return positions


# Тестирование алгоритма
def test_karp_rabin():
    text = "ABAAABCDABC"
    pattern1 = "ABC"
    pattern2 = "AA"
    pattern3 = "XYZ"

    print(f"Тест 1: {karp_rabin(text, pattern1)}")
    print(f"Тест 2: {karp_rabin(text, pattern2)}")
    print(f"Тест 3: {karp_rabin(text, pattern3)}")

    assert karp_rabin(text, pattern1) == [4, 8], "Ошибка в тесте 1"
    assert karp_rabin(text, pattern2) == [2, 3], "Ошибка в тесте 2"
    assert karp_rabin(text, pattern3) == [], "Ошибка в тесте 3"

    print("Все тесты пройдены!")


# Запуск тестов
test_karp_rabin()
