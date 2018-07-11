# MapReduce Python
## MapReduce Python Example

### Exemples : 

	* Exemple 1: Total des ventes par magasin
	* Exemple 4: Calculer maximum et minimum du salaire
	* Exemple 5: Calculer moyenne de l'écart type du Salaire
	* Exemple 6: Anagram 

### Exemple 1 : en à utiliser un fichier input sous la forme suivant:

		 date | temps | magasin| produit | cout | paiement

### Exemple 4 & 5: en à utiliser un fichier input sous la forme suivant:   

		 id , age , sexe , adresse , salaire

### Exemple 6 : en à utiliser un fichier input sous la forme suivant:

		melon barre deviner lemon
		arbre fiable fable vendre
		devenir faible barbe

### Executer le program MapReduce Python on local
pour test avant de passer en MapReduce pour détecter les erreurs Syntaxique
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
### Commande d'exécution du program MapReduce en Python :

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

### Commande d'afficher contenu de fichier Output :

```bash
hadoop fs -cat <chemin de fichier output>/part-00000 
```

### Commande de suppression du répertoire Output :

```bash
hadoop fs -rm -r <répertoire de fichier output>
```

### Execution d'un exemple :
en va choisi l'exemple 1 pour tester

copier l'exemple 1 dans le chemin suivant: /home/cloudera

```bash
# créer répertoire input dans HDFS
hadoop fs -mkdir /user/input
```

```bash
# transférer le fichier input.text du local vers HDFS
hadoop fs -copyFromLocal /home/cloudera/Exemple1/input.txt  input/ 
```

```bash
# execution Program Mapreduce
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar
-Dmaperd.reduce,tasks=1
-file /home/cloudera/Exemple1/mapper.py
-mapper "python /home/cloudera/Exemple1/mapper.py"
-file /home/cloudera/Exemple1/reducer.py
-reducer "python /home/cloudera/Exemple1/reducer.py"
-input Exemple1/input.txt #exemple
-output out
```

```bash
# afficher le contenu de fichier output
hadoop fs -cat out/part-00000 
```

```bash
# suppression du répertoire Output
hadoop fs -rm -r out
``
