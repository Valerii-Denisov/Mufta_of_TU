#import pyperclip as clipboard
import function_for_atvi as ffa
thickness_body = float(input("Введи толщину стенки корпуса: \n"))
diameter_body = float(input("Введи диаметр корпуса: \n"))
flag = True
while flag:
    thickness_shell = float(input("Введи толщину стенки обечайки/накладки (не может быть меньше толщины "
                            "корпуса): \n"))
    if thickness_shell >= thickness_body:
        flag = False
    else:
        print("Толщина стенки обечайки не может быть меньше толщины корпуса")
strength_class = float(input("Введи класс прочности муфты (без буквы 'K'): \n"))
pressure = float(input("Введи рабочее давление: \n"))
working_coefficient = float(input("Введи коэффициент работы: \n"))
exploitation_temperature = int(input("Введи минимальную температуру стенки при эксплуатации (без знака '-'): \n"))


# Переменные из базы данных
# реализовать поле разворачивания бд в сети
"""material_korp = f'Труба тип 3-Т {int(diameter_body)}х{thickness_body} - K{int(strength_class)} ' \
                f'ГОСТ 20295-85'  # Должна браться из БД материала на основанни введенных параметров муфты
one_mass = 308.74  # вес 1 метра из БД на материал"""
# костыль
material_korp = input("Введи обозначение материала:\n")
one_mass = float(input("Введи вес 1 м.п. трубы:\n"))

result_variables = ffa.variables_of_TU(strength_class, exploitation_temperature, thickness_body)

temporary_resistance = result_variables[0]
yield_strength = result_variables[1]
relative_elongation = result_variables[2]
temp_kcv = result_variables[3]
kcv_value = result_variables[4]
temp_kcu = result_variables[5]
kcu_value = result_variables[6]
equiv1 = result_variables[7]
equiv2 = result_variables[8]
climatic_version = result_variables[9]


result = ffa.math_of_thickness(pressure, diameter_body, working_coefficient, thickness_body)
print(result)
if result:
    ffa.write_to_file_m1(diameter_body, thickness_body, strength_class, material_korp, temporary_resistance, yield_strength,
                                      relative_elongation, temp_kcv, kcv_value, temp_kcu, kcu_value, equiv1, equiv2,
                                      one_mass, climatic_version, thickness_shell, pressure, working_coefficient)
