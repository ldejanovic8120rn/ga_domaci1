# Genetski algoritmi - domaci 1

### 1. Zadatak je implementiran u programskom jeziku - Java
### 2. Eksterne biblioteke koje program koristi su:
  - subprocess
  - math
  - random

### 3. Način konfigurisanje programa:
  - Može se kreirati po želji konfiguracioni fajl, koji će biti prosleđen programu preko komandne linije
  - U konfiguracionom fajlu zadavati parametre u obliku: POP_NUM=10 (primer konfiguracionog fajla - **config1.txt**)
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

### 4. Kod se može kompajlirati i pokrenuti na lokalnoj mašini komandom:
```bash
python main.py
```
