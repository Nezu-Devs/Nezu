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

def parse_desc(_type, val, key):
    if _type == 'function' and val.__doc__:
        # _desc = (
        #     f'{val.__doc__}'[:40] + '...'
        #     if len(val.__doc__) > 43
        #     else val.__doc__
        # )
        _desc = val.__doc__
    elif _type == 'function':
        _desc = 'No docstring'
    else:
        _desc = str(val)
    
    cut_lines = '\n'+' '*12
    if '\n' in _desc:
        l = _desc.split('\n')
        for line in l:
            while len(line)>80:
                cut_lines += line[0:80] + '\n'+' '*12
                line = line[80:]
            else:
                cut_lines += line +'\n'+' '*12
    elif len(_desc)+len(_type)+len(key)>80-7:
        print(len(_desc))
        print(len(_type))
        print(len(key))
        while len(_desc)>80:
            print(len(_desc))
            cut_lines += _desc[0:80] + '\n'+' '*12
            _desc = _desc[80:]
        else:
            cut_lines += _desc
    else:
        cut_lines = _desc
    return cut_lines
    

def get_output(loc, glob, bins, long_str, color):
    # from .name_parser import parse_name

    is_undefined = False
    key = parse_name(long_str)
    _sep0 = ' '

    if key in loc:
        try:
            _val = eval(long_str, glob, loc)

            _src = 'L'
            _src = _src + ('g' if key in glob else '.')
            _src = _src + ('b' if key in bins else '.')
            _type = type(_val).__name__
            _sep1 = ':'
            _sep2 = '  =>  '
        except Exception:
            is_undefined = True

    elif key in glob:
        try:
            _val = eval(long_str, glob, loc)
            _src = '.G'
            _src = _src + ('b' if key in bins else '.')
            _type = type(_val).__name__
            _sep1 = ':'
            _sep2 = '  =>  '
        except Exception:
            is_undefined = True

    elif key in bins:
        try:
            _val = eval(long_str, bins)
            _src = '..B'
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
        _src = '...'
        _val = ''
        _type = ''
        _sep1 = ''
        _sep2 = ''

    _desc = parse_desc(_type,_val, long_str)


    return (
        f'\u001b[36m{_src}\u001b[35m{_sep0}\u001b[0m{long_str}\u001b[35m{_sep1}\u001b[31m{_type}\u001b[35m{_sep2}\u001b[33m{_desc}\u001b[0m'
        if color
        else f'{_src}{_sep0}{long_str}{_sep1}{_type}{_sep2}{_desc}'
    )
