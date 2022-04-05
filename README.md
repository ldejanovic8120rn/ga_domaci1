# Genetski algoritmi - domaci 1

### 1. Zadatak je implementiran u programskom jeziku - Python
### 2. Eksterne biblioteke koje program koristi su:
  - subprocess
  - math
  - random

### 3. Način konfigurisanje programa:
  - Može se kreirati po želji konfiguracioni fajl, koji će biti prosleđen programu preko komandne linije
  - U konfiguracionom fajlu zadavati parametre u obliku: POP_NUM=10 
  - Primer konfiguracionog fajla - [config1.txt](https://github.com/ldejanovic8120rn/ga_domaci1/blob/master/config1.txt)
  - Parametri konfiguracionog fajla (mogu biti u proizvoljnom redosledu i ne moraju svi biti navedeni):
    - **POP_NUM** - broj populacije (int)
    - **NPOP_NUM** - broj dobijenih jedinki (int)
    - **COEFF_NUM** - broj koeficijenta (int)
    - **BITS_NUM** - broj bitova za kodovanje/dekodovanje koeficijenta (int)
    - **P_L** - donja granica intervala za koeficijente
    - **P_H** - gornja granica intervala za koeficijente
    - **TOURNAMENT_SIZE** - broj jedinki koje učestvuju u odabiru za parenje
    - **PROBABILITY** - verovatnoća mutacije
    - **MAX_ITER** - maksimalan broj generacija

### 4. Kompajliranje g.c programa:
  - Potrebno je pre pokretanja kompajlirati g.c program ili otkomentarisati metodu **compile_c_program()**, koja automatski kompajlira g.c program i nakon toga se može pokrenuti program komandom navedenom u koraku 5.

### 5. Kod se može pokrenuti na lokalnoj mašini komandom:
```bash
python main.py
```
