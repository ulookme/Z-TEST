#SUJET
#Une comp.agnie pharmaceutique veut savoir si le procédé de fabrication
# qu’elle utilise fournit effectivement des comprimés dosés à 5mg de principe actif d’un médicament 

#REMARQUE PROBLEME
#On remarque que la dose moyenne est de 4,85 ms sur sur 100 médicament produit sur une valeur de 5 théorique 

#QUESTION
#La moyenne ￼ de dosage actif  est-elle significativement différente des principe actif d’un médicament dosé normalement a 5mg ?
#Hypothèse nulle (H0) : μ = μH0
#Le dosage en principe actif des comprimés du lot ne diffère pas du dosage prévu par le processus de fabrication (5mg)

#Hypothèse alternative bilatérale (H1) : μ  μH0 Le dosage en principe actif des comprimés du lot diffère du dosage prévu par le processus de fabrication (5mg)

#LOIE ET FONTION DE RESOLUTION
# la fonction que jvais utiliser pour cette teste statistique est le distribution de la loie normale  en plus de la loie student (t)

#conclusion : tyeste d'ecart reduit z 
#on prend le resultat de Z - la variance 0,5
#a. Test de l’écart réduit Z α =0.05 → Zα = 2,96
#La table donne la probabilité α pour que l'écart-réduit dépasse en valeur absolue une valeur donnée ε,
#  c'est-à- dire la probabilité extérieure à l'intervalle [-ε,ε]. La probabilité α s'obtient par addition des nombres inscrits en marge


# pour le second teste de student la conclusion est qu'on garde l'hypothse Null  car 
# la Pvalue est superieur que alpha qui est à.5 et les stat est minimum comparé au teste précedant.


#####----on applique la loie de sutend quand l'échantillon est superieur a 30 ou quand elle suit la loie normale ---###########
import numpy as np
from statsmodels.stats.proportion import proportions_ztest as ztest
from math import sqrt
from scipy import stats
import scipy.stats as stat

a = 0.05
dosage_reel = 5
n = 100
dosage_moyen = 4.85
var = 0.50
ecart = sqrt(var)

stat, pval = ztest(a, n, dosage_moyen - dosage_reel, prop_var=var)
print('{0:0.3f}'.format(pval))
print(stat)
Z=stat
print(Z) 
print(pval)

rvs = stats.norm.rvs(loc=dosage_moyen, scale=ecart, size=n)
test = stats.ttest_1samp(rvs,dosage_reel)
print(rvs)
print(test)

#|to| = 1,39 → 0,16< P < 0,05 : on accepte  H0



