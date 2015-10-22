# coding: utf-8

from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer, Nested, MetaField

import settings


class Journal(DocType):

    jid = String()
    collections = Nested(properties={'acronym': String(index='not_analyzed'),
                                     'name': String(index='not_analyzed')})
    use_licenses = String(fields={'license_code': String(index='not_analyzed'),
                                  'reference_url': String(index='not_analyzed'),
                                  'disclaimer': String(index='not_analyzed')})
    admission_date = String(index='not_analyzed')  # Verificar o tipo
    national_code = String(index='not_analyzed')
    subject_categories = String(index='not_analyzed')
    study_areas = String(index='not_analyzed')
    social_networks = Nested(properties={'network': String(index='not_analyzed'),
                                         'account': String(index='not_analyzed')})
    title = String()
    title_iso = String()
    short_title = String()
    created = Date()
    updated = Date()
    acronym = String(index='not_analyzed')
    scielo_issn = String(index='not_analyzed')
    print_issn = String(index='not_analyzed')
    eletronic_issn = String(index='not_analyzed')
    subject_descriptors = String(index='not_analyzed')
    init_year = String(index='not_analyzed')
    init_vol = String(index='not_analyzed')
    init_num = String(index='not_analyzed')
    final_num = String(index='not_analyzed')
    final_vol = String(index='not_analyzed')
    final_year = String(index='not_analyzed')
    copyrighter = String(index='not_analyzed')
    online_submission_url = String(index='not_analyzed')
    cover_url = String(index='not_analyzed')
    logo_url = String(index='not_analyzed')
    previous_journal_id = String()
    other_titles = Nested(properties={'title': String(index='not_analyzed'),
                                      'category': String(index='not_analyzed')})
    publisher_name = String(index='not_analyzed')
    publisher_country = String(index='not_analyzed')
    publisher_state = String(index='not_analyzed')
    publisher_city = String(index='not_analyzed')
    publisher_address = String(index='not_analyzed')
    publisher_telephone = String(index='not_analyzed')
    current_status = String(index='not_analyzed')
    mission = Nested(properties={'description': String(index='not_analyzed'),
                                 'language': String(index='not_analyzed')})

    class Meta:
        index = settings.INDEX
        dynamic = MetaField('strict')
