# ==========================================================
# 01. OBJEKTORIENTĒTĀ PROGRAMMĒŠANA — DARBA FAILS
# ==========================================================
# Šeit raksti savus risinājumus.
# Teorija, piemēri un atgādne: teorija.py
# Uzdevumu numuri iet cauri visam blokam.
# ==========================================================


# ----------------------------------------------------------
# 11-001 · Kāpēc vajadzīgas klases
# ----------------------------------------------------------

# 1. Burtnīcā: dotajam aprakstam «bibliotēkas grāmata» pieraksti, kādi dati par to jāglabā un
#    kādas darbības ar to var veikt.




# 2. Burtnīcā: tas pats «skolas ēdnīcas pasūtījumam».




# 3. Burtnīcā: dotajā programmā ir trīs paralēli saraksti (vardi, klases, atzimes).
#    Pieraksti, kas notiks, ja no viena saraksta izdzēsīs elementu, bet no citiem ne.




# 4. ★ Atrodi savā 10. klases kodā vietu, kur būtu noderējusi klase, un pieraksti, kāpēc.





# ----------------------------------------------------------
# 11-002 · Klase un objekts
# ----------------------------------------------------------

# 5. Izveido klasi Skolens ar atribūtiem vards un klase. Izveido divus objektus un
#    izvadi to atribūtus.

# class Skolens:
#     def __init__(self, vards, klase):
#         self.vards = vards
#         self.klase = klase

# kristers = Skolens("Kristers", "10.c")
# janis = Skolens("Jānis", "9.b")

# print(kristers.vards, kristers.klase)

# 6. Izveido klasi Prece ar atribūtiem nosaukums un cena. Izveido trīs objektus.

# class Prece:
#     def __init__(self, nosaukums, cena):
#         self.nosaukums = nosaukums
#         self.cena = cena

# p1 = Prece("Twix", 0.79)
# p2 = Prece("Snickers", 0.89)
# p3 = Prece("Mars", 0.67)

# 7. Nomaini viena objekta atribūta vērtību un pārbaudi, ka otrs objekts nemainījās.

# p1.nosaukums = "Bounty"
# print(p1.nosaukums)

# 8. Izveido klasi Punkts ar atribūtiem x un y un izvadi divu punktu koordinātas.




# 9. ★ Izveido divus objektus ar vienādām atribūtu vērtībām un pārbaudi, vai tie ir vienādi
#    (==). Paskaidro rezultātu.


# p4 = Prece("Mars", 0.67)
# p5 = Prece("Mars", 0.67)


# ----------------------------------------------------------
# 11-003 · Konstruktors
# ----------------------------------------------------------

# 10. Pārraksti klasi Skolens tā, lai vārdu un klasi padod objekta izveides brīdī.




# 11. Izveido klasi Gramata ar konstruktoru (nosaukums, autors, gads) un izveido
#    trīs objektus.

class Gramata:
    def __init__(self, nosaukums, autors, gads):
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads

g1 = Gramata("The Brand Gap", "Marty Neumeier", "2018")
g2 = Gramata("Influence", "Robert B. Cialdini", "2012")
g3 = Gramata("Thinking, Fast and Slow", "Daniel Kahneman", "2012")

# 12. Izveido klasi Konts ar konstruktoru (ipasnieks, atlikums) un izvadi abu kontu
#    atlikumus.

class Konts:
    def __init__(self, ipasnieks, atlikums=0):
        self.ipasnieks = ipasnieks
        self.atlikums = atlikums

# 13. Izveido klasi Taisnsturis ar konstruktoru (platums, augstums).




# 14. ★ Uzraksti konstruktoru, kuram daļai parametru ir noklusējuma vērtības, un izveido
#    objektus abos veidos.

atis = Konts("Atis")
konrads = Konts("Konrāds", 123)

print(atis.atlikums, konrads.atlikums)

# ----------------------------------------------------------
# 11-004 · Metodes
# ----------------------------------------------------------

# 15. Klasei Taisnsturis pievieno metodes laukums() un perimetrs().

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

# 16. Klasei Konts pievieno metodi ieskaitit(summa), kas palielina atlikumu.

