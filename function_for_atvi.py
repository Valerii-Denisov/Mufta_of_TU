"""Модуль содержит функции для АТВИ"""


def variables_of_TU (strength_class, exploitation_temperature, thickness_body):
    # Переменные из ТУ
    if strength_class <= 48:
       temporary_resistance = 470  # параметр указанный в ту на муфты
       yield_strength = 305  # параметр указанный в ту на муфты
    elif 48 < strength_class <= 52:
        temporary_resistance = 510  # параметр указанный в ту на муфты
        yield_strength = 390  # параметр указанный в ту на муфты
    elif 52 < strength_class <= 56:
        temporary_resistance = 550  # параметр указанный в ту на муфты
        yield_strength = 450  # параметр указанный в ту на муфты
    elif 56 < strength_class <= 60:
        temporary_resistance = 590  # параметр указанный в ту на муфты
        yield_strength = 485  # параметр указанный в ту на муфты

    relative_elongation = 20  # параметр указанный в ту на муфты

    if -exploitation_temperature <= -20:
        climatic_version = "УХЛ"
        temp_kcv = exploitation_temperature  # температура зависит от климатического исполнения муфты и минимальной
        # температуры стенки
        temp_kcu = 60  # температура зависит от климатического исполнения муфты и минимальной температуры стенки
    elif -exploitation_temperature >= -5:
        climatic_version = "У"
        temp_kcv = 5  # температура зависит от климатического исполнения муфты и минимальной /
        # температуры стенки
        temp_kcu = 40  # температура зависит от климатического исполнения муфты и минимальной температуры стенки

    if 6 <= thickness_body <= 10:
        kcv_value = 35  # параметр указанный в ту на муфты
        kcu_value = 35  # параметр указанный в ту на муфт
    elif 10 < thickness_body <= 25:
        kcv_value = 49  # параметр указанный в ту на муфты
        kcu_value = 49  # параметр указанный в ту на муфт
    elif thickness_body > 25:
        kcv_value = 59  # параметр указанный в ту на муфты
        kcu_value = 59  # параметр указанный в ту на муфт
    else:
        print("Толщина не допускается по ТУ")

    if strength_class <= 50:
        equiv1 = 0.41  # параметр указанный в ту на муфт
        equiv2 = 0.19  # параметр указанный в ту на муфт
    elif 50 < strength_class < 60:
        equiv1 = 0.43  # параметр указанный в ту на муфт
        equiv2 = 0.21  # параметр указанный в ту на муфт
    elif strength_class == 60:
        equiv1 = 0.45  # параметр указанный в ту на муфт
        equiv2 = 0.23  # параметр указанный в ту на муфт
    result_variables = (temporary_resistance, yield_strength, relative_elongation, temp_kcv, kcv_value, temp_kcu,
                        kcu_value, equiv1, equiv2, climatic_version)
    return result_variables

def math_of_thickness(pressure, diameter_body, working_coefficient, thickness_body):
    """Функция анализа толщины стенки"""
    environment = str(input("Введи среду (Газ/Нефть): \n"))
    environment = environment.lower()
    if environment == "газ":
        if pressure <= 5.4:
            if diameter_body <= 1020:
                reliability_coefficient_for_the_purpose = 1
            elif diameter_body == 1220 or diameter_body == 1420:
                reliability_coefficient_for_the_purpose = 1.05
        if 5.4 < pressure <= 7.4:
            if diameter_body <= 1020:
                reliability_coefficient_for_the_purpose = 1
            elif diameter_body == 1220:
                reliability_coefficient_for_the_purpose = 1.05
            elif diameter_body == 1420:
                reliability_coefficient_for_the_purpose = 1.1
        if 7.4 < pressure <= 9.8:
            if diameter_body <= 530:
                reliability_coefficient_for_the_purpose = 1
            elif 630 <= diameter_body <= 1020:
                reliability_coefficient_for_the_purpose = 1.05
            elif diameter_body == 1220:
                reliability_coefficient_for_the_purpose = 1.1
            elif diameter_body == 1420:
                reliability_coefficient_for_the_purpose = 1.15
    elif environment == "нефть":
        if diameter_body <= 1020:
            reliability_coefficient_for_the_purpose = 1
        elif diameter_body == 1220:
            reliability_coefficient_for_the_purpose = 1.05
    material_reliability_coefficient = 1.4  # внести параметры для выбора коэффициента
    nominal_resistance = 560  # выбирается по материалу, добавить данный согласно сортаменту
    calculated_resistance_of_the_material = (nominal_resistance * working_coefficient) / (material_reliability_coefficient *
                                                                                 reliability_coefficient_for_the_purpose
                                                                                 )
    calculated_thickness = (1.1 * pressure * diameter_body) / (2 * (calculated_resistance_of_the_material + 1.1
                                                                      * pressure))
    print(calculated_thickness)
    if thickness_body >= calculated_thickness:
        result = True
        print("Толщина стенки проходит расчет.")
    else:
        result = False
        print("Толщина не прошла.")
    return (result)


