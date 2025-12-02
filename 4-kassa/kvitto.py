
# ============================================================
# kvitto.py
def skriv_kvitto(korg):
    """Skriver ut kvitto"""
    print("\n" + "="*50)
    print("KVITTO".center(50))
    print("="*50)
    total = 0
    for vara in korg:
        summa = vara["pris"] * vara["antal"]
        total += summa
        print(f"{vara['namn']:20} {vara['antal']:3}st x {vara['pris']:8.2f} = {summa:10.2f}")
    print("-"*50)
    print(f"{'TOTALT':44} {total:10.2f}")
    print("="*50)

