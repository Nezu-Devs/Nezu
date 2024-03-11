"""Elegant debuging tool"""
from inspect import currentframe
from typing import Any, Self


class Nezu:
    """Nezu object"""

    def __init__(self, id: str):
        from .parts.os_env import os_bool, os_int

        self._id = id
        self.seek = os_int(id, 'SEEK')
        self.color = os_bool(id, 'COLOR')
        self._locked = os_bool(id, 'LOCK')

        self.hard = self.__call__

    def __call__(self, seek: int = 0, color: bool = False, lock: bool = False):
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
        if not self._locked:
            self.seek = seek
            self.color = color
            self._locked = lock
        else:
            raise RuntimeError(
                f'This Nezu object #{self._id} is locked and cannot be changed.'
            )

    def __iter__(self):
        return iter(
            [
                ('id', self._id),
                ('seek', self.seek),
                ('color', self.color),
            ]
        )

    def json(self, path: str = 'nezu.json', **kwargs):
        """
        Initialaze nezu via json file
        """
        if not self._locked:
            import json

            with open(path, 'r', **kwargs) as file:
                all_data = json.load(file)
            nezu_data = all_data.get(self._id, {})
            self.seek = nezu_data.get('seek', 0)
            self.color = nezu_data.get('color', False)

        else:
            raise RuntimeError(
                f'This Nezu object #{self._id} is locked and cannot be changed.'
            )

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
            from .parts.parser import get_output

            FRAME = currentframe().f_back
            LINE = FRAME.f_lineno
            LOCAL = FRAME.f_locals
            GLOBAL = FRAME.f_globals
            BINS = FRAME.f_builtins

            if len(keys) < 2:
                prfx = f'@{LINE}'.rjust(7) + ' '
                desc = '  |  '.join(
                    [
                        get_output(LOCAL, GLOBAL, BINS, key, self.color)
                        for key in keys
                    ]
                )
                sufx = f'  |  << {note} >>' if note != None else ''
            else:
                prfx = f'@{LINE}'.rjust(7) + f' {"-"*70}\n\t'
                desc = '\n\t'.join(
                    [
                        get_output(LOCAL, GLOBAL, BINS, key, self.color)
                        for key in keys
                    ]
                )
                sufx = f'\n\t<< {note} >>' if note != None else ''
                sufx += f'\n\t{"-"*70}'

            print(f'{prfx}{desc}{sufx}')


def real_nezu():
    defaults = {'id': 'nezu'}
    return Nezu(**defaults)


ず = nezu = real_nezu()
ね = say = nezu.say

if __name__ == '__main__':
    print('Nezu is elegant debuging module')

