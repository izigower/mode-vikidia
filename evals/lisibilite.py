#!/usr/bin/env python3
"""Score de lisibilité d'un texte français (Kandel et Moles) ou anglais (Flesch).

Kandel-Moles est l'adaptation française de la formule de Flesch :
    score = 207 - 1,015 x (mots / phrase) - 73,6 x (syllabes / mot)
Plus le score est haut, plus le texte est facile. Repères :
    > 70  facile (primaire, collège)
    50-70 standard
    < 30  très difficile (texte universitaire, juridique)

En anglais (option --en), c'est la formule d'origine, Flesch Reading Ease :
    score = 206,835 - 1,015 x (mots / phrase) - 84,6 x (syllabes / mot)

Usage :
    python3 lisibilite.py fichier.txt
    python3 lisibilite.py --en file.txt
    echo "Un texte." | python3 lisibilite.py
"""
import re
import sys

VOYELLES = "aeiouyàâäéèêëîïôöùûüœæ"


def syllabes(mot: str) -> int:
    mot = mot.lower()
    # un « e » muet final ne compte pas (sauf mots très courts : « le », « de »)
    if len(mot) > 3 and mot.endswith(("e", "es", "ent")) and not mot.endswith(("ée", "ées")):
        mot = re.sub(r"(e|es|ent)$", "", mot)
    groupes = re.findall(f"[{VOYELLES}]+", mot)
    return max(1, len(groupes))


def syllabes_en(mot: str) -> int:
    mot = mot.lower()
    if len(mot) > 3 and mot.endswith("e") and not mot.endswith(("le", "ee")):
        mot = mot[:-1]
    mot = re.sub(r"(ed|es)$", "", mot) if len(mot) > 4 else mot
    return max(1, len(re.findall(r"[aeiouy]+", mot)))


def analyser(texte: str, anglais: bool = False) -> dict:
    phrases = [p for p in re.split(r"[.!?…:;]+", texte) if re.search(r"\w", p)]
    mots = re.findall(r"[A-Za-zÀ-ÿœæŒÆ]+(?:['’-][A-Za-zÀ-ÿœæŒÆ]+)*", texte)
    nb_syll = sum((syllabes_en if anglais else syllabes)(m) for m in mots)
    mpp = len(mots) / max(1, len(phrases))
    spm = nb_syll / max(1, len(mots))
    if anglais:
        score = 206.835 - 1.015 * mpp - 84.6 * spm
    else:
        score = 207 - 1.015 * mpp - 73.6 * spm
    return {
        "phrases": len(phrases),
        "mots": len(mots),
        "mots_par_phrase": round(mpp, 1),
        "syllabes_par_mot": round(spm, 2),
        "score": round(score),
        "niveau": niveau(score),
    }


def niveau(score: float) -> str:
    if score >= 70:
        return "facile (collège)"
    if score >= 50:
        return "standard (lycée)"
    if score >= 30:
        return "difficile (études supérieures)"
    return "très difficile (spécialiste)"


if __name__ == "__main__":
    args = sys.argv[1:]
    anglais = "--en" in args
    args = [a for a in args if a != "--en"]
    texte = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
    for cle, valeur in analyser(texte, anglais).items():
        print(f"{cle:>18} : {valeur}")
