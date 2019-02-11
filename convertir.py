# coding=UTF-8
import click
import markdown2

@click.command()
@click.option('-i',"--input-file","input_file", default='', help='chemin du fichier à convertir.')
@click.option("-o","--output-directory","output_directory", default='', help = 'Chemin du fichier de sortie')
# @click.option("-k", "--kikoolol", default = False, help = "")

def convertir (input_file, output_directory):
        ifile = input_file
        od = output_directory
        html_code_head = (
            '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Titre</title>\n</head>\n<body>\n'
        )
        html_code_foot = "</body>\n</html>"
       
        html = markdown2.markdown_path(ifile)

        html_code = html_code_head + html + html_code_foot
        page = open(od + "index.html", "w+", encoding="UTF-8").write(html_code)
# # Bonus kikoolol
#         if k == True:
#                 listkikoo = ["<p>Kikoo</p>", "<p>lol</p>", "<p>mdr</p>", "<p>ptdr</p>"]
#                 html.append(random.choice(listkikoo))
#         print(html)
if __name__ == '__main__':
        convertir()