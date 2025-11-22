# Labb 2 – Lösenordskollaren

## Översikt

 **Description**
 Den läser vanliga dåliga lösenord från passwords.txt (som "admin", "password", "test" osv.) och skapar sedan alla möjliga varianter av dessa ord:

*"admin" → "Admin", "aDmin", "adMin", "ADmin", "2admin", "admin3", "Ad+min" osv.
 "password" → "Password", "pAssword", "PA ssword", "0password", "password7" osv.*

 Den sparar alla dessa varianter i all_passwords.txt.
 Poängen: Hackare vet att folk ofta tar vanliga ord (som "admin") och bara lägger till en siffra eller stor bokstav (som "Admin123"). Så programmet skapar alla sådana "förutsägbara" varianter.


### Kurs
DD1321

### Skapare
Rasmus Mattsson

### Datum
2025-11-21


## Filer

### password_generator.py
Program som genererar olika lösenordsvarianter med stora bokstäver och inskjutna specialtecken/siffror

### password_checker.py
Program som kollar om ett lösenord är säkert genom att jämföra med en lista av dåliga lösenordsvarianter


## Commands

### Create password variations
```
python3 password_generator.py
```

### Check common passwords
```
python3 password_checker "Your password"
```


