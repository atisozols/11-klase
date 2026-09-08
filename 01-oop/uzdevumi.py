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

class Skolens:
    def __init__(self, vards, klase):
        self.vards = vards
        self.klase = klase

kristers = Skolens("Kristers", "10.c")
janis = Skolens("Jānis", "9.b")

print(kristers.vards, kristers.klase)

# 6. Izveido klasi Prece ar atribūtiem nosaukums un cena. Izveido trīs objektus.

class Prece:
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena

p1 = Prece("Twix", 0.79)
p2 = Prece("Snickers", 0.89)
p3 = Prece("Mars", 0.67)

# 7. Nomaini viena objekta atribūta vērtību un pārbaudi, ka otrs objekts nemainījās.

p1.nosaukums = "Bounty"
# print(p1.nosaukums)

# 8. Izveido klasi Punkts ar atribūtiem x un y un izvadi divu punktu koordinātas.




# 9. ★ Izveido divus objektus ar vienādām atribūtu vērtībām un pārbaudi, vai tie ir vienādi
#    (==). Paskaidro rezultātu.


p4 = Prece("Mars", 0.67)
p5 = Prece("Mars", 0.67)


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




# 16. Klasei Konts pievieno metodi ieskaitit(summa), kas palielina atlikumu.




# 17. Klasei Gramata pievieno metodi apraksts(), kas atgriež tekstu
#    "Blēdis · Anšlavs Eglītis, 1943".




# 18. Klasei Skolens pievieno metodi videja_atzime(), ja atzīmes glabājas sarakstā.




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




# 25. Izveido klasi Skaititajs ar metodēm palielinat(), atiestatit() un vertiba().




# 26. Izveido klasi Grozs, kurā var pievienot preces un izvadīt kopsummu.




# 27. Izveido klasi Termometrs, kas atceras visas izmērītās temperatūras un atgriež vidējo.




# 28. ★ Klasei Konts pievieno darījumu vēsturi un metodi, kas izvada pēdējos piecus darījumus.





# ----------------------------------------------------------
# 11-007 · Praktikums: klases
# ----------------------------------------------------------

# 29. Kases čeks. Klase Ceks ar metodēm pievienot(prece, cena), summa(),
#    izdrukat(). Čeka izdruka ir izlīdzināta kolonnās.




# 30. Rezervācija. Klase Rezervacija ar atribūtiem un metodi atcelt(), kas maina
#    statusu un neļauj atcelt divreiz.




# 31. ★ Pulkstenis. Klase Laiks ar metodēm pieskaitit_minutes(n) un teksts(),
#    kas pareizi pāriet pār stundu un diennakts robežu.





# ----------------------------------------------------------
# 11-008 · Objektu kolekcija
# ----------------------------------------------------------

# 32. Izveido piecu Skolens objektu sarakstu un izvadi visu vārdus.




# 33. Atrodi sarakstā skolēnu ar augstāko vidējo atzīmi.




# 34. Izvadi tikai tos skolēnus, kuru vidējā atzīme ir virs klases vidējās.




# 35. Sakārto grāmatu sarakstu pēc izdošanas gada.




# 36. ★ Sagrupē skolēnus pa klasēm vārdnīcā, kur atslēga ir klase, bet vērtība — objektu saraksts.





# ----------------------------------------------------------
# 11-009 · Objekti un datnes
# ----------------------------------------------------------

# 37. Klasei Gramata pievieno metodi uz_rindu(), kas atgriež CSV rindu.




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




# 46. ★ Pievieno klasei metodi ir_deriga(), kas atgriež visu problēmu sarakstu, nevis met kļūdu.





# ----------------------------------------------------------
# 11-011 · Objekta izvade
# ----------------------------------------------------------

# 47. Klasei Gramata pievieno _str_ un izvadi objektu ar print.




# 48. Klasei Konts pievieno _str_ ar summu divos ciparos aiz komata.




# 49. Izvadi objektu sarakstu ciklā tā, lai iznāk izlīdzināta tabula.




# 50. ★ Pievieno klasei metodi kopsavilkums(), kas atgriež vairākrindu tekstu ar rāmīti.





# ----------------------------------------------------------
# 11-012 · Iekapsulēšana
# ----------------------------------------------------------

# 51. Pārraksti klasi Konts tā, lai atlikumu var mainīt tikai ar metodēm.




# 52. Burtnīcā: pieraksti, kuri no dotās klases atribūtiem drīkstētu būt publiski un kuri ne.




# 53. Pievieno klasei metodi, kas atgriež atribūta vērtību, bet neļauj to mainīt.




# 54. ★ Uzraksti klasi, kurā viens atribūts tiek aprēķināts no citiem un tāpēc to vispār nav
#    jēgas glabāt.





# ----------------------------------------------------------
# 11-013 · Mantošana
# ----------------------------------------------------------

# 55. Izveido klasi Darbinieks un apakšklasi Skolotajs, kas pievieno priekšmetu.




# 56. Izveido klasi Transportlidzeklis un divas apakšklases ar atšķirīgu metodi.




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
