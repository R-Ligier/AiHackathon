import urllib2

def gtfs_query():
    numberline="http://datamine.mta.info/mta_esi.php?key=067b7c2881d68b0b6e7b0ca67a26c664&feed_id=1"

    response = urllib2.urlopen(numberline)
    html = response.read()

    return html

gtfs_query()