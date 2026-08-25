#!/usr/bin/env python3
"""Pārbauda bloku konsistenci: stundu numerācija, [K]/[A] ritms, uzdevumu numuri.

Lietošana:
    python3 bin/parbaudit.py
"""
import re
from pathlib import Path

KLASE = Path.cwd().name.split("-")[0]


def uzdevumu_numuri(teksts):
    """Uzdevumu numuri tikai no **Uzdevumi** sadaļām, ne no jebkuras rindas,
    kas sākas ar ciparu — tāds var būt arī parasts teksts, piemēram "02. blokā"."""
    numuri = []
    iekša = kods = False
    for rinda in teksts.split("\n"):
        if rinda.lstrip().startswith("```"):
            kods = not kods
            continue
        if kods:
            continue
        if rinda.strip() == "**Uzdevumi**":
            iekša = True
            continue
        if iekša and rinda.startswith("**"):
            iekša = False
        if iekša:
            m = re.match(r"^(\d+)\. ", rinda)
            if m:
                numuri.append(int(m.group(1)))
    return numuri
kludas = 0
visi_numuri, visi_uzdevumi = [], 0

for d in sorted(Path(".").glob("0*/")):
    readme = d / "README.md"
    if not readme.exists():
        continue
    t = readme.read_text(encoding="utf-8")
    stundas = re.findall(rf"^## {KLASE}-(\d{{3}}) · ", t, re.M)
    numuri = [int(n) for n in stundas]
    visi_numuri += numuri

    uzd = uzdevumu_numuri(t)
    visi_uzdevumi += len(uzd)
    if uzd != list(range(1, len(uzd) + 1)):
        print(f"  ! {d.name}: uzdevumu numerācija nav secīga")
        kludas += 1

    zinojums = f"{d.name:32} {KLASE}-{numuri[0]:03d} … {KLASE}-{numuri[-1]:03d}  {len(numuri):2} st.  {len(uzd):3} uzd."

    if KLASE == "12":
        kartes = re.findall(rf"^## {KLASE}-(\d{{3}}) · .*\n`\[([KA])\]`", t, re.M)
        if len(kartes) != len(stundas):
            print(f"  ! {d.name}: {len(stundas) - len(kartes)} stundām trūkst [K]/[A]")
            kludas += 1
        slikti = [n for n, v in kartes if (v == "A") != (int(n) % 6 in (5, 0))]
        if slikti:
            print(f"  ! {d.name}: nepareizs [K]/[A]: {slikti}")
            kludas += 1
        att = sum(1 for _, v in kartes if v == "A")
        zinojums += f"  [A] {att}"
    print(zinojums)

truk = [i for i in range(1, max(visi_numuri) + 1) if i not in visi_numuri] if visi_numuri else []
dubulti = [i for i in set(visi_numuri) if visi_numuri.count(i) > 1]
if truk:
    print("  ! trūkstošas stundas:", truk); kludas += 1
if dubulti:
    print("  ! dubultas stundas:", dubulti); kludas += 1

print(f"\nkopā: {len(visi_numuri)} stundas, {visi_uzdevumi} uzdevumi")
print("kļūdas:" , kludas if kludas else "nav")