def name_m1(diameter_body, thickness_body, strength_class, pressure, working_coefficient, climatic_version):
    """Функция формирует наименование муфты М1"""
    mufta_name = f"Муфта М1 {int(diameter_body)}({thickness_body}K{int(strength_class)})-{pressure}-{working_coefficient}"\
                 f"-{climatic_version}-ТУ 1469-025-04834179-2010"

    return mufta_name


def name_m2(diameter_body, thickness_body, strength_class, climatic_version):
    """Функция формирует наименование муфты М2"""
    mufta_name = f"Муфта М2 {int(diameter_body)}({thickness_body}K{int(strength_class)})"\
                 f"-{climatic_version}-ТУ 1469-025-04834179-2010"

    return mufta_name


def atvi_korpusa(diameter_body, material_korp, thickness_body, strength_class, temporary_resistance, yield_strength,
                 relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2,
                 one_mass):
    """Функция анализа корпуса. Применим к муфтам M1 и М2"""

    if diameter_body < 1420:
        length = 3000  # параметр указанный в ту на муфт
    elif diameter_body == 1420:
        length = 4000  # параметр указанный в ту на муфт

    if 52 <= strength_class < 60:
        strength_class = f'K{strength_class}-K60'
    elif strength_class < 52:
        strength_class = f'K{strength_class}-K{strength_class+8}'
    mass = one_mass*length//1000
    material_korpus = f'Корпус - 1 шт.\nМатериал: {material_korp}. Допускается применять трубу по другим НТД из ' \
                      f'реестра ПАО "Газпром" с толщиной стенки от {thickness_body} до {round(thickness_body+4,0)} ' \
                      f'включительно, классом прочности {strength_class}.\nТрубы должны поставляться без ' \
                      f'антикоррозионного покрытия.\nВременное сопротивление \u03C3в={temporary_resistance}-' \
                      f'{temporary_resistance+130} МПа.\nПредел текучести \u03C3т\u2265{yield_strength}МПа.' \
                      f'\nОтносительно удлинение не менее {relative_elongation}%.\nОтношение \u03C3в/\u03C3т\u2A7D0.9. ' \
                      f'\nKCV(-{temp_kcv}°C)\u2265{kcv_value} Дж/см2.\nKCU(-{temp_kcu}°C)\u2265{kcu_value} Дж/см2.' \
                      f'\nЭквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\nДлина: {length} мм.' \
                      f'\nМасса детали: {mass} кг.\n'
    return material_korpus


