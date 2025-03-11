def shift_and(pattern, text):
    """Алгоритм Shift-And для поиска подстроки."""
    m, n = len(pattern), len(text)
    if m > n:
        return []

    # Подготовка битовых карт для символов
    alphabet = set(text) | set(pattern)
    B = {ch: 0 for ch in alphabet}

    for j in range(m):
        B[pattern[j]] |= 1 << (m - 1 - j)

    uHigh = 1 << (m - 1)  # Маска для старшего бита
    M = 0  # Начальное состояние автомата

    positions = []
    for i in range(n):
        M = ((M >> 1) | uHigh) & B.get(text[i], 0)

        if M & 1:  # Если установлен младший бит, найдено вхождение
            positions.append(i - m + 1)

    return positions


# Тестирование алгоритма Shift-And
def test_shift_and():
    text = "abracadabra"
    pattern1 = "abra"
    pattern2 = "cad"
    pattern3 = "xyz"

    print(f"Тест 1: {shift_and(pattern1, text)}")
    print(f"Тест 2: {shift_and(pattern2, text)}")
    print(f"Тест 3: {shift_and(pattern3, text)}")

    assert shift_and(pattern1, text) == [0, 7], "Ошибка в тесте 1"
    assert shift_and(pattern2, text) == [4], "Ошибка в тесте 2"
    assert shift_and(pattern3, text) == [], "Ошибка в тесте 3"

    print("Все тесты пройдены!")


# Запуск тестов
test_shift_and()
