def test_nav_order():
    # simple check that nav partial contains required links in order
    nav = open('themes/zavaa-dark/layouts/partials/nav.html').read()
    assert 'Home' in nav and 'Daily' in nav
    assert 'Workshops' in nav
    # workshops should be last link before closing nav
    assert nav.rfind('Workshops') > nav.rfind('Build Log')
    # icons should be included via svg <use>
    assert 'class="icon"' in nav


def test_hero_graphic():
    index = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'hero-bg' in index
    assert 'hero-content' in index
    assert 'source.unsplash.com' in open('themes/zavaa-dark/layouts/partials/head.html').read()

def test_theme_toggle():
    nav = open('themes/zavaa-dark/layouts/partials/nav.html').read()
    assert 'theme-toggle' in nav


def test_footer_links():
    footer = open('themes/zavaa-dark/layouts/partials/footer.html').read()
    # template should reference githubUrl param and templatesUrl param
    assert '{{ .Site.Params.githubUrl }}' in footer
    assert '{{ .Site.Params.templatesUrl }}' in footer


def test_toggle_script():
    head = open('themes/zavaa-dark/layouts/partials/head.html').read()
    assert 'theme-toggle' in head
    assert 'localStorage' in head

def test_archetype_image():
    content = open('archetypes/daily.md').read()
    assert 'image:' in content

def test_sample_post_has_image():
    post = open('content/daily/2025-01-15-example.md').read()
    assert 'image:' in post

def test_nav_fixed():
    head = open('themes/zavaa-dark/layouts/partials/head.html').read()
    assert 'position:fixed' in head
    assert 'backdrop-filter' in head

def test_hero_cta():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="cta"' in idx

def test_footer_credit():
    footer = open('themes/zavaa-dark/layouts/partials/footer.html').read()
    assert 'Unsplash' in footer

def test_home_intro():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="intro"' in idx

def test_testimonial_present():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="testimonial"' in idx

def test_toggle_script_domready():
    head = open('themes/zavaa-dark/layouts/partials/head.html').read()
    assert 'DOMContentLoaded' in head

def test_services_section():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="services"' in idx

def test_about_section():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="about"' in idx

def test_project_highlight():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'project-highlight' in idx

def test_social_icons_in_footer():
    footer = open('themes/zavaa-dark/layouts/partials/footer.html').read()
    assert 'icon-twitter' in footer and 'icon-github' in footer


def test_stats_section():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="stats"' in idx
    # template should include stat-card markup and chart icon
    assert 'stat-card' in idx
    assert 'icon-chart' in idx


def test_clients_section():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="clients"' in idx
    assert 'client-logo' in idx


def test_cta_banner():
    idx = open('themes/zavaa-dark/layouts/index.html').read()
    assert 'class="cta-banner"' in idx


def test_new_icons():
    svg = open('static/icons.svg').read()
    # verify newly added symbols as well
    for name in [
        'icon-chart','icon-clients','icon-code','icon-download',
        'icon-chat','icon-calendar','icon-rocket','icon-check-circle'
    ]:
        assert name in svg

