# ============================================================
# 03. BLOKS — BIBLIOTĒKAS, API UN DATI NO TĪMEKĻA
# ============================================================
# Lielāko daļu koda, kas tev vajadzīgs, kāds jau ir uzrakstījis.
# Šis bloks ir par to, kā to atrast, pievienot un lietot.
#
# Komentārs  # ?  nozīmē: vispirms uzmini, ko rinda izvadīs, tikai tad palaid.
# ============================================================

import json
import math
import random
import statistics
from datetime import date, timedelta


# ============================================================
# 1. MODULIS UN BIBLIOTĒKA                             [11-033]
# ============================================================
# modulis     — viens .py fails ar funkcijām
# pakotne     — vairāki moduļi kopā
# bibliotēka  — viss, ko kāds sagatavojis lietošanai
#
# Trīs importa veidi:
#
#   import math                  ->  math.sqrt(16)
#   from math import sqrt        ->  sqrt(16)
#   from math import sqrt as s   ->  s(16)
#
# Šo nelieto:
#   from math import *      — nav skaidrs, no kurienes funkcija nāk,
#                             un tā var pārrakstīt tavu paša funkciju.

# print(math.sqrt(16))
# print(math.pi)

# Savs modulis: fails paligs.py ar funkciju sveiciens()
#   from paligs import sveiciens
#
# Ja modulī ir arī izmēģinājumu kods, to liek šādā blokā, lai tas
# neizpildītos importēšanas brīdī:
#
#   if __name__ == "__main__":
#       print(sveiciens("Anna"))


# ============================================================
# 2. STANDARTA BIBLIOTĒKA                              [11-034]
# ============================================================
# Nāk līdzi Python — nekas nav jāuzstāda.

# random — nejaušība
# print(random.randint(1, 6))                  # kauliņš
# print(random.choice(["Anna", "Roberts"]))    # izloze
# print(random.sample(range(1, 50), 6))        # 6 dažādi skaitļi

# datetime — datumi
# sodien = date.today()
# gada_beigas = date(2027, 5, 31)
# print((gada_beigas - sodien).days)            # cik dienu atlicis

# statistics — statistika
atzimes = [8, 9, 7, 6, 9, 10, 7]
# print(statistics.mean(atzimes))               # vidējais
# print(statistics.median(atzimes))             # mediāna
# print(statistics.mode(atzimes))               # biežākā vērtība

# math — matemātika
# print(math.sqrt(144))
# print(math.ceil(4.1), math.floor(4.9))
# print(round(math.hypot(3, 4), 2))             # hipotenūza


# ============================================================
# 3. ĀRĒJA BIBLIOTĒKA                                  [11-035]
# ============================================================
# Ārējās bibliotēkas jāuzstāda:
#
#   pip install requests
#
# Projekta bibliotēkas pieraksta requirements.txt:
#
#   requests==2.32.3
#
# Tad cits cilvēks visu uzstāda ar vienu komandu:
#
#   pip install -r requirements.txt
#
# Pirms svešas bibliotēkas pievienošanas pārbaudi:
#   1) kad tā pēdējo reizi atjaunināta;
#   2) kāda tai licence;
#   3) cik cilvēku to lieto;
#   4) vai dokumentācijā ir piemēri.


# ============================================================
# 4. JSON                                              [11-036]
# ============================================================
# JSON izskatās gandrīz kā Python vārdnīca, un tieši par to tas
# arī pārvēršas.
#
#   {"vards": "Anna", "atzimes": [8, 9, 7]}
#      teksts            saraksts
#
# Atšķirības: JSON vienmēr dubultpēdiņas, true/false ar mazo burtu,
# null vietā Python ir None.

TEKSTS = """
{
  "pilseta": "Tukums",
  "iedzivotaji": 17000,
  "skolas": [
    {"nosaukums": "Raiņa ģimnāzija", "skoleni": 500},
    {"nosaukums": "2. vidusskola", "skoleni": 420}
  ]
}
"""

dati = json.loads(TEKSTS)          # teksts -> Python
# print(dati["pilseta"])
# print(dati["skolas"][0]["nosaukums"])
# print(len(dati["skolas"]))

# for skola in dati["skolas"]:
#     print(skola["nosaukums"], skola["skoleni"])

# Python -> teksts
# print(json.dumps(dati, ensure_ascii=False, indent=2))

# Droša piekļuve — get() ar noklusējumu, ja lauka nav:
# print(dati.get("pasts", "nav zinams"))       # ?


