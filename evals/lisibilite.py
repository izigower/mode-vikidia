#!/usr/bin/env python3
"""Score de lisibilité d'un texte français (formule de Kandel et Moles).

Kandel-Moles est l'adaptation française de la formule de Flesch :
    score = 207 - 1,015 x (mots / phrase) - 73,6 x (syllabes / mot)
Plus le score est haut, plus le texte est facile. Repères :
    > 70  facile (primaire, collège)
    50-70 standard
    < 30  très difficile (texte universitaire, juridique)

Usage :
    python3 lisibilite.py fichier.txt
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


def analyser(texte: str) -> dict:
    phrases = [p for p in re.split(r"[.!?…:;]+", texte) if re.search(r"\w", p)]
    mots = re.findall(r"[A-Za-zÀ-ÿœæŒÆ]+(?:['’-][A-Za-zÀ-ÿœæŒÆ]+)*", texte)
    nb_syll = sum(syllabes(m) for m in mots)
    mpp = len(mots) / max(1, len(phrases))
    spm = nb_syll / max(1, len(mots))
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
    texte = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    for cle, valeur in analyser(texte).items():
        print(f"{cle:>18} : {valeur}")
