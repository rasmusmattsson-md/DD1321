import datetime

def full_personnummer(pnr):
    pnr = str(pnr).replace("-", "")
    y = int(pnr[:2])
    m = int(pnr[2:4])
    d = int(pnr[4:6])
    
    today = datetime.date.today()
    current_y = today.year % 100
    
    # Determine century
    if y < current_y:
        century = 2000
    elif y > current_y:
        century = 1900
    else:  # Same year – check month/day
        if m < today.month or (m == today.month and d <= today.day):
            century = 2000
        else:
            century = 1900
    
    return str(century + y) + pnr[2:]


def calc_age(pnr):
    pnr = str(pnr).replace("-", "")
    y = int(pnr[:2])
    m = int(pnr[2:4])
    d = int(pnr[4:6])
    
    today = datetime.date.today()
    current_y = today.year % 100
    
    # Determine century
    if y < current_y:
        century = 2000
    elif y > current_y:
        century = 1900
    else:
        if m < today.month or (m == today.month and d <= today.day):
            century = 2000
        else:
            century = 1900
    
    birth_year = century + y
    age = today.year - birth_year
    
    # Change birthday hasn't occurred yet this year
    if today.month < m or (today.month == m and today.day < d):
        age -= 1
    
    return age


def merge(hok, dvf):
    for pnr, person in hok.items():
        full = full_personnummer(pnr)
        if full in dvf:
            info = dvf[full]
            person.email = info["email"]
            person.mobile = info["mobile"]

        person.age = calc_age(pnr)