def atvi_shell(diameter_body, material_korp, thickness_shell, strength_class, temporary_resistance, yield_strength,
               relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2, one_mass):
    """Функция анализа обечайки. Применим к муфтам M1"""

    if diameter_body < 1420:
        length = 2500  # параметр указанный в ту на муфт
    elif diameter_body == 1420:
        length = 3500  # параметр указанный в ту на муфт

    if 52 <= strength_class < 60:
        strength_class = f'K{strength_class}-K60'
    elif strength_class < 52:
        strength_class = f'K{strength_class}-K{strength_class+8}'
    mass = one_mass*length//1000
    material_shell = f'Обечайка - 1 шт.\nМатериал: {material_korp}. Допускается применять трубу по другим НТД из ' \
                     f'реестра ПАО "Газпром" с толщиной стенки от {thickness_shell} до {round(thickness_shell+4,0)} ' \
                     f'включительно, классом прочности {strength_class}.\nТрубы должны поставляться без ' \
                     f'антикоррозионного покрытия.\nДопускается изготавливать из листа. Лист должен быть проверен на ' \
                     f'сплошность УЗК методом: 2 класс по ' \
                     f'ГОСТ 22727.\n Временное сопротивление \u03C3в={temporary_resistance}-' \
                     f'{temporary_resistance+130} МПа.\nПредел текучести \u03C3т\u2265{yield_strength}МПа.' \
                     f'\nОтносительно удлинение не менее {relative_elongation}%.\nОтношение \u03C3в/\u03C3т\u2A7D0.9. '\
                     f'\nKCV(-{temp_kcv}°C)\u2265{kcv_value} Дж/см2.\nKCU(-{temp_kcu}°C)\u2265{kcu_value} Дж/см2.' \
                     f'\nЭквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\nДлина: {length} мм.' \
                     f'\nМасса детали: {mass} кг.\n'
    return material_shell


def atvi_shell_input(material_korp, thickness_body, strength_class, temporary_resistance, yield_strength,
                     relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2, thickness_shell,
                     diameter_body):
    """Функция анализа вставки. Применим к муфтам M1"""
    if 52 <= strength_class < 60:
        strength_class = f'K{strength_class}-K60'
    elif strength_class < 52:
        strength_class = f'K{strength_class}-K{strength_class+8}'
    length = 100
    widh = ((diameter_body+thickness_body)*3.1416)-(((diameter_body+thickness_body)*3.1416)-100)
    mass = (length/1000)*(widh/1000)*thickness_shell*7.85
    material_shell_input = f'Вставка - 2 шт.\nМатериал: {material_korp}. Допускается применять трубу по другим НТД из ' \
                      f'реестра ПАО "Газпром" с толщиной стенки от {thickness_body} до {round(thickness_body+4,0)} ' \
                      f'включительно, классом прочности {strength_class}.\nТрубы должны поставляться без ' \
                      f'антикоррозионного покрытия.\nДопускается изготавливать из листа. Лист должен быть проверен ' \
                      f'на сплошность УЗК методом: 2 класс по ' \
                      f'ГОСТ 22727.\n Временное сопротивление \u03C3в={temporary_resistance}-' \
                      f'{temporary_resistance+130} МПа.\nПредел текучести \u03C3т\u2265{yield_strength}МПа.' \
                      f'\nОтносительно удлинение не менее {relative_elongation}%.\nОтношение \u03C3в/\u03C3т\u2A7D0.9. ' \
                      f'\nKCV(-{temp_kcv}°C)\u2265{kcv_value} Дж/см2.\nKCU(-{temp_kcu}°C)\u2265{kcu_value} Дж/см2.' \
                      f'\nЭквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\nДлина: {length} мм.' \
                      f'\nМасса детали: {mass} кг.\n'
    return material_shell_input


def atvi_shell_overlay(material_korp, thickness_body, strength_class, temporary_resistance, yield_strength,
                       relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2, thickness_shell,
                       diameter_body):
    """Функция анализа накладки. Применим к муфтам M1"""
    if diameter_body < 1420:
        length = 2500  # параметр указанный в ту на муфт
    elif diameter_body == 1420:
        length = 3500  # параметр указанный в ту на муфт

    if 52 <= strength_class < 60:
        strength_class = f'K{strength_class}-K60'
    elif strength_class < 52:
        strength_class = f'K{strength_class}-K{strength_class+8}'
    length = length-2*thickness_shell
    widh = ((diameter_body+thickness_body)*3.1416)-(((diameter_body+thickness_body)*3.1416)-100)+20
    mass = (length/1000)*(widh/1000)*thickness_shell*7.85
    material_korpus = f'Накладка - 1 шт.\nМатериал: {material_korp}. Допускается применять трубу по другим НТД из ' \
                      f'реестра ПАО "Газпром" с толщиной стенки от {thickness_body} до {round(thickness_body+4,0)} ' \
                      f'включительно, классом прочности {strength_class}.\nТрубы должны поставляться без ' \
                      f'антикоррозионного покрытия.\nДопускается изготавливать из листа. Лист должен быть проверен ' \
                      f'на сплошность УЗК методом: 2 класс по ' \
                      f'ГОСТ 22727.\n Временное сопротивление \u03C3в={temporary_resistance}-' \
                      f'{temporary_resistance+130} МПа.\nПредел текучести \u03C3т\u2265{yield_strength}МПа.' \
                      f'\nОтносительно удлинение не менее {relative_elongation}%.\nОтношение \u03C3в/\u03C3т\u2A7D0.9. ' \
                      f'\nKCV(-{temp_kcv}°C)\u2265{kcv_value} Дж/см2.\nKCU(-{temp_kcu}°C)\u2265{kcu_value} Дж/см2.' \
                      f'\nЭквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\nДлина: {length} мм.' \
                      f'\nМасса детали: {mass} кг.\n'
    return material_korpus


