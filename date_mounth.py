from datetime import datetime


def mounth_(date):
    mon = {'январ': 'jan', 'феврал': 'feb', 'март': 'mar', 'апрел': 'apr', 'ма': 'may',
           'июн': 'jun', 'июл': 'jul', 'август': 'aug', 'сентябр': 'sep', 'октябр': 'oct', 'ноябр': 'nov',
           'декабр': 'dec'}
    date.lower()
    date_ = date.split()
    if date_[0] == 'сегодня':
        da = 0
    elif date_[0] == 'вчера':
        da = 1
    else:
        day = date_[0]
        date_ = date_[1][:-1]
        m = mon[date_]
        datee = day+' '+m+' '+str(datetime.today().year)
        d = datetime.strptime(datee, '%d %b %Y')
        da = int((datetime.now() - d).days)
    return da




# date = '23 Июля'
# x = mounth_(date)
# print(x)