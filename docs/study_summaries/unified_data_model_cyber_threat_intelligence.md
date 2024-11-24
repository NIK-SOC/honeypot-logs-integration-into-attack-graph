# Összefoglaló: A Unified Data Model for Cyber Threat Intelligence in Operational Technology Networks

## Elméleti háttér

1. **Kiberfenyegetettségi modellek és szabványok**:
   - **STIX (Structured Threat Information Expression):** Széles körben elfogadott szabvány a kiberfenyegetési információk reprezentálására.
   - **ATT&CK Framework:** Az MITRE által kifejlesztett keretrendszer, amely segít azonosítani a fenyegetési taktikákat és technikákat.

2. **IT és OT biztonság közötti különbségek**:
   - **IT:** Adatok bizalmassága és integritása az elsődleges szempont.
   - **OT:** Rendszerek rendelkezésre állása kiemelt fontosságú, mivel közvetlenül hatnak a fizikai folyamatokra.

3. **Támadási gráfok és fenyegetési elemzések**:
   - A támadási gráfok segítségével vizualizálják a támadók potenciális útvonalait az IT és OT rendszerek között.

---

## Módszertan

1. **Adatgyűjtés**:
   - **Elsődleges források:** Nyilvános adatbázisok, mint a STIX és ATT&CK.
   - **Másodlagos források:** OT rendszerek kiberbiztonsági eseteiből származó tapasztalatok.

2. **Egységes adatmodell kidolgozása**:
   - Egy új adatmodellt terveztek, amely az IT és OT rendszerek entitásait és kapcsolatait egyesíti.

3. **Validáció és tesztelés**:
   - Valós támadási szcenáriókon keresztül validálták a modellt.

---

## Eredmények

1. **Egységes adatmodell**:
   - Egy új adatmodellt hoztak létre, amely a STIX szabványra épült, de kiegészült az OT rendszerek sajátosságaival.

2. **Jobb fenyegetettségi átláthatóság**:
   - Az IT és OT rendszerek fenyegetettségi adatainak egységes feldolgozását tette lehetővé.

3. **Gyakorlati alkalmazhatóság**:
   - A modellt ipari környezetekben tesztelték, ahol bizonyítottan növelte a hatékonyságot.

4. **Támadási gráfok fejlesztése**:
   - Az adatmodell javította a támadási gráfok létrehozását és pontosabb elemzéseket tett lehetővé.

---

## Tanulságok és javaslatok

1. **STIX szabvány kiterjesztése**:
   - Az OT-specifikus fenyegetettségi információk kezelése érdekében a STIX szabvány további fejlesztése szükséges.

2. **IT és OT integráció fontossága**:
   - Az IT és OT rendszerek közötti szoros együttműködés elengedhetetlen a modern ipari környezetekben.

3. **További kutatási lehetőségek**:
   - Valós idejű adatelemzés és automatizált támadási gráfok generálása további fejlesztést igényel.

---

Source:
```
@mastersthesis{vijayakumar2020unified,
  title     = {A Unified Data Model for Cyber Threat Intelligence in Operational Technology Networks},
  author    = {Vijayakumar, S.},
  year      = {2020},
  school    = {Eindhoven University of Technology},
  type      = {Master's Thesis},
  url       = {https://research.tue.nl/en/studentTheses/a-unified-data-model-for-cyber-threat-intelligence-in-operational},
  note      = {Accessed: 2024-11-23}
}

@misc{openai2024chatgpt,
  author       = {OpenAI},
  title        = {ChatGPT language model},
  year         = {2024},
  howpublished = {Online},
  url          = {https://chatgpt.com/share/67438b7e-3044-8013-ac54-a2ae7ba48299},
  note         = {Accessed: Nov. 24, 2024}
}
```

Created by Sandor R. Bakos
