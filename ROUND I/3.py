from datetime import datetime, timedelta

def compute_prev_date(dates_list):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    backdates = []
    for date in dates_list:
        change = datetime.strptime(date, '%Y-%m-%d')
        backdate = (change - timedelta(days=1)).strftime('%d %b %Y')
        backdates.append(backdate)
    return backdates 
print(compute_prev_date(['2022-11-01', '2022-11-02']))