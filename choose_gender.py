from generator_compliment import compliment

def init_choose(lang):
    if lang == 1:
        x = input("Введите пол для генерации комплимента: ")
        return compliment(x, 1)
    elif lang == 2:
        x = input("Choose gender for generating compliment: ")
        return compliment(x, 2)
    else:
        raise ValueError("Поддерживаются только значения 1 (русский) и 2 (английский).")
