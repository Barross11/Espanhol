print("Vamos te ajudar a conjulgar alguns verbos :)")
def main():
    while True:
        verbo = input("Me diga o seu verbo no infinitivo> ").lower()
        tamanho_verbo = len(verbo)
        posicao = verbo.find("r")+1
        if posicao <= 0:
            print(">> Você precisa colocar um verbo no infinitivo")
            continue
        elif posicao == tamanho_verbo:
            irregulares = ['tener', 'venir', 'caber']
            if verbo in irregulares and verbo[-2:] == 'ar':
                verbo = verbo.replace('ar', 'dr')
            elif verbo in irregulares and verbo[-2:] == 'er':
               verbo = verbo.replace('er', 'dr')
            elif verbo in irregulares and verbo[-2:] == 'ir':
                 verbo = verbo.replace('ir', 'dr')
            opções = ["yo", "tu", "él", "ella", "usted", "nosotros", "nosotras", "vosotros", "ellas", "ellos", "ustedes"]
            print(f"Essas sãs as suas opções de sujeitos ------ {opções}")
            if posicao > 0 and posicao == tamanho_verbo:
                sujeito = input("Me diga o sujeito> ").lower()
                if sujeito == "yo":
                    print(f"{sujeito} {verbo}é")
                elif sujeito == "tu":
                    print(f"{sujeito} {verbo}ás")
                elif sujeito == "él" or sujeito == "ella" or sujeito == "usted" or sujeito == "el":
                    print(f"{sujeito} {verbo}á")
                elif sujeito == "nosotros" or sujeito == "nosotras":
                    print(f"{sujeito} {verbo}emos")
                elif sujeito == "vosotros":
                    print(f"{sujeito} {verbo}éis")
                elif sujeito == "ellos" or sujeito == "ellas" or sujeito == "ustedes":
                    print(f"{sujeito} {verbo}án")
                else:
                    print("Algum erro aconteceu :(")
                break
        else:
            print(">> Você precisa colocar um verbo no infinitivo")
if __name__ == "__main__":
    main()
