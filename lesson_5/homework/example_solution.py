import sys
import random
import string


def check_if_help(args):
    help_text = "Jedinym pouzitelnym parametrem je tento prikaz 'help',"\
                "vsechny ostatni parametry jsou interaktivne vyplnovany uzivatelem na pozadani." \
                "Pokud se ocekava ciselny parametr, je mozne zadat i 0 (ale ne prazdny retezec)."
    try:
        if args[0] == 'help':
            print(help_text)
            sys.exit(0)
    except IndexError:
        return # Pokud chybi parametr, nechci delat nic

    # Stejne tak by toto slo osetrit podminkou na delku argumentu
    # bud osetrime vstup predtim nez s nim chceme neco delat - podminka,
    # nebo az potom co vime ze je neco spatne - vyjimka

def get_user_information():
    print('Registrace do knihovny')
    print('Krok 1: Vyplneni osobnich informaci')
    user = {}
    user['name'] = input('Zadej uzivatelske jmeno: ')
    user['email'] = input('Zadej email pro registraci: ')

    if '@' not in user['email']:
        print('[ERROR] Neplatny format emailu (musi obsahovat zavinac)!')
        exit(1)

    day, month, year = input('Zadej datum narozeni v dd/mm/yyyy formatu: ').split('/')
    user['birth_date'] = {'day': day, 'month': month, 'year': year}
    # Pripadne vice informaci ...
    return user

def get_password_parameters():
    print('Krok 2: Zadani parametru hesla')
    params = {}
    try:
        params['length'] = int(input('Zadej pozadovanou delku hesla: '))
        params['no_numbers'] = int(input('Zadej pozadovany pocet cisel: '))
        params['no_uppercase_letters'] = int(input('Zadej pozadovany pocet velkych pismen: '))
        params['no_lowercase_letters'] = int(input('Zadej pozadovany pocet malych pismen: '))
        params['no_special_chars'] = int(input(f'Zadej pozadovany pocet specialnich znaku ({string.punctuation}): '))
        pet_name = input('Zadej jmeno mazlicka, ktere bude obsazeno v hesle nebo prazdny retezec (zmackni enter): ')
        params['pet_name'] = pet_name
    except ValueError:
        print('[ERROR] Hodnota zadana ve spatnem formatu!')
        exit(1)

    sum_of_required_chars = params['no_uppercase_letters'] + \
                            params['no_lowercase_letters'] + \
                            params['no_special_chars'] + \
                            params['no_numbers'] + \
                            len(params['pet_name'])
    if  sum_of_required_chars > params['length']:
        print(f'[ERROR] Pozadavky na pocet znaku ({sum_of_required_chars}) presahuji celkovou pozadovanou delku ({params["length"]}) hesla!')
        exit(1)
    else:
        params['no_random_chars_to_generate'] = params['length'] - sum_of_required_chars

    return params

def check_params_for_personal_info(password_params, user_info):
    print('Krok 3: Kontroluji zda parametry hesla neobsahuji osobni udaje ...')

    # Tady zalezi jake berete osobni udaje a jake parametry pro heslo
    # Ja u pouze kontroluji ze jmeno mazlicka neni stejne jako username, ale obdobne by se pridali dalsi kontroly
    if password_params['pet_name'] == user_info['name']:
        print('[ERROR] Jmeno mazlicka nemuze byt stejne jako username!')
        exit(1)

def generate_password(pwd_params):
    print('Krok 4: Generuji heslo ...')
    password = ''

    # misto metody join jde pro vytvoreni stringu pouzit i for cyklus
    # string = ''
    # for num in list:
    #     string += str(num)
    password += "".join(random.choices(string.ascii_uppercase, k=pwd_params['no_uppercase_letters']))
    password += "".join(random.choices(string.ascii_lowercase, k=pwd_params['no_lowercase_letters']))
    password += "".join(random.choices(string.punctuation, k=pwd_params['no_special_chars']))
    password += "".join(random.choices(string.digits, k=pwd_params['no_numbers']))
    # Zbyvajici znaky do chybejici delky
    password += "".join(random.choices(string.digits + string.ascii_letters, k=pwd_params['no_random_chars_to_generate']))

    # Zamichame pred vlozenim mazlicka
    password_char_list = list(password)
    random.shuffle(password_char_list)
    password = "".join(password_char_list)

    # Vlozeni jmena mazlicka na nahodne misto
    # -1 protoze indexujeme od 0 a pocitame s delkou
    pet_name_len = len(pwd_params['pet_name'])
    max_index_of_pet_name_start = pwd_params['length'] - pet_name_len - 1
    index_to_insert_pet_name = random.randint(0, max_index_of_pet_name_start)
    password = password[:index_to_insert_pet_name] + pwd_params['pet_name'] + password[index_to_insert_pet_name:]

    return password

def make_registration():
    user_info = get_user_information()
    pwd_params = get_password_parameters()
    check_params_for_personal_info(pwd_params, user_info)
    user_info['password'] = generate_password(pwd_params)
    return user_info


check_if_help(sys.argv[1:])
user = make_registration()
print(user)

# NOTES:
# misto input funkci pro parametry bzchom mohli pouzit vice parametru prikazove radky, ja jsem pouzila parameter pouze pro napovedu
# uzivatele bychom mohli reprezentovat také jako objek třídy User místo slovníku

