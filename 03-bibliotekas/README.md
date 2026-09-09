# 03. Bibliotēkas, API un dati no tīmekļa

**14 stundas (11-033 – 11-046)** · Standarta 5. temats “Kā izvēlēties un efektīvi savā
projektā izmantot jau esošu risinājumu?”

**Bloka mērķis:** atrast, pievienot un lietot ārējo bibliotēku un iegūt datus no publiskas
programmsaskarnes (API), tos apstrādāt un attēlot.

**Teorija un piemēri:** [`teorija.py`](teorija.py) · **Darba fails:** [`uzdevumi.py`](uzdevumi.py)
**Pārbaudes darbi:** privātajā `sv-fv` repozitorijā
**Noslēgums:** SV3 — datora darbs (11-046)

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 03-bibliotekas/README.md && python3 bin/darbafails.py 03-bibliotekas -->

| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |
| --- | --- | --- | --- |
| 11-033 | Modulis, bibliotēka, pakotne. Koda importēšana. | Importē moduli un lieto tā funkcijas; sadala savu kodu vairākos moduļos. |  |
| 11-034 | Standarta bibliotēka: `math`, `random`, `datetime`, `statistics`. | Izvēlas standarta bibliotēkas funkciju uzdevuma risināšanai, nevis raksta to pats. |  |
| 11-035 | Ārējas bibliotēkas meklēšana, uzstādīšana un dokumentācijas lasīšana. | Atrod uzdevumam piemērotu bibliotēku, uzstāda to ar `pip` un lieto pēc dokumentācijas. |  |
| 11-036 | JSON formāts. Datu struktūra un pārveide. | Nolasa JSON datus un piekļūst vajadzīgajām vērtībām ligzdotā struktūrā. |  |
| 11-037 | Programmsaskarne (API). Pieprasījums un atbilde. | Nosūta pieprasījumu publiskai API un apstrādā saņemtos datus. |  |
| 11-038 | Pieprasījuma parametri. Atbildes filtrēšana un apstrāde. | Veido pieprasījumu ar parametriem un no atbildes atlasa vajadzīgo. |  |
| 11-039 | Praktikums: datu ieguve un apstrāde no API. | Patstāvīgi iegūst datus no API, apstrādā tos un saglabā rezultātu. | **FV5** (dators) |
| 11-040 | API atslēgas. Noslēpumu glabāšana ārpus koda. | Skaidro, kāpēc atslēgu nedrīkst rakstīt kodā, un glabā to atsevišķi. |  |
| 11-041 | Kļūdu apstrāde tīmekļa pieprasījumos. | Apstrādā tīkla kļūdas un negaidītas atbildes, neļaujot programmai avarēt. |  |
| 11-042 | Iegūto datu attēlošana. Informācijas dizaina pamatprincipi. | Sagatavo datus un izveido diagrammu, kas atbild uz konkrētu jautājumu. |  |
| 11-043 | Atvērtā koda licences. Bibliotēkas izvēles kritēriji. | Salīdzina atvērtā koda licences un pamato bibliotēkas izvēli savam projektam. | **FV6** (papīrs) |
| 11-044 | Praktikums: pilna datu ķēde no API līdz attēlojumam. | Iegūst datus no API, apstrādā, saglabā un attēlo tos. |  |
| 11-045 | Bibliotēkas un API: atkārtojums pirms pārbaudes darba. | Atkārto bloka prasmes un pārbauda savu darba vidi. |  |
| 11-046 | Pārbaudes darbs: programma ar ārēju bibliotēku un API. | Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā. | **SV3** |

<!-- TABULA:BEIGAS -->

---

## 11-033 · Modulis un bibliotēka
`prakse` · `teorija.py` §1

**Tēma:** Modulis, bibliotēka, pakotne. Koda importēšana.
**SR:** Importē moduli un lieto tā funkcijas; sadala savu kodu vairākos moduļos.
**Standarts:** T.O.2.4.11. · T.Li.2.

**Gaita**
- 5' — cik daudz jau ir uzrakstīts tavā vietā
- 10' — demo §1: `import`, `from ... import`, savs modulis
- 20' — uzdevumi
- 5' — kāpēc `from modulis import *` ir slikta ideja