# class Konts:
#     def __init__(self, atlikums):
#         self.atlikums = atlikums   # konkrētā situācijā, kur mums ir konts k, k ieņems self vietu un k.atlikums saņems vērtību     

#     def parbaudit(self):
#         return self.atlikums   
    
#     def ieskaitit(self, summa):
#         self.atlikums += summa
#         return True

# k = Konts(120) # Konstruktors.__init__(k, 120)
# print(k.atlikums)
# k.ieskaitit(20)
# print(k.atlikums)

# 17. Klasei Gramata pievieno metodi apraksts(), kas atgriež tekstu
#    "Blēdis · Anšlavs Eglītis, 1943".

class Gramata:
    def __init__(self, nosaukums, autors, gads):
        self.nosaukums = nosaukums
        self.autors = autors
        self.gads = gads

    def apraksts(self):
        return f"{self.nosaukums} · {self.autors}, {self.gads}"
    
g = Gramata("Blēdis", "Anšlavs Eglītis", "1943")
print(g.apraksts())

# 18. Klasei Skolens pievieno metodi videja_atzime(), ja atzīmes glabājas sarakstā.

class Skolens:
    def __init__(self, vards, klase, atzimes=[]):
        self.vards = vards
        self.klase = klase
        self.atzimes = atzimes

    def pievienot_atzimi(self, atzime):
        self.atzimes.append(atzime)

    def videja_atzime(self):
        return round(sum(self.atzimes) / len(self.atzimes), 2)


    



# 19. ★ Klasei Punkts pievieno metodi attalums(cits), kas atgriež attālumu līdz citam punktam.



# ----------------------------------------------------------
# 11-005 · self
# ----------------------------------------------------------

# 20. Burtnīcā: dotajā klasē atrodi trīs vietas, kur trūkst self, un pieraksti, kas notiks.



# 21. Burtnīcā: pieraksti, ko izvadīs dotā programma ar trim objektiem.



# 22. Datorā: izlabo doto klasi, kurā metodes maina lokālu mainīgo, nevis atribūtu.



# 23. ★ Uzraksti klasi, kurā metode atgriež pati sevi (return self), un izsauc divas metodes
#    vienā rindā.


# ----------------------------------------------------------
# 11-006 · Objekta stāvoklis
# ----------------------------------------------------------

# 24. Klasei Konts pievieno metodi iznemt(summa), kas neļauj atlikumam kļūt negatīvam un
#    atgriež True vai False.

# class Konts:
#     def __init__(self, atlikums):
#         self.atlikums = atlikums   # konkrētā situācijā, kur mums ir konts k, k ieņems self vietu un k.atlikums saņems vērtību     

#     def parbaudit(self):
#         return self.atlikums   
    
#     def ieskaitit(self, summa):
#         self.atlikums += summa
#         return True

#     def iznemt(self, summa):
#         if self.atlikums >= summa:
#             self.atlikums -= summa
#             return True
#         else:
#             return False

# 25. Izveido klasi Skaititajs ar metodēm palielinat(), atiestatit() un vertiba().

class Skaititajs:
    def __init__(self, solis=1):
        self.v = 0
        self.solis = solis

    def palielinat(self):
        self.v += self.solis
        return True

    def atiestatit(self):
        self.v = 0
        return True

    def vertiba(self):
        return self.v

s = Skaititajs()

for _ in range(10):
    s.palielinat()

print(s.vertiba())

# 26. Izveido klasi Grozs, kurā var pievienot preces un izvadīt kopsummu.


class Prece:
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena

class Grozs:
    def __init__(self):
        self.saraksts = []

    def pievienot(self, prece):
        self.saraksts.append(prece)
        return True

    def kopsumma(self):
        summa = 0
        for prece in self.saraksts:
            summa += prece.cena
        return summa

grozs = Grozs()
grozs.pievienot(Prece("Txix", 1.79))
grozs.pievienot(Prece("Maize", 1.25))
print(grozs.kopsumma())

# 27. Izveido klasi Termometrs, kas atceras visas izmērītās temperatūras un atgriež vidējo.

