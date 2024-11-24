# Összefoglaló: A támadási gráfok használata a SOC-ok optimalizálásában

## Elméleti háttér
A tanulmány célja, hogy bemutassa a támadási gráfok szerepét és alkalmazási lehetőségeit a Security Operation Center-ek (SOC-ok) optimalizálásában. A támadási gráfok olyan vizualizációs eszközök, amelyek segítenek a hálózati sebezhetőségek és támadási útvonalak feltérképezésében. Ezek az eszközök az **ISO 27001 szabvány** által meghatározott kockázatelemzési folyamat támogatásában játszanak szerepet, ahol azonosítani és rangsorolni kell a sebezhetőségeket, miközben figyelembe veszik a támadók viselkedését és képességeit.

## Módszertan
1. **Támadási gráf fejlesztése**: 
   - A gráf a **STIX adatsémára** épül, amely a kiberfenyegetettséggel kapcsolatos információkat strukturálja.
   - A gráf adatbázis a **Neo4j** technológián alapszik, amely lehetővé teszi az adatok vizualizálását, elemzését és lekérdezését.

2. **Honeypot alapú adatok gyűjtése**:
   - A SOC-hoz honeypotok kapcsolódnak, amelyek támadási mintákat és eszközöket rögzítenek.
   - **Capture The Flag (CTF)** játékok segítségével gyűjtött adatok támadási gráfokba kerülnek.

3. **Támadók profilozása**:
   - Támadói jellemzők meghatározása, mint például:
     - Eszközök, technikák
     - Képességek
     - Célzott támadások
   - Ezeket az információkat támadási gráfok optimalizálására használják.

4. **IDS/IPS optimalizáció**:
   - Támadási gráfok alapján finomhangolják az **IDS/IPS rendszereket**, hogy csökkentsék a hamis pozitív és negatív riasztások arányát.

## Eredmények
- A támadási gráfok hozzájárulnak a SOC folyamatainak optimalizálásához:
  - **Kockázatelemzés**: Segít a sebezhetőségek és a támadási útvonalak azonosításában és rangsorolásában.
  - **Támadók viselkedésének előrejelzése**: A gráfok segítségével előre jelezhetők a támadók következő lépései.
  - **IDS/IPS hatékonyság növelése**: Finomhangolás a gráfok és elemzések alapján.

- A gráfok lehetővé teszik:
  - A támadási lépések és kapcsolataik vizualizálását.
  - A védekezési stratégiák kidolgozását.
  
- A kutatás során a gráf-alapú modellek és algoritmusok használata segítette az összetett hálózati problémák egyszerűsítését és elemzését.

## Konklúzió
A tanulmány rávilágít, hogy a támadási gráfok alkalmazása a SOC-ok működésében jelentős előnyökkel jár. A gráfok támogatják a biztonsági események követését, a kockázatértékelést, valamint a támadók viselkedésének elemzését és előrejelzését. Az eredmények kiemelik a gráf-alapú megközelítések kutatási és gyakorlati potenciálját a kiberbiztonság területén.

---

Source:
```
@misc{openai2024chatgpt,
  author       = {OpenAI},
  title        = {ChatGPT language model},
  year         = {2024},
  howpublished = {Online},
  url          = {https://chatgpt.com/share/67438c0d-f444-8013-9afa-0b55f8aaf0eb},
  note         = {Accessed: Nov. 24, 2024}
}
```

Created by Sandor R. Bakos