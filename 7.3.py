import os


class WordsFinder:
    def __init__(self):
        self.filename = None  # Изначально имя файла не задано
        self.words = []  # Список слов из найденного файла

    def search(self):
        """Поиск файлов с учетом директории и конечных символов, вскрытие найденного файла и создание словаря"""
        # Проходим по всем файлам в указанной директории и её поддиректориях
        for root, dirs, files in os.walk(r'C:\Users\Home\PycharmProjects\pythonProject'):
            for file in files:
                if file.endswith('L.txt'):  # Проверка, что файл заканчивается на 'L.txt'
                    file_path = os.path.join(root, file)  # Полный путь к файлу
                    with open(file_path, 'r', encoding='utf-8') as f:
                        self.words = []  # Очищаем список слов
                        for line in f:
                            self.words.extend(line.strip().split())  # Разделяем строку на слова и добавляем в список
                    self.filename = file  # Сохраняем имя найденного файла
                    return {file: self.words}  # Возвращаем словарь с именем файла и его словами
        return {}  # Если файл не найден, возвращаем пустой словарь

    def find(self, word):
        """Возвращает позицию первого вхождения слова (по счёту)"""
        if not self.words:  # Если файл не был найден или метод search не был вызван
            raise ValueError("No file has been searched. Please run search() first.")

        for index, w in enumerate(self.words):
            if w.lower() == word.lower():  # Для игнорирования регистра
                return {self.filename: index + 1}  # Позиция с 1
        return None  # Если слово не найдено

    def count(self, word):
        """Возвращает количество вхождений слова"""
        all_words = self.search()
        count_dict = {}
        for name, words in all_words.items():
            count_dict[name] = sum(1 for w in words if w.lower() == word.lower())  # Считаем вхождения
        return count_dict


# Пример использования:
finder = WordsFinder()  # Создаем объект
print(finder.search() ) # Ищем файл и получаем его содержимое
print(finder.find('златая'))  # Ищем слово 'златая' в найденном файле
print(finder.count('златая'))  # Считаем количество вхождений слова 'златая'

