# Támadási gráf megvalósítása graf-adatbázisban

## **Elméleti háttér**
### **Kiberbiztonság és fenyegetések**
- A kiberfenyegetések egyre gyakoribbak és kifinomultabbak, különösen kritikus szektorokban, mint az energia, egészségügy és pénzügy.
- A becslések szerint 2024-re 22,3 milliárd eszköz csatlakozik az IoT-hoz, amely növeli a támadások kockázatát.

### **Támadási gráfok**
- A támadási gráfok a hálózati biztonsági állapotokat és a támadók viselkedését ábrázolják:
  - **Csomópontok (node):** A hálózat állapotai vagy lépések.
  - **Élek (edge):** Kapcsolatok a csomópontok között.
- Variánsok:
  - Védelmi fák (defense trees).
  - Bayesian támadási gráfok.
- Problémák: méretezhetőség, dinamikus frissíthetőség.

### **STIX formátum**
- A **STIX (Structured Threat Information Expression)** egy szabványosított formátum, amely kiberbiztonsági objektumokat és kapcsolataikat írja le:
  - **STIX Domain Objektumok (SDO):** Például támadási minták, malware, sebezhetőségek.
  - **STIX Kapcsolati Objektumok (SRO):** Például indicates vagy mitigates
  - **STIX Meta Objektumok:** Jelölés-definíciók.

### **Graf-adatbázis**
- A Neo4j graf-adatbázis kiválasztása:
  - **Labeled Property Graph (LPG):** Címkézett tulajdonsággráf-modell.
  - **Cypher lekérdező nyelv:** Hatékony mintázatkeresés és gráfbejárás.

---

## **Módszertan**
### **Adatgyűjtés**
- Nyilvános JSON formátumú mintaadatok:
  - 65 STIX objektum és 90 kapcsolat.
  - Típusok: támadási minták, malware, sebezhetőségek, kapcsolatok.

### **Transzformációs szabályok**
- A STIX objektumok gráf elemekké való átalakítása:
  - **Csomópontok:** Domain objektumok, például malware.
  - **Élek:** Kapcsolatok, például indicates.
  - **Tulajdonságok:** Kulcs-érték párok az objektumokból.

### **Gráf építése**
1. **Csomópontok létrehozása:** Minden domain objektumból.
2. **Kapcsolatok létrehozása:** STIX kapcsolatok vagy hivatkozások alapján.
3. **Beágyazott dokumentumok feldolgozása:** Külön csomópontokká alakítás kapcsolatokkal.

### **Importálási eljárás**
- A Neo4j APOC bővítmény használata:
  - **apoc.load.json:** JSON fájlok betöltése.
  - **apoc.create.node:** Dinamikus csomópontok létrehozása.
  - **apoc.create.relationship:** Dinamikus kapcsolatok létrehozása.

---

## **Eredmények**
### **Gráf modell**
- A gráf domain csomópontokat (pl. malware, kampányok) és kapcsolati éleket tartalmazott.
- A gráf tulajdonságai lehetővé tették a kiberbiztonsági minták és kapcsolatok vizualizációját.

### **Használati eset a Security Operation Centerben (SOC)**
- Az Óbudai Egyetem SOC rendszere integrálta a támadási gráfot:
  - Mintafelismerés sebezhetőségek és fenyegetések esetén.
  - Kapcsolatok vizualizálása a biztonsági objektumok között.

### **Skálázhatóság és hatékonyság**
- A Neo4j LPG modellje és a Cypher nyelv hatékony gráfbejárást biztosított.
- A dinamikus transzformációs szabályok rugalmas importálási folyamatot tettek lehetővé.

---

## **Következtetések**
- A támadási gráfok hatékony eszközök a kiberbiztonsági adatok elemzésére és vizualizálására.
- A STIX alapú adatok Neo4j-be történő integrációja skálázható és hatékony megoldást kínált.
- A kutatás alapot nyújt további gráfegyszerűsítési és valós idejű SOC alkalmazások fejlesztéséhez.

---

Source:
```
@misc{openai2024chatgpt,
  author       = {OpenAI},
  title        = {ChatGPT language model},
  year         = {2024},
  howpublished = {Online},
  url          = {https://chatgpt.com/share/67438dff-3314-8013-82ed-a1222b463370},
  note         = {Accessed: Nov. 24, 2024}
}
```

Created by Sandor R. Bakos