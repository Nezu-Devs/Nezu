def parse_name(long_str):
    if long_str.count('.') and long_str.count('['):
        i = min(long_str.index('.'), long_str.index('['))
    elif long_str.count('.'):
        i = long_str.index('.')
    elif long_str.count(']'):
        i = long_str.index(']')
    else:
        i = 0
    key = long_str[:i] if i else long_str

    return key


def get_output(loc, glob, bins, long_str, color):
    # from .name_parser import parse_name

    is_undefined = False
    key = parse_name(long_str)
    _sep0 = ' '

    if key in loc:
        try:
            _val = eval(long_str, glob, loc)
            _src = 'l'
            _type = type(_val).__name__
            _sep1 = ':'
            _sep2 = '  =>  '
        except Exception:
            is_undefined = True

    elif key in glob:
        try:
            _val = eval(long_str, glob, loc)
            _src = 'g'
            _type = type(_val).__name__
            _sep1 = ':'
            _sep2 = '  =>  '
        except Exception:
            is_undefined = True

    elif key in bins:
        try:
            _val = eval(long_str, bins)
            _src = 'b'
            _type = (
                type(_val).__name__
                if type(_val).__name__ != 'builtin_function_or_method'
                else 'function'
            )
            _sep1 = ':'
            _sep2 = '  =>  '
        except Exception:
            is_undefined = True

    else:
        is_undefined = True

    if is_undefined:
        _src = 'u'
        _val = ''
        _type = ''
        _sep1 = ''
        _sep2 = ''

    if _type == 'function' and _val.__doc__:
        _desc = (
            f'{_val.__doc__}'[:40] + '...'
            if len(_val.__doc__) > 43
            else _val.__doc__
        )
    elif _type == 'function':
        _desc = 'No docstring'
    else:
        _desc = _val

    return (
        f'\u001b[36m{_src}\u001b[35m{_sep0}\u001b[0m{long_str}\u001b[35m{_sep1}\u001b[31m{_type}\u001b[35m{_sep2}\u001b[33m{_desc}\u001b[0m'
        if color
        else f'{_src}{_sep0}{long_str}{_sep1}{_type}{_sep2}{_desc}'
    )
