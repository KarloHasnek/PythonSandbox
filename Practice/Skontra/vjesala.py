class ANSI():
	def background(code):
		return "\33[{code}m".format(code=code)

	def style_text(code):
		return "\33[{code}m".format(code=code)

	def color_text(code):
		return "\33[{code}m".format(code=code)



s1 = ANSI.background(
	90) + ANSI.color_text(36) + ANSI.style_text(8) + "Program zadaje nepoznatu riječ." \
         "\nIgrač pogađa zadanu riječ utipkavanjem pojedinačnih" \
         "\nmalih slova hrvatske abecede." \
         "\n\nIgra se moze ponoviti najviše 4 puta" \
         "\njer program ima toliko nepoznatih riječi."\
        "\nBroj pokušaja jednak je broju slova u riječi puta 2."
print(s1)

lista = ["bubreg","lav","palindrom","mobitel"] ##naša lista

def randomiremove(l): ##funkcija koja uzima jednu random stvar iz naše liste, te istu stvar remove-a
    from random import choice
    nepoznata_rijec = choice(l)
    l.remove(nepoznata_rijec)
    return nepoznata_rijec

def s2(x,y): ##dio teksta koji se ponavlja svakim početkom nove igre
    return f"\n\n--------------------{x}.IGRA--------------------"\
    f"\n\nDopušta se najviše {y} pokušaja pogađanja slova"\
    "\n,te sva slova su mala"

def provjera(slovo,rijec,prazna_rijec): ##provjerava postoji li naše uneseno slovo u našoj riječi te vraća praznu riječ
    for i in range(len(rijec)):
        if slovo is rijec[i]:
            prazna_rijec[i] = slovo
    return ''.join(prazna_rijec)

def main(x,brojigre):
    prazna_rijec = ["_" for i in range(len(x))]
    pokusaj = 1
    broj_pokusaja = (len(x))*2
    print(s2(brojigre,broj_pokusaja))
    while pokusaj<=broj_pokusaja:
        unos = str(input("Unesi malo slovo: "))
        print(provjera(unos,x,prazna_rijec))
        pokusaj += 1
        if provjera(unos,x,prazna_rijec) == x:
            print("\nČestitam riječ uspiješno pogođena!")
            break
    else:
        print(f"Riječ je bila \"{x}\". Više sreće drugi put :(")
igra = 1
while len(lista) > 0:
    randomvarijabla = input("\nPRITISNI ENTER ZA NOVU IGRU")
    main(randomiremove(lista),igra)
    igra += 1

print("\nPotrosili ste sve riječi,za novu igru stisnite ctrl+alt+del.")