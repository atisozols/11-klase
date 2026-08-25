#!/usr/bin/env python3
"""Pārģenerē stundu tabulu bloka README failā no pašām stundu kartītēm.

Lietošana:
    python3 bin/tabula.py 01-vide-un-pamati/README.md
    python3 bin/tabula.py */README.md          # visiem blokiem uzreiz

Tabula tiek ierakstīta starp komentāriem TABULA:SAKUMS un TABULA:BEIGAS,
tāpēc tēmu un SR raksta tikai vienā vietā — pašā stundas kartītē.
"""
import re
import sys
from pathlib import Path

SAKUMS = "<!-- TABULA:SAKUMS"
BEIGAS = "<!-- TABULA:BEIGAS -->"
STUNDA = re.compile(r"^## (\d{2}-\d{3}) · (.+)$", re.M)


def stundas(teksts):
    for m in STUNDA.finditer(teksts):
        nr = m.group(1)
        sakums = m.end()
        nakama = STUNDA.search(teksts, sakums)
        kartite = teksts[sakums:nakama.start() if nakama else len(teksts)]
        tema = re.search(r"^\*\*Tēma:\*\* (.+)$", kartite, re.M)
        sr = re.search(r"^\*\*SR:\*\* (.+)$", kartite, re.M)
        if not tema or not sr:
            print(f"  ! {nr}: trūkst Tēma vai SR", file=sys.stderr)
            continue
        yield nr, tema.group(1).strip(), sr.group(1).strip()


def apstrada(cels):
    teksts = Path(cels).read_text(encoding="utf-8")
    if SAKUMS not in teksts or BEIGAS not in teksts:
        print(f"  ! {cels}: nav TABULA marķieru", file=sys.stderr)
        return
    rindas = ["| Nr. | Tēma | Sasniedzamais rezultāts |", "| --- | --- | --- |"]
    skaits = 0
    for nr, tema, sr in stundas(teksts):
        rindas.append(f"| {nr} | {tema} | {sr} |")
        skaits += 1

    pirms, atlikums = teksts.split(SAKUMS, 1)
    komentars, pec = atlikums.split("-->", 1)
    _, pec = pec.split(BEIGAS, 1)
    jauns = (
        pirms + SAKUMS + komentars + "-->\n\n"
        + "\n".join(rindas) + "\n\n" + BEIGAS + pec
    )
    Path(cels).write_text(jauns, encoding="utf-8")
    print(f"  {cels}: {skaits} stundas")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for cels in sys.argv[1:]:
        apstrada(cels)
