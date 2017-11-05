# MapreducePythonPrograms
## Hadoop MapReduce Programs Examples with Python

### Exemples : 

	* Exemple 1 Total des ventes par magasin
	* Exemple 4 Calculer maximum et minimum du salaire
	* Exemple 5 calculer moyenne de l'écart type du Salaire
	* Exemple 6 anagram 

### Exemple1 : en à utiliser un fichier input sous la forme suivant:

		 date | temps | magasin| produit | cout | paiement

### Exemple 4 & 5: en à utiliser un fichier input sous la forme suivant:   

		 id , age , sexe , adresse , salaire

### Exemple 6 : en à utiliser un fichier input sous la forme suivant:

		melon barre deviner lemon
		arbre fiable fable vendre
		devenir faible barbe 

### Copier le fichier input on HDFS
```bash
hdfs dfs -CopyFromLocal <chemain du ficher map on Local> <nom de dossier>
```
ou
```bash
hadoop fs -CopyFromLocal <chemain du ficher map on Local> <nom de dossier>
```
### la commande d'exécution du program MapReduce en Python :

```bash
hadoop jar <chemain de fichier streaming.jar> 
-Dmaperd.reduce,tasks=1
-file  <chemain du ficher map on Local>
-mapper "python <chemain du ficher map  on Local>"
-file <chemain du ficher reduce on Local>
-reducer "python <chemain du ficher reduce on Local>"
-input <chemain du ficher input on HDFS>
-output <chemain du ficher output on HDFS>
```
	
### exemple de commande : 
	
	
```bash
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar
-Dmaperd.reduce,tasks=1
-file /home/cloudera/workspace/wordcount/mapper.py
-mapper "python /home/cloudera/workspace/wordcount/mapper.py"
-file /home/cloudera/workspace/wordcount/reducer.py
-reducer "python /home/cloudera/workspace/wordcount/reducer.py"
-input myinput/
-output out
```


