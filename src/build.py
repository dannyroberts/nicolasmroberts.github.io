import jinja2
import os
from collections import namedtuple

Page = namedtuple('Page', ['name', 'title', 'background_image'])

TEMPLATE_DIR = 'templates'
PAGES = [
    Page(name='index', title='Home', background_image='parallaxHome.jpg'),
    Page(name='projects', title='Projects', background_image='parallaxProj.jpg'),
    Page(name='scripts', title='Scripts', background_image='parallaxScripts.jpg'),
    Page(name='cv', title='CV', background_image='parallaxCV.jpg'),
    Page(name='photos', title='Photos', background_image='parallaxPhotos.jpg'),
]

def build():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR)
    )
    for page in PAGES:
        template = env.get_template('{page}.html.j2'.format(page=page.name))
        output = template.render(current_page=page, PAGES=PAGES)
        with open('{page}.html'.format(page=page.name), 'w') as f:
            f.write(output)


if __name__ == '__main__':
    build()