class Termometrs:
    def __init__(self):
        self.saraksts = []
    
    def temperatura(self, vertiba):
        self.saraksts.append(vertiba)
        return True

    def videja(self):
        return sum(self.saraksts) / len(self.saraksts)

t = Termometrs()
t.temperatura(30)
t.temperatura(27)
t.temperatura(32)
t.temperatura(29)
t.temperatura(30)
print(t.videja())

# 28. ★ Klasei Konts pievieno darījumu vēsturi un metodi, kas izvada pēdējos piecus darījumus.

class Konts:
    def __init__(self, atlikums):
        self.atlikums = atlikums   # konkrētā situācijā, kur mums ir konts k, k ieņems self vietu un k.atlikums saņems vērtību     
        self.darijumi = []

    def parbaudit(self):
        self.darijumi.append(f"tika pieprasīts atlikums: {self.atlikums}")
        return self.atlikums   
    
    def ieskaitit(self, summa):
        self.atlikums += summa
        self.darijumi.append(f"tika ieskaitīts kontā {summa}; atlikums: {self.atlikums}")
        return True

    def iznemt(self, summa):
        if self.atlikums >= summa:
            self.atlikums -= summa
            self.darijumi.append(f"tika izņemts {summa}; atlikums: {self.atlikums}")
            return True
        else:
            self.darijumi.append(f"izņemt {summa} neizdevās; atlikums: {self.atlikums}")
            return False

    def darijumu_vesture(self):
        return self.darijumi[-5:]

k = Konts(100)
k.ieskaitit(20)
k.parbaudit()
k.iznemt(50)
k.parbaudit()
k.iznemt(100)

for darijums in k.darijumu_vesture():
    print(darijums)

# ----------------------------------------------------------
# 11-007 · Praktikums: klases
# ----------------------------------------------------------

# 29. Kases čeks. Klase Ceks ar metodēm pievienot(prece, cena), summa(),
#    izdrukat(). Čeka izdruka ir izlīdzināta kolonnās.

# class Ceks:
#     def __init__(self):
#         self.preces = {}

#     def pievienot(self, prece, cena):
#         self.preces[prece] = cena

#     def summa(self):
#         s = 0
#         for prece, cena in self.preces.items():
#             s += cena
#         return s

#     def izdrukat(self):
#         print("-" * 10 + " ČEKS " + "-" * 10)
        
#         for prece, cena in self.preces.items():
#             print(f"{prece:<21} {cena}")

#         print("-" * 26)

#         print(f"{'kopā: ':<21} {self.summa():.2f}")

# c = Ceks()
# c.pievienot("maize", 1.29)
# c.pievienot("vafeltorte", 7.49)
# print(round(c.summa(), 2))
# c.izdrukat()


# 30. Rezervācija. Klase Rezervacija ar atribūtiem un metodi atcelt(), kas maina
#    statusu un neļauj atcelt divreiz.

class Rezervacija:
    def __init__(self, vards):
        self.vards = vards
        self.ir_aktiva = True

    def atcelt(self):
        if self.ir_aktiva:
            self.ir_aktiva = False

        else:
            raise Exception("Nav iespējams atcelt jau atceltu rezervāciju")

    def statuss(self):
        return f"Vārds: {self.vards}; Aktīva: {"Jā" if self.ir_aktiva else "Nē"}"


# r = Rezervacija("Atis")
# print(r.statuss())
# r.atcelt()
# print(r.statuss())
# r.atcelt()




# 31. ★ Pulkstenis. Klase Laiks ar metodēm pieskaitit_minutes(n) un teksts(),
#    kas pareizi pāriet pār stundu un diennakts robežu.


# 23:45 + 00:25 -> 00:10
# 12:23 + 00:34 -> 12:57
# 12:30 + 00:45 -> 13:15
# 12:15 + 00:123 -> 14:18

