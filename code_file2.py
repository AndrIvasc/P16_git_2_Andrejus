import logging

# Šioms užduotims nebūtina kurti advanced loggerių su handleriais.
# Kurkime tik atlikus laikui, o pradžioje naudokime basicConig.
# 1 užduotis. išsibandyti bent 3 lygių logginimą, kodą kuriame naudosim
# pasirenkam patys ir pagal savo įsivaizdavimą sudedam reikiamo
# lygio log žinutes.

logger = logging.getLogger()  # sukuriamas logerio objektas

# objektas darbui su zurnalo failu

file_handler = logging.FileHandler("log_file.log",
                                   encoding="utf-8")

# objektas darbui su terminalu
stream_handler = logging.StreamHandler()

# nustatom zinuciu formata per spec objekta
formatter = logging.Formatter("Not a Thread id is %(thread)d and the path name of the log %(pathname)s ||\n"
                              "You can find it in this module -> %(module)s ||\n"
                              "The numeric loging level for mes is ->>> %(levelno)s and its %(levelname)s ||\n"
                              "The message is %(message)s"
                              "\n")

# nustatom formatus handleriam
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# prijungiam handlerius prie pagr logger objekto
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# zinuciu lygis bendras
logger.setLevel(logging.DEBUG)
# lygis konkreciai rasymui i faila
file_handler.setLevel(logging.DEBUG)


def gauk_sumas_a(*args):
    logger.debug("Starting gauk_sumas_a function with arguments: %s", args)
    even_sum = 0
    odd_sum = 0

    for nr in args:
        if nr % 2 == 0:
            even_sum += nr
        else:
            odd_sum += nr

    logger.info("Even sum: %d, Odd sum: %d", even_sum, odd_sum)
    return even_sum, odd_sum


logger.debug("Calling gauk_sumas_a with test values (1, 1)")
print(gauk_sumas_a(1, 1))



def filtruok_stringus_b(*args, lt=False):
    logger.debug("Starting filtruok_stringus_b function with arguments: %s, lt=%s", args, lt)
    english_vowels = "aeiouAEIOU"
    lithuanian_vowels = "AaĄąEeĘęĖėIiĮįYyOoUuŲųŪū"

    vowels = lithuanian_vowels if lt else english_vowels
    result = [string for string in args if string[0] in vowels]

    if not result:
        logger.warning("No strings found that start with vowels for the given arguments: %s", args)
    elif len(result) < len(args):
        logger.warning("Some strings did not start with vowels: %s", set(args) - set(result))

    logger.info("Filtered strings: %s", result)
    return result


logger.debug("Calling filtruok_stringus_b with test values and lt=True")
print(filtruok_stringus_b("Ąžuolas", "mėsa", "Mes", "obuolis", "Oras", lt=True))

def check_autonrs_a(*autonrs):
    logger.debug("Starting check_autonrs_a function with arguments: %s", autonrs)
    valid_autonrs = []

    for auto_nr in autonrs:
        if len(auto_nr) == 6 and auto_nr[:3].isalpha() and auto_nr[:3].isupper() and auto_nr[3:].isdigit():
            valid_autonrs.append(auto_nr)
            logger.info("Valid auto number found: %s", auto_nr)
        elif len(auto_nr) == 6 and auto_nr[0] == "E" and auto_nr[1].isalpha() and auto_nr[1].isupper() and auto_nr[2:].isdigit():
            valid_autonrs.append(auto_nr)
            logger.info("Valid 'E' auto number found: %s", auto_nr)
        else:
            logger.critical("Invalid auto number encountered: %s", auto_nr)

    if not valid_autonrs:
        logger.critical("No valid auto numbers were found in the input!")

    return valid_autonrs

print(check_autonrs_a("ABC123", "FE9911", "Ea2456", "Bd2222", "EB9999", "DDD999"))
