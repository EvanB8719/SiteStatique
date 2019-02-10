import click
import markdown2

@click.command()
@click.option('-i', help='chemin du fichier à convertir.')
@click.option('-i')
@click.option("-k", "--kikoolol", default = False, help = "Si c'est vrai ajouter un mot kikoo")
@click.option("-a", help="le dossier contenant des modèles de pages web à compléter", action="store_true")

def convertir (chemin):
    f = open(chemin, 'r', encoding='utf-8')
    text2 = f.readlines()
    f.close()
    i = 0
    for text1 in text2 :
        markdown = text2 [i]
        markdown = markdown.lstrip()
        html = markdown2.markdown(md)
        i += 1

# Bonus kikoolol
        if kikoolol == True:
                listkikoo = ["<p>Kikoo</p>", "<p>lol</p>", "<p>mdr</p>", "<p>ptdr</p>"]
                html.append(random.choice(listkikoo))
        print(html)
# Bonus allemand
        TextAV = open("bonus/Texte_Normal.txt", "r")
        TextNO = TextAV.read()
        print (TextNO)

        TextAP = open("bonus/Texte_Allemand.txt", "w")

        Remplacement_des_lettres = TextNO.replace("ss", "z").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "")
        print(Remplacement_des_lettres)

        TextAP.write(Remplacement_des_lettres)

        TextAV.close()
        TextAP.close()

    if __name__ == '__main__':

        convertir()