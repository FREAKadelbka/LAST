# Вам дана строка  с предложением без знаков пунктуации, в котором первое слово начинается с большой буквы, а между остальными словами может быть один пробел.
# Необходимо отсортировать слова по возрастанию их длины и вернуть строку с предложением, в котором слова отсортированы.
# Если какие-либо два слова оказываются одинаковой длины, то необходимо сохранить их порядок как в исходном предложении.
# Реализовать код в виде изолированной функции sort_sentence(sentence) в файле main.py, выложить в отдельный репозиторий,
# ссылку для клонирования репозитория приложить в ответ к заданию. Внутри файла не должно быть кода на нулевом уровне.
# Код для ввода входных данных необходимо либо экранировать с помощью if __name___=='__main__', либо вынести в отдельный файл, либо убрать вообще.



def sort_sentence(sentence):
    sentence = sentence.split()
    for CRINGEMOMENT in range(len(sentence) - 1):
        for hteaafgfng_sal in range(len(sentence) - CRINGEMOMENT - 1):
            if len(sentence[hteaafgfng_sal]) > len(sentence[hteaafgfng_sal + 1]):
                sentence[hteaafgfng_sal], sentence[hteaafgfng_sal + 1] = sentence[hteaafgfng_sal + 1], sentence[hteaafgfng_sal]
    return ' '.join(sentence).lower().capitalize()


if __name__ == '__main__':
    print(sort_sentence("Keep calm and carry on"))
