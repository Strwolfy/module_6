import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punct in punctuation:
                        content = content.replace(punct, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден, пропускаем его.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
            else:
                result[name] = -1  # Если слово не найдено
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word)
        return result


# Пример использования
# Сначала создайте текстовый файл `test_file.txt` с содержимым:
# it's a text for task, найти везде! Используйте его для самопроверки. Успехов в решении задачи. text text text

finder = WordsFinder('test_file.txt')

# Все слова
print(finder.get_all_words())

# Найти позицию первого вхождения слова 'TEXT'
print(finder.find('TEXT'))

# Посчитать количество вхождений слова 'teXT'
print(finder.count('teXT'))
