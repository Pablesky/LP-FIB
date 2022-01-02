# Projecte de Compiladors i Python 2021 2022
##### Pablo Vega Gallego
###### LP-FIB Q1  
# Llenguatge Llull
Aquest llenguatge és un llenguatge similar a C. Ha sigut creat amb ANTLR4 i Pyhton.
L'esquelet de la gramàtica és una estructura anomenada bloc, que és un conjunt de instruccions, on instruccions és el contenidor general que emmagatzema **TOTES** les funcionalitats del codi.

# Contingut important de la carpeta
A la carpeta podem trobar aquests fitxers importants:
* **beat.py**: És el main del batificador, en aquest fitxer podem trobar el codi que fa la crida a l'arbre visitador. Aquest programa agafa un fitxer com a entrada i el programa dona com a resultat el contingut del fitxer prinitificat amb colors i espais.
* **beatVisitor.py**: És el programa que defineix com s'ha de imprimir cada tipus de la gramàtica.
* **llull.py**: És el main del intèrpret del llenguatge. En aquest fitxer trobem el que codi que fa la crida a l'arbre visitador. Aquest programa agafa com a entrada un fitxer. Optativament també accepta el nom de la funció per la qual es vol començar l'execució del programa juntament amb els paràmetres d'entrada (només admet valors numèrics).
* **llullTreeVisitor.py**: És el programa que defineix com s'ha d'executar cada tipus de la gramàtica.
* **Makefile**: Aquest programa regenera els fitxers de l'ANTLR4 a partir de la gramàtica, en aquesta cas a partir del fitxer **llull.g4**.
* **llull.g4**: El contingut de la gramàtica del llenguatge.
* **requirements.txt**: Les llibreries fetes servir per a poder imprimir amb color per el terminal.

# Com realitzar una prova de l'intèrpret
Per a poder realitzar una execució d'un codi basta amb escriure:
```
python3 llull.py <fitxer_per_a_interpretar> <funcio_per_on_començar> <variables_de_la_funcio>
```
Per a poder realitzar una execució del pretty printer:
```
python3 beat.py <fitxer_per_a_printejar>
```

# Exepcions
* Divisió entre 0.
* La funció no existeix.
* Hem cridat la funció amb diferents paràmetres de les declarades.
* Sobredeclaració de la funció.
* No es poden operar taules.
* La funció té dos paràmetres amb el mateix.
* L'índex de l'array es fora del rang.