**Uzdevumi**
1. Importē `math` un aprēķini kvadrātsakni, kāpinājumu un skaitli π.
2. Izveido savu moduli `paligs.py` ar divām funkcijām un importē to citā failā.
3. Pārraksti importu trīs dažādos veidos un pieraksti, ar ko tie atšķiras.
4. Pārnes savu 01. bloka klasi `Gramata` atsevišķā modulī un importē to.
5. ★ Uzraksti moduli, kurā ir gan funkcijas, gan `if __name__ == "__main__":` bloks
   pašpārbaudei. Paskaidro komentārā, kāpēc tas vajadzīgs.

**Mājasdarbs:** 4. uzdevums

## 11-034 · Standarta bibliotēka
`prakse` · `teorija.py` §2

**Tēma:** Standarta bibliotēka: `math`, `random`, `datetime`, `statistics`.
**SR:** Izvēlas standarta bibliotēkas funkciju uzdevuma risināšanai, nevis raksta to pats.
**Standarts:** T.O.2.4.13. · T.O.2.4.10.

**Gaita**
- 5' — kuras funkcijas jau esam uzrakstījuši paši, lai gan nevajadzēja?
- 10' — demo §2: četri moduļi un to biežāk lietotās funkcijas
- 20' — uzdevumi
- 5' — kad rakstīt pašam un kad ņemt gatavu

**Uzdevumi**
6. Ar `random` uzraksti programmu, kas izlozē klases dežurantu no saraksta.
7. Ar `datetime` aprēķini, cik dienu atlicis līdz mācību gada beigām.
8. Ar `statistics` aprēķini atzīmju vidējo, mediānu un modu; salīdzini ar savu ciklu.
9. Ar `math` aprēķini trijstūra hipotenūzu.
10. ★ Ar `random` uzraksti programmu, kas ģenerē 1000 kauliņu metienus un pārbauda, vai
    katrs skaitlis parādās aptuveni vienādi bieži.

**Mājasdarbs:** 7. uzdevums

## 11-035 · Ārēja bibliotēka
`prakse` · `teorija.py` §3

**Tēma:** Ārējas bibliotēkas meklēšana, uzstādīšana un dokumentācijas lasīšana.
**SR:** Atrod uzdevumam piemērotu bibliotēku, uzstāda to ar `pip` un lieto pēc dokumentācijas.
**Standarts:** T.O.2.4.11. · T.O.2.4.10. · T.O.2.3.3.

**Gaita**
- 5' — kur meklēt bibliotēku un kā saprast, vai tā ir uzturēta
- 10' — demo §3: `pip install`, `requirements.txt`, dokumentācijas struktūra
- 20' — uzdevumi
- 5' — kas jāpārbauda pirms svešas bibliotēkas pievienošanas projektam

**Uzdevumi**
11. Uzstādi bibliotēku `requests` un pārbaudi, ka imports strādā.
12. Atrodi `requests` dokumentācijā, kā nosūtīt pieprasījumu ar parametriem, un pieraksti
    piemēru komentārā.
13. Izveido `requirements.txt` ar savām bibliotēkām.
14. Atrodi PyPI vietnē bibliotēku, kas prot kaut ko tavam projektam noderīgu, un pieraksti
    tās nosaukumu, licenci un pēdējās versijas datumu.
15. ★ Salīdzini divas bibliotēkas, kas dara vienu un to pašu, un pamato, kuru izvēlētos.

**Mājasdarbs:** 13. uzdevums

## 11-036 · JSON
`prakse` · `teorija.py` §4

**Tēma:** JSON formāts. Datu struktūra un pārveide.
**SR:** Nolasa JSON datus un piekļūst vajadzīgajām vērtībām ligzdotā struktūrā.
**Standarts:** T.O.2.4.14. · T.V.2.3.6.

**Gaita**
- 5' — CSV pret JSON: kad kurš
- 10' — demo §4: JSON ir vārdnīcas un saraksti; `json.loads`, `json.dumps`
- 20' — uzdevumi
- 5' — ligzdota struktūra: kā tikt līdz dziļi paslēptai vērtībai

