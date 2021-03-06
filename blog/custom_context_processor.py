from blog.models import Entry
from tagging.models import Tag
import datetime, time

MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')

def archive(request):
    archive_data = []
    count = {}
    mcount = {}
    entries = Entry.objects.filter(status = 1)
    for entry in entries:
        year = entry.pub_date.year
        month = entry.pub_date.month
        if year not in count:
            count[year] = 1
            mcount[year] = {}
        else:
            count[year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.keys(), reverse=True):
        archive_data.append({'isyear': True,
                             'year': year, 
                             'count': count[year],})
        for month in sorted(mcount[year].keys(), reverse=True):
            archive_data.append({'isyear': False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[month], 
                                 'count': mcount[year][month],})
    return {'archive':archive_data}


def tag_cloud(request):
    MAX_WEIGHT = 5
    tag_list = Tag.objects.usage_for_model(Entry, counts = True)
    if tag_list:
        min_count = max_count = tag_list[0].count
        for tag in tag_list:
            # tag_count = tag.count
            if tag.count < min_count:
                min_count = tag.count
            if max_count < tag.count:
                max_count = tag.count
        range = float(max_count - min_count)
        if range == 0.0:
            range = 1.0
        for tag in tag_list:
            tag.weight = int(MAX_WEIGHT * (tag.count - min_count) / range)

    return {'tag_list':tag_list}