# coding: utf-8

from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer, Nested, MetaField

import settings


class Issue(DocType):

    iid = String(index="not_analyzed")
    sections = Nested(properties={'order': Integer(index='not_analyzed'),
                                  'subjects': Nested(properties={
                                    "name": String(index='not_analyzed'),
                                    "language": String(index='not_analyzed')})
                                  })
    volume = String(index="not_analyzed")
    number = String(index="not_analyzed")
    created = Date()
    updated = Date()
    start_month = String(index="not_analyzed")
    end_month = String(index="not_analyzed")
    year = String(index="not_analyzed")
    use_licenses = String(fields={'license_code': String(index='not_analyzed'),
                                  'reference_url': String(index='not_analyzed'),
                                  'disclaimer': String(index='not_analyzed')})
    cover_url = String(index='not_analyzed')
    label = String(index='not_analyzed')
    order = Integer()
    bibliographic_legend = String(index='not_analyzed')

    class Meta:
        index = settings.INDEX
        parent = MetaField(type='journal')