**Uzdevumi**
16. Dotajā JSON tekstā atrodi un izvadi trīs vērtības.
17. Pārveido Python vārdnīcu par JSON tekstu un saglabā to datnē.
18. Nolasi JSON datni un izveido no tās objektu sarakstu (izmanto 01. bloka klasi).
19. Dotajā ligzdotajā JSON izvadi visu masīva elementu kādu lauku.
20. ★ Uzraksti funkciju, kas droši paņem vērtību no ligzdotas struktūras un atgriež
    noklusējumu, ja ceļa nav.

**Mājasdarbs:** 18. uzdevums

## 11-037 · Dati no API
`prakse` · `teorija.py` §5

**Tēma:** Programmsaskarne (API). Pieprasījums un atbilde.
**SR:** Nosūta pieprasījumu publiskai API un apstrādā saņemtos datus.
**Standarts:** T.O.2.4.11. · T.O.2.3.3.

**Gaita**
- 5' — ar ko API atšķiras no mājaslapas
- 10' — demo §5: `requests.get`, statusa kods, `.json()`
- 20' — uzdevumi
- 5' — kā izpētīt nezināmu API atbildi

**Uzdevumi**
21. Iegūsti datus no `https://api.chucknorris.io/jokes/random` un izvadi tikai joka tekstu.
22. Iegūsti nejaušu lietotāju no `https://randomuser.me/api/` un izvadi vārdu, valsti un e-pastu.
23. Uzraksti programmu, kas iegūst 10 lietotājus un saglabā tos CSV datnē.
24. Izvadi API atbildes statusa kodu un paskaidro, ko tas nozīmē.
25. ★ Atrodi `data.gov.lv` datu kopu, iegūsti to ar programmu un izvadi pirmos piecus ierakstus.

**Mājasdarbs:** 23. uzdevums

## 11-038 · API parametri
`prakse` · `teorija.py` §6

**Tēma:** Pieprasījuma parametri. Atbildes filtrēšana un apstrāde.
**SR:** Veido pieprasījumu ar parametriem un no atbildes atlasa vajadzīgo.
**Standarts:** T.O.2.4.11. · T.V.2.3.6.

**Gaita**
- 5' — URL uzbūve: ceļš, `?`, parametri, `&`
- 10' — demo §6: `params=`, laikapstākļu API
- 20' — uzdevumi
- 5' — kāpēc parametrus nevajag salikt virknē pašrocīgi

**Uzdevumi**
26. Iegūsti Tukuma laikapstākļu prognozi un izvadi šodienas temperatūru.
27. Papildini programmu tā, lai pilsētas koordinātas prasa lietotājam.
28. Iegūsti septiņu dienu prognozi un izvadi katras dienas augstāko temperatūru.
29. Aprēķini nedēļas vidējo temperatūru no saņemtajiem datiem.
30. ★ Salīdzini divu pilsētu prognozes un izvadi, kurā būs siltāk.

**Mājasdarbs:** 28. uzdevums

## 11-039 · Praktikums: API
`prakse` · FV5 (dators)

**Tēma:** Praktikums: datu ieguve un apstrāde no API.
**SR:** Patstāvīgi iegūst datus no API, apstrādā tos un saglabā rezultātu.
**Standarts:** T.O.2.4.11. · T.O.2.4.14.

**Gaita**
- 5' — uzdevumu nolasīšana
- 20' — patstāvīgs darbs
- 15' — **FV5** pie datora

**Uzdevumi**
31. **Vārdu saraksts.** Programma iegūst 20 nejaušus lietotājus, atlasa tikai tos no Eiropas
    un saglabā CSV datnē ar vārdu, valsti un vecumu.
32. **Laikapstākļu atskaite.** Programma iegūst nedēļas prognozi un izvada dienu skaitu, kad
    temperatūra būs zem nulles, un aukstāko dienu.
