#modules
from random import choice
from simple_colors import green, red, blue, yellow

#database
words = ["godina", "slova", "pjetao", "kuhinja", "lampa", "osoba", "konzola", "ulica", "dvor", "hodnik", "kabina",
         "monitor", "apartman", "prostor", "rublje", "voda", "ovan", "otok", "paun", "konj", "patka", "sablja",
         "gumica", "boja", "cvijet", "prozor", "sjemenke", "ormar", "stol", "olovka", "karta", "papir", "mobitel"]


def pre_game():
    word = ''.join(choice(words))
    word = [*word]
    placeholder = ''.join('_' for _ in range(len(word)))
    print(placeholder)
    placeholder = list(placeholder)
    numerator = ''.join(str(i) for i in range(1, len(word)+1))
    print(numerator)
    return game_on(word, placeholder, numerator)


def game_on(word, placeholder, numerator):
    broj_pogresaka = 0
    while broj_pogresaka < 8:
        lista_unosa = []
        unos = str(input("Unesite slovo: "))
        #provjera ako je unos vec iskoristen
        if unos in lista_unosa or len(unos) != 1:
            print(f'{yellow("Uneseni znak nije valjan ili je već iskorišten!")}')
        else:
            lista_unosa.append(unos)
            #ako unos nije iskoristen
            if unos in word:
                for i in range(len(word)):
                    if word[i] == unos:
                        placeholder[i] = unos

            else:
                broj_pogresaka += 1
                print(f'slovo {green(unos)} se ne nalazi u zadanoj rijeci.')

            print(f'{"".join(placeholder)}\n{numerator}')
            if placeholder.count("_") == 0 or broj_pogresaka == 7:
                return post_game(placeholder)


def post_game(placeholder):
    br_preostalih_slova = placeholder.count("_")
    if br_preostalih_slova == 0:
        print(f'{blue("Čestitamo!")} Pogodili ste traženu riječ.')
    elif br_preostalih_slova < 3:
        print("Skoro! Više sreće drugi put.")
    else:
        print("Ha ha. Nebi ja bia loš")
    print(f'Kako bi igrali ponovno pritisnite {green("<Enter>")}')
    print(f'Za izlaz iz igre prisitnite {green("<q>")}')
    user_confirmation = ' '
    while user_confirmation != '' or user_confirmation != 'q':
        user_confirmation = input(": ")
        if user_confirmation == 'q':
            #print(f'Odigrali ste {broj_odigranih_partija}partija od kojih ste pobjedili {broj_pobjeda}')
            quit()
        elif user_confirmation == '':
            pre_game()
        else:
            print("Uneseni znak nije prepoznat, pokusajte ponovo.")


def main():
    #starting screen and game info
    print("".center(43, "-"))
    print("Vješala".center(43, "-"))
    print("".center(43, "-"), "\nPravila:")
    print(f'1.Za svaku riječ imate {red("7")} pokušaja.\n2.Sva unesena slova moraju biti {red("mala")} slova.')
    print("".center(43, "-"))
    input(f'Za početak igre pritisnite {green("<Enter>")}: ')
    pre_game()


main()
