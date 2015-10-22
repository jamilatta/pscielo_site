# coding: utf-8

from datetime import datetime
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

from journal import Journal
from issue import Issue
from article import Article

# Define a default Elasticsearch client
connections.create_connection(hosts=['192.168.169.146'])

# create the mappings in elasticsearch
# Journal.init()
# Issue.init()
# Article.init()

# create and save and journal
journal = Journal(_id=1,
                  jid="id do scielo manager",
                  title='Revista de ElasticSearch XYZ',
                  created=datetime.now(),
                  social_networks=[{"network": "twitter", "account": "@jamil"},
                                   {"network": "twitter", "account": "@juan"}])

journal.save()

journal = Journal.get(id=1)

print journal.title

s = Search(index="iopac").query("match", title="elasticsearch")

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.title)

# Display cluster health
print connections.get_connection().cluster.health()