33. ★ **Kešošana.** Papildini kādu no programmām tā, lai tā saglabā atbildi datnē un otrreiz
    to neprasa no API, ja datne nav vecāka par stundu.

**Mājasdarbs:** pabeigt 31. uzdevumu

## 11-040 · API atslēgas un drošība
`jaukta` · `teorija.py` §7

**Tēma:** API atslēgas. Noslēpumu glabāšana ārpus koda.
**SR:** Skaidro, kāpēc atslēgu nedrīkst rakstīt kodā, un glabā to atsevišķi.
**Standarts:** T.V.3.1.3. · T.O.3.1.3.

**Gaita**
- 10' — kas notiek, ja atslēga nonāk publiskā repozitorijā
- 10' — demo §7: `.env`, `os.environ`, `.gitignore`
- 15' — uzdevumi
- 5' — kāpēc atslēgas noplūde ir arī naudas jautājums

**Uzdevumi**
34. Pārnes API atslēgu no koda uz `.env` datni un ielasi to programmā.
35. Pievieno `.env` savam `.gitignore` un pārbaudi ar `git status`.
36. Izveido `.env.paraugs` ar tukšām vērtībām, ko var droši komitēt.
37. ★ Atrodi internetā piemēru, kur atslēgas noplūde radījusi reālas sekas, un pieraksti,
    kas notika.

**Mājasdarbs:** 36. uzdevums

## 11-041 · Kļūdu apstrāde
`prakse` · `teorija.py` §8

**Tēma:** Kļūdu apstrāde tīmekļa pieprasījumos.
**SR:** Apstrādā tīkla kļūdas un negaidītas atbildes, neļaujot programmai avarēt.
**Standarts:** T.V.1.3.2. · T.O.2.4.11.

**Gaita**
- 5' — kas var noiet greizi: nav interneta, serveris nestrādā, atbilde nav JSON
- 10' — demo §8: `try`/`except`, statusa koda pārbaude, taimauts
- 20' — uzdevumi
- 5' — ko rādīt lietotājam, kad kaut kas nav pieejams

**Uzdevumi**
38. Papildini savu API programmu ar `try`/`except`, lai tā nekrīt bez interneta.
39. Pārbaudi statusa kodu un izvadi saprotamu paziņojumu, ja tas nav 200.
40. Pievieno taimautu un pārbaudi, kas notiek, ja serveris neatbild.
41. Apstrādā gadījumu, kad atbildē trūkst gaidītā lauka.
42. ★ Uzraksti funkciju, kas mēģina pieprasījumu trīs reizes, pirms padodas.

**Mājasdarbs:** 39. uzdevums

## 11-042 · Datu attēlošana
`prakse` · `teorija.py` §9

**Tēma:** Iegūto datu attēlošana. Informācijas dizaina pamatprincipi.
**SR:** Sagatavo datus un izveido diagrammu, kas atbild uz konkrētu jautājumu.
**Standarts:** T.V.2.3.6. · T.V.2.2.1.

**Gaita**
- 5' — laba un slikta diagramma: divi piemēri uz ekrāna
- 10' — demo §9: dati uz CSV, diagramma izklājlapā; `matplotlib` kā ★ ceļš
- 20' — uzdevumi
- 5' — kāda diagramma kuram jautājumam (līnija, stabiņi, sektori)

**Uzdevumi**
43. Saglabā nedēļas temperatūras CSV datnē un izveido līniju diagrammu izklājlapā.
44. Izveido stabiņu diagrammu par lietotāju sadalījumu pa valstīm.
45. Pieraksti, kāds jautājums ir katrai no tavām diagrammām un vai tā uz to atbild.
46. Uzlabo vienu diagrammu: nosaukums, asu paraksti, mērvienības.
47. ★ Izveido to pašu diagrammu ar `matplotlib` un saglabā to kā attēlu.

**Mājasdarbs:** 45. uzdevums

## 11-043 · Licences un izvēle
`jaukta` · FV6 (papīrs)

**Tēma:** Atvērtā koda licences. Bibliotēkas izvēles kritēriji.
**SR:** Salīdzina atvērtā koda licences un pamato bibliotēkas izvēli savam projektam.
**Standarts:** T.V.3.1.5. · T.O.3.1.5.

