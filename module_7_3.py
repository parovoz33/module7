import string


class WordsFinder:
    def __init__(self, *file_names):
        # Принимаем неограниченное количество файлов и сохраняем их в атрибут file_names
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        # Пунктуация, которую нужно убрать
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Приводим текст к нижнему регистру
                    # Удаляем пунктуацию
                    for punct in punctuation:
                        text = text.replace(punct, '')
                    # Разбиваем текст на слова
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()  # Игнорируем регистр при поиске
        word_positions = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1  # Возвращаем позицию (индексация с 1)
            else:
                word_positions[file_name] = None  # Если слово не найдено

        return word_positions

    def count(self, word):
        word = word.lower()  # Игнорируем регистр при подсчете
        word_count = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word)  # Считаем количество вхождений

        return word_count


# Пример использования:
finder = WordsFinder('test_file.txt')

# Все слова
print(finder.get_all_words())

# Поиск слова
print(finder.find('text'))

# Подсчет вхождений слова
print(finder.count('text'))
