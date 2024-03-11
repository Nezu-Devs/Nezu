from ..nezu import real_nezu


def test_hide(capsys):
    nezu = real_nezu()
    nezu(2)
    lis = [
        'l i:int  =>  0',
        'l i:int  =>  1',
        'l i:int  =>  2',
        '',
        '',
    ]
    for i in range(5):
        nezu.say('i', hide=i)
        said = capsys.readouterr().out
        assert said[8:-1] == lis[i]


def test_color(capsys):
    nezu = real_nezu()
    nezu(1, True)
    biggus = 'dickus'
    nezu.say('biggus')
    said = capsys.readouterr().out
    expected = f'\u001b[36ml\u001b[35m \u001b[0mbiggus\u001b[35m:\u001b[31mstr\u001b[35m  =>  \u001b[33mdickus\u001b[0m'
    assert said[8:-1] == expected


# def test_list(capsys):
#     nezu = real_nezu()
#     nezu(1)
#     biggus = ['dickus']
#     nezu.say('biggus[0]')
#     said = capsys.readouterr().out
#     expected = f'l biggus:str  =>  dickus'
#     assert said[8:-1] == expected


def test_obj(capsys):
    nezu = real_nezu()
    nezu(1)

    class Biggus:
        txt: str = 'dickus'

    biggus = Biggus()
    nezu.say('biggus.txt')
    said = capsys.readouterr().out
    expected = f'l biggus.txt:str  =>  dickus'
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
    nezu.say('spam.child.child.txt')
    said = capsys.readouterr().out
    expected = f'l spam.child.child.txt:str  =>  bacon'
    assert said[8:-1] == expected


def test_scope_b(capsys):
    nezu = real_nezu()
    nezu(1)
    nezu.say('print')
    said = capsys.readouterr().out
    assert said[8] == f'b'


def test_scope_l(capsys):
    nezu = real_nezu()
    nezu(1)
    print = 'egg'
    nezu.say('print')
    said = capsys.readouterr().out
    assert said[8] == f'l'


biggus = 'dickus'


def test_scope_g(capsys):
    nezu = real_nezu()
    nezu(1)
    nezu.say('biggus')
    said = capsys.readouterr().out
    assert said[8] == f'g'


def test_multiline(capsys):
    nezu = real_nezu()
    nezu(1)
