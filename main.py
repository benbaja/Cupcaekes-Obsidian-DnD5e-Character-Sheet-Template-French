import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from bs4 import BeautifulSoup
    import requests

    return BeautifulSoup, requests


@app.cell
def _(BeautifulSoup):
    # liste de sorts
    spell_names = []
    with open("spell-list.xml", "r") as f:
        spell_names_soup = BeautifulSoup(f, features="xml")
    for spell_name in spell_names_soup.find_all('spell'):
        spell_names.append(spell_name.get_text())
    return (spell_names,)


@app.cell
def _(BeautifulSoup, requests, spell_names):
    # telecharge chaque fiche de sort au format HTML
    url_template = "https://www.aidedd.org/dnd/sorts.php?vf="
    r = requests.get(url_template+spell_names[0])
    spell_soup = BeautifulSoup(r.text, features="html5lib")
    return (spell_soup,)


@app.cell
def _(spell_soup):
    full_name = spell_soup.find("h1").text
    return


@app.cell
def _():
    return


@app.cell
def _():
    # extrait les métadonnées
    sorts_dict = {}
    return


@app.cell
def _():
    # sauvegarde au format markdown
    return


if __name__ == "__main__":
    app.run()
