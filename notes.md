# DATA TO MANUALLY CHANGE

## VIENNE

- [x] DANSEREAU dit Biernay, Pierre - Saint-Georges-Lès. Enlever le "(AUCUNE REF)"

## Dordogne

- [ ] CHANTAL, dit lafleur (Dordogne ville BERGERAC) le text fini avec "plaque commemorative" p.40
- [ ] JOYAL, dit Bergerac (dordogne ville BERGERAC) revoir la bio p.40

- [ ] Check for other "PLAQUE COMMEMORATIVE" text to correct them back to its original text

- [ ] Too many "Plaque commemorative" at the end of characters so might as well put a regex to detect them instead of transforming them into uppercases in parenthesis

- [ ] Verify if there is a character in LE PIZOU, town
- [ ] Do a regex to identify if the word "Biraben" and "Généanet" and "Biraben-Migrations.fr" is in parenthesis as well so we know it is the end of a character
- [ ] Transform all the uppercases Biraben into lower cases (same goes for the "voir..." buntil the end of the parenthesis)

(Plaque commémorative)
([...] Biraben)
([...] Généanet)
([...] voir)

# Gironde

- [ ] Ajouter :

`
Carignan-de-Bordeaux (33360)

BIZEUX, BIZUT, BISUS ou GUICHARD
dit La Rose, Jean-Baptiste.
Né le 03-03-1667. Fils de Bertrand
Bisus ou Visus et de Jeanne Dubois.
Marié à 1) Marie-Madeleine Barsa ou
Bresa (Marié à la Gaumine, à Verchères
(Qc), le 27-06-1695, le mariage
est officialisé), à Montréal (Qc), le
01-07-1696. Marie-Madeleine Barsa
ou Bresa décède, à Montréal (Qc), le
19-06-1703. Cinq enfants. 2) Catherine-
Gertrude Forgues, à Montréal
(Qc), le 29-10-1703. Contrat de mariage
(greff e Pierre Raimbault). Quatre
enfants. Décédé à Beaumont (Qc), le
10-12-1711. Soldat de la compagnie
de M. Levasseur. (NR-FG-PRDH)
`
