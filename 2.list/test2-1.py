months=[
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]

endings = ['st', 'nd', 'rd']+17*['th']+17*['th']+['st', 'nd', 'rd']+7*['th']

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

month_num = int(month)
day_num = int(day)

month_name = months[month_num-1]
ordinal = day + endings[day_num-1]

print month_name+' '+ordinal+'.'+year
