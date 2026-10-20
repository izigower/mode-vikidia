# Contribuer

## Ajouter une explication à la galerie

1. Pose ta question avec `/vikidia` (ou le prompt universel).
2. Mesure la réponse : `python3 evals/lisibilite.py reponse.txt`.
3. Crée `galerie/<sujet>.md` en copiant [galerie/api.md](galerie/api.md).
4. Ouvre une PR intitulée `galerie: <sujet>`.

Une explication entre dans la galerie si :

- son score dépasse 65 ;
- elle est **juste** (une erreur suffit pour la refuser, même si c'est joli) ;
- un enfant de 10 ans pourrait la lire à voix haute sans buter.

## Améliorer le skill

Ouvre d'abord une issue avec un **avant/après** : la réponse actuelle et
celle que tu voudrais. Les règles changent seulement si l'exemple convainc.

## Autres langues

Une version anglaise pourrait s'inspirer de la *Simple English Wikipedia*.
Crée `skills/simple-en/` et ouvre une PR.
