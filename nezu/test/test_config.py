from ..nezu import real_nezu
from os import environ as env


def test_no_config():
    env['NEZU_SEEK'] = '0'
    env['NEZU_COLOR'] = '0'
    nezu = real_nezu()
    assert dict(nezu) == {'id': 'nezu', 'seek': 0, 'color': False}


def test_hard_config_seek():
    nezu = real_nezu()
    nezu(seek=1)
    assert dict(nezu) == {'id': 'nezu', 'seek': 1, 'color': False}


def test_hard_config_color():
    nezu = real_nezu()
    nezu(color=True)
    assert dict(nezu) == {'id': 'nezu', 'seek': 0, 'color': True}


def test_json_config_seek():
    content = '{"nezu":{"seek":1}}'
    with open('nezu.json', 'w') as f:
        print(content, file=f)
    nezu = real_nezu()
    nezu.json()
    assert dict(nezu) == {'id': 'nezu', 'seek': 1, 'color': False}


def test_json_config_color():
    content = '{"nezu":{"color":true}}'
    with open('nezu.json', 'w') as f:
        print(content, file=f)
    nezu = real_nezu()
    nezu.json()
    assert dict(nezu) == {'id': 'nezu', 'seek': 0, 'color': True}
