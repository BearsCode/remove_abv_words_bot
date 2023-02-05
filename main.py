def remove_abv_words(text):
    words = text.split()
    new_words = [word for word in words if "абв" not in word]
    return " ".join(new_words)

text = input("Введите текст: ")
print("Результат:", remove_abv_words(text))
