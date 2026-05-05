import os

def test_section_indexes():
    for section in ['daily','guides','open-source','build-log','workshops']:
        path = os.path.join('content', section, '_index.md')
        assert os.path.exists(path)

    assert open('static/CNAME').read().strip() == 'freelancer-automation.com'