class Pulkstenis:
    def __init__(self, stundas, minutes):
        self.stundas = stundas
        self.minutes = minutes

    def teksts(self):
        print(f"{self.stundas}:{self.minutes}")

    def pieskaitit_minutes(self, n):
        result_m = self.minutes + n
        result_h = self.stundas + (result_m // 60)

        self.stundas, self.minutes = result_h % 24, result_m % 60

p = Pulkstenis(13, 46)
p.pieskaitit_minutes(4444)
p.teksts()

# ----------------------------------------------------------
# 11-008 · Objektu kolekcija
# ----------------------------------------------------------

# 32. Izveido piecu Skolens objektu sarakstu un izvadi visu vārdus.

# sk_saraksts = [
#     Skolens("Jānis", "11b", [10, 9, 8]),
#     Skolens("Andris", "12c", [6, 8, 3]),
#     Skolens("Aleksejs", "12c", [8, 9, 6]),
#     Skolens("Miķelis", "11a", [9, 9, 10])
#     ]

# for skolens in sk_saraksts:
#     print(skolens.klase, skolens.vards)

# 33. Atrodi sarakstā skolēnu ar augstāko vidējo atzīmi.

# krutakais_dzeks = None
# for skolens in sk_saraksts:
#     if not krutakais_dzeks:
#         krutakais_dzeks = skolens

#     else:
#         if skolens.videja_atzime() > krutakais_dzeks.videja_atzime():
#             krutakais_dzeks = skolens

# print(krutakais_dzeks.vards)

# 34. Izvadi tikai tos skolēnus, kuru vidējā atzīme ir virs klases vidējās.




# 35. Sakārto grāmatu sarakstu pēc izdošanas gada.




# 36. ★ Sagrupē skolēnus pa klasēm vārdnīcā, kur atslēga ir klase, bet vērtība — objektu saraksts.





# ----------------------------------------------------------
# 11-009 · Objekti un datnes
# ----------------------------------------------------------

# 37. Klasei Gramata pievieno metodi uz_rindu(), kas atgriež CSV rindu. -> <Atribūts1>,<Atribūts2>,...,<AtribūtsN>




# 38. Uzraksti funkciju, kas no CSV rindas izveido Gramata objektu.




# 39. Saglabā visu grāmatu sarakstu datnē un ielasi to atpakaļ jaunā programmā.




# 40. Papildini programmu tā, lai jaunu grāmatu var pievienot un tā saglabājas.




# 41. ★ Uzraksti metodi, kas pārbauda, vai CSV rinda ir derīga, un atgriež None, ja nav.





# ----------------------------------------------------------
# 11-010 · Validācija klasē
# ----------------------------------------------------------


# 42. Klasē Konts neļauj izveidot objektu ar negatīvu atlikumu.




# 43. Klasē Skolens neļauj pievienot atzīmi, kas nav no 1 līdz 10.




# 44. Klasē Gramata pārbaudi, ka gads ir no 1500 līdz šodienai.




# 45. Uzraksti programmu, kas noķer kļūdu ar try / except un turpina darbu.

# class Konts:
#     def __init__(self, ipasnieks, atlikums=0):
#         try:
#             self.ipasnieks = ipasnieks
#             self.atlikums = float(atlikums)
#         except:
#             print("Radās kļūda, using default values")
#             self.atlikums = 0

#     def __str__(self):
#         return f"{round(self.atlikums, 2)}"

# k = Konts(input("vārds: "), input("sākuma atlikums: "))
# print(k.ipasnieks, k.atlikums)

# 46. ★ Pievieno klasei metodi ir_deriga(), kas atgriež visu problēmu sarakstu, nevis met kļūdu.





# ----------------------------------------------------------
# 11-011 · Objekta izvade
# ----------------------------------------------------------

# 47. Klasei Gramata pievieno _str_ un izvadi objektu ar print.




# 48. Klasei Konts pievieno _str_ ar summu divos ciparos aiz komata.


# konti = [
#     Konts("Atis", 123.45),
#     Konts("Mārtiņš", 143.5),
#     Konts("Pēteris", 50.67)
#     ]



# 49. Izvadi objektu sarakstu ciklā tā, lai iznāk izlīdzināta tabula.

# print("-- Īpašnieks -- | -- Atlikums --")
# for konts in konti:
#     print(f"{konts.ipasnieks:<15} | {str(konts):<9}")

# 50. ★ Pievieno klasei metodi kopsavilkums(), kas atgriež vairākrindu tekstu ar rāmīti.



# ----------------------------------------------------------
# 11-012 · Iekapsulēšana
# ----------------------------------------------------------

# 51. Pārraksti klasi Konts tā, lai atlikumu var mainīt tikai ar metodēm.

class Konts:
    def __init__(self, ipasnieks, atlikums=0):
        try:
            self.ipasnieks = ipasnieks
            self.atlikums = float(atlikums)
        except:
            print("Radās kļūda, using default values")
            self.atlikums = 0

    def iznemt(self, summa):
        if summa <= self.atlikums:
            self.atlikums -= summa
        else:
            raise Exception("Nevar izņemt, nepietiek līdzekļu")

    def papildinat(self, summa):
        self.atlikums += float(summa)

    def __str__(self):
        return f"{round(self.atlikums, 2)}"

k = Konts("Atis", 123.45)

# print(k)
# k.iznemt(200)
# print(k)

class KreditKonts(Konts):
    def iznemt(self, summa):
        self.atlikums -= summa

kk = KreditKonts("Atis", 143.00)
kk.iznemt(200)
print(kk)

# 52. Burtnīcā: pieraksti, kuri no dotās klases atribūtiem drīkstētu būt publiski un kuri ne.




# 53. Pievieno klasei metodi, kas atgriež atribūta vērtību, bet neļauj to mainīt.




# 54. ★ Uzraksti klasi, kurā viens atribūts tiek aprēķināts no citiem un tāpēc to vispār nav
#    jēgas glabāt.





# ----------------------------------------------------------
# 11-013 · Mantošana
# ----------------------------------------------------------

# 55. Izveido klasi Darbinieks un apakšklasi Skolotajs, kas pievieno priekšmetu.




# 56. Izveido klasi Transportlidzeklis un divas apakšklases ar atšķirīgu metodi.

# Uzrakstīt klasi Transportlidzeklis un 3 klases, kas to manto. Katrai izveidot savu __str__ metodi.

class Transportlidzeklis:
    def __init__(self, marka, krasa, ritenu_skaits, ietilpiba=1):
        self.marka = marka
        self.krasa = krasa
        self.ritenu_skaits = ritenu_skaits
        self.ietilpiba = ietilpiba

    def __str__(self):
        return f"{self.marka}, {self.krasa}, {self.ritenu_skaits}, {self.ietilpiba}"
        
class Automasina(Transportlidzeklis):
    def __init__(self, marka, krasa, ritenu_skaits, degvielas_tips, paterins, ietilpiba=1):
        super().__init__(marka, krasa, ritenu_skaits, ietilpiba)
        self.degvielas_tips = degvielas_tips
        self.paterins = paterins

    def __str__(self):
        return f"{self.marka}, {self.krasa}, {self.ritenu_skaits}, {self.ietilpiba}, {self.degvielas_tips}, {self.paterins}"

bmw = Automasina("BMW", "melna", 4, "diesel", 8, 5)
ricuks = Transportlidzeklis("Cube", "melna", 2)

# 57. Pārraksti divas savas iepriekšējās klases tā, lai kopīgais būtu virsklasē.




# 58. ★ Uzraksti apakšklasi, kas pārraksta (override) virsklases metodi, un parādi abu darbību.





# ----------------------------------------------------------
# 11-014 · Klašu diagramma
# ----------------------------------------------------------

# 59. Burtnīcā: uzzīmē klašu diagrammu bibliotēkas sistēmai (grāmata, lasītājs, izsniegums).




# 60. Burtnīcā: uzzīmē diagrammu savai 11-007 čeka programmai.




# 61. ★ Burtnīcā: uzzīmē diagrammu sistēmai ar mantošanu (lietotājs un administrators).





# ----------------------------------------------------------
# 11-015 · Atkārtojums pirms pārbaudes darba
# ----------------------------------------------------------

# 62. Burtnīcā: uzraksti klasi Ekskursija ar konstruktoru un divām metodēm.




# 63. Burtnīcā: dots klases kods — pieraksti, ko izvadīs programma, kas to lieto.




# 64. Burtnīcā: dotajā klasē ir trīs kļūdas. Atrodi un izlabo.




# 65. ★ Burtnīcā: uzraksti apakšklasi dotajai virsklasei.
