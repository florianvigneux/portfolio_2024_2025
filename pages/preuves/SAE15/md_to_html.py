import markdown

def convert(md_file: str, html_file: str) -> None:
    """
    Convertit un fichier Markdown en fichier HTML valide.
    """
    with open(md_file, 'r') as md:
        md_content = md.read()
        
    html_converti = markdown.markdown(md_content)
    html_converti = html_converti.replace("\n", "<br>\n")

    with open(html_file, 'w') as html:
        html.write("<!DOCTYPE html>\n")
        html.write("<html lang='fr'>\n")
        html.write("<head>\n")
        html.write("<meta charset='UTF-8'>\n")
        html.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        html.write("<title>Fiche Pokémon</title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write(html_converti)
        html.write("</body>\n")
        html.write("</html>\n")