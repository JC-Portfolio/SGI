class Validations:

    @staticmethod
    def _test_number(value, args):
        is_int, is_float = False

        if isinstance(value, float):
            is_float = True
        elif isinstance(is_int, int):
            is_int = True

        return is_int or is_float

    @staticmethod
    def _test_less_than(value, args):

        if Validations._test_number(value, args) is False:
            if isinstance(value, str):
                value = len(str(value))
            else:
                return False

        return value < float(args[0])

    @staticmethod
    def _test_less_or_equal_than(value, args):

        if Validations._test_number(value, args) is False:
            if isinstance(value, str):
                value = len(str(value))
            else:
                return False

        return float(value) <= float(args[0])

    @staticmethod
    def _test_more_than(value, args):

        if Validations._test_number(value, args) is False:
            if isinstance(value, str):
                value = len(str(value))
            else:
                return False
        return value > float(args[0])

    @staticmethod
    def _test_more_or_equal_than(value, args):

        if Validations._test_number(value, args) is False:
            if isinstance(value, str):
                value = len(str(value))
            else:
                return False
        return value >= float(args[0])

    @staticmethod
    def _test_not_empty(value, args):
        types = {'{}', '[]', "", None, 'null', 'Null'}
        if value in types:
            return False
        return True

    @staticmethod
    def _test_cpf(value, args):

        if value is None:
            return False

        try:
            if isinstance(int(value), int):

                numbers = [int(digit) for digit in value if digit.isdigit()]

                if len(numbers) != 11:
                    return False

                sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
                expected_digit = (sum_of_products * 10 % 11) % 10
                if numbers[9] != expected_digit:
                    return False

                sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
                expected_digit = (sum_of_products * 10 % 11) % 10
                if numbers[10] != expected_digit:
                    return False

                return True
        except ValueError:
            return False

    @staticmethod
    def _test_cnpj(value, args):

        if value is None:
            return False

        try:
            if isinstance(int(value), int):
                cnpj = value

                if (not cnpj) or (len(cnpj) < 14):
                    return False

                integers = list(map(int, cnpj))
                new = integers[:12]

                prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                while len(new) < 14:
                    r = sum([x * y for (x, y) in zip(new, prod)]) % 11
                    if r > 1:
                        f = 11 - r
                    else:
                        f = 0
                    new.append(f)
                    prod.insert(0, 6)

                if new == integers:
                    return True
                return False
        except ValueError:
            return False

    @staticmethod
    def _test_more_or_equal_than_str(value, args):
        if value is None:
            return False
        return len(value) >= int(args[0])

    @staticmethod
    def _test_more_than_str(value, args):
        if value is None:
            return False
        return len(value) > int(args[0])

    @staticmethod
    def _test_less_or_equal_than_str(value, args):
        if value is None:
            return False
        return len(value) <= int(args[0])

    @staticmethod
    def _test_less_than_str(value, args):
        if value is None:
            return False
        return len(value) < int(args[0])


