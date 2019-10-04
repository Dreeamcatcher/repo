# 1. Напишите класс `Fraction` для работы с дробями. Пусть дробь в нашем классе предстает в виде `числитель/знаменатель`.
# Дробное число должно создаваться по запросу `Fraction(a, b)`, где `a` – это числитель, а `b` – знаменатель дроби.
# 2. Добавьте возможность сложения (сложения через оператор сложения) для дроби.
# Предполагается, что операция сложения может проводиться как только между дробями,
# так и между дробью и целым числом. Результат оперции должен быть представлен в виде дроби.
# 3. Добавьте возможность взятия раздости (вычитания через оператор вычитания) для дробей.
# Предполагается, что операция вычитания может проводиться как только для двух дробей, так и для дроби и целого числа.
# Результат оперции должен быть представлен в виде дроби.
# 4. Добавьте возможность умножения (умножения через оператор умножения) для дробей.
# Предполагается, что операция умножения может проводиться как только для двух дробей, так и для дроби и целого числа.
# Результат оперции должен быть представлен в виде дроби.
# 5. Добавьте возможность приведения дроби к целому числу через стандартную функцию `int()`.
# 6. Добавьте возможность приведения дроби к числу с плавающей точкой через стандартную функцию `float()`.
# 7. Создайте дочерний класс `OperationsOnFraction` и добавьте туда собственные методы `getint` и `getfloat`,
# которые будут возвращять целую часть дроби и представление дроби в виде числа с плавающей точкой соответственно.


class Fraction:

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other, action='add'):
        """Сложение дробей"""
        new_fraction = Fraction()
        if type(other) is int:
            new_fraction.numerator = self.numerator + other * self.denominator
            if action == 'sub':
                new_fraction.numerator -= 2 * other * self.denominator
            new_fraction.denominator = self.denominator
        elif type(other) is Fraction:
            # приводим знаменатели к общему
            common_denominator = self.get_common_denominator(other)

            new_fraction.numerator = self.numerator * (common_denominator / self.denominator)
            new_fraction.numerator += other.numerator * (common_denominator / other.denominator)
            if action == 'sub':
                new_fraction.numerator -= 2 * other.numerator * (common_denominator / other.denominator)
            new_fraction.denominator = common_denominator
        return new_fraction.reduction()

    def __sub__(self, other):
        """Вычитание дробей"""
        return self.__add__(other, action='sub')

    def __str__(self):
        """Форматированный вывод"""
        return str(int(self.numerator)) + '/' + str(int(self.denominator))

    def get_common_denominator(self, other):
        """Общий знаменатель (наименьшее общее кратное двух знаменателей)"""
        num_1, num_2 = self.denominator, other.denominator
        max_denominator = num_1 * num_2
        while num_1 != 0 and num_2 != 0:
            if num_1 > num_2:
                num_1 %= num_2
            else:
                num_2 %= num_1
        return max_denominator // (num_1 + num_2)

    def reduction(self):
        """Сокращение дроби"""

        def get_common_multiplier(num_1, num_2):
            """Наибольший общий делитель двух чисел)"""
            num_1, num_2 = abs(num_1), abs(num_2)
            while num_1 != 0 and num_2 != 0:
                if num_1 > num_2:
                    num_1 %= num_2
                else:
                    num_2 %= num_1
            return num_1 + num_2

        common_multiplier = get_common_multiplier(self.numerator, self.denominator)
        self.numerator /= common_multiplier
        self.denominator /= common_multiplier

        return self


a = Fraction(1, 2)
b = Fraction(1, 2)
с = 5
print(a)
print(b)
print(a - 5)
