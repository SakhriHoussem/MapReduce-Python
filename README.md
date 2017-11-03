# MapreducePythonPrograms
## Hadoop Mapreduce Programs Exemples with Python

### Exemples : 

	* Exemple 1 Total des ventes par magazin 
	* Exemple 4 Calcule maximum et minimum du salaire  
  	* Exemple 5 calcule moyenne de l ecart type du Salaire
	* Exemple 6 anagram 

### Exemple1 : en a utiliser un fichier input sous la forme suivant:

		 date | temps | magazin| produit | cout | paiement

### Exemple 4 & 5: en a utiliser un fichier input sous la forme suivant:   

		 id , age , sexe , adresse , salaire

### Exemple 6 : en a utiliser un fichier input sous la forme suivant:

		melon barre deviner lemon
		arbre fiable fable vendre
		devenir faible barbe 

### la commende d execution du program MapReduce en Pyhton :

`hadoop jar <chemain de fichier streaming.jar>  
    -Dmaperd.reduce,tasks=1   
    -file  <chemain du ficher map on Local> 
    -mapper "python <chemain du ficher map  on Local>" 
    -file <chemain du ficher reduce on Local> 
    -reducer "python <chemain du ficher reduce on Local>" 
    -input <chemain du ficher input on HDFS> 
    -output <chemain du ficher output on HDFS>`
	
### exemple de commande : 
	
	
`hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar 
    -Dmaperd.reduce,tasks=1   -file /home/cloudera/workspace/wordcount/mapper.py
     -mapper "python /home/cloudera/workspace/wordcount/mapper.py"
     -file /home/cloudera/workspace/wordcount/reducer.py 
     -reducer "python /home/cloudera/workspace/wordcount/reducer.py"
     -input myinput/  -output out`


