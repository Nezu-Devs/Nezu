from nezu.nezu import real_nezu

def test_hide(capsys):
    nezu = real_nezu()
    nezu(2)
    lis = [
        '--0--',
        '--1--',
        '--2--',
        '',
        '',
    ]
    for i in range(5):
        nezu.say(f'--{i}--', hide=i)
        said = capsys.readouterr().out
        assert said[8:-1] == lis[i]

def test_color(capsys):
    nezu = real_nezu()
    nezu(1, color=True)
    biggus = 'dickus'
    nezu.say(biggus)
    said = capsys.readouterr().out
    expected = f'\033[92mdickus\033[0m'
    assert said[8:-1] == expected