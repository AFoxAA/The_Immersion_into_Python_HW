import re

# --- Первый вариант с использованием генератора словаря ---
def count_words(text: str) -> list[tuple[str, int]]:

    # Очищаем строку от всех символов, кроме букв, цифр, подчеркивания и пробелов
    text: str = re.sub(r'[^\w\s]', '', text.lower())

    words_in_text: list[str] = text.split()
    words_dictionary: dict[str, int] = {word: words_in_text.count(
        word) for word in words_in_text}

    words_sorted: list[tuple[str, int]] = sorted(words_dictionary.items(),
                          key=getting_a_value, reverse=True)
    result_words: list[tuple[str, int]] = words_sorted[:10]

    return result_words

# Возвращение второго элемента кортежа
def getting_a_value(word_tuple: tuple[str, int]) -> int:
    return word_tuple[1]


# # --- Второй вариант ---
# def count_words(text: str) -> list[tuple[str, int]]:
#     text: str = re.sub(r'[^\w\s]', '', text.lower())
#     words_in_text: list[str] = text.split()
#     words_dictionary: dict = {}

#     for word in words_in_text:
#         if word in words_dictionary:
#             words_dictionary[word] += 1
#         else:
#             words_dictionary[word] = 1

#     words_sorted: list[tuple[str, int]] = sorted(
#         words_dictionary.items(), key=getting_a_value, reverse=True)
#     result_words: list[tuple[str, int]] = words_sorted[:10]

#     return result_words


# def getting_a_value(word_tuple: tuple[str, int]) -> int:
#     return word_tuple[1]


if __name__ == "__main__":

    text: str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vehicula
                    sollicitudin sapien vel eleifend. Suspendisse potenti. Duis pretium finibus
                    libero, eget condimentum sem. Aliquam eleifend ultrices urna, eu efficitur leo
                    venenatis a. In hac habitasse platea dictumst. Nunc feugiat cursus metus,
                    vitae ullamcorper tortor efficitur non. Nulla commodo, mi ac fermentum cursus,
                    libero nunc tincidunt ipsum, vitae fermentum est dolor non odio. Donec
                    sollicitudin, felis vitae feugiat rhoncus, risus massa gravida justo, eget
                    fringilla felis risus sed lectus. Quisque tempor venenatis neque, id dapibus
                    eros aliquet nec. Vivamus rutrum dui arcu, et maximus enim semper eu. Quisque
                    efficitur nulla non enim rutrum, ut efficitur dui tristique. Sed congue
                    venenatis lobortis. In hac habitasse platea dictumst. Nulla luctus metus a
                    neque aliquet, sit amet consectetur dolor vulputate. Proin lobortis mauris vel
                    felis volutpat, vitae volutpat lectus dignissim. Sed lacinia tellus ut risus
                    mollis, sit amet fringilla justo luctus."""
    
    result: list[tuple[str, int]] = count_words(text)
    for word, count in result:
        print(f'{word}: {count}')
