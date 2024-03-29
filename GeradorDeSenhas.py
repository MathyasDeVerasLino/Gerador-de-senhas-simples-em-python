import string
import random

                            # VARIAVEIS

Preference = input("prefere com ou sem caracteres especiais? ").lower()
PassWordSize = int(input("por favor, digite o tamanho de senha desejado: "))

                            # FUNCTIONS

def SpecialPassword(size = PassWordSize):
    WithSpecialCharacters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(WithSpecialCharacters) for _ in range(PassWordSize))

def OnlyNumbersPassword(size = PassWordSize):
    return "".join(random.choice(string.digits) for _ in range(PassWordSize))

                        ######MAIN CODE######

if Preference == "com":
   print("senha gerada: ", SpecialPassword())

elif Preference == "sem":
    print("senha gerada: ", OnlyNumbersPassword())
else:
    print("por favor, voce precisa digitar um valor valido(com ou sem.).")

