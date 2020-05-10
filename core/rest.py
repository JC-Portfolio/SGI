from flask import request, jsonify


class Rest:
    functions = {'POST': 'make_insert,_insert_validations',
                 'PUT': 'make_update,_update_validations',
                 'DEL': 'make_del'}

    def __init__(self, service_obj, insert_validations, update_validations):
        self._obj = service_obj
        self._method_response = {}
        self._insert_validations = insert_validations
        self._update_validations = update_validations

    @classmethod
    def _detect_method(cls):
        method = request.method
        func_method = cls.functions[method]
        func_method, args = func_method.split(',')

        return func_method, args, method

    def request_data(self):
        return self._obj.data()

    def response(self, method, http_status=200):

        response = jsonify({'message': self._method_response.get(method, 'Sem mensagem')})
        response.status_code = http_status

        return response

    def call_rest_method(self):
        func, args, method = Rest._detect_method()
        args = getattr(self, args)
        self.request_data()

        self._obj.__getattribute__(func)(args)

        return self.response(method)





