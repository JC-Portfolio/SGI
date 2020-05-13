from flask import jsonify


class ApiException(Exception):

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def return_dict(self):
        dict_to_return = {}

        if self.payload is not None:
            dict_to_return['payload'] = self.payload

        dict_to_return['message'] = self.message

        return dict_to_return


def api_handle(error):

    response = jsonify(error.return_dict())
    response.status_code = error.status_code

    return response


