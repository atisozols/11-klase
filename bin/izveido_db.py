#!/usr/bin/env python3
"""Izveido mācību datubāzi skola.db.

Datubāze ir apzināti "nekārtīga": daļai skolēnu trūkst e-pasta, dažiem nav
nevienas atzīmes, dažos pulciņos nav neviena dalībnieka. Tas ir vajadzīgs,
lai LEFT JOIN un IS NULL uzdevumiem būtu īstas atbildes.

Lietošana:
    python3 bin/izveido_db.py 02-datubazes/skola.db
"""
import random
import sqlite3
import sys
from pathlib import Path

random.seed(2026)          # lai datubāze katru reizi sanāk vienāda

VARDI_S = ["Anna", "Elza", "Marta", "Līva", "Katrīna", "Alise", "Emīlija", "Paula",
           "Sofija", "Laura", "Beāte", "Amēlija", "Estere", "Marija", "Ance"]
VARDI_Z = ["Roberts", "Emīls", "Kārlis", "Markuss", "Rihards", "Daniels", "Gustavs",
           "Artūrs", "Reinis", "Toms", "Niklāvs", "Ralfs", "Edgars", "Matīss", "Jēkabs"]
UZVARDI = ["Bērziņš", "Kalniņš", "Ozols", "Liepiņš", "Krūmiņš", "Zariņš", "Vanags",
           "Eglītis", "Priede", "Lācis", "Balodis", "Vītols", "Celms", "Dzenis",
           "Rozītis", "Sproģis", "Auziņš", "Grīnbergs", "Jansons", "Riekstiņš"]

PRIEKSMETI = ["Programmēšana", "Matemātika", "Latviešu valoda", "Angļu valoda",
              "Fizika", "Ķīmija", "Bioloģija", "Vēsture", "Ģeogrāfija", "Sports"]

PULCINI = [("Robotika", "otrdiena", 12), ("Koris", "pirmdiena", 40),
           ("Basketbols", "trešdiena", 15), ("Debates", "ceturtdiena", 20),
           ("Fotogrāfija", "piektdiena", 10), ("Šahs", "otrdiena", 16),
           ("Teātris", "trešdiena", 18), ("Astronomija", "piektdiena", 8)]


def uzvards_sieviesu(u):
    return u[:-1] + "a" if u.endswith("š") else (u[:-1] + "e" if u.endswith("s") else u)


