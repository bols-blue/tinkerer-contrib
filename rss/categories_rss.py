# -*- coding: utf-8 -*-
'''
    categories_rss
    ~~~~~~~~~~~~~~

    RSS feeds for categories.

    Based on tinkerer.ext.rss.

    :copyright: Copyright 2013 by Atamert Ölçgen
    :license: BSD license
'''
from rss import rss
from tinkerer import utils


def html_collect_pages(app):
    '''
    Collect html pages and emit event
    '''
    for name, context, template in generate_feeds(app):
        yield (name, context, template)


def generate_feeds(app):
    env = app.builder.env
    categories = env.filing["categories"]

    for category_name, posts in env.filing["categories"].items():
        for name, context, template in rss.generate_feed(app, category_name, posts):
            slug = utils.name_from_title(name)
            yield ("rss/categories/%s" % slug, context, template)


def setup(app):
    app.connect("html-collect-pages", html_collect_pages)
