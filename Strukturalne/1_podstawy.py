print("CDV")
print(10)
'''
komentarz
blokowy
'''
#potęgowanie
potega=2 **10
print(potega)

#pobieranie danych z klawiatury
name=input()
#+oznacza konkatenacje
print("Twoje imie to: "+name)
nazwisko=input()
print("Twoje imie to "+name+", nazwisko "+nazwisko)
'''
użytkownik podaje z klawiatury swój wiek z klawiatury,
wyświetl dane w formacie : Twoj wiek:... lat:...
'''
#end="" to zakończenie ciągiem pustym
print("Podaj swój wiek", end="")
age=input()
print(type(age))
print("Twój wiek ",age," lat")
age1=20
print(type(age1))
surname="Kowalski"
firstLetter=surname[0]
print(firstLetter)

lenght = len(surname)
print(lenght)

lastLetter=surname[len(surname)-1]
print(lastLetter)
