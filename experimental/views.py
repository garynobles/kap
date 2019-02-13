from django.shortcuts import render
import psycopg2

# import json
# options = [[x.id, unicode[x] for x in my_model.objects.all()]
# options_for_js = json.dumps(options)
#
# # In your Django template
# var my_array = {{ options_for_js|safe }}

# Create your views here.


import os
import sys
import psycopg2
#import progressbar as pb

from datetime import datetime
from timeit import default_timer as timer
import scipy.spatial.distance

# class Pointcloud2Volume():
    # def top(self):
def Pointcloud2Volume(request):
    top = 'pc_201407060711'
    print("creating tables")
    return render(request, 'Pointcloud2Volume/pointcloud2volume.html')
        # self.statusBar().showMessage('Importing Top...')
        # print("Started")
        #
        # top = 'pc_201407060711'
        # #top = 'pc_201407061221'
        #
        # print("creating tables")
        # # create a temp table
        #
        # # connect to the PostgreSQL server
        # conn = psycopg2.connect("dbname=kap_pointcloud host=localhost user=postgres password=Gnob2009")
        # cur = conn.cursor()
        # cur.execute("""DROP TABLE IF EXISTS pc_processing.top CASCADE;""")
        #
        # cur.execute("""
        #     CREATE TABLE pc_processing.top (
        #             id serial NOT NULL,
        #             x double precision,
        #             y double precision,
        #             z double precision,
        #             geom geometry,
        #             dist double precision,
        #             CONSTRAINT pc_top_pkey PRIMARY KEY (id));
        # """)
        #
        #
        # cur.close()
        # conn.commit()
        # conn.close()
        # print("tabbles created")
        # # bring in the data
        #
        #
        # # connect to the PostgreSQL server
        # conn = psycopg2.connect("dbname=kap_pointcloud host=localhost user=postgres password=Gnob2009")
        # cur = conn.cursor()
        # print("inserting data")
        # cur.execute("""
        # INSERT INTO pc_processing.top( x,y,z)
        #     SELECT st_x(PC_EXPLODE(pa)::geometry) as x,st_y(PC_EXPLODE(pa)::geometry) as y,st_z(PC_EXPLODE(pa)::geometry) as z
        #     from public.{}
        #     order by x,y,z
        #     --LIMIT 100000;
        # """.format(top)
        #             )
        # print("updating geometry")
        # cur.execute("""
        # UPDATE pc_processing.top
        #     SET geom=ST_GeomFromText('POINT('||x||' '||y||' '||z||')',32635);
        # """)
        #
        # conn.commit()
        # cur.close()
        #
        #
        #
        # conn.close()
        # self.statusBar().showMessage('Top Imported')



def webviewer3d(request):

    # instance = MyModel.objects.values('x')[0]
    # description = instance['x']

    # connect to the PostgreSQL server
    conn = psycopg2.connect("dbname=kap_pointcloud host=localhost user=postgres password=Gnob2009")
    cur = conn.cursor()
    # cur.execute("""SELECT array_to_json(array_agg(basesample)) FROM pc_processing.basesample""")
    # SELECT x - 580991 AS x, y - 4275267  AS y, z - 192 AS z  FROM pc_processing.basesample

    cur.execute("""SELECT x FROM pc_processing.basesample order by id ASC LIMIT 1500""")
    coord_x = cur.fetchall()
    cur.execute("""SELECT y FROM pc_processing.basesample order by id ASC LIMIT 1500""")
    coord_y = cur.fetchall()
    cur.execute("""SELECT z FROM pc_processing.basesample order by id ASC LIMIT 1500""")
    coord_z = cur.fetchall()



    # cur.execute("""SELECT x FROM pc_processing.filtered_top_dist  order by id ASC LIMIT 15""")
    # coord_x = cur.fetchall()
    # cur.execute("""SELECT y FROM pc_processing.filtered_top_dist order by id ASC LIMIT 15""")
    # coord_y = cur.fetchall()
    # cur.execute("""SELECT z FROM pc_processing.filtered_top_dist order by id ASC LIMIT 15""")
    # coord_z = cur.fetchall()

    cur.execute("""SELECT x,y,z FROM pc_processing.filtered_top_dist TABLESAMPLE BERNOULLI (1) LIMIT 150""")
    coords = cur.fetchall()




    # conn.commit()
    # self.statusBar().showMessage('Ready')
    length=len(coord_z)


    cur.close()

    conn.close()


    # min_x = coord_x.min()
    # min_y = coord_y.min()
    # min_z = coord_z.min()

    min_x = min(coord_x)
    min_y = min(coord_y)
    min_z = min(coord_z)


    max_x = max(coord_x)
    max_y = max(coord_y)
    max_z = max(coord_z)

    positionx = min_x[0] + ((max_x[0] - min_x[0]) / 2)

    context = {
    'coord_x':coord_x,
    'coord_y':coord_y,
    'coord_z':coord_z,
    'length':length,
    'min_x':min_x,
    'min_y':min_y,
    'min_z':min_z,
    'max_x':max_x,
    'max_y':max_y,
    'max_z':max_z,

    'positionx':positionx,
    }


    return render(request, 'threejs/index.html', context
    )
