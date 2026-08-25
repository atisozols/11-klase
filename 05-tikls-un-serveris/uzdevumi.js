// ==========================================================
// 05. TĪKLS, SERVERIS, DROŠĪBA, MAŠĪNMĀCĪŠANĀS — DARBA FAILS
// ==========================================================
// Šeit raksti savus risinājumus.
// Teorija, piemēri un atgādne: teorija.js
// Uzdevumu numuri iet cauri visam blokam.
// ==========================================================


// ----------------------------------------------------------
// 11-063 · Klients un serveris
// ----------------------------------------------------------

// 1. Burtnīcā: uzzīmē soļus no adreses ievadīšanas līdz lapas parādīšanai.




// 2. Burtnīcā: pieraksti, kura daļa notiek tavā datorā un kura — kaut kur citur.




// 3. Ar komandu ping noskaidro kādas vietnes IP adresi un pieraksti to.




// 4. ★ Noskaidro, cik ilgi ceļo pieprasījums līdz serverim Latvijā un līdz serverim ASV.
//    Kāpēc atšķiras?





// ----------------------------------------------------------
// 11-064 · HTTP
// ----------------------------------------------------------

// 5. Atver DevTools cilni Network un pieraksti, cik pieprasījumu veic viena mājaslapa.




// 6. Atrodi vienu pieprasījumu un pieraksti tā metodi, statusa kodu un atbildes izmēru.




// 7. Atrodi lapu, kas atgriež 404, un pieraksti, kā pārlūks to parāda.




// 8. Pieraksti, ko nozīmē kodi 200, 301, 400, 401, 404, 500.




// 9. ★ Atrodi pieprasījumu, kas atgriež JSON, nevis HTML, un pieraksti tā adresi.





// ----------------------------------------------------------
// 11-065 · Pirmais serveris
// ----------------------------------------------------------

// 10. Izveido projektu ar npm init -y un uzstādi Express.




// 11. Uzraksti serveri, kas uz / atbild ar tekstu Sveika, pasaule.




// 12. Pievieno maršrutu /laiks, kas atgriež pašreizējo laiku.




// 13. Pievieno maršrutu /sveiciens/anna, kas atbild ar Sveika, anna.




// 14. ★ Pievieno maršrutu, kas atgriež nejaušu skaitli no 1 līdz 6, un atsvaidzini lapu
//    piecas reizes.





// ----------------------------------------------------------
// 11-066 · Maršruti un JSON
// ----------------------------------------------------------

// 15. Izveido maršrutu /skoleni, kas atgriež JSON masīvu ar trim izdomātiem skolēniem.




// 16. Izveido maršrutu /skoleni/:id, kas atgriež vienu skolēnu pēc id.




// 17. Ja tāda id nav, atgriez statusa kodu 404 un paskaidrojumu JSON formātā.




// 18. Izveido maršrutu, kas pieņem parametru ?klase=11.a un atgriež tikai tos skolēnus.




// 19. ★ Pievieno parametru ?kartot=uzvards un atgriez sakārtotu sarakstu.





// ----------------------------------------------------------
// 11-067 · Klients: fetch un DOM
// ----------------------------------------------------------

// 20. Izveido HTML lapu, kas ar fetch paņem datus no /skoleni un izvada tos konsolē.




// 21. Attēlo saņemtos skolēnus kā sarakstu lapā.




// 22. Attēlo tos tabulā ar diviem stabiņiem.




// 23. Pievieno pogu, kas datus pārlādē no jauna.




// 24. ★ Pievieno ievades lauku, kas filtrē sarakstu pēc uzvārda, nepieprasot datus no jauna.





// ----------------------------------------------------------
// 11-068 · Datubāze serverī
// ----------------------------------------------------------

// 25. Pieslēdz skola.db savam serverim ar Knex un izvadi skolēnu skaitu konsolē.




// 26. Pārtaisi maršrutu /skoleni tā, lai dati nāk no datubāzes.




// 27. Izveido maršrutu /klases, kas atgriež klases ar skolēnu skaitu katrā.




// 28. Izveido maršrutu /skoleni/:id/atzimes, kas atgriež viena skolēna atzīmes ar priekšmetu
//    nosaukumiem.




// 29. ★ Pievieno maršrutu, kas atgriež katras klases vidējo atzīmi, sakārtotu dilstoši.





