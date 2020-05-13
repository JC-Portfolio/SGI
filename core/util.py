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
    try:
        if len(field) >= 1:
            for i in field:
                dic = dic['{}'.format(i)]
    except KeyError:
        dic = None

    return dic


def response(message=None, http_status=200, data=None):
    obj_to_return = {
        "message": message if message else 'Sem messagem',
    }
    if data:
        obj_to_return['data'] = data

    return obj_to_return, http_status


def sanitize_obj(_list, fields_to_remove):
    #_list --> lista de objetos json para serem limpos
    #required_field --> campos indesejados , ex:  ['id', 'profile_id', 'status', 'name', 'email', 'profile_id']

    if _list:
        for index, obj in enumerate(_list):
            _list[index] = {key: obj[key] for key in obj.keys() if key not in fields_to_remove}


