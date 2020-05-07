from core.validations import Validations
from core.util import dict_value


class InsertValidations(Validations):

    def __init__(self, _dict):
        self._my_obj = _dict
        self._obj = []
        self._field = None
        self._message = None

    def add_raw(self, string, function, message=None): #TODO testar implementação
        self.__setattr__(f"_test_{function.__name__}", function)
        self._obj.append({"status": self._test(self._string_to_dict(string)), "message": message, "field": self._field})
        return self

    def add(self, string, message=None):
        self._obj.append({"status": self._test(self._string_to_dict(string)), "message": message, "field": self._field})
        return self

    def _string_to_dict(self, string):
        string = string.split('IS')
        self._field = string[0].strip()

        def extract_args(condition):
            condition = condition.split(':')

            field = condition[0].strip()
            args = condition[1].split(',') if len(condition) == 2 else []
            return {field: args}

        def extract_condition_or(condition):
            return [x.strip() for x in condition.split('OR')]

        def extract_condition_and(condition):
            return [extract_args(x) for x in condition.split('AND')]

        def condition_to_dict(condition):
            dic = {}

            for c in condition:
                key = next(iter(c.keys()))
                dic[key] = c[key]

            return dic

        conditions = extract_condition_or(string[1])
        conditions = [extract_condition_and(x) for x in conditions]

        return [condition_to_dict(x) for x in conditions]

    def is_valid(self):
        for i in self._obj:
            if i.get('status', None) is False:
                # TODO CRIAR NOVA CLASSE DE EXEPTIONS E ERRORS HANDLERS
                raise ApiException(error=self._obj)

    def _test(self, array):
        def process_test(item):
            for key in item.keys():
                value = dict_value(self._my_obj, self._field)
                args = item[key]
                status = getattr(InsertValidations, '_test_{}'.format(key))(value, args)
                item[key] = status

            return all([x for x in item.values()])

        array = [process_test(x) for x in array]

        return True in array

