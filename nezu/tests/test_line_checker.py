"""Very fragile test code. Do not attempt to reformat."""
from nezu.nezu import real_nezu

nezu = real_nezu()
nezu(1)


def test_line_checker(capsys):
    nezu.say()
    said = capsys.readouterr().out
    assert said.strip() == '@9'

    nezu.say()
    said = capsys.readouterr().out
    assert said.strip() == '@13'
