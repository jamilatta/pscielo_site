import psycopg2
import psycopg2.extras

import settings

try:
    conn = psycopg2.connect("dbname='%s' user='%s' host='localhost' password='%s'" % (
                            settings.DB_NAME, settings.DB_USER, settings.DB_PASS))
except:
    print "I am unable to connect to the database"

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def get_collection_by_id(collection_id):
    try:
        query = "SELECT id, name, acronym FROM journalmanager_collection WHERE id = %s" % collection_id
        cur.execute(query)
    except:
        print "I can't execute the query: %s" % query
    else:
        collection = cur.fetchone()
        return {
            'name': collection[1],
            'acronym': collection[2],
        }


def get_collections_id_of_journal(journal_id):
    try:
        query = "SELECT collection_id FROM journalmanager_membership WHERE journal_id = %s" % journal_id
        cur.execute(query)
    except:
        print "I can't execute the query: %s" % query
    else:
        collections = cur.fetchall()
        results = []
        for collection in collections:
            results.append(collection['collection_id'])
        return results


def get_all_journals():
    try:
        query = """SELECT * FROM journalmanager_journal"""
        cur.execute(query)
    except:
        print "I can't execute the query: %s" % query
    else:

        rows = cur.fetchall()
        results = []
        for row in rows:
            journal_collections = []
            for collection_id in get_collections_id_of_journal(row['id']):
                collection_data = get_collection_by_id(collection_id)
                journal_collections.append(collection_data)

            try:
                journal_row = {
                    "jid": row['id'],  # TODO: FIX it on mananger
                    "collections": journal_collections,
                    # "use_licenses": row[''],
                    # "admission_date": row[''],
                    "national_code": row['national_code'],
                    # "subject_categories": row[''],
                    # "study_areas": row[''],
                    "social_networks": [{'network': 'twitter', 'account': row['twitter_user']}],
                    "title": row['title'],
                    "title_iso": row['title_iso'],
                    "short_title": row['short_title'],
                    "created": row['created'],
                    "updated": row['updated'],
                    "acronym": row['acronym'],
                    "scielo_issn": row['scielo_issn'],
                    "print_issn": row['print_issn'],
                    "eletronic_issn": row['eletronic_issn'],
                    "subject_descriptors": row['subject_descriptors'],
                    "init_year": row['init_year'],
                    "init_vol": row['init_vol'],
                    "init_num": row['init_num'],
                    "final_num": row['final_num'],
                    "final_vol": row['final_vol'],
                    "final_year": row['final_year'],
                    "copyrighter": row['copyrighter'],
                    "online_submission_url": row['url_online_submission'],
                    # "cover_url": row[''],
                    # "logo_url": row[''],
                    # "previous_journal_id": row['previous_title'],  # TODO: FIX to uuid
                    # "other_titles": row[''],
                    "publisher_name": row['publisher_name'],
                    "publisher_country": row['publisher_country'],
                    "publisher_state": row['publisher_state'],
                    "publisher_city": row['publication_city'],
                    # "publisher_address": row[''],
                    # "publisher_telephone": row[''],
                    # "current_status": row[''],
                    # "mission": row[''],
                }
            except Exception, e:
                print "%s for journal %s" % (e.message, row['id'])
            else:
                results.append(journal_row)
        return results
