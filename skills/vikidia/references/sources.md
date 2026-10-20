# Chercher des infos : Vikidia d'abord

Quand tu dois vérifier ou compléter une explication avec une recherche,
commence par Vikidia : les articles sont déjà pensés pour être compris.

Les pages web de Vikidia refusent souvent les robots (erreur 403). Passe par
son API MediaWiki, qui répond sans problème.

## L'ordre de recherche

1. **Vikidia dans la langue de la question**, si `<langue>.vikidia.org`
   existe (fr, en, es, it, de, ca, eu, ru…).
2. **Vikidia en français**, l'édition la plus fournie. Lis la page, puis
   réécris l'explication dans la langue de la question. Ne traduis pas mot à
   mot, applique les règles du skill.
3. **Simple English Wikipedia** (`simple.wikipedia.org`), surtout pour une
   question en anglais.
4. **Wikipédia** dans la langue de la question, en dernier recours. Le texte
   sera difficile : c'est à toi de le simplifier.

Vikidia est une source pour enfants : elle peut manquer de détails ou être en
retard sur un sujet récent (technologie, actualité). Dans ce cas, vérifie les
faits sur Wikipédia et garde Vikidia pour le ton et les images.

## Les requêtes

Chercher un article (remplace `fr` par la langue) :

```
https://fr.vikidia.org/w/api.php?action=query&list=search&srsearch=<mots>&srlimit=3&format=json
```

Lire le texte d'un article et trouver ses équivalents dans les autres langues :

```
https://fr.vikidia.org/w/api.php?action=query&titles=<Titre>&prop=extracts|langlinks&explaintext=1&lllimit=50&format=json
```

Dans `langlinks`, `simple` désigne la Simple English Wikipedia et `wp`
Wikipédia. Une page qui n'a pas de lien vers une langue peut quand même
exister dans cette langue : fais une recherche directe pour vérifier.

## Citer

Le contenu de Vikidia est sous licence CC BY-SA. Reformule toujours avec tes
propres mots, ne recopie pas de paragraphes, et ajoute la source en bas de la
réponse :

```markdown
*Source : Vikidia, « Photosynthèse » (fr.vikidia.org/wiki/Photosynthèse)*
```