def mufta_bottom(diameter_body, equiv1, equiv2):
    """Принимает диаметр муфты, производит расчет диаметра днища и заготовки, вес и возвращает строку с атви днища"""
    bottom_thickness = 10  # поумолчанию 10 мм
    bottom_diametr = round(diameter_body+20)
    work_piece_side = round(bottom_diametr+15)
    weight_of_work_piece = (work_piece_side/1000)**2*bottom_thickness*7.85
    atvi_string = f"Днище - 1 шт.\nДиаметр днища: {bottom_diametr} мм.\nРазмеры заготовки: {work_piece_side}x" \
                  f"{work_piece_side} мм.\nВес заготовки: {round(weight_of_work_piece,2)} кг.\nМатериал:\nИзготовление"\
                  f" из листа толщиной 10 мм, из стали марки 09Г2С ГОСТ 19281 класс прочности 265.\n" \
                  f"Эквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\n" \
                  f"Материал должен быть проверен на сплошность УЗК методом: 2 класс по " \
                  f"ГОСТ 22727.\nДопускается применение листа из стали марки 10Г2ФБЮ.\n"
    return atvi_string


def balka_plug(diameter_body, thickness_shell, equiv1, equiv2):
    """принимает диаметр муфты, производит расчет размера заглушки и заготовки, вес и возвращает строку с атви
    заглушки"""
    plug_thickness = 10  # по умолчанию 10 мм
    if diameter_body <= 426:
        plug_length = 170
        plug_heinght = round((160+thickness_shell)/2)
    elif 426 < diameter_body < 1020:
        plug_length = 208
        plug_heinght = round((200+thickness_shell)/2)
    elif diameter_body >= 1020:
        plug_length = 260
        plug_heinght = round((240+thickness_shell)/2)
    work_piece_length = plug_length+15
    work_piece_heinght = plug_heinght+15
    weight_of_work_piece = (work_piece_length/1000)*(work_piece_heinght/1000)*plug_thickness*7.85
    atvi_string = f"Заглушка - 6 шт.\nРазмеры заглушки: {plug_length}x{plug_heinght} мм.\n" \
                  f"Размеры заготовки: {work_piece_length}x{work_piece_heinght} мм.\n" \
                  f"Вес заготовки: {round(weight_of_work_piece,2)} кг.\nМатериал:\n" \
                  f"Изготовление из листа по ГОСТ 19903 толщиной 10 мм, из стали марки 09Г2С ГОСТ 19281 класс " \
                  f"прочности 265.\n Эквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\n" \
                  f"Материал должен быть проверен на сплошность УЗК методом: 2 класс по ГОСТ 22727.\n"\
                  f"Допускается применение листа из стали марки 10Г2ФБЮ.\n"
    return atvi_string


