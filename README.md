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
### pour Test ou compiler un program MapReduce Python on local

avant de passer en MapReduce pour détecter les erreurs Syntaxique

```bash
	cat <chemin de fichier input on local> | python <chemin de fichier mapper.py on local> | python <chemin de fichier reducer.py on local>
```
### Copier le fichier input on HDFS
```bash
	hdfs dfs -CopyFromLocal <chemin du ficher input on Local> <nom de dossier de destination>
```
ou : 
```bash
	hadoop fs -CopyFromLocal <chemin du fichier input on Local> <nom de dossier de destination>
```
### la commande d'exécution du program MapReduce en Python :

```bash
hadoop jar <chemin de fichier streaming.jar> 
-Dmaperd.reduce,tasks=1
-file  <chemin du ficher map on Local>
-mapper "python <chemin du ficher map  on Local>"
-file <chemin du ficher reduce on Local>
-reducer "python <chemin du ficher reduce on Local>"
-input <chemin du ficher input on HDFS>
-output <chemin du ficher output on HDFS>
```
	
### exemple des commandes : 
	
```bash
hadoop fs -copyFromLocal /home/cloudera/workspace/Exemple1/input.txt  input/ 
```

```bash
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar
-Dmaperd.reduce,tasks=1
-file /home/cloudera/workspace/Exemple1/mapper.py
-mapper "python /home/cloudera/Exemple1/wordcount/mapper.py"
-file /home/cloudera/workspace/Exemple1/reducer.py
-reducer "python /home/cloudera/Exemple1/wordcount/reducer.py"
-input myinput/
-output out
```


