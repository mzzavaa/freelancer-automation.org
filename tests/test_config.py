import toml

def test_hugo_config():
    cfg = toml.load('hugo.toml')
    assert cfg['baseURL'].startswith('https://')
    assert cfg['theme'] == 'zavaa-dark'