**Gaita**
- 15' — **FV6** uz papīra, datori vēl aizvērti
- 10' — MIT, GPL, Apache: ko katra atļauj un ko prasa
- 15' — uzdevumi

**Uzdevumi**
48. Burtnīcā: aizpildi tabulu par trim licencēm — vai drīkst pārdot, vai jāatklāj savs kods.
49. Burtnīcā: dotajam scenārijam izvēlies licenci un pamato.
50. Pārbaudi, kāda licence ir bibliotēkām, kuras lieto tavā projektā.
51. ★ Burtnīcā: pieraksti, kas notiek, ja projektā apvieno MIT un GPL bibliotēkas.

**Mājasdarbs:** 50. uzdevums

## 11-044 · Praktikums: no API līdz diagrammai
`prakse`

**Tēma:** Praktikums: pilna datu ķēde no API līdz attēlojumam.
**SR:** Iegūst datus no API, apstrādā, saglabā un attēlo tos.
**Standarts:** T.O.2.4.11. · T.V.2.3.6.

**Gaita**
- 5' — uzdevuma nolasīšana
- 30' — patstāvīgs darbs
- 5' — divi brīvprātīgie rāda rezultātu

**Uzdevumi**
52. Izvēlies vienu API un izveido programmu, kas iegūst datus, tos apstrādā, saglabā CSV un
    sagatavo vienu diagrammu, kas atbild uz konkrētu jautājumu.
53. ★ Papildini programmu tā, lai to var palaist ar dažādiem parametriem no komandrindas.

**Mājasdarbs:** pabeigt

## 11-045 · Atkārtojums
`prakse`

**Tēma:** Bibliotēkas un API: atkārtojums pirms pārbaudes darba.
**SR:** Atkārto bloka prasmes un pārbauda savu darba vidi.
**Standarts:** viss bloks

**Gaita**
- 10' — kopīgi: JSON ceļš līdz vērtībai, statusa kodi, kļūdu apstrāde
- 25' — treniņa uzdevums pārbaudes darba formātā
- 5' — pārbaudi, ka `requests` strādā un `.env` ir vietā

**Uzdevumi**
54. Izpildi treniņa uzdevumu: API → apstrāde → izvade, 25 minūtēs.
55. Pārbaudi, ka tavā datorā ir uzstādītas visas vajadzīgās bibliotēkas.
56. ★ Uzraksti sev atgādni ar piecām lietām, ko pārbaudīt, ja API pieprasījums nestrādā.

**Mājasdarbs:** gatavoties SV3

## 11-046 · Pārbaudes darbs
`pārbaudes darbs`

**Tēma:** Pārbaudes darbs: programma ar ārēju bibliotēku un API.
**SR:** Demonstrē bloka sasniedzamos rezultātus patstāvīgā darbā.
**Standarts:** viss bloks

**Gaita**
- 40' — darbs pie datora; commit ik pēc 10 minūtēm

**Materiāli:** SV3 — divi varianti, datora darbs (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Ja skolas tīklā API nedarbojas**, viss bloks nesabrūk: `teorija.py` §4 ir saglabāts JSON
  piemērs, un uzdevumus var pildīt ar to. Pārbaudi tīklu **pirms** 11-037, nevis stundas laikā.
- **Ja `pip install` ir liegts**, `requests` vietā strādā standarta bibliotēkas
  `urllib.request` — kods ir garāks, bet dara to pašu. §5 ir abi varianti. Ārējās bibliotēkas
  prasme tad tiek apgūta ar kādu citu, mazāku pakotni.
- **Diagrammas taisām izklājlapā, ne kodā.** Tas ir ātrāk, un standarts to tieši tā arī
  paredz. `matplotlib` ir ★ ceļš tiem, kas grib.
- **API atslēgas stunda nav teorija.** Šie skolēni glabā kodu publiskā repozitorijā. 11-040
  ir vienīgā vieta, kur viņi uzzina, ka atslēga kodā nozīmē atslēgu internetā uz visiem laikiem.
