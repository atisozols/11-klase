# Vērtēšanas kārtība — programmēšana

## Vērtēšanas veidi

| | Kad | Kā vērtē |
| --- | --- | --- |
| **Diagnosticējošā** | Kursa un bloka sākumā | Bez vērtējuma; nosaka, ar ko sākt |
| **Formatīvā (FV)** | Bloka vidū, katru otro nedēļu | Atgriezeniskā saite, apguves līmenis (i/ni, %) |
| **Summatīvā (SV)** | Bloka noslēgumā | 10 ballu skala |

## Darbu forma

Katrs pārbaudes darbs ir **vai nu papīra, vai datora darbs**. Šos divus veidus nekad
neapvieno vienā darbā: ja dators ir vaļā praktiskajai daļai, tad prasība “neizpildi kodu”
nav izpildāma, un tāds uzdevums vairs neko nemēra.

### Papīra darbs

Dators ir aizvērts. Skolēns raksta ar roku:

- izseko koda izpildi un pieraksta izvadi;
- atrod un izlabo kļūdas dotā kodā;
- skaidro jēdzienus un pamato izvēli;
- **uzraksta koda fragmentus ar roku**.

Šis ir vienīgais formāts, kas pilnībā pasargā no AI rīkiem, un tas prasa sintaksi no galvas.
Vērtējot ar roku rakstītu kodu, sīkas sintakses neprecizitātes, kas neietekmē loģiku
(viena aizmirsta kols, trūkstošas pēdiņas), atskaita ne vairāk kā 1 punktu no uzdevuma.

### Datora darbs

Skolēns raksta un palaiž programmu pēc dotas specifikācijas. Atļauta Python dokumentācija un
w3schools — tieši tā, kā to nosaka centralizētā eksāmena programma. **Nav atļauti** AI rīki.
Kods jāsaglabā repozitorijā vismaz reizi 10 minūtēs; darba pieaugums commit vēsturē ir daļa
no darba.

### Kurā klasē kurš formāts

| Nr. | Forma | Kāpēc tieši tā |
| --- | --- | --- |
| SV1 | papīrs | OOP jēdzieni un koda lasīšana — svarīgs domu gājiens, ne rezultāts |
| SV2 | biļetes | SQL vaicājumu var uzrakstīt un tūlīt pamatot mutiski |
| SV3 | dators | rezultāts ir strādājoša programma ar ārēju API |
| SV4 | biļetes | skolēns aizstāv **savu** izpēti un specifikāciju |
| SV5 | papīrs | tīkla un drošības jēdzieni, HTTP izpratne |
| SV6 | dators | projekts un tā aizstāvēšana |

Formatīvās pārbaudes arī ir vienā formātā katra, bet tur formāta izvēle ir brīvāka:
papīrs, kad jāpārbauda izpratne, dators, kad jāpārbauda, vai programma strādā.

Papīra darbus izdrukā no `.md` faila (`sv-fv` repozitorijā):

```
npx md-to-pdf 11-klase/sv/sv1-a.md --config-file pdf-config.js
```

### Biļetes

SV2 un SV4 notiek biļešu formā: skolēns velk biļeti un atbild mutiski, vajadzības gadījumā
rakstot kodu uz tāfeles vai rādot savu darbu ekrānā. Biļetes ir vienīgais formāts, kurā var
pārbaudīt, vai skolēns saprot **savu** darbu — tāpēc SV4 ir tieši tāds.

## Vērtējuma veidošanās

| Darbs | Īpatsvars |
| --- | --- |
| SV1–SV5 | 65 % |
| SV6 — gala projekts un aizstāvēšana (bloks 06) | 35 % |

## Snieguma līmeņu apraksts (SLA)

Visos praktiskajos darbos programmēšanas labās prakses principu ievērošana tiek vērtēta
atsevišķi pēc šī apraksta (tāda pati skala kā centralizētajā eksāmenā):

| Sācis apgūt | Turpina apgūt | Apguvis | Apguvis padziļināti |
| --- | --- | --- | --- |
| Labās prakses principus lieto lielākajā daļā koda, bet nekonsekventi vai daļēji korekti | Lieto kopumā korekti un konsekventi, pieļaujot dažas neprecizitātes | Lieto korekti un konsekventi | Lieto vienmēr korekti un konsekventi, pats piedāvā un izmanto līdzīgus principus |

**Labās prakses principi:**

1. Katru atsevišķu priekšrakstu raksta jaunā rindā.
2. Koda loģiskās daļas atdala ar tukšu rindu.
3. Izmanto atkāpes, lai parādītu struktūru iekļaušanu citās struktūrās.
4. Izvairās no garām koda rindām.
5. Mainīgo un funkciju nosaukumus veido jēgpilnus.
6. Ar komentāriem skaidro koda loģiskās daļas.

## Kur glabājas darbi

Pārbaudes darbu varianti un vērtēšanas kritēriji **neatrodas šajā repozitorijā vispār**.
Tie ir atsevišķā privātā repozitorijā `sv-fv`:

```
sv-fv/11-klase/fv/   FV1, FV2 …   formatīvās pārbaudes
sv-fv/11-klase/sv/   SV1 …        varianti A un B, kritēriji un atbildes
```

Stundu ikdienas uzdevumi **nav** pārbaudes darbi — tie ir bloka `README.md` pie attiecīgās
stundas un ir publiski pieejami.

Formatīvās pārbaudes netiek publicētas tāpēc, ka iepriekš redzams uzdevums nemēra neko:
skolēns var atnākt ar jau sagatavotu risinājumu. Ja gribi kādu variantu vēlāk padarīt par
treniņu materiālu, nokopē to uz bloka katalogu. Kritērijus un atbildes nekopē nekad.

## Uzlabošana

Katru SV var uzlabot vienu reizi konsultāciju laikā divu nedēļu laikā pēc darba
saņemšanas. Uzlabotais vērtējums aizstāj iepriekšējo.

## Diferenciācija

Katrā stundā uzdevumi ir divos līmeņos:

- **B (bāze)** — jāprot visiem; ar šiem uzdevumiem strādā kopā;
- **★** — papilduzdevums tiem, kas bāzi paveic ātrāk. ★ uzdevumi neietekmē vērtējumu
  negatīvi, bet tiek ņemti vērā, veidojot semestra vērtējumu, un ir ieejas punkts
  algoritmu treniņu trasei (skat. `kurss/zvaigznu-trase.md`).

Pārbaudes darbos ★ līmeņa uzdevums ir pēdējais un dod punktus, kas ļauj sasniegt
augstāko vērtējumu, bet nav nepieciešams, lai iegūtu labu vērtējumu.
