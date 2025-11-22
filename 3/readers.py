import openpyxl
from models import Person

def load_sheet(path):
    return openpyxl.load_workbook(path).active


def read_dvf(sheet):
    personer = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        pnr = str(row[2]).replace("-", "")  # Ta bort bindestreck, behåll som str
        personer[pnr] = {
            "namn": row[1],
            "personnummer": pnr,
            "epost": row[3],
            "mobil": row[4],
        }
    return personer


def read_hok(sheet):
    personer = {}
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if not row or len(row) < 5:
            continue

        namn, personnummer, typ, ras, djurnamn = row
        pnr = str(personnummer).replace("-", "")  # Normalisera till 10 siffror

        if pnr not in personer:
            personer[pnr] = Person(namn, pnr)

        personer[pnr].add_pet(typ, djurnamn, ras)

    return personer