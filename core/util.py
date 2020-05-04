import uuid


def create_uuid():
    return str(uuid.uuid4())


def sql_to_dict(sql_obj):
    sql_columns = sql_obj.__table__.columns.keys()

    sql_dict = {key: sql_obj.__getattribute__(key) for key in sql_columns}

    return sql_dict


def dict_value(dic, field):
    # notação de objetos javascript para nested dicts -- > document.cpf

    field = field.split('.')
    print(field)
    try:
        if len(field) >= 1:
            for i in field:
                dic = dic['{}'.format(i)]
    except KeyError:
        dic = None

    return dic

#todo REFAZER RESPONSE


def response(message=None, http_status=200, data=None):
    obj_to_return = {
        "message": message if message else 'Sem messagem',
    }
    if data:
        obj_to_return['data'] = data

    return obj_to_return, http_status