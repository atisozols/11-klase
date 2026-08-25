# 04. bloks — teorija un paraugi

Šis ir bloka atgādne. Uzdevumus pildi [`uzdevumi.md`](uzdevumi.md) failā.

## §1 Kāpēc programmatūra neizdodas

Visbiežākais iemesls nav slikts kods, bet gan tas, ka izstrādātājs uzbūvēja ko citu, nekā
pasūtītājam vajadzēja. Starp «vajag sistēmu pieteikumiem» un strādājošu programmu ir simtiem
lēmumu, un katru no tiem kāds pieņem — vai nu pasūtītājs apzināti, vai izstrādātājs uz labu
laimi.

**Specifikācija ir vieta, kur šie lēmumi tiek pierakstīti pirms rakstīšanas.** Tā aizsargā
abus: pasūtītāju no tā, ka saņem ko citu, un izstrādātāju no tā, ka «tas taču bija skaidrs».

## §2 Ieinteresētās puses

Ieinteresētā puse ir ikviens, kuru risinājums ietekmē. Skolas ēdnīcas sistēmā tie ir skolēni,
ēdnīcas darbinieki, grāmatvedība, administrācija un vecāki, kas maksā.

**Mērķauditorija ir tā puse, kuras vajadzības risinājums risina pirmām kārtām.** «Visi» nav
atbilde — risinājums, kas domāts visiem, parasti neder nevienam. Izvēlies vienu un pieraksti,
kāpēc tieši to.

## §3 Izpētes metodes

| Metode | Ko dod | Ko nedod | Cik ilgi |
| --- | --- | --- | --- |
| Intervija | dziļu izpratni, negaidītas atbildes | skaitļus, vispārinājumu | 20–40 min uz cilvēku |
| Aptauja | skaitļus, sadalījumu | konteksta, «kāpēc» | 15 min izveide, dienas gaidīšana |
| Novērojums | ko cilvēks **tiešām** dara | ko viņš domā un jūt | 30–60 min |
| Esošo risinājumu analīze | ātru priekšstatu, idejas | tavas mērķauditorijas specifiku | 30 min |

Divas metodes ir labāk nekā viena: intervija pasaka **kāpēc**, aptauja pasaka **cik daudz**.

Cik cilvēku pietiek? Piecas intervijas atklāj lielāko daļu problēmu. Aptaujai jācenšas pēc
20 un vairāk.

## §4 Intervijas jautājumi

**Slikts:** «Vai tev nešķiet, ka pašreizējā sistēma ir neērta?»
Tas pasaka, kādu atbildi tu gaidi, un pieklājīgs cilvēks tev piekritīs.

**Labs:** «Pastāsti, kā tu pēdējo reizi pieteicies pulciņam.»

Likumi:
1. **Jautā par pagātni, ne par nākotni.** «Ko tu darīji pagājušajā nedēļā» ir ticams;
   «vai tu lietotu šādu lietotni» ir minējums.
2. **Atvērts, ne slēgts.** Jautājums, uz kuru var atbildēt ar «jā», parasti tā arī tiek
   atbildēts.
3. **Neuzspied atbildi.** Ja jautājumā ir vārds «neērti», atbildē tas būs arī.
4. **Klusē.** Pēc atbildes pagaidi. Otra puse bieži turpina, un tieši tur ir vērtīgākais.
5. **Pieraksti citātus, ne kopsavilkumus.** Pēc nedēļas «viņam nepatika process» neko nenozīmē.

## §5 Aptauja

Jautājumu veidi:

- **izvēle** — kad atbilžu ir maz un tās zināmas iepriekš;
- **skala 1–5** — kad mēra apmierinātību vai biežumu;
- **atvērts** — ne vairāk par diviem; tos ir grūti apstrādāt.

Datu validācija aptaujā ir tas pats, kas validācija programmā: neļauj ievadīt vecumu 200 vai
tukšu obligāto lauku. Ja to nedari, apstrādes brīdī dati būs jāsakārto ar roku.

## §6 Lietotāja stāsti

Forma:

> Kā **[loma]** es gribu **[darbību]**, lai **[ieguvums]**.

Piemēri:

> Kā skolēns es gribu redzēt brīvās vietas pulciņā, lai zinātu, vai vēl var pieteikties.
>
> Kā pulciņa vadītājs es gribu redzēt dalībnieku sarakstu, lai zinātu, cik vietu vēl ir.

Stāsts ir par lielu, ja tajā ir vārds «un» vai ja to nevar izdarīt vienā stundā. Tad to sadala.

## §7 Prasības

**Funkcionālā prasība** — ko sistēma dara:

> Sistēma ļauj skolēnam pieteikties pulciņam, ja tajā ir brīvas vietas.

**Nefunkcionālā prasība** — cik labi tā to dara:

> Saraksta ielāde nav ilgāka par 2 sekundēm ar 500 ierakstiem.

Prasība, kuru nevar pārbaudīt, nav prasība. «Programmai jābūt ērtai» nav prasība.
«Pieteikšanās aizņem ne vairāk par trim klikšķiem» ir.

Katra prasība sākas ar «Sistēma …» un apraksta vienu lietu.

## §8 Struktūrskices

Skice nav dizains. Tajā ir kastītes, uzraksti un pogas — nav krāsu, fontu un attēlu. Mērķis
ir vienoties par to, **kas** ir ekrānā un **kur**, nevis kā tas izskatās.

Katrai skicei pieraksti, kas notiek, nospiežot katru pogu. Puse nesaprašanās rodas tieši tur.

## §9 Projekta vadība

Labs uzdevums ir tāds, ko var izpildīt vienā stundā un par kuru var pateikt «gatavs» vai
«nav gatavs». «Uztaisīt sistēmu» nav uzdevums. «Izveidot tabulu `pieteikumi` un pievienot
tai trīs testa ierakstus» ir.

GitHub Projects dēlis ar trim kolonnām pilnīgi pietiek. Uzdevums, kas «Procesā» stāv divas
nedēļas, ir vai nu par lielu, vai iestrēdzis — abos gadījumos ar to kaut kas jādara.

## §10 Laika plānošana

06. blokā ir 24 stundas. No tām aizstāvēšanai aiziet 2, testēšanai un labošanai 3,
dokumentācijai 2. Izstrādei paliek aptuveni 15.

Tāpēc plānā vajadzīgas divas lietas:

1. **Starpposmi** — kas būs gatavs 8. un 16. stundā;
2. **Saraksts «ko izmetīšu»** — prasības, no kurām atteiksies, ja pietrūks laika. Šo
   sarakstu uzraksti **tagad**, kamēr esi mierīgs, nevis pēdējā nedēļā.