def balka_m2(diameter_body, thickness_shell, equiv1, equiv2):
    """принимает диаметр муфты, производит расчет размера балки и заготовок, вес и возвращает строку с атви balki"""
    if diameter_body == 1420:
        plate_length = 3000
    else:
        plate_length = 2000
    if diameter_body <= 426:
        plate_vertikal_heinght = round(160+thickness_shell)
        plate_gorisontal_heinght = 160
        plate_thickness = 10
    elif 426 < diameter_body < 1020:
        plate_vertikal_heinght = round(200+thickness_shell)
        plate_gorisontal_heinght = 200
        plate_thickness = 16
    elif diameter_body >= 1020:
        plate_vertikal_heinght = round(240+thickness_shell)
        plate_gorisontal_heinght = 240
        plate_thickness = 20
    work_piece_plate_length = plate_length+15
    work_piece_gorisontal_heinght = plate_gorisontal_heinght+15
    work_piece_vertikal_heinght = plate_vertikal_heinght+15
    weight_of_work_piece_gorisontal = round((work_piece_plate_length/1000)*(work_piece_gorisontal_heinght/1000) *
                                            plate_thickness*7.85)
    weight_of_work_piece_vertical = round((work_piece_plate_length/1000)*(work_piece_vertikal_heinght/1000) *
                                            plate_thickness*7.85)
    atvi_string = f"Балка - 3 шт.\nВес балки: {(weight_of_work_piece_gorisontal+weight_of_work_piece_vertical*2)}\n\n" \
                  f"Балка состоит:\n1) Пластина горизонтальная - 1 шт." \
                  f"\nРазмеры пластины: {plate_length}x{plate_gorisontal_heinght} мм." \
                  f"\nРазмеры заготовки: {work_piece_plate_length}x{work_piece_gorisontal_heinght} мм.\n" \
                  f"Вес заготовки: {round(weight_of_work_piece_gorisontal)} кг." \
                  f"\nМатериал:\nИзготовление из листа по ГОСТ 19903 толщиной {plate_thickness} мм, " \
                  f"из стали марки 09Г2С ГОСТ 19281 класс прочности 265.\n" \
                  f"Эквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\n" \
                  f"Материал должен быть проверен на сплошность УЗК методом: 2 класс по ГОСТ 22727." \
                  f"\nДопускается применение листа из стали марки 10Г2ФБЮ.\n\n2) Пластина вертикальная - 2 шт." \
                  f"\nРазмеры пластины: {plate_length}x{plate_vertikal_heinght} мм." \
                  f"\nРазмеры заготовки: {work_piece_plate_length}x{work_piece_vertikal_heinght} мм." \
                  f"\nВес заготовки: {round(weight_of_work_piece_vertical)} кг.\nМатериал:" \
                  f"\nИзготовление из листа по ГОСТ 19903 толщиной {plate_thickness} мм," \
                  f" из стали марки 09Г2С ГОСТ 19281 класс прочности 265.\n" \
                  f"Эквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\n" \
                  f"Материал должен быть проверен на сплошность УЗК методом: 2 класс по ГОСТ 22727.\n" \
                  f"Допускается применение листа из стали марки 10Г2ФБЮ."
    return atvi_string


def balka_m1(diameter_body, thickness_shell, equiv1, equiv2):
    """принимает диаметр муфты, производит расчет размера балки и заготовок, вес и возвращает строку с атви balki"""
    if diameter_body == 1420:
        plate_length = 3000
    else:
        plate_length = 2000
    if diameter_body <= 426:
        plate_vertikal_heinght = 160
        plate_gorisontal_heinght = 160
        plate_thickness = 10
    elif 426 < diameter_body < 1020:
        plate_vertikal_heinght = 200
        plate_gorisontal_heinght = 200
        plate_thickness = 16
    elif diameter_body >= 1020:
        plate_vertikal_heinght = 240
        plate_gorisontal_heinght = 240
        plate_thickness = 20
    work_piece_plate_length = plate_length+15
    work_piece_gorisontal_heinght = plate_gorisontal_heinght+15
    work_piece_vertikal_heinght = plate_vertikal_heinght+15
    weight_of_work_piece_gorisontal = round((work_piece_plate_length/1000)*(work_piece_gorisontal_heinght/1000) *
                                            plate_thickness*7.85)
    weight_of_work_piece_vertical = round((work_piece_plate_length/1000)*(work_piece_vertikal_heinght/1000) *
                                            plate_thickness*7.85)
    atvi_string = f"Балка - 3 шт.\nВес балки: {(weight_of_work_piece_gorisontal+weight_of_work_piece_vertical*2)}\n\n" \
                  f"Балка состоит:\n1) Пластина - 3 шт." \
                  f"\nРазмеры пластины: {plate_length}x{plate_gorisontal_heinght} мм." \
                  f"\nРазмеры заготовки: {work_piece_plate_length}x{work_piece_gorisontal_heinght} мм.\n" \
                  f"Вес заготовки: {round(weight_of_work_piece_gorisontal)} кг." \
                  f"\nМатериал:\nИзготовление из листа по ГОСТ 19903 толщиной {plate_thickness} мм, " \
                  f"из стали марки 09Г2С ГОСТ 19281 класс прочности 265.\n" \
                  f"Эквивалент углерода:\nCEiiw\u2A7D{equiv1}.\nCEPcm\u2A7D{equiv2}.\n" \
                  f"Материал должен быть проверен на сплошность УЗК методом: 2 класс по ГОСТ 22727." \
                  f"\nДопускается применение листа из стали марки 10Г2ФБЮ.\n\n"
    return atvi_string


