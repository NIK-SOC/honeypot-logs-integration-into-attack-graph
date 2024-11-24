# Fontos fogalmak a tanulmányokból

## Kiberbiztonság
**Mit jelent?**  
Az informatikai rendszerek és eszközök védelme a kiberfenyegetésektől, mint például támadások, adatlopások vagy rendszerek működésképtelenné tétele.

**Kontextus:**  
A digitális eszközök terjedésével nő a kiberfenyegetések száma és komplexitása, különösen az IoT területén.

---

## Security Operation Center (SOC)
**Mit jelent?**  
Egy olyan központ, amely a kiberbiztonsági események monitorozásáért és kezeléséért felel.

**Funkciók:**
- Adatok gyűjtése és elemzése a rendszerek biztonságáról.
- Támadások felismerése és visszakövetése.

**Példa:**  
Az Óbudai Egyetem SOC rendszere, amely a támadási gráfokat is felhasználja a védelem erősítésére.

---

## Cyber Threat Intelligence (CTI)
**Mit jelent?**  
A CTI kiberfenyegetésekre vonatkozó információk gyűjtését, elemzését és megosztását jelenti. Ezek az információk segítenek a szervezeteknek megérteni, milyen fenyegetések leselkednek rájuk, és hogyan tudják ezeket kivédeni.

**Példák:**
- Támadási IP-címek.
- Malware minták.
- Támadók által használt taktikák és technikák.

**Miért fontos?**  
Az IT és OT rendszerekben kulcsfontosságú a fenyegetések gyors és pontos azonosítása.

---

## Támadási gráfok
**Mit jelent?**  
Egy gráf, amely vizualizálja, hogyan tud egy támadó lépésről lépésre behatolni egy rendszerbe.

**Példa:**  
Egy támadó először egy gyenge jelszóval rendelkező hálózati eszközön keresztül fér hozzá a rendszerhez, majd onnan eléri az adatbázisokat.

**Miért hasznos?**  
Segít a rendszergazdáknak azonosítani a sérülékeny pontokat és megtervezni a védekezési stratégiákat.

---

## Támadási mintázatok (Attack Patterns)
**Mit jelent?**  
Olyan mintázatok, amelyek leírják, hogyan használnak a támadók bizonyos gyengeségeket.

**Kapcsolat:**  
A gráfban a támadási mintázatok csomópontokként jelennek meg, és kapcsolódnak más objektumokhoz (pl. malware-hez vagy sebezhetőségekhez).

---

## Sebezhetőség (Vulnerability)
**Mit jelent?**  
Egy informatikai rendszer gyengesége, amelyet támadók kihasználhatnak.

**Példa:**  
Egy rosszul konfigurált hálózati eszköz, amely lehetővé teszi illetéktelen hozzáférést.

---

## Operational Technology (OT)
**Mit jelent?**  
Az OT olyan rendszereket jelöl, amelyek fizikai folyamatokat irányítanak (például gyárak, energiatermelés, közlekedés).

**Miért különleges?**
- Az OT rendszerek gyakran elavult technológiákra épülnek, amelyeket eredetileg nem kiberbiztonsági szempontok szerint terveztek.
- Egy támadás az OT rendszerek ellen például gyártási folyamatokat állíthat meg, vagy áramszünetet okozhat.

**Példák:**
- Egy ipari robotvezérlő rendszere.
- Egy vízszivattyú vezérlőrendszere.

---

## IT és OT közötti különbségek
**IT (Information Technology):**
- Főleg az adatok tárolására, feldolgozására és megosztására koncentrál.
- Példa: Adatbázisok, ügyfélkapcsolati rendszerek.

**OT (Operational Technology):**
- Fizikai gépek és folyamatok irányítására szolgál.
- Példa: Egy szivattyú vezérlőrendszere.

**Miért fontos?**  
Az IT rendszerek általában könnyebben védhetők, míg az OT rendszerek leállása súlyos gazdasági vagy fizikai következményekkel járhat.

---

## Honeypot logok
**Mit jelent?**  
A honeypot logok olyan naplófájlok, amelyek a honeypot rendszerekben keletkeznek, és a támadók tevékenységeit, viselkedését rögzítik. A honeypot rendszerek szándékosan sérülékeny környezetek, amelyeket a támadók becsapására és megfigyelésére használnak.

**Funkciók:**
- Rögzítik a támadók IP-címét, használt eszközeit és technikáit.
- Információt szolgáltatnak a támadások céljairól és módszereiről.

**Példa:**  
Egy honeypot rendszerben lévő nyílt SSH-port logolja a támadók által használt bejelentkezési kísérleteket és brute force támadásokat.

**Miért hasznos?**  
- Segít a kiberfenyegetések azonosításában és megértésében.
- Alapvető információkat nyújt a kiberbiztonsági védekezési stratégiák fejlesztéséhez.
- Javítja a fenyegetésekkel kapcsolatos hírszerzést (CTI).

---

## Unified Data Model (Egységes Adatmodell)
**Mit jelent?**  
Egy olyan modell, amely szabványos módon képes leírni az IT és OT rendszerek entitásait, kapcsolatait és fenyegetéseit.

**Miért hasznos?**
- Egyszerűsíti az adatkezelést az IT és OT rendszerek között.
- Megkönnyíti a kiberbiztonsági elemzéseket és az automatizált védelmi rendszerek kialakítását.

---

## STIX (Structured Threat Information Expression)
**Mit jelent?**  
Egy szabványosított formátum, amely kiberfenyegetettségi adatok (mint például malware-ek, támadási módszerek) strukturált leírására szolgál.

**Példák:**
- Malware tulajdonságainak (pl. fájl hash-ek, IP-címek) rögzítése és megosztása más szervezetekkel.

**Miért fontos?**  
Lehetővé teszi a fenyegetettségi adatok egységes és hatékony megosztását, különösen nagy szervezetek vagy kormányzatok között.

---

## Neo4j graf-adatbázis
**Mit jelent?**  
Egy népszerű graf-adatbázis, amely a **Labeled Property Graph (LPG)** modellt használja.

**Fő jellemzők:**
- **Címkézett csomópontok és élek:** A gráf elemei külön tulajdonságokkal rendelkeznek.
- **Cypher nyelv:** Hatékonyan kezeli a gráfok bejárását és a mintakeresést.

**Előny:**  
Gyors gráfbejárás és mintaillesztés az indexmentes szomszédsági megközelítés révén.

---

## APOC (Awesome Procedures on Cypher)
**Mit jelent?**  
A Neo4j kiterjesztése, amely dinamikus gráf létrehozására és adatimportálásra alkalmas.

**Fontos funkciók:**
- **apoc.load.json:** JSON adatok betöltése.
- **apoc.create.node:** Csomópontok létrehozása dinamikusan.
- **apoc.create.relationship:** Kapcsolatok létrehozása.

---
