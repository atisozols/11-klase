# ==========================================================
# 03. BIBLIOTĒKAS, API UN DATI NO TĪMEKĻA — DARBA FAILS
# ==========================================================
# Šeit raksti savus risinājumus.
# Teorija, piemēri un atgādne: teorija.py
# Uzdevumu numuri iet cauri visam blokam.
# ==========================================================


# ----------------------------------------------------------
# 11-033 · Modulis un bibliotēka
# ----------------------------------------------------------

# 1. Importē math un aprēķini kvadrātsakni, kāpinājumu un skaitli π.




# 2. Izveido savu moduli paligs.py ar divām funkcijām un importē to citā failā.




# 3. Pārraksti importu trīs dažādos veidos un pieraksti, ar ko tie atšķiras.




# 4. Pārnes savu 01. bloka klasi Gramata atsevišķā modulī un importē to.




# 5. ★ Uzraksti moduli, kurā ir gan funkcijas, gan if _name == "main_": bloks
#    pašpārbaudei. Paskaidro komentārā, kāpēc tas vajadzīgs.





# ----------------------------------------------------------
# 11-034 · Standarta bibliotēka
# ----------------------------------------------------------

# 6. Ar random uzraksti programmu, kas izlozē klases dežurantu no saraksta.




# 7. Ar datetime aprēķini, cik dienu atlicis līdz mācību gada beigām.




# 8. Ar statistics aprēķini atzīmju vidējo, mediānu un modu; salīdzini ar savu ciklu.




# 9. Ar math aprēķini trijstūra hipotenūzu.




# 10. ★ Ar random uzraksti programmu, kas ģenerē 1000 kauliņu metienus un pārbauda, vai
#    katrs skaitlis parādās aptuveni vienādi bieži.





# ----------------------------------------------------------
# 11-035 · Ārēja bibliotēka
# ----------------------------------------------------------

# 11. Uzstādi bibliotēku requests un pārbaudi, ka imports strādā.




# 12. Atrodi requests dokumentācijā, kā nosūtīt pieprasījumu ar parametriem, un pieraksti
#    piemēru komentārā.




# 13. Izveido requirements.txt ar savām bibliotēkām.




# 14. Atrodi PyPI vietnē bibliotēku, kas prot kaut ko tavam projektam noderīgu, un pieraksti
#    tās nosaukumu, licenci un pēdējās versijas datumu.




# 15. ★ Salīdzini divas bibliotēkas, kas dara vienu un to pašu, un pamato, kuru izvēlētos.





# ----------------------------------------------------------
# 11-036 · JSON
# ----------------------------------------------------------

# 16. Dotajā JSON tekstā atrodi un izvadi trīs vērtības.




# 17. Pārveido Python vārdnīcu par JSON tekstu un saglabā to datnē.




# 18. Nolasi JSON datni un izveido no tās objektu sarakstu (izmanto 01. bloka klasi).




# 19. Dotajā ligzdotajā JSON izvadi visu masīva elementu kādu lauku.




# 20. ★ Uzraksti funkciju, kas droši paņem vērtību no ligzdotas struktūras un atgriež
#    noklusējumu, ja ceļa nav.





# ----------------------------------------------------------
# 11-037 · Dati no API
# ----------------------------------------------------------

# 21. Iegūsti datus no https://api.chucknorris.io/jokes/random un izvadi tikai joka tekstu.




# 22. Iegūsti nejaušu lietotāju no https://randomuser.me/api/ un izvadi vārdu, valsti un e-pastu.




# 23. Uzraksti programmu, kas iegūst 10 lietotājus un saglabā tos CSV datnē.




# 24. Izvadi API atbildes statusa kodu un paskaidro, ko tas nozīmē.




# 25. ★ Atrodi data.gov.lv datu kopu, iegūsti to ar programmu un izvadi pirmos piecus ierakstus.





# ----------------------------------------------------------
# 11-038 · API parametri
# ----------------------------------------------------------

# 26. Iegūsti Tukuma laikapstākļu prognozi un izvadi šodienas temperatūru.




# 27. Papildini programmu tā, lai pilsētas koordinātas prasa lietotājam.




