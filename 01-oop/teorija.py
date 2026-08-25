# ============================================================
# 01. BLOKS — OBJEKTORIENTĒTĀ PROGRAMMĒŠANA
# ============================================================
# Līdz šim dati un darbības bija atsevišķi: saraksti un vārdnīcas
# glabāja datus, funkcijas ar tiem kaut ko darīja.
#
# Klase saliek abus kopā: viena vieta, kurā ir gan dati (atribūti),
# gan darbības ar tiem (metodes).
#
# Komentārs  # ?  nozīmē: vispirms uzmini, ko rinda izvadīs, tikai tad palaid.
# ============================================================


# ============================================================
# 1. KĀPĒC KLASES                                      [11-001]
# ============================================================
# Bez klasēm 30 skolēnu dati izskatās šādi:

vardi = ["Anna", "Roberts"]
klases = ["11.a", "11.b"]
atzimes = [[8, 9, 7], [6, 5, 8]]

# Problēma: šie trīs saraksti ir saistīti tikai ar indeksu. Ja no
# viena izdzēš elementu un no citiem ne, dati sajūk, un neviens
# par to nepaziņo. Anna pēkšņi ir 11.b ar Roberta atzīmēm.
#
# Ar klasi viena skolēna dati ir vienā vietā un tos nevar sajaukt.


# ============================================================
# 2. KLASE UN OBJEKTS                                  [11-002]
# ============================================================
# Klase ir VEIDNE. Objekts ir konkrēts eksemplārs pēc tās veidnes.
#
#   klase Skolens        -> veidne: katram skolēnam ir vārds un klase
#   objekts anna         -> konkrēts skolēns ar konkrētām vērtībām

class Punkts:
    x = 0
    y = 0


# a = Punkts()
# b = Punkts()
# a.x = 3
# a.y = 4
# print(a.x, a.y)
# print(b.x, b.y)      # ?   vai b mainījās kopā ar a?

# Šāda klase ir reti noderīga — vērtības jāpiešķir pa vienai pēc
# izveides. Tāpēc gandrīz vienmēr izmanto konstruktoru.


# ============================================================
# 3. KONSTRUKTORS                                      [11-003]
# ============================================================
# __init__ izpildās automātiski, kad izveido objektu. Tas saņem
# sākuma vērtības un saglabā tās objektā.

class Skolens:
    def __init__(self, vards, klase):
        self.vards = vards
        self.klase = klase


# anna = Skolens("Anna", "11.a")
# roberts = Skolens("Roberts", "11.b")
# print(anna.vards, anna.klase)
# print(roberts.vards, roberts.klase)

# self.vards = vards
# ^^^^^^^^^^   ^^^^^
# objekta      parametrs, kas atnāca
# atribūts     no izsaukuma
#
# Ja aizmirst self., vērtība nonāk lokālā mainīgajā, kas pazūd
# līdzi ar metodes beigām.


# ============================================================
# 4. METODES                                           [11-004]
# ============================================================
# Metode ir funkcija, kas pieder klasei un var lietot objekta atribūtus.

class Taisnsturis:
    def __init__(self, platums, augstums):
        self.platums = platums
        self.augstums = augstums

    def laukums(self):
        return self.platums * self.augstums

    def perimetrs(self):
        return 2 * (self.platums + self.augstums)

    def ir_kvadrats(self):
        return self.platums == self.augstums


# t = Taisnsturis(6, 4)
# print(t.laukums())        # 24
# print(t.perimetrs())      # 20
# print(t.ir_kvadrats())    # False

# Metodes nosaukums ir darbības vārds, tāpat kā funkcijai.
# Metode, kas kaut ko aprēķina, ATGRIEŽ vērtību, nevis izvada to.


# ============================================================
# 5. self                                              [11-005]
# ============================================================
# Viena metode apkalpo visus objektus. self ir tas objekts, uz kura
# metode šoreiz tika izsaukta.
#
#   t.laukums()   ->   Taisnsturis.laukums(t)
#
# Tāpēc self ir pirmais parametrs katrā metodē — Python to padod pats.

# Bieža kļūda: trūkst self.
# class Konts:
#     def __init__(self, atlikums):
#         atlikums = atlikums          # <- lokāls mainīgais, pazūd
#
#     def parbaudit(self):
#         return atlikums              # <- NameError


# ============================================================
# 6. OBJEKTA STĀVOKLIS                                 [11-006]
# ============================================================
# Objekts atceras savu stāvokli starp metožu izsaukumiem.

class Konts:
    def __init__(self, ipasnieks, atlikums=0):
        self.ipasnieks = ipasnieks
        self.atlikums = atlikums

    def ieskaitit(self, summa):
        self.atlikums += summa

    def iznemt(self, summa):
        if summa > self.atlikums:
            return False              # nepietiek naudas
        self.atlikums -= summa
        return True


# k = Konts("Anna", 50)
# k.ieskaitit(30)
# print(k.atlikums)         # 80
# print(k.iznemt(100))      # ?
# print(k.atlikums)         # ?

# Metode, kas maina stāvokli, bieži atgriež True/False — vai darbība
# izdevās. Tā izsaucējs var reaģēt.


