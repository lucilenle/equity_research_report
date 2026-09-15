# Portfolio — Equity research Pandora A/S

Site statique d'une page présentant une note d'analyste et un modèle de valorisation
sur Pandora A/S (Nasdaq Copenhague, PNDORA).

Lucile Engelaere, Master 1 CCA, IAE Lyon.

## Contenu

```
index.html                                 la page (CSS et JS inclus, aucune dépendance à installer)
assets/Pandora_Equity_Research_Note.pdf    note d'analyste, 6 pages
assets/Pandora_Equity_Research_Model.xlsx  modèle Excel, 9 onglets
.nojekyll                                  désactive le traitement Jekyll de GitHub Pages
```

## Mettre en ligne sur GitHub Pages

1. Créer un compte sur github.com si ce n'est pas déjà fait.
2. Créer un dépôt public nommé `equity-research-pandora`.
3. Téléverser le contenu de ce dossier à la racine du dépôt.
   Par l'interface web : bouton « Add file », puis « Upload files », glisser les
   fichiers et le dossier `assets`, puis « Commit changes ».
   En ligne de commande :

   ```bash
   git init
   git add .
   git commit -m "Portfolio equity research Pandora"
   git branch -M main
   git remote add origin https://github.com/VOTRE-PSEUDO/equity-research-pandora.git
   git push -u origin main
   ```

4. Dans le dépôt : onglet **Settings**, rubrique **Pages**.
   Sous « Build and deployment », choisir **Deploy from a branch**,
   branche `main`, dossier `/ (root)`, puis **Save**.
5. Attendre une à deux minutes. L'adresse sera :
   `https://VOTRE-PSEUDO.github.io/equity-research-pandora/`

## Avant de publier

- Remplacer l'adresse e-mail et le lien LinkedIn dans le pied de page d'`index.html`
  (chercher `VOTRE.EMAIL@exemple.fr`).
- Vérifier le cours de bourse de référence si la publication a lieu longtemps après
  la rédaction, et regénérer les fichiers si besoin.

## QR code

La page génère elle-même un QR code pointant vers sa propre adresse, visible en bas
de page. Rien à configurer.

Pour une version imprimable en haute définition (CV, affiche), utiliser le script
`make_qr.py` fourni à côté de ce dossier :

```bash
python3 make_qr.py https://VOTRE-PSEUDO.github.io/equity-research-pandora/
```

Il produit `qr-portfolio.svg` (vectoriel, idéal pour l'impression) et `qr-portfolio.png`.
