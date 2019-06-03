from django.shortcuts import render
from django.db import connection

import psycopg2
import agensgraph
# Create your views here.

def overview(request):
    # allstorage = Storage.objects.all()
    return render(request, 'dataimport/imports.html',
    {
        # 'storage':allstorage
    })


def updategygaiasamplerows(request):
    # pass
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO kap.sample
(area_easting, area_northing, context_number, sample_number, sample_type, weight, description, recovery_method )
(
	SELECT
	
	a.area_easting, a.area_northing, a.context_number, a.sample_number,
	a.material, a.weight_kilograms, a.sample_description, a.recovery_type

FROM samples.samples a

LEFT JOIN kap.sample b
	ON a.area_easting = b.area_easting AND a.area_northing = b.area_northing AND a.sample_number = b.sample_number AND a.context_number = b.context_number
WHERE
(a.area_easting IS  NULL AND a.area_northing IS  NULL AND a.sample_number IS   NULL AND a.context_number IS  NULL)
OR
(b.area_easting IS  NULL AND b.area_northing IS  NULL AND b.sample_number IS  NULL AND b.context_number IS  NULL)

)

        """)
        return render(request, 'dataimport/imports.html',
        {
            # 'storage':allstorage
        })



#         INSERT INTO kap.sample
# (area_easting, area_northing, context_number, sample_number, sample_type, weight, description, recovery_method )
# (
# 	SELECT
# 	--b.area_easting AS "NEW easting", b.area_northing AS "NEW northing", b.sample_number AS "NEW sample", b.context_number AS "NEW context",
# 	a.area_easting, a.area_northing, a.context_number, a.sample_number,
# 	a.material, a.weight_kilograms, a.sample_description, a.recovery_type
#
# FROM samples.samples a
# --FULL OUTER JOIN kap.sample b
# LEFT JOIN kap.sample b
# 	ON a.area_easting = b.area_easting AND a.area_northing = b.area_northing AND a.sample_number = b.sample_number AND a.context_number = b.context_number
# WHERE
# (a.area_easting IS  NULL AND a.area_northing IS  NULL AND a.sample_number IS   NULL AND a.context_number IS  NULL)
# OR
# (b.area_easting IS  NULL AND b.area_northing IS  NULL AND b.sample_number IS  NULL AND b.context_number IS  NULL)
#
# )



# Graph

def graph_samples(request):
    # allstorage = Storage.objects.all()
    conn = psycopg2.connect("dbname=agens host=localhost user=agens password=Gnob2009 port=5433")
    cur = conn.cursor()

    cur.execute("""SET graph_path = publications;""")

    pubId = self.lePubId.text()
    pubType = self.lePubType.text()
    pubTitle = self.lePubTitle.text()
    pubYear = self.lePubYear.text()
    pubPageNumbers = self.lePubPageNumbers.text()

    cypher = "CREATE (n:Publication { name:  \'" + pubId + "\', title: \'" + pubTitle + "\', year: \'" + pubYear + "\', pages: \'" + pubPageNumbers + "\' })"
    # cypher = "MATCH (n:Person {name:'Landeschi'}),(p:Publication{name: 'Landeschi et al. 2018'}) CREATE (n)-[:PersonOf]->(p);"
    print(cypher)
    cur.execute(cypher)

    cur.close()
    conn.commit()
    return render(request, 'dataimport/imports.html',
    {
        # 'storage':allstorage
    })