# ============================================================
# 7. OBJEKTU KOLEKCIJA                                 [11-008]
# ============================================================
# Īsts uzdevums sākas nevis ar vienu objektu, bet ar sarakstu.

# skoleni = [
#     Skolens("Anna", "11.a"),
#     Skolens("Roberts", "11.b"),
#     Skolens("Elza", "11.a"),
# ]
#
# for skolens in skoleni:
#     print(skolens.vards)

# Filtrēšana:
# no_a = []
# for skolens in skoleni:
#     if skolens.klase == "11.a":
#         no_a.append(skolens)

# Kārtošana pēc atribūta — key pasaka, pēc kā kārtot:
# pec_varda = sorted(skoleni, key=lambda s: s.vards)
# for skolens in pec_varda:
#     print(skolens.vards)


# ============================================================
# 8. OBJEKTI UN DATNES                                 [11-009]
# ============================================================
# Objekts pats zina, kā sevi pierakstīt datnē. Tas ir viss OOP
# jēgas kodols: dati un darbības ar tiem ir vienuviet.

class Gramata:
    def __init__(self, nosaukums, autors, gads):
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads

    def uz_rindu(self):
        return f"{self.nosaukums},{self.autors},{self.gads}"


def no_rindas(rinda):
    """Izveido Gramata objektu no CSV rindas."""
    lauki = rinda.strip().split(",")
    return Gramata(lauki[0], lauki[1], int(lauki[2]))


# g = Gramata("Bledis", "Anslavs Eglitis", 1943)
# print(g.uz_rindu())
# g2 = no_rindas("Straumeni,Edvarts Virza,1933")
# print(g2.autors)

# Saglabāšana:
# with open("gramatas.csv", "w", encoding="utf-8") as datne:
#     for gramata in gramatas:
#         datne.write(gramata.uz_rindu() + "\n")


# ============================================================
# 9. VALIDĀCIJA KLASĒ                                  [11-010]
# ============================================================
# Klase var neļaut izveidot nederīgu objektu. Tad neviens, kas to
# lieto, nevar aizmirst pārbaudīt.

class DrossKonts:
    def __init__(self, ipasnieks, atlikums=0):
        if atlikums < 0:
            raise ValueError("Atlikums nevar but negativs")
        self.ipasnieks = ipasnieks
        self.atlikums = atlikums


# k = DrossKonts("Anna", -50)      # ValueError

# Kļūdu var noķert un turpināt darbu:
# try:
#     k = DrossKonts("Anna", -50)
# except ValueError as kluda:
#     print("Neizdevas izveidot kontu:", kluda)


# ============================================================
# 10. OBJEKTA IZVADE: __str__                          [11-011]
# ============================================================
# Bez __str__ print(objekts) izvada atmiņas adresi.

class Prece:
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena

    def __str__(self):
        return f"{self.nosaukums:<15}{self.cena:>8.2f} EUR"


# p = Prece("Piens", 1.09)
# print(p)

# Tabula no objektiem:
# for prece in preces:
#     print(prece)


# ============================================================
# 11. IEKAPSULĒŠANA                                    [11-012]
# ============================================================
# Ja atlikumu var mainīt no ārpuses, visas pārbaudes ir bezjēdzīgas:
#
#   k.atlikums = 1000000
#
# Python neaizliedz, bet ir vienošanās: atribūts ar apakšsvītru
# priekšā ir klases iekšēja lieta un no ārpuses to neaiztiek.

class SlegtsKonts:
    def __init__(self, ipasnieks, atlikums=0):
        self.ipasnieks = ipasnieks
        self._atlikums = atlikums        # iekšējs

    def atlikums(self):
        return self._atlikums

    def ieskaitit(self, summa):
        if summa <= 0:
            return False
        self._atlikums += summa
        return True


# k = SlegtsKonts("Anna", 50)
# print(k.atlikums())
# k.ieskaitit(-10)          # neizdodas, atlikums nemainās


# ============================================================
# 12. MANTOŠANA                                        [11-013]
# ============================================================
# Ja divām klasēm ir daudz kopīga, kopīgo izceļ virsklasē.

class Darbinieks:
    def __init__(self, vards, alga):
        self.vards = vards
        self.alga = alga

    def apraksts(self):
        return f"{self.vards}, alga {self.alga} EUR"


class Skolotajs(Darbinieks):
    def __init__(self, vards, alga, prieksmets):
        super().__init__(vards, alga)     # izsauc virsklases konstruktoru
        self.prieksmets = prieksmets

    def apraksts(self):                   # pārraksta virsklases metodi
        return f"{self.vards}, {self.prieksmets} skolotajs"


# d = Darbinieks("Janis", 1200)
# s = Skolotajs("Anna", 1300, "programmesana")
# print(d.apraksts())
# print(s.apraksts())
# print(s.alga)            # ?   no kurienes Skolotajam ir alga?

# Uzmanību: mantošana ir noderīga retāk, nekā šķiet. Ja neesi drošs,
# ka apakšklase TIEŠĀM ir virsklases paveids, labāk divas atsevišķas
# klases.
