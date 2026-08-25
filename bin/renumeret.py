#!/usr/bin/env python3
"""Pārnumurē bloka uzdevumus tā, lai numerācija ietu cauri visam blokam.

Uzdevumu numuri README failā līdz šim sākās no 1 katrā stundā. Šis skripts
tos pārnumurē 1..N bloka ietvaros un vienlaikus salabo atsauces:
  **Mājasdarbs:** 3. uzdevums
  Papildini 2. uzdevumu ...
  Papildini 10-018 1. uzdevumu ...
"""
import re
import sys
from pathlib import Path

STUNDA = re.compile(r"^## (\d{2}-\d{3}) · ", re.M)


def sadali(teksts):
    """Sadala README stundās: [(nr, sakums, beigas), ...]."""
    atzimes = [(m.group(1), m.start()) for m in STUNDA.finditer(teksts)]
    for i, (nr, sak) in enumerate(atzimes):
        beig = atzimes[i + 1][1] if i + 1 < len(atzimes) else len(teksts)
        yield nr, sak, beig


def uzdevumu_rindas(kartite):
    """Atgriež uzdevumu rindu indeksus kartītē (tikai Uzdevumi sadaļā)."""
    rindas = kartite.split("\n")
    iekša = False
    kods = False
    for i, rinda in enumerate(rindas):
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
        if iekša and re.match(r"^\d+\. ", rinda):
            yield i
    return


def apstrada(cels):
    teksts = Path(cels).read_text(encoding="utf-8")
    kartes = {}          # stunda -> {vecais: jaunais}
    gabali = []
    skaititajs = 0
    pozicija = 0

    for nr, sak, beig in sadali(teksts):
        gabali.append(teksts[pozicija:sak])
        kartite = teksts[sak:beig]
        rindas = kartite.split("\n")
        karte = {}
        for i in uzdevumu_rindas(kartite):
            vecais = int(re.match(r"^(\d+)\. ", rindas[i]).group(1))
            skaititajs += 1
            karte[vecais] = skaititajs
            rindas[i] = re.sub(r"^\d+\. ", f"{skaititajs}. ", rindas[i])
        kartes[nr] = karte
        gabali.append("\n".join(rindas))
        pozicija = beig

    gabali.append(teksts[pozicija:])
    jauns = "".join(gabali)

    # Atsauces ar norādītu stundu: "10-018 1. uzdevumu"
    def ar_stundu(m):
        stunda, num, aste = m.group(1), int(m.group(2)), m.group(3)
        jaunais = kartes.get(stunda, {}).get(num)
        return f"{stunda} {jaunais}. {aste}" if jaunais else m.group(0)

    jauns = re.sub(r"(\d{2}-\d{3}) (\d+)\. (uzdevum\w*)", ar_stundu, jauns)

    # Atsauces bez stundas — attiecas uz to pašu stundu
    gabali = []
    pozicija = 0
    for nr, sak, beig in sadali(jauns):
        gabali.append(jauns[pozicija:sak])
        kartite = jauns[sak:beig]
        karte = kartes.get(nr, {})

        def bez_stundas(m):
            num, aste = int(m.group(1)), m.group(2)
            # jau pārnumurēts? (jaunie numuri ir lielāki par stundas uzdevumu skaitu)
            if num in karte.values():
                return m.group(0)
            jaunais = karte.get(num)
            return f"{jaunais}. {aste}" if jaunais else m.group(0)

        kartite = re.sub(r"(?<!\d[-–] )(\d+)\. (uzdevum\w*)", bez_stundas, kartite)
        gabali.append(kartite)
        pozicija = beig
    gabali.append(jauns[pozicija:])
    jauns = "".join(gabali)

    Path(cels).write_text(jauns, encoding="utf-8")
    print(f"  {cels}: {skaititajs} uzdevumi")


if __name__ == "__main__":
    for cels in sys.argv[1:]:
        apstrada(cels)
