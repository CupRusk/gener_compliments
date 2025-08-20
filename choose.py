from generator_compliment import compliment

def init_choose(lang):
    # Проверка = ввод 1 или 2. иначе ValueError
    if lang not in (1, 2):
        raise ValueError("Only values 1 (Russian) and 2 (English) are supported.")
    
    # Собираем основные данные 
    gender = input("Введите пол: " if lang == 1 else "Choose gender: ")
    name = input("Введите имя: " if lang == 1 else "Enter recipient's name: ")
    while True:
        try:
            age = int(input("Введите возраст: " if lang == 1 else "Enter recipient's age: "))
            break
        except ValueError:
            print("Пожалуйста, введите число." if lang == 1 else "Please enter a number.")
    # Все собранные данные в генератор
    return compliment(gender, age, name, lang)
