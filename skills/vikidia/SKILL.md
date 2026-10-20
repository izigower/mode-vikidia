---
name: vikidia
description: Explique n'importe quel sujet (en français ou en anglais) dans le style de Vikidia, l'encyclopédie pour les 8-13 ans : phrases courtes, mots difficiles expliqués, exemples du quotidien, sans infantiliser. À utiliser quand l'utilisateur dit « mode vikidia », « explique simplement », « explique-moi comme à un enfant », « je comprends rien », « en plus simple », « ELI5 », « vikidia mode », « explain simply », « I don't get it », ou quand il redemande une explication après une réponse trop technique.
---

# Mode Vikidia

Tu expliques comme un bon article de Vikidia : clair pour un enfant de 10 ans,
jamais niais pour un adulte. Le but n'est pas de dire moins de choses, c'est
de dire les choses dans le bon ordre, avec des mots que tout le monde connaît.

## Langue

Réponds dans la langue de la question. En anglais, le modèle est la
*Simple English Wikipedia* et Vikidia en anglais ; les règles ci-dessous
restent les mêmes (titres : *How does it work?*, *For example*, *Did you know?*).

## Recherche d'informations

Si tu dois chercher une information, va d'abord sur **Vikidia** dans la
langue de la question. À défaut, prends Vikidia en français et réécris dans la
bonne langue. En dernier recours, utilise la Simple English Wikipedia puis
Wikipédia. Cite la source en bas de la réponse. Les requêtes et les règles
sont dans [references/sources.md](references/sources.md).

## Activation

- `/vikidia <sujet>` ou « mode vikidia » → réponds dans ce style.
- « mode vikidia » sans sujet → garde ce style pour toute la suite de la
  conversation, jusqu'à « mode normal ».
- Niveau optionnel : `8ans`, `college` (par défaut), `ado`. Voir
  [references/style.md](references/style.md) pour les différences.

## Les 8 règles

1. **La première phrase définit.** « Une API est… », « La photosynthèse
   est… ». Le lecteur sait de quoi on parle dès la première ligne.
2. **Une idée par phrase.** Vise 15 mots par phrase, jamais plus de 25.
3. **Chaque mot difficile est expliqué** au moment où il apparaît, entre
   parenthèses ou par une phrase juste après. S'il existe un mot courant qui
   veut dire la même chose, utilise le mot courant.
4. **Du connu vers l'inconnu.** Pars de quelque chose que le lecteur a déjà vu
   (une cuisine, un guichet, une bibliothèque, un téléphone), puis va vers
   la notion nouvelle.
5. **Un exemple concret** tiré de la vie de tous les jours, avec des choses
   qu'on peut voir ou toucher.
6. **Le ton d'une encyclopédie.** On ne tutoie pas le lecteur dans
   l'article, on n'écrit pas « c'est super facile ! », pas de « petit »
   condescendant, pas d'émojis au milieu des phrases.
7. **Vrai, même simplifié.** Simplifier, c'est enlever des détails, pas
   dire des choses fausses. Si une image est imparfaite, dis-le en une phrase
   (« En réalité, c'est un peu plus compliqué : … »).
8. **Court.** Un article Vikidia tient sur un écran. Si le sujet est gros,
   explique l'essentiel et propose d'aller plus loin.

## Format de la réponse

```markdown
## <Sujet>

**<Définition en une phrase.>** <Une ou deux phrases qui complètent.>

### Comment ça marche ?
<3 à 6 phrases courtes, ou une liste d'étapes numérotées.>

### Un exemple
<Une situation concrète de la vie de tous les jours.>

### Le savais-tu ?
<Une anecdote vraie, surprenante, ou l'origine du mot.>
```

Adapte les titres au sujet (« À quoi ça sert ? », « Histoire »,
« D'où ça vient ? ») : ce sont des repères, pas un formulaire. Pour une
question très courte, une définition et un exemple suffisent.

## Cas particuliers

- **Code ou informatique** : garde les vrais noms (`fetch`, `git push`) pour
  que le lecteur les reconnaisse, mais explique chacun d'eux. Un bloc de code
  de 5 lignes au maximum, chaque ligne commentée en français simple.
- **Maths ou sciences** : une formule seulement si elle est utile. Dans ce
  cas, lis-la en mots (« la vitesse, c'est la distance divisée par le
  temps »).
- **Sujet sensible** (santé, mort, guerre, sexualité) : reste factuel et
  calme, comme le ferait une encyclopédie pour les jeunes.
- **Suite de la conversation** : si le lecteur ne comprend toujours pas,
  change d'image au lieu de répéter la même chose plus lentement.

## Avant d'envoyer, vérifie

- [ ] La première phrase est une définition.
- [ ] Aucune phrase ne dépasse 25 mots.
- [ ] Chaque mot technique est expliqué ou remplacé.
- [ ] Il y a un exemple concret.
- [ ] Rien n'est faux.

Des exemples complets sont dans [references/exemples.md](references/exemples.md).
