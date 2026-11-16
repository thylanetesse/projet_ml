# Projet tutoré Machine Learning : prédire le défaut de crédit

**Étudiant·e :** thy-lan.etesse@etudiant.univ-rennes.fr  
**Enseignant :** Alexis Gaillard, alexis.gaillard@synar-ia.fr (Université de Rennes, 2026–2027)

---

## 1. Le sujet

Une banque taïwanaise veut repérer, parmi les titulaires de ses cartes de crédit, ceux qui **ne paieront pas leur prochaine échéance**.
C'est un problème de **classification binaire** : la cible est `default payment next month` (1 = défaut, 0 = pas de défaut).

## 2. Les données

- **Source :** Default of Credit Card Clients, UCI Machine Learning Repository (Yeh & Lien, 2009)
- **Lien :** https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- 30 000 clients, 23 variables explicatives, environ **22 % de défauts**
- 6 mois d'historique, d'avril à septembre 2005 (montants en NT$, dollars taïwanais)

| Variable | Description | Valeurs |
|---|---|---|
| `LIMIT_BAL` | Plafond de crédit (client et famille) | NT$ |
| `SEX` | Sexe | 1 = homme, 2 = femme |
| `EDUCATION` | Niveau d'études | 1 = master ou plus, 2 = licence, 3 = lycée, 4 = autre (0, 5, 6 non documentés) |
| `MARRIAGE` | Situation familiale | 1 = marié, 2 = célibataire, 3 = autre (0 non documenté) |
| `AGE` | Âge | années |
| `PAY_0`, `PAY_2` … `PAY_6` | Statut de remboursement, de septembre (`PAY_0`) à avril (`PAY_6`) | −1 = payé à temps, 1 à 9 = mois de retard (−2 et 0 non documentés) |
| `BILL_AMT1` … `BILL_AMT6` | Montant du relevé, de septembre (1) à avril (6) | NT$ |
| `PAY_AMT1` … `PAY_AMT6` | Montant payé, de septembre (1) à avril (6) | NT$ |
| `default payment next month` | **Cible** | 1 = défaut, 0 = pas de défaut |

## 3. Points de vigilance

- **Codes non documentés :** `EDUCATION` prend les valeurs 0, 5 et 6, et `PAY_x` vaut parfois −2 ou 0. Il faut enquêter, trancher et justifier votre choix.
- **Dimension temporelle :** les 6 mois de factures et de paiements permettent de construire de meilleures variables (taux de remboursement, tendance, nombre de mois de retard consécutifs).
- **Variables sensibles :** sexe, âge, situation familiale. Le scoring de crédit est classé « à haut risque » par l'AI Act européen.
- **Classes déséquilibrées :** avec 22 % de défauts, l'accuracy seule est trompeuse.
- **Fuite de données :** une variable qui contient déjà la réponse fausse tous les résultats.

## 4. Les questions à traiter

1. Quels comportements de paiement annoncent un défaut ?
2. Quel modèle bat une régression logistique, et de combien ?
3. Quel seuil choisir si un défaut non détecté coûte plus cher qu'un bon client refusé ?
4. Le modèle se trompe-t-il autant pour tous les groupes de clients ?

## 5. La démarche

1. **Explorer** : distributions, liens avec la cible, anomalies
2. **Préparer** : nettoyage, encodage, nouvelles variables
3. **Modéliser** : un modèle de référence, puis des modèles plus riches
4. **Évaluer** : métriques adaptées, seuil, interprétation
5. **Restituer** : une recommandation claire pour le métier

## 6. Règle d'or

> **Si vous ne savez pas l'expliquer, vous ne le gardez pas.**

## 7. Ce qui sera évalué à l'oral

1. **Le code** : expliquer précisément un extrait choisi par l'enseignant.
2. **Les modèles** : réexpliquer leur fonctionnement (par exemple la forêt aléatoire).
3. **Les décisions** : pourquoi le modèle s'appuie sur telle ou telle information.
4. **Les variables** : ce que signifie chaque variable et son rôle dans l'analyse.

**Objectif final : savoir réexpliquer votre code et vos choix, sans l'IA.**

## 8. Rappel Git

Vous pouvez mettre les données dans le dépôt.

Pour valider que votre projet fonctionne, je clonerai votre dépôt et je lancerai le code. Il doit donc s'exécuter directement après un `git clone` : données incluses, chemins relatifs, et dépendances listées (par exemple dans un `requirements.txt`).
