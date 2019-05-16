from django import template
# from django.contrib.auth.models import Group
import datetime

from django.db import connection

register = template.Library()

register.simple_tag
def count_new_gygaia_botany_rows():
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT count(*)
        FROM kap.sample a
        -- FROM samples.samples a
        LEFT JOIN samples.samples b
        --FULL OUTER JOIN kap.sample b
        ON a.area_easting = b.area_easting AND a.area_northing = b.area_northing AND a.sample_number = b.sample_number AND a.context_number = b.context_number
        WHERE
        (a.area_easting IS  NULL AND a.area_northing IS  NULL AND a.sample_number IS   NULL AND a.context_number IS  NULL)
        OR
        (b.area_easting IS  NULL AND b.area_northing IS  NULL AND b.sample_number IS  NULL AND b.context_number IS  NULL)


        """)
        count = cursor.fetchall()
        count = str(count).strip('[]').strip('()').strip(',')
        return count

@register.simple_tag
def count_new_gygaia_rows():
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT count(*)
        FROM samples.samples a
        LEFT JOIN kap.sample b
        --FULL OUTER JOIN kap.sample b
        ON a.area_easting = b.area_easting AND a.area_northing = b.area_northing AND a.sample_number = b.sample_number AND a.context_number = b.context_number
        WHERE
        (a.area_easting IS  NULL AND a.area_northing IS  NULL AND a.sample_number IS   NULL AND a.context_number IS  NULL)
        OR
        (b.area_easting IS  NULL AND b.area_northing IS  NULL AND b.sample_number IS  NULL AND b.context_number IS  NULL)


        """)
        count = cursor.fetchall()
        count = str(count).strip('[]').strip('()').strip(',')
        return count
