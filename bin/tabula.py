#!/usr/bin/env python3
"""Pārģenerē stundu tabulu bloka README failā no pašām stundu kartītēm.

Lietošana:
    python3 bin/tabula.py 01-vide-un-pamati/README.md
    python3 bin/tabula.py */README.md          # visiem blokiem uzreiz

Tabula tiek ierakstīta starp komentāriem TABULA:SAKUMS un TABULA:BEIGAS,
tāpēc tēmu un SR raksta tikai vienā vietā — pašā stundas kartītē.

Kolonna "Pārbaude" tiek aizpildīta automātiski:
  FV — no kartītes tagu rindas, piemēram  `prakse` · FV3 (dators)
  SV — kartītēm ar veidu `pārbaudes darbs`; numurs tiek ņemts no kartītes
       virsraksta vai, ja tur tā nav, no bloka galvenes rindas "Noslēgums".
"""
import re
import sys
from pathlib import Path

SAKUMS = "<!-- TABULA:SAKUMS"
BEIGAS = "<!-- TABULA:BEIGAS -->"
STUNDA = re.compile(r"^## (\d{2}-\d{3}) · (.+)$", re.M)
FV = re.compile(r"\bFV(\d+)\s*\(([^)]+)\)")
SV_VAI_ME = re.compile(r"\b(SV|ME)(\d+)\b")


def bloka_sv(teksts):
    """Bloka summatīvā darba numurs no galvenes rindas "Noslēgums"."""
    galvene = teksts.split("<!-- TABULA:SAKUMS", 1)[0]
    for rinda in galvene.split("\n"):
        if "Noslēgums:" in rinda:
            m = SV_VAI_ME.search(rinda)
            if m:
                return m.group(1) + m.group(2)
    return None


def parbaude(nosaukums, kartite, sv_numurs):
    """Ko rādīt kolonnā "Pārbaude": FV ar formu, SV/ME numuru vai tukšu."""
    tagi = kartite.strip().split("\n", 1)[0] if kartite.strip() else ""

    m = FV.search(tagi)
    if m:
        return f"**FV{m.group(1)}** ({m.group(2)})"

    if "`pārbaudes darbs`" in tagi:
        m = SV_VAI_ME.search(nosaukums)
        if m:
            return f"**{m.group(1)}{m.group(2)}**"
        if sv_numurs:
            return f"**{sv_numurs}**"
        return "**pārbaudes darbs**"

    return ""


def stundas(teksts):
    sv_numurs = bloka_sv(teksts)
    for m in STUNDA.finditer(teksts):
        nr, nosaukums = m.group(1), m.group(2)
        sakums = m.end()
        nakama = STUNDA.search(teksts, sakums)
        kartite = teksts[sakums:nakama.start() if nakama else len(teksts)]
        tema = re.search(r"^\*\*Tēma:\*\* (.+)$", kartite, re.M)
        sr = re.search(r"^\*\*SR:\*\* (.+)$", kartite, re.M)
        if not tema or not sr:
            print(f"  ! {nr}: trūkst Tēma vai SR", file=sys.stderr)
            continue
        yield (nr, tema.group(1).strip(), sr.group(1).strip(),
               parbaude(nosaukums, kartite, sv_numurs))


def apstrada(cels):
    teksts = Path(cels).read_text(encoding="utf-8")
    if SAKUMS not in teksts or BEIGAS not in teksts:
        print(f"  ! {cels}: nav TABULA marķieru", file=sys.stderr)
        return
    rindas = ["| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |",
              "| --- | --- | --- | --- |"]
    skaits = parbaudes = 0
    for nr, tema, sr, p in stundas(teksts):
        rindas.append(f"| {nr} | {tema} | {sr} | {p} |")
        skaits += 1
        parbaudes += bool(p)

    pirms, atlikums = teksts.split(SAKUMS, 1)
    komentars, pec = atlikums.split("-->", 1)
    _, pec = pec.split(BEIGAS, 1)
    jauns = (
        pirms + SAKUMS + komentars + "-->\n\n"
        + "\n".join(rindas) + "\n\n" + BEIGAS + pec
    )
    Path(cels).write_text(jauns, encoding="utf-8")
    print(f"  {cels}: {skaits} stundas, {parbaudes} pārbaudes")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for cels in sys.argv[1:]:
        apstrada(cels)