# ============================================================
# 5. DATI NO API                                       [11-037]
# ============================================================
# API atdod datus programmai (JSON), mājaslapa — cilvēkam (HTML).
#
# Ar requests (jāuzstāda):
#
#   import requests
#   atbilde = requests.get("https://api.chucknorris.io/jokes/random")
#   print(atbilde.status_code)        # 200 = viss kārtībā
#   dati = atbilde.json()
#   print(dati["value"])
#
# Bez requests, tikai ar standarta bibliotēku:
#
#   from urllib.request import urlopen
#   with urlopen("https://api.chucknorris.io/jokes/random") as atbilde:
#       dati = json.loads(atbilde.read().decode("utf-8"))
#   print(dati["value"])
#
# Nezināmu API vispirms izpēta:
#   1) atver adresi pārlūkā un apskata atbildi;
#   2) izdrukā visu atbildi ar json.dumps(..., indent=2);
#   3) tikai tad raksta kodu, kas paņem vajadzīgo lauku.


# ============================================================
# 6. PIEPRASĪJUMA PARAMETRI                            [11-038]
# ============================================================
# URL uzbūve:
#
#   https://api.open-meteo.com/v1/forecast?latitude=56.97&longitude=23.15&daily=temperature_2m_max
#   \______________________________/ \____/\____________________________________________________/
#            adrese                    ?                     parametri, atdalīti ar &
#
# Parametrus nesaliek virknē pašrocīgi — bibliotēka to izdara pareizi
# (piemēram, pārveido atstarpes un garumzīmes):
#
#   parametri = {
#       "latitude": 56.97,
#       "longitude": 23.15,
#       "daily": "temperature_2m_max",
#       "timezone": "Europe/Riga",
#   }
#   atbilde = requests.get("https://api.open-meteo.com/v1/forecast", params=parametri)
#   dati = atbilde.json()
#   print(dati["daily"]["temperature_2m_max"])


# ============================================================
# 7. API ATSLĒGAS                                      [11-040]
# ============================================================
# Daļa API prasa atslēgu — tā identificē, kurš prasa datus.
#
# ATSLĒGU NEKAD NERAKSTA KODĀ:
#
#   ATSLEGA = "sk-a83hd..."      # <- šis nonāks GitHub un paliks vēsturē
#
# Atslēgu glabā .env datnē, kas ir .gitignore sarakstā:
#
#   API_ATSLEGA=sk-a83hd...
#
# Programmā to ielasa:
#
#   import os
#   atslega = os.environ.get("API_ATSLEGA")
#
# Repozitorijā komitē .env.paraugs ar tukšām vērtībām, lai cits zina,
# kādas atslēgas vajag:
#
#   API_ATSLEGA=
#
# Publiskā repozitorijā nonākusi atslēga ir jāatsauc un jānomaina.
# Izdzēst komitu nepietiek — vēsturē tas paliek.


# ============================================================
# 8. KĻŪDU APSTRĀDE                                    [11-041]
# ============================================================
# Tīkls ir vieta, kur viss var noiet greizi: nav interneta, serveris
# nestrādā, atbilde nav JSON, trūkst gaidītā lauka.
#
#   try:
#       atbilde = requests.get(adrese, timeout=5)
#       if atbilde.status_code != 200:
#           print("Serveris atbildeja ar kodu", atbilde.status_code)
#       else:
#           dati = atbilde.json()
#   except requests.exceptions.Timeout:
#       print("Serveris neatbild")
#   except requests.exceptions.RequestException:
#       print("Neizdevas sazinaties ar serveri")
#
# Biežākie statusa kodi:
#   200  viss kārtībā
#   400  slikts pieprasījums
#   401  nav atļaujas (atslēga)
#   404  nav atrasts
#   429  par daudz pieprasījumu
#   500  servera kļūda


# ============================================================
# 9. DATU ATTĒLOŠANA                                   [11-042]
# ============================================================
# Vienkāršākais ceļš: saglabā CSV un uztaisi diagrammu izklājlapā.

def saglaba_csv(cels, galvene, rindas):
    """Saglabā datus CSV datnē diagrammas veidošanai."""
    with open(cels, "w", encoding="utf-8") as datne:
        datne.write(",".join(galvene) + "\n")
        for rinda in rindas:
            datne.write(",".join(str(v) for v in rinda) + "\n")


# temperaturas = [("2026-09-01", 18.4), ("2026-09-02", 16.1)]
# saglaba_csv("temperaturas.csv", ["datums", "temperatura"], temperaturas)

# Diagrammas izvēle:
#   līnija    — kā vērtība mainās laikā
#   stabiņi   — kategoriju salīdzinājums
#   sektori   — daļas no veselā (tikai tad, ja daļu ir maz)
#
# Katrai diagrammai ir jāatbild uz konkrētu jautājumu. Ja nevari to
# jautājumu uzrakstīt vienā teikumā, diagramma nav vajadzīga.
