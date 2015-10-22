# coding: utf-8

from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer, Nested, MetaField

import settings


class Article(DocType):

    aid = String(index="not_analyzed")
    created = Date()
    updated = Date()
    htmls = Nested(properties={'language': String(index='not_analyzed'),
                               'source': String(index='not_analyzed')})
    domain_key = String(index="not_analyzed")

    class Meta:
        index = settings.INDEX
        parent = MetaField(type='issue')
        dynamic = MetaField('strict')
