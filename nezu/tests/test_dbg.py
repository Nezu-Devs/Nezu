from nezu.nezu import real_nezu


def test_hide(capsys):
    nezu = real_nezu()
    nezu(2)
    lis = [
        'L.. i:int  =>  0',
        'L.. i:int  =>  1',
        'L.. i:int  =>  2',
        '',
        '',
    ]
    for i in range(5):
        nezu.dbg('i', hide=i)
        said = capsys.readouterr().out
        assert said[8:-1] == lis[i]


def test_color(capsys):
    nezu = real_nezu()
    nezu(1, True)
    biggus = 'dickus'
    nezu.dbg('biggus')
    said = capsys.readouterr().out
    expected = f'\u001b[36mL..\u001b[35m \u001b[0mbiggus\u001b[35m:\u001b[31mstr\u001b[35m  =>  \u001b[33mdickus\u001b[0m'
    assert said[8:-1] == expected


# def test_list(capsys):
#     nezu = real_nezu()
#     nezu(1)
#     biggus = ['dickus']
#     nezu.dbg('biggus[0]')
#     said = capsys.readouterr().out
#     expected = f'l biggus:str  =>  dickus'
#     assert said[8:-1] == expected


def test_obj(capsys):
    nezu = real_nezu()
    nezu(1)

    class Biggus:
        txt: str = 'dickus'

    biggus = Biggus()
    nezu.dbg('biggus.txt')
    said = capsys.readouterr().out
    expected = f'L.. biggus.txt:str  =>  dickus'
    assert said[8:-1] == expected


def test_nesterd_obj(capsys):
    nezu = real_nezu()
    nezu(1)

    class Egg:
        txt: str = 'bacon'

    class Ham:
        child = Egg()

    class Spam:
        child = Ham()

    spam = Spam()
    nezu.dbg('spam.child.child.txt')
    said = capsys.readouterr().out
    expected = f'L.. spam.child.child.txt:str  =>  bacon'
    assert said[8:-1] == expected


def test_scope_b(capsys):
    nezu = real_nezu()
    nezu(1)
    nezu.dbg('print')
    said = capsys.readouterr().out
    assert said[8:11] == f'..B'


def test_scope_l(capsys):
    nezu = real_nezu()
    nezu(1)
    ham = 'egg'
    nezu.dbg('ham')
    said = capsys.readouterr().out
    assert said[8:11] == f'L..'


global_biggus = 'dickus'


def test_scope_g(capsys):
    nezu = real_nezu()
    nezu(1)
    nezu.dbg('global_biggus')
    said = capsys.readouterr().out
    assert said[8:11] == f'.G.'


def test_shadowing_L_b(capsys):
    nezu = real_nezu()
    nezu(1)
    print = 'egg'
    nezu.dbg('print')
    said = capsys.readouterr().out
    assert said[8:11] == f'L.b'


global_nortius = 'maximus'


def test_shadowing_Lg(capsys):
    nezu = real_nezu()
    nezu(1)
    global_nortius = 'minimus'
    nezu.dbg('global_nortius')
    said = capsys.readouterr().out
    assert said[8:11] == f'Lg.'


default_breakpoint = breakpoint
breakpoint = 69


def test_shadowing_Gb(capsys):
    nezu = real_nezu()
    nezu(1)
    nezu.dbg('breakpoint')
    said = capsys.readouterr().out
    assert said[8:11] == f'.Gb'


def test_shadowing_Lgb(capsys):
    nezu = real_nezu()
    nezu(1)
    breakpoint = 420
    nezu.dbg('breakpoint')
    said = capsys.readouterr().out
    assert said[8:11] == f'Lgb'


breakpoint = default_breakpoint


def test_multiline(capsys):
    nezu = real_nezu()
    nezu(1)
    biggus = 'BIGGUS'
    dickus = 'DICKUS'
    nezu.dbg('biggus', 'dickus')
    said = capsys.readouterr().out
    a, b, c, d, _ = said.split('\n')
    assert a[8:] == '-' * 70
    assert b[8:] == f'L.. biggus:str  =>  BIGGUS'
    assert c[8:] == f'L.. dickus:str  =>  DICKUS'
    assert d[8:] == '-' * 70
    # assert said == ''
