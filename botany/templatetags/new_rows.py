from django import template
# from django.contrib.auth.models import Group
import datetime

from django.db import connection

register = template.Library()

# @register.filter(name='has_group')
# def has_group(user, group_name):
#     group =  Group.objects.get(name=group_name)
#     return group in user.groups.all()

@register.simple_tag
def count_new_rows():
    # return datetime.datetime.now()
# def count_new_rows():
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


@register.simple_tag
def update_new_rows():
    # return datetime.datetime.now()
# def count_new_rows():
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO kap.sample
(area_easting, area_northing, context_number, sample_number, sample_type, weight, description, recovery_method )
(
	SELECT
	--b.area_easting AS "NEW easting", b.area_northing AS "NEW northing", b.sample_number AS "NEW sample", b.context_number AS "NEW context",
	a.area_easting, a.area_northing, a.context_number, a.sample_number,
	a.material, a.weight_kilograms, a.sample_description, a.recovery_type

FROM samples.samples a
--FULL OUTER JOIN kap.sample b
LEFT JOIN kap.sample b
	ON a.area_easting = b.area_easting AND a.area_northing = b.area_northing AND a.sample_number = b.sample_number AND a.context_number = b.context_number
WHERE
(a.area_easting IS  NULL AND a.area_northing IS  NULL AND a.sample_number IS   NULL AND a.context_number IS  NULL)
OR
(b.area_easting IS  NULL AND b.area_northing IS  NULL AND b.sample_number IS  NULL AND b.context_number IS  NULL)

)

        """)
        # count = cursor.fetchall()
        # return count
