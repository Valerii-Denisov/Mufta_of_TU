class MuftaM1:
    """Класс описывает муфту М1"""
    def __init__(self, thickness_body, diameter_body, thickness_shell,
                 strength_class, pressure, working_coefficient,
                 exploitation_temperature, material_korp, one_mass,
                 environment):
        """Инициализирует атрубуты класса"""
        self.thickness_body = thickness_body
        self.diameter_body = diameter_body
        self.thickness_shell = thickness_shell
        self.strength_class = strength_class
        self.pressure = pressure
        self.working_coefficient = working_coefficient
        self.exploitation_temperature = exploitation_temperature
        self.material_korp = material_korp
        self.one_mass = one_mass
        self.environment = environment

    def variables_of_tu(self):
        """Инициализирует переменные из ТУ"""
        if self.strength_class <= 48:
            temporary_resistance = 470  # параметр указанный в ту на муфты
            yield_strength = 305  # параметр указанный в ту на муфты
        elif 48 < self.strength_class <= 52:
            temporary_resistance = 510  # параметр указанный в ту на муфты
            yield_strength = 390  # параметр указанный в ту на муфты
        elif 52 < self.strength_class <= 56:
            temporary_resistance = 550  # параметр указанный в ту на муфты
            yield_strength = 450  # параметр указанный в ту на муфты
        elif 56 < self.strength_class <= 60:
            temporary_resistance = 590  # параметр указанный в ту на муфты
            yield_strength = 485  # параметр указанный в ту на муфты

        relative_elongation = 20  # параметр указанный в ту на муфты

        if -self.exploitation_temperature <= -20:
            climatic_version = "УХЛ"
            temp_kcv = self.exploitation_temperature  # температура зависит от климатического исполнения муфты и минимальной
            # температуры стенки
            temp_kcu = 60  # температура зависит от климатического исполнения муфты и минимальной температуры стенки
        elif -self.exploitation_temperature >= -5:
            climatic_version = "У"
            temp_kcv = 5  # температура зависит от климатического исполнения муфты и минимальной /
            # температуры стенки
            temp_kcu = 40  # температура зависит от климатического исполнения муфты и минимальной температуры стенки

        if 6 <= self.thickness_body <= 10:
            kcv_value = 35  # параметр указанный в ту на муфты
            kcu_value = 35  # параметр указанный в ту на муфт
        elif 10 < self.thickness_body <= 25:
            kcv_value = 49  # параметр указанный в ту на муфты
            kcu_value = 49  # параметр указанный в ту на муфт
        elif self.thickness_body > 25:
            kcv_value = 59  # параметр указанный в ту на муфты
            kcu_value = 59  # параметр указанный в ту на муфт
        else:
            print("Толщина не допускается по ТУ")

        if self.strength_class <= 50:
            equiv1 = 0.41  # параметр указанный в ту на муфт
            equiv2 = 0.19  # параметр указанный в ту на муфт
        elif 50 < self.strength_class < 60:
            equiv1 = 0.43  # параметр указанный в ту на муфт
            equiv2 = 0.21  # параметр указанный в ту на муфт
        elif self.strength_class == 60:
            equiv1 = 0.45  # параметр указанный в ту на муфт
            equiv2 = 0.23  # параметр указанный в ту на муфт
        result_variables = (temporary_resistance, yield_strength,
                            relative_elongation, temp_kcv, kcv_value, temp_kcu,
                            kcu_value, equiv1, equiv2, climatic_version)
        return result_variables