def write_to_file_m2(diameter_body, thickness_body, strength_class, material_korp, temporary_resistance, yield_strength,
                                      relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2,
                                      one_mass, climatic_version, thickness_shell):
    """Модуль записывает текст АТВИ в файл"""
    atvi_file = open(f"""АТВИ {name_m2(diameter_body, thickness_body, strength_class, climatic_version)}.txt""",
                     "w", encoding="utf-8")
    atvi_file.write(f"{name_m2(diameter_body, thickness_body, strength_class, climatic_version)}\n"
                    f"""1. {atvi_korpusa(diameter_body, material_korp, thickness_body, strength_class, 
                                      temporary_resistance, yield_strength,
                                      relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2,
                                      one_mass)}\n"""
                    f"2. {mufta_bottom(diameter_body, equiv1, equiv2)}\n"
                    f"3. {balka_plug(diameter_body, thickness_shell, equiv1, equiv2)}\n"
                    f"4. {balka_m2(diameter_body, thickness_shell, equiv1, equiv2)}")
    atvi_file.close()


def write_to_file_m1(diameter_body, thickness_body, strength_class, material_korp, temporary_resistance, yield_strength,
                                      relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2,
                                      one_mass, climatic_version, thickness_shell, pressure, working_coefficient):
    atvi_file = open(f"""АТВИ {name_m1(diameter_body, thickness_body, strength_class, pressure, working_coefficient, 
                                       climatic_version)}.txt""", "w", encoding="utf-8")
    atvi_file.write(f"""{name_m1(diameter_body, thickness_body, strength_class, pressure, working_coefficient, 
                                       climatic_version)}\n"""
                    f"""1. {atvi_korpusa(diameter_body, material_korp, thickness_body, strength_class, 
                                      temporary_resistance, yield_strength,
                                      relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2,
                                      one_mass)}\n"""
                    f"""2. {atvi_shell(diameter_body, material_korp, thickness_shell, strength_class, 
                                       temporary_resistance, yield_strength, relative_elongation, temp_kcv, kcv_value, 
                                       temp_kcu, kcu_value, equiv1, equiv2, one_mass)}\n"""
                    f"""3. {atvi_shell_input(material_korp, thickness_body, strength_class, temporary_resistance, 
                                             yield_strength, relative_elongation, temp_kcv, kcv_value, temp_kcu, 
                                             kcu_value, equiv1, equiv2, thickness_shell, diameter_body)}\n"""
                    f"""4. {atvi_shell_overlay(material_korp, thickness_body, strength_class, temporary_resistance, 
                                               yield_strength, relative_elongation, temp_kcv, kcv_value, temp_kcu, 
                                               kcu_value, equiv1, equiv2, thickness_shell, diameter_body)}"""
                    f"5. {balka_plug(diameter_body, thickness_shell, equiv1, equiv2)}\n"
                    f"6. {balka_m1(diameter_body, thickness_shell, equiv1, equiv2)}")
    atvi_file.close()
