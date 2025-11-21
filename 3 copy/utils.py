import datetime

def full_personnummer(pnr):
    y = int(pnr[:2])
    current_y = int(datetime.date.today().strftime("%y"))
    century = 2000 if y <= current_y else 1900
    return int(str(century + y) + pnr.replace("-", ""))


def calc_age(pnr):
    y = int(pnr[:2])
    current_y = int(datetime.date.today().strftime("%y"))
    century = 2000 if y <= current_y else 1900
    birth_year = century + y
    return datetime.date.today().year - birth_year


def merge(hok, dvf):
    for pnr, person in hok.items():
        full = full_personnummer(pnr)
        if full in dvf:
            info = dvf[full]
            person.epost = info["epost"]
            person.mobil = info["mobil"]

        person.ålder = calc_age(pnr)
