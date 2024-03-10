"""Elegant debuging tool"""
from inspect import currentframe
from typing import Any, Self


class Nezu:
    """Nezu object"""

    def __init__(
        self,
        id: str | None = None,
        seek: int = 0,
        color: bool = False,
        null: bool = False,
    ):
        self.__id = id
        self.__seek = seek
        self.__color = color
        self.__null = True
        self.hard = self.__call__
        if self.__id == 'nezu':
            self.argv = self.__argv

    def __call__(self, seek: int = 0, color: bool = False):
        """
        Hard coded configuration.

        Parameters
        ------------
            seek: int = 0
                How deep to seek for hidden calls of `say` function?
                Say function is called with `hide` parameter (0 by default).
                If `seek => hide` message will be displayed.
            color: bool = False
                Determine if output is colored.

        """
        if self.null:
            self.__seek = seek
            self.__color = color

    def __iter__(self):
        lis = [
            ('id', self.__id),
            ('seek', self.__seek),
            ('color', self.__color),
        ]
        return iter(lis)

    @property
    def null(self, where='Nowhere'):
        """Determine if object can be configured"""
        if not self.__null:
            raise RuntimeError('This object, can only be configured once')
        else:
            # print(where)
            self.__null = False
            return True
        

    @property
    def seek(self):
        """
        How deep to seek for hidden calls of `say` function?
        Say function is called with `hide` parameter (0 by default).
        If `seek => hide` message will be displayed.
        """
        return self.__seek

    @seek.setter
    def seek(self, depth: int) -> Self:
        """
        How deep to seek for hidden calls of `say` function?
        Say function is called with `hide` parameter (0 by default).
        If `depth => hide` message will be displayed.

        Parameters
        ------------
            depth:int
        """
        self.__seek = depth
        return self

    @property
    def color(self):

        return self.__color

    @color.setter
    def color(self, b: bool):
        """
        Determine if output is colored.

        Parameters
        ------------
        - b: bool
        """
        self.__color = b
        return self

    def __argv(self):
        """ """
        if self.null and self.id == 'nezu':
            from argparse import ArgumentParser

            parser = ArgumentParser()

            parser.add_argument(
                '--nezu', action='store_true', help='Enable nezu debuger.'
            )
            parser.add_argument(
                '--nezu-color',
                action='store_true',
                help='Enable nezu debuger in color.',
            )
            parser.add_argument(
                '--nezu-seek',
                type=int,
                choices=range(1, 11),
                help='Seek for hidden debug messages.',
            )

            args = parser.parse_args()
            self.__seek = (
                args.nezu or args.nezu_color
                if not args.nezu_seek
                else args.nezu_seek
            )
            self.__color = args.nezu_color
        else:
            raise RuntimeError(
                'Only object of id `nezu` can be called with argv.'
            )

    def json(self, path: str = 'nezu.json', **kwargs):
        """
        Initialaze nezu via json file
        """
        if self.null:
            import json

            with open(path, 'r', **kwargs) as file:
                all_data = json.load(file)
            nezu_data = all_data.get(self.__id, {})
            self.__seek = nezu_data.get('seek', 0)
            self.__color = nezu_data.get('color', False)

    def os(self):
        """
        Initialaze nezu via os environmental variables
        """
        # if self.null:
        from os import getenv

        seek = getenv(f'{self.__id.upper()}_SEEK')
        seek = int(seek) if seek != None else 0
        self.__seek = seek
        color = getenv(f'{self.__id.upper()}_COLOR')
        color = color.casefold() if color != None else 'False'
        color = (
            True
            if color in ('true', 't')
            or color.isdecimal()
            and int(color) != 0
            else False
        )
        self.__color = color

    def __lgu(self, loc, glob, bins, long_str):
        is_undefined = False
        key = self.__parse_str(long_str)
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
            if self.color
            else f'{_src}{_sep0}{long_str}{_sep1}{_type}{_sep2}{_desc}'
        )

    def __parse_str(self, long_str):
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

    def say(self, *keys: str, note: str = None, hide: int = 1) -> None:
        """
        Parameters
        ------------
        
        - `*keys:str`
            
            Names of varables to inspect

        - `note:str=None`
            
            Optional comment. Ignored if equal to None.

        - `hide:int=1`
            
            How deep do you want to hide this message.
            If `hide <= 0`, this message will be displayed by default.

        
        Description
        ------------
        Function `say` displays following data in that order for each inspected varable:
        
        - number of line it was called at
        
        - scope of inspected variable
        
        - name of inspected variable
        
        - type of inspected variable
        
        - value of inspected variable
        """

        if self.seek >= hide:
            FRAME = currentframe().f_back
            LINE = FRAME.f_lineno
            LOCAL = FRAME.f_locals
            GLOBAL = FRAME.f_globals
            BINS = FRAME.f_builtins

            if len(keys) < 2:
                prfx = f'@{LINE}'.rjust(7) + ' '
                desc = '  |  '.join(
                    [self.__lgu(LOCAL, GLOBAL, BINS, key) for key in keys]
                )
                sufx = f'  |  << {note} >>' if note != None else ''
            else:
                prfx = f'@{LINE}'.rjust(7) + f' {"-"*70}\n\t'
                desc = '\n\t'.join(
                    [self.__lgu(LOCAL, GLOBAL, BINS, key) for key in keys]
                )
                sufx = f'\n\t<< {note} >>' if note != None else ''
                sufx += f'\n\t{"-"*70}'

            print(f'{prfx}{desc}{sufx}')

def real_nezu():
    defaults = {'id':'nezu', 'null':True}
    return Nezu(**defaults)
ず = nezu = real_nezu()
ね = say = nezu.say
