from readers import load_sheet, read_dvf, read_hok
from utils import merge
from writers import write_species

def main():
    dvf = read_dvf(load_sheet("DVF.xlsx"))
    hok = read_hok(load_sheet("HoK.xlsx"))

    merge(hok, dvf)

    write_species(hok, "hund", "hundmänniskor.xlsx")
    write_species(hok, "katt", "kattmänniskor.xlsx")

if __name__ == "__main__":
    main()