# 28. Iegūsti septiņu dienu prognozi un izvadi katras dienas augstāko temperatūru.




# 29. Aprēķini nedēļas vidējo temperatūru no saņemtajiem datiem.




# 30. ★ Salīdzini divu pilsētu prognozes un izvadi, kurā būs siltāk.





# ----------------------------------------------------------
# 11-039 · Praktikums: API
# ----------------------------------------------------------

# 31. Vārdu saraksts. Programma iegūst 20 nejaušus lietotājus, atlasa tikai tos no Eiropas
#    un saglabā CSV datnē ar vārdu, valsti un vecumu.




# 32. Laikapstākļu atskaite. Programma iegūst nedēļas prognozi un izvada dienu skaitu, kad
#    temperatūra būs zem nulles, un aukstāko dienu.




# 33. ★ Kešošana. Papildini kādu no programmām tā, lai tā saglabā atbildi datnē un otrreiz
#    to neprasa no API, ja datne nav vecāka par stundu.





# ----------------------------------------------------------
# 11-040 · API atslēgas un drošība
# ----------------------------------------------------------

# 34. Pārnes API atslēgu no koda uz .env datni un ielasi to programmā.




# 35. Pievieno .env savam .gitignore un pārbaudi ar git status.




# 36. Izveido .env.paraugs ar tukšām vērtībām, ko var droši komitēt.




# 37. ★ Atrodi internetā piemēru, kur atslēgas noplūde radījusi reālas sekas, un pieraksti,
#    kas notika.





# ----------------------------------------------------------
# 11-041 · Kļūdu apstrāde
# ----------------------------------------------------------

# 38. Papildini savu API programmu ar try/except, lai tā nekrīt bez interneta.




# 39. Pārbaudi statusa kodu un izvadi saprotamu paziņojumu, ja tas nav 200.




# 40. Pievieno taimautu un pārbaudi, kas notiek, ja serveris neatbild.




# 41. Apstrādā gadījumu, kad atbildē trūkst gaidītā lauka.




# 42. ★ Uzraksti funkciju, kas mēģina pieprasījumu trīs reizes, pirms padodas.





# ----------------------------------------------------------
# 11-042 · Datu attēlošana
# ----------------------------------------------------------

# 43. Saglabā nedēļas temperatūras CSV datnē un izveido līniju diagrammu izklājlapā.




# 44. Izveido stabiņu diagrammu par lietotāju sadalījumu pa valstīm.




# 45. Pieraksti, kāds jautājums ir katrai no tavām diagrammām un vai tā uz to atbild.




# 46. Uzlabo vienu diagrammu: nosaukums, asu paraksti, mērvienības.




# 47. ★ Izveido to pašu diagrammu ar matplotlib un saglabā to kā attēlu.





# ----------------------------------------------------------
# 11-043 · Licences un izvēle
# ----------------------------------------------------------

# 48. Burtnīcā: aizpildi tabulu par trim licencēm — vai drīkst pārdot, vai jāatklāj savs kods.




# 49. Burtnīcā: dotajam scenārijam izvēlies licenci un pamato.




# 50. Pārbaudi, kāda licence ir bibliotēkām, kuras lieto tavā projektā.




# 51. ★ Burtnīcā: pieraksti, kas notiek, ja projektā apvieno MIT un GPL bibliotēkas.





# ----------------------------------------------------------
# 11-044 · Praktikums: no API līdz diagrammai
# ----------------------------------------------------------

# 52. Izvēlies vienu API un izveido programmu, kas iegūst datus, tos apstrādā, saglabā CSV un
#    sagatavo vienu diagrammu, kas atbild uz konkrētu jautājumu.




# 53. ★ Papildini programmu tā, lai to var palaist ar dažādiem parametriem no komandrindas.





# ----------------------------------------------------------
# 11-045 · Atkārtojums
# ----------------------------------------------------------

# 54. Izpildi treniņa uzdevumu: API → apstrāde → izvade, 25 minūtēs.




# 55. Pārbaudi, ka tavā datorā ir uzstādītas visas vajadzīgās bibliotēkas.




# 56. ★ Uzraksti sev atgādni ar piecām lietām, ko pārbaudīt, ja API pieprasījums nestrādā.
