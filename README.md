<div align="center">

# mode-vikidia

**Ton IA t'explique tout comme un article de Vikidia :<br>des phrases courtes, des mots expliqués, des exemples de la vraie vie.**

<img src="demo/demo.gif" alt="Avant / après : la même question posée sans puis avec /vikidia" width="880">

<sub>Même question, même IA. Lisibilité mesurée avec <a href="evals/lisibilite.py">la formule de Kandel et Moles</a> : 26 → 72 sur 100.</sub>

</div>

---

## Pourquoi ?

Les IA répondent comme Wikipédia : c'est juste, mais souvent illisible quand
on découvre un sujet. [Vikidia](https://fr.vikidia.org), l'encyclopédie des
8-13 ans, prouve qu'on peut tout expliquer clairement **sans parler comme à
un bébé**. Ce skill apprend ce style à ton IA.

## Installation

### Claude Code (2 commandes)

```
/plugin marketplace add izigower/mode-vikidia
/plugin install mode-vikidia@mode-vikidia
```

Ou à la main : copie `skills/vikidia/` dans `~/.claude/skills/`.

### Claude.ai

Paramètres → Capacités → Skills → importer le dossier `skills/vikidia` en zip.

### ChatGPT, Le Chat, Gemini…

Copie [prompts/universel.md](prompts/universel.md) dans les instructions
personnalisées, ou au début d'une conversation.

## Utilisation

| Tu écris | Il se passe |
|---|---|
| `/vikidia c'est quoi une API ?` | une réponse dans le style Vikidia |
| `mode vikidia` | toute la suite de la conversation en mode Vikidia |
| `mode normal` | retour aux réponses habituelles |
| `/vikidia 8ans la photosynthèse` | encore plus simple |
| `/vikidia ado la blockchain` | un peu plus technique |
| « je comprends rien » | le skill se déclenche tout seul |

## Les 8 règles

1. La première phrase **définit**.
2. **Une idée** par phrase.
3. Chaque mot difficile est **expliqué** sur place.
4. On part du **connu** pour aller vers l'inconnu.
5. Un **exemple** de la vie de tous les jours.
6. Le ton d'une **encyclopédie**, jamais niais.
7. **Vrai**, même simplifié.
8. **Court** : ça tient sur un écran.

Le détail est dans [skills/vikidia/SKILL.md](skills/vikidia/SKILL.md).

## La galerie

[galerie/](galerie/) rassemble les meilleures explications produites avec le
skill. **Ajoute la tienne** : une PR avec ta question, la réponse et son
score de lisibilité. Mode d'emploi dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Mesurer

```bash
python3 evals/lisibilite.py ma-reponse.txt
```

Le script donne un score de 0 à 100 (formule de Kandel et Moles, la version
française de Flesch). Au-dessus de 70, un collégien suit sans peine.

---

<sub>Projet indépendant, inspiré du style de Vikidia et sans lien avec
l'association Vikidia. Licence MIT. Fait avec Claude Code.</sub>