def izveido(cels):
    Path(cels).unlink(missing_ok=True)
    con = sqlite3.connect(cels)
    con.executescript("""
        CREATE TABLE skolotaji (
            id INTEGER PRIMARY KEY,
            vards TEXT NOT NULL,
            uzvards TEXT NOT NULL,
            epasts TEXT UNIQUE
        );
        CREATE TABLE klases (
            id INTEGER PRIMARY KEY,
            nosaukums TEXT NOT NULL UNIQUE,
            audzinatajs_id INTEGER REFERENCES skolotaji(id)
        );
        CREATE TABLE skoleni (
            id INTEGER PRIMARY KEY,
            vards TEXT NOT NULL,
            uzvards TEXT NOT NULL,
            klase_id INTEGER REFERENCES klases(id),
            epasts TEXT,
            dzimsanas_gads INTEGER
        );
        CREATE TABLE prieksmeti (
            id INTEGER PRIMARY KEY,
            nosaukums TEXT NOT NULL UNIQUE,
            skolotajs_id INTEGER REFERENCES skolotaji(id)
        );
        CREATE TABLE atzimes (
            id INTEGER PRIMARY KEY,
            skolens_id INTEGER REFERENCES skoleni(id),
            prieksmets_id INTEGER REFERENCES prieksmeti(id),
            atzime INTEGER CHECK (atzime BETWEEN 1 AND 10),
            datums TEXT
        );
        CREATE TABLE pulcini (
            id INTEGER PRIMARY KEY,
            nosaukums TEXT NOT NULL UNIQUE,
            skolotajs_id INTEGER REFERENCES skolotaji(id),
            diena TEXT,
            vietu_skaits INTEGER
        );
        CREATE TABLE dalibnieki (
            id INTEGER PRIMARY KEY,
            skolens_id INTEGER REFERENCES skoleni(id),
            pulcins_id INTEGER REFERENCES pulcini(id),
            pieteikts TEXT
        );
    """)

    # skolotāji
    skolotaji = []
    for i in range(12):
        vards = random.choice(VARDI_S + VARDI_Z)
        uzvards = random.choice(UZVARDI)
        if vards in VARDI_S:
            uzvards = uzvards_sieviesu(uzvards)
        epasts = f"{vards.lower()}.{uzvards.lower()}@skola.lv"
        epasts = epasts.translate(str.maketrans("āčēģīķļņōŗšūž", "acegiklnorsuz"))
        skolotaji.append((i + 1, vards, uzvards, epasts))
    con.executemany("INSERT INTO skolotaji VALUES (?,?,?,?)", skolotaji)

    # klases
    klases = [(i + 1, n, i + 1) for i, n in enumerate(["10.a", "10.b", "11.a", "11.b", "12.a", "12.b"])]
    con.executemany("INSERT INTO klases VALUES (?,?,?)", klases)

    # priekšmeti
    prieksmeti = [(i + 1, n, random.randint(1, 12)) for i, n in enumerate(PRIEKSMETI)]
    con.executemany("INSERT INTO prieksmeti VALUES (?,?,?)", prieksmeti)

    # skolēni
    skoleni = []
    sid = 1
    for klase_id, nosaukums, _ in klases:
        for _ in range(random.randint(9, 13)):
            sieviete = random.random() < 0.5
            vards = random.choice(VARDI_S if sieviete else VARDI_Z)
            uzvards = random.choice(UZVARDI)
            if sieviete:
                uzvards = uzvards_sieviesu(uzvards)
            gads = 2026 - (16 + int(nosaukums[:2]) - 10)
            # daļai skolēnu e-pasts nav zināms
            if random.random() < 0.15:
                epasts = None
            else:
                epasts = f"{vards.lower()}.{uzvards.lower()}{sid}@skola.lv".translate(
                    str.maketrans("āčēģīķļņōŗšūž", "acegiklnorsuz"))
            skoleni.append((sid, vards, uzvards, klase_id, epasts, gads))
            sid += 1
    con.executemany("INSERT INTO skoleni VALUES (?,?,?,?,?,?)", skoleni)

    # atzīmes — dažiem skolēniem nav nevienas
    atzimes = []
    aid = 1
    for skolens in skoleni:
        if random.random() < 0.08:
            continue
        for prieksmets in random.sample(prieksmeti, random.randint(4, 9)):
            for _ in range(random.randint(1, 4)):
                menesis = random.randint(9, 12)
                diena = random.randint(1, 28)
                atzimes.append((aid, skolens[0], prieksmets[0],
                                min(10, max(1, int(random.gauss(7.2, 1.8)))),
                                f"2025-{menesis:02d}-{diena:02d}"))
                aid += 1
    con.executemany("INSERT INTO atzimes VALUES (?,?,?,?,?)", atzimes)

    # pulciņi — divos nav neviena dalībnieka
    pulcini = [(i + 1, n, random.randint(1, 12), d, v) for i, (n, d, v) in enumerate(PULCINI)]
    con.executemany("INSERT INTO pulcini VALUES (?,?,?,?,?)", pulcini)

    dalibnieki = []
    did = 1
    for pulcins in pulcini[:6]:
        for skolens in random.sample(skoleni, random.randint(5, 14)):
            dalibnieki.append((did, skolens[0], pulcins[0], "2025-09-15"))
            did += 1
    con.executemany("INSERT INTO dalibnieki VALUES (?,?,?,?)", dalibnieki)

    con.commit()
    skaits = {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
              for t in ["skolotaji", "klases", "skoleni", "prieksmeti", "atzimes",
                        "pulcini", "dalibnieki"]}
    con.close()
    print(f"  {cels}")
    for tabula, n in skaits.items():
        print(f"    {tabula:12} {n:5}")


if __name__ == "__main__":
    izveido(sys.argv[1] if len(sys.argv) > 1 else "02-datubazes/skola.db")
