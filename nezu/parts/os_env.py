from os import getenv


def os_bool(id: str, param: str):
    val = getenv(f'{id.upper()}_{param.upper()}')
    val = val.casefold() if val != None else 'False'
    val = (
        True
        if val in ('true', 't') or val.isdecimal() and int(val) != 0
        else False
    )
    return val


def os_int(id: str, param: str):
    val = getenv(f'{id.upper()}_{param.upper()}')
    val = int(val) if val != None else 0
    return val
