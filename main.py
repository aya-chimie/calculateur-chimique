
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def accueil():
    return """
    <html>
    <head>
        <title>Calculateur chimique</title>
    </head>
    <body>
        <h1>Calcul de la quantite de matiere</h1>

        <form action="/calculer" method="post">

            <label>Choisir la methode :</label>

            <select name="methode">
                <option value="masse">A partir de la masse</option>
                <option value="concentration">A partir de la concentration</option>
                <option value="entites">A partir du nombre d'entites</option>
            </select>

            <br><br>

            <label>Masse (g) :</label>
            <input type="number" step="any" name="masse">

            <br><br>

            <label>Masse molaire (g/mol) :</label>
            <input type="number" step="any" name="molaire">

            <br><br>

            <label>Concentration (mol/L) :</label>
            <input type="number" step="any" name="concentration">

            <br><br>

            <label>Volume (L) :</label>
            <input type="number" step="any" name="volume">

            <br><br>

            <label>Nombre d'entites :</label>
            <input type="number" step="any" name="entites">

            <br><br>

            <button type="submit">Calculer</button>
        </form>
    </body>
    </html>
    """


@app.post("/calculer", response_class=HTMLResponse)
def calculer(
    methode: str = Form(...),
    masse: str = Form(""),
    molaire: str = Form(""),
    concentration: str = Form(""),
    volume: str = Form(""),
    entites: str = Form("")
):

    NA = 6.022e23

    try:
        if methode == "masse":

            m = float(masse.replace(",", "."))
            M = float(molaire.replace(",", "."))

            if m < 0 or M <= 0:
                resultat = "Valeurs invalides"
            else:
                n = m / M
                resultat = f"{n:.6g} mol"

        elif methode == "concentration":

            C = float(concentration.replace(",", "."))
            V = float(volume.replace(",", "."))

            if C < 0 or V < 0:
                resultat = "Valeurs invalides"
            else:
                n = C * V
                resultat = f"{n:.6g} mol"

        elif methode == "entites":

            N = float(entites.replace(",", "."))

            if N < 0:
                resultat = "Valeurs invalides"
            else:
                n = N / NA
                resultat = f"{n:.6e} mol"

        else:
            resultat = "Methode invalide"

    except ValueError:
        resultat = "Veuillez remplir les champs necessaires correctement"

    return f"""
    <html>
    <body>
        <h1>Resultat du calcul</h1>
        <h2>Quantite de matiere : {resultat}</h2>
        <a href="/">Retour a l'accueil</a>
    </body>
    </html>
    """
