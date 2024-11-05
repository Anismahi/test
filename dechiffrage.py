
message_chiffré=input('entrez votre message à déchiifrer:')


liste=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for x in range(len(liste)):
    liste.append(liste[x])

def chiffrage_lettre(lettre,liste,clef):
    for i in range(len(liste)):
        if lettre==' ':
            return ' '
        elif liste[i]==lettre:
            return str(liste[i+clef])
    return '?'

for clef in range (1,26):
    message_déchiffré=str()
    for lettre in message_chiffré:
        message_déchiffré+=chiffrage_lettre(lettre,liste,clef)
    print(message_déchiffré)
    
a=input()
