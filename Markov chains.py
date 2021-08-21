# подключаем библиотеку numpy
import numpy as np
# подключаем уровень доступа "private" для методов класса
from accessify import private
# подключаем библиотеку регулярных выражений
import re
# подключаем библиотеку для сохранения модели в отдельном файле
import pickle


# класс, представляющий случайный текст,
# сгенерированный на основе другого текста
# из файла
class Text:

    # генератор, который возвращает объект — список пар слов
    @private
    def create_couples(self):
        # перебираем слова в отформатированном тексте,
        # за исключением последнего слова
        for i in range(len(self.splitted_text) - 1):
            # генерируем новую пару соседних слов
            yield (self.splitted_text[i], self.splitted_text[i + 1])

    # обучение модели
    def fit_Text(self, text):

        # копируем содержимое текствого файла в переменную
        self.text = text

        # приводим текст к lowercase
        self.text = self.text.lower()

        # токенизация (разбитие текста на слова)
        # и удаление неалфавитных символов
        self.splitted_text =  re.findall(r'\w+', self.text)

        # список пар соседних слов
        couples = self.create_couples()

        # создание словаря, хранящего
        # для каждого слова-ключа список значений-слов,
        # которые идут после него в исходном тексте
        dictionary = {}

        # перебираем попарно слова из списка пар
        for first_word, second_word in couples:
            # если первое слово присутствует в словаре
            if first_word in dictionary.keys():
                # то добавляем второе слово в качестве
                # значения для первого слова-ключа
                dictionary[first_word].append(second_word)
            # если первое слово отсутствует в словаре, то
            else:
                # создаём новый элемент словаря с ключом first_world
                # и меняем ключ first_world на ключ second_word
                dictionary[first_word] = [second_word]

         # открываем файл для записи в бинарном режиме
        file = open('model.txt', 'wb')

        # записываем в файл наш словарь
        model = pickle.dump(dictionary, file)

        # закрываем файл
        file.close()

    # генерация текста
    def generate_Text(self):

        # открываем файл для чтения в бинарном режиме
        file = open('model.txt', 'rb')

        # загружаем в переменную содержимое файла
        dictionary = pickle.load(file)

        # мощность генерируемого текста
        quantity_of_words = 50

        # выбираем случайное состояние
        first_word = np.random.choice(self.splitted_text)

        # добавляем состояние в генерируемый текст
        self.consequence = [first_word]

        # сэмплирование:
        # добавление новых слов в текст
        for i in range(quantity_of_words):
            # выбираем случайно слово-значение для данного слова-ключа
            # и добавляем его в текст
            self.consequence.append(np.random.choice(dictionary[self.consequence[-1]]))

    # печать текста
    def printText(self):
        # объединяем список строк
        print(' '.join(self.consequence))


def main():

  # открываем файл и копируем текст в переменную
  raw_text = open('mumu.txt', encoding='utf8').read()

  # создаем объект класса Text
  text = Text()

  # обучение
  text.fit_Text(raw_text)

  # вызов метода, генерирующего текст
  text.generate_Text()

  # печать текста
  text.printText()

# вызов главной функции
main()
