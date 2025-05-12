# DATA TO MANUALLY CHANGE

## VIENNE

- [x] DANSEREAU dit Biernay, Pierre - Saint-Georges-Lès. Enlever le "(AUCUNE REF)"

## Dordogne

- [ ] CHANTAL, dit lafleur (Dordogne ville BERGERAC) le text fini avec "plaque commemorative" A REAJUSTER APRES LEXTRACTION p.40
- [ ] JOYAL, dit Bergerac (dordogne ville BERGERAC) revoir la bio p.40

- [ ] Check for other "PLAQUE COMMEMORATIVE" text to correct them back to its original text

- [ ] Too many "Plaque commemorative" at the end of characters so might as well put a regex to detect them instead of transforming them into uppercases in parenthesis

- [ ] Verify if there is a character in LE PIZOU, town \*
- [ ] Do a regex to identify if the word "Biraben" and "Généanet" and "Biraben-Migrations.fr" is in parenthesis as well so we know it is the end of a character
- [ ] Transform all the uppercases Biraben into lower cases (same goes for the "voir..." buntil the end of the parenthesis)
