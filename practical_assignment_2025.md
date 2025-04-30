**Praktiskā darba uzdevums: Pilnas kaudzes (Full-Stack) izstrāde ar PostgreSQL, Express.js (Knex) un Next.js**

---

## 1. Projekta mērķis  
Izveidot nelielu interneta lietotni, kurā tās lietotājs var apskatīt un pievienot ierakstus datu bāzei. Šis uzdevums nodrošina pieredzi ar:  
- PostgreSQL datu bāzes modelēšanu atbilstoši glabājamajai informācijai
- Express.js servera izveidi un REST API vaicājumiem, izmantojot Knex bibliotēku kā ietvaru datu bāzes operācijām  
- Next.js front-end izstrādi ar vairāku skatu sistēmu  

## 2. Tehnoloģijas
- **Datu bāze:** PostgreSQL  
- **Serveris:** Node.js + Express.js + Knex  
- **Frontend:** Next.js (React) un TailwindCSS 

## 3. Obligātie prasību punkti  
1. **Datu bāze**  
   - Izveido vismaz **trīs** savstarpēji saistītas tabulas (piemērs: `users`, `posts`, `comments`).  
   - Katrai tabulai jābūt primārām atslēgām, ārējām atslēgām (ja tādas nepieciešamas) un atbilstošiem datu tipiem.  

2. **Express.js serveris**  
   - Konfigurē Knex savienojumu ar PostgreSQL.
   - Galvenajai no tabulām (ja nepieciešams - vairāk kā vienai) izstrādāt trīs ceļus/maršrutus (endpoints) - divus `GET` un vienu `POST`. 
   - **GET**  
     - `GET /api/<tabula>` – atgriež visus ierakstus no izvēlētās tabulas.  
     - `GET /api/<tabula>/:id` – atgriež vienu ierakstu pēc tā ID.  
   - **POST**  
     - `POST /api/<tabula>` – pievieno jaunu ierakstu (pieņem datus JSON formātā).  
   - Katra no servera puses funkcijām veic JSON validāciju (piem., pārbaudi obligātos laukus un datu atbilstību/pareizību) un atbilstošu kļūdu apstrādi (400/404/500).  

3. **Next.js frontend**  
   - Izveido **vismaz trīs** dažādus skatus (`page.js` failus strukturētus atbilstoši mājaslapas struktūrai), piemēram:  
     1. **Saraksta skats** – parāda visus ierakstus no kādas tabulas.  
     2. **Detalizētais skats** – parāda vienu ierakstu (izmantojot dinamisku maršrutu, piem. `/posts/[id]`).  
     3. **Ieraksta veidošanas forma** – lapa ar formu jauna ieraksta pievienošanai (`POST /api/<tabula>`).  
   - Izmanto komponentes (.jsx), lai strukturētu vizuālo saskarni, elmentu stiliem izmanto TailwindCSS.  

## 4. Rīcības soļi  
1. **Projektu iestatīšana**
   - Izveido servera puses programmu (`npm init`), instalē Express, Nodemon, Pg un Knex.
   - Inicializē front-end puses tīmekļa programmu ar `npx create-next-app` (bez TypeScript, ar TailwindCSS)
   - Izveido tabulas, izmantojot vai nu SQL Shell vai pgAdmin, ievieto tajās sākuma datus.

3. **Datu bāzes savienojums**  
   - Izveido Knex savienojuma failu. (`/config/db.js`)  

4. **API izstrāde**  
   - Izstrādā Express.js servera failu (`server.js`).  
   - Pievieno GET/POST funkcionalitāti atbilstoši prasībām.  
   - Testē ar Thunder Client vai Postman, vai citu rīku.  

5. **Frontend izstrāde**  
   - Savieno ar servera pusi, izmantojot `fetch()`, lai izgūtu/parādītu datus un pievienotu jaunus ierakstus.
   - Noteikti pielieto arī tādas funkcijas kā `map()` dinamiskai datu izvadei skatos, kur tas ir nepieciešams.

## 5. Atrādīšanas kārtība  
- Demonstrēt funkcionalitāti ar tīmekļa lietotni.  
- Parādīt tīmekļa lietotnes izveidotās komponentes un struktūru.
- Demonstrēt `server.js` failu servera pusē.
- Parādīt SQL CREATE skriptus. Vēlams saglabāt tos teksta vai `.sql` failā.

## 6. Novērtēšanas kritēriji  
| Kritērijs                                                                 | Svars |
|---------------------------------------------------------------------------|-------|
| Datu bāzes struktūra                                                      | 25%   |
| Servera puses izstrāde                                                    | 25%   |
| Front-end funkcionalitāte un dizains                                      | 25%   |
| Koda organizācija                                                         | 15%   |
| Papildus iespējas (piem., DELETE)                                         | 10%   |

---

**Veiksmi izstrādē!** 