// ----------------------------------------------------------
// 11-069 · Pilna ķēde
// ----------------------------------------------------------

// 30. Izveido lapu, kas rāda visu klašu sarakstu ar skolēnu skaitu, ņemot datus no datubāzes.




// 31. Pievieno iespēju uzklikšķināt uz klases un redzēt tās skolēnus.




// 32. ★ Pievieno katram skolēnam vidējo atzīmi, aprēķinātu datubāzē, nevis pārlūkā.





// ----------------------------------------------------------
// 11-070 · POST un formas
// ----------------------------------------------------------

// 33. Pievieno maršrutu POST /pulcini, kas pieņem jaunu pulciņu un ievieto to datubāzē.




// 34. Izveido formu lapā, kas nosūta datus uz šo maršrutu.




// 35. Pievieno validāciju serverī: nosaukums nedrīkst būt tukšs, vietu skaits — pozitīvs.




// 36. Ja dati nav derīgi, atgriez statusa kodu 400 un paskaidrojumu.




// 37. ★ Pēc veiksmīgas pievienošanas atsvaidzini sarakstu lapā, nepārlādējot visu lapu.





// ----------------------------------------------------------
// 11-071 · Kļūdu apstrāde serverī
// ----------------------------------------------------------

// 38. Papildini visus savus maršrutus ar try/catch.




// 39. Atgriez 404, ja ieraksta nav, un 400, ja dati nav derīgi.




// 40. Pārbaudi, kas notiek, ja datubāzes fails ir pārsaukts. Panāc, lai serveris nekrīt.




// 41. Attēlo kļūdas paziņojumu lapā lietotājam saprotamā valodā.




// 42. ★ Pieraksti, kāpēc kļūdas tekstā nedrīkst nokļūt SQL vaicājums vai faila ceļš.





// ----------------------------------------------------------
// 11-072 · Lokālais tīkls
// ----------------------------------------------------------

// 43. Noskaidro sava datora lokālo IP adresi un pieraksti to.




// 44. Palaid savu serveri un atver to no klasesbiedra datora, izmantojot IP adresi.




// 45. Pāros: izveido telefona karstvietu ar paroli un pieslēdz tai otru ierīci.




// 46. Pieraksti, ar ko atšķiras lokālā un publiskā IP adrese.




// 47. ★ Noskaidro, kas ir portu pāradresācija, un pieraksti, kāpēc tā ir drošības risks.





// ----------------------------------------------------------
// 11-073 · Drošība
// ----------------------------------------------------------

// 48. Uzraksti programmu, kas aprēķina teksta jaucējvērtību, un pārbaudi, ka vienādam tekstam
//    tā vienmēr ir vienāda.




// 49. Pārbaudi, kas notiek ar jaucējvērtību, ja tekstā maina vienu burtu.




// 50. Pievieno savai datubāzei tabulu lietotaji, kurā parole glabājas kā jaucējvērtība.




// 51. Uzraksti pārbaudi, kas salīdzina ievadīto paroli ar saglabāto.




// 52. ★ Noskaidro, kas ir «sāls» (salt) un kāpēc ar to jaucējvērtība kļūst drošāka.





// ----------------------------------------------------------
// 11-074 · Mašīnmācīšanās
// ----------------------------------------------------------

// 53. Burtnīcā: dotajiem pieciem uzdevumiem atzīmē, kuriem der parasts algoritms un kuriem
//    mašīnmācīšanās.




// 54. Burtnīcā: pieraksti, kādi dati būtu vajadzīgi, lai iemācītu programmu atpazīt surogātpastu.




// 55. ★ Pieraksti piemēru, kur nepilnīgi ievaddati padarītu teorētiski labu risinājumu par
//    nederīgu.





// ----------------------------------------------------------
// 11-075 · Mašīnmācīšanās praksē un ētika
// ----------------------------------------------------------

// 56. Izmēģini gatavu tiešsaistes risinājumu un atrodi gadījumu, kad tas kļūdās.




// 57. Pieraksti, kāpēc, tavuprāt, tas kļūdījās.




// 58. Diskusijai: uzraksti vienu argumentu par un vienu pret mašīnmācīšanās lietošanu skolēnu
//    darbu vērtēšanā.




// 59. ★ Atrodi rakstu par neobjektīviem datiem mašīnmācīšanā un uzraksti trīs teikumu kopsavilkumu.
