import click
import markdown2

@click.command()
@click.option('-i', help='chemin du fichier à convertir.')
@click.option("-o", help = 'Chemin du fichier de sortie')
# @click.option("-k", "--kikoolol", default = False, help = "Si c'est vrai ajouter un mot kikoo")

def convertir (i, o):

    f = open(i, 'r', encoding='utf-8')
    text2 = f.readlines()
    f.close()
    i = 0

    for text1 in text2 :

        markdown = text2 [i]
        markdown = markdown.lstrip()
        html = markdown2.markdown(markdown)
        i += 1
        page = open(o)

# # Bonus kikoolol
#         if k == True:
#                 listkikoo = ["<p>Kikoo</p>", "<p>lol</p>", "<p>mdr</p>", "<p>ptdr</p>"]
#                 html.append(random.choice(listkikoo))
#         print(html)
    if __name__ == '__main__':

        convertir()