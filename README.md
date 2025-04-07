<style>
    .Droite {
        text-align: right;
    }
    .heatMap {
        width: 100%;
    }
    .heatMap th {
        background: #cfd8dc;
        word-wrap: break-word;
        text-align: center;
    }
    .heatMap tr:nth-child(1) { background: #e1f5fe ; }
    .heatMap tr:nth-child(2) { background: #b3e5fc ; }
    .heatMap tr:nth-child(3) { background: #e1f5fe ; }
    .heatMap tr:nth-child(4) { background: #b3e5fc ; }
    .heatMap tr:nth-child(5) { background: #e1f5fe ; }
    .heatMap tr:nth-child(6) { background: #b3e5fc ; }
	.heatMap tr:nth-child(7) { background: #e1f5fe ; }
    .heatMap tr:nth-child(8) { background: #b3e5fc ; }
    .heatMap tr:nth-child(9) { background: #e1f5fe ; }
    .heatMap tr:nth-child(10) { background: #b3e5fc ; }
    .heatMap tr:nth-child(11) { background: #e1f5fe ; }
    .heatMap tr:nth-child(12) { background: #b3e5fc ; }

    details {  
        
        border:5px solid #ffffff;
        background: #ffffff;
        color: #000000;
    }

    summary {
        font-size: 24px;
        font-weight: bold;
    }

    .Yellow {
        background: yellow;
    }
</style> 

<!--- PRESENTATION------------------------------------------>
<!---------------------------------------------------------->

<details>
<summary>0. Présentation</summary>
La synchronisation de l'Arrimage consiste à échanger des données entre 2 DBs d'ORBIS 

**DB1 :	RNPP**

Cette DB contient :

<div class="heatMap">

|Id|Structure|
|:--:|:--|
|103|Personne|
|107|Carte nationale d'identité|
|617|CR|
|743|CR CEDEAO|
|807|CREF|
</div>

**DB2 :	Arrimage**

Cette DB contient :

<div class="heatMap">

|Id|Structure|
|:--:|:--|
|106|Toutes les cartes|
|107|Personne|
|108|Demande de modification du numéro de téléphone|
|109|Demande de modification du numéro de passeport|
|110|Demande de modification du permis de conduire|
</div>

L'échange se fait dans les 2 sens 

</details>


<!--- DEPLOIEMENT------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>1. Deploiement</summary>


**Sur Serveur2 / ArrimageProd**


+ Il faut executer :	
<div class="heatMap">

|Description|Sript sql|
|--|--|
|Mise à jour du schéma|[_0_UpdateSchemas.sql](./_0_UpdateSchemas.sql)|
|Drop keys|[Drop_FK_Arrimage.sql](./Drop_FK_Arrimage.sql)|
| |[_2_PROC_ARRIM_PrepareEnvoi_Tables_ARRIM.sql](./_2_PROC_ARRIM_PrepareEnvoi_Tables_ARRIM.sql)|
| |[_2_PROC_ARRIM_RecupImport_Tables_RNPP.sql](./_2_PROC_ARRIM_RecupImport_Tables_RNPP)|
| |[_2_PROC_ARRIM_Nettoyage_Tables_ARRIM.sql](./_2_PROC_ARRIM_Nettoyage_Tables_ARRIM.sql)|

</div>
Chacun des fichiers doit être ouvert dans SSMS, puis Executé.      

Dans chaque fichier SQL, il faut modifier le nom de la base Cible   
    -   ArimageTest -> ???  
    -   rnppbt-v3 -> ???

****

**Sur Serveur1 / RNPP**

+ Il faut executer :	
<div class="heatMap">

|Description|Sript sql|
|--|--|
|Mise à jour du schéma|[_0_UpdateSchemas.sql](./_0_UpdateSchemas.sql)|
||[_1_CreateLink.sql](./_1_CreateLink.sql)|
| |[_2_PROC_RNPP_RecupImport_Tables_ARRIM.sql](./_2_PROC_RNPP_RecupImport_Tables_ARRIM.sql)|
| |[_2_PROC_RNPP_PrepareEnvoi_Tables_RNPP.sql](./_2_PROC_RNPP_PrepareEnvoi_Tables_RNPP.sql)|
| |[_2_PROC_RNPP_Execution.sql](./_2_PROC_RNPP_Execution.sql)|

</div>
Chacun des fichiers doit être ouvert dans SSMS, puis Executé.

Dans chaque fichier SQL, il faut modifier le nom de la base Cible   
    -   ArimageTest -> ???  
    -   rnppbt-v3 -> ???

****

**_1_CreateLink.sql** ... link vers le Serveur ArrimageTest

il faut personnaliser  : 	@ServerName, @User, @Password

**_2_PROC_RNPP_Execution**

Cette procédure permet d'exécuter le processus complet ... à partir de RNPP
||Liste des procédures appelées|
|--|--|
||Link.ArrimageProd.ARRIM.ARRIM_PrepareEnvoi_Tables_ARRIM|
||ARRIM.RNPP_RecupImport_Tables_ARRIM|
||Link.ArrimageProd.ARRIM.ARRIM_Nettoyage_Tables_ARRIM|
||ARRIM.RNPP_PrepareEnvoi_Tables_RNPP|
||Link.ArrimageProd.ARRIM.ARRIM_RecupImport_Tables_RNPP|
		
il faut personnaliser  : **Link.ArrimageProd**

+ Il faut créer un JOB SQL ... pour exécuter la procédure **ARRIM.RNPP_Execution** ! .. une fois par Jour.



</details>


<!--- UTILISATION------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>2. Utilisation</summary>

Pour effectuer le transfert des données d'arrimage,

il faut exécuter, dans la base RNPP,  la commande SQL : 

**Récupération des données d'arrimage uniquement**

        declare	@Full		int = 0
        declare @Histo		int = 0
	    execute  ARRIM.RNPP_Execution @Full,  @histo

**Premier lancement pour envoyer les personnes et les cartes vers l'ARRIMAGE**
        
        declare	@Full		int = 1
        declare @Histo		int = 0
	    execute  ARRIM.RNPP_Execution @Full,  @histo

**Execution complète**
        
        declare	@Full		int = 1
        declare @Histo		int = 1
	    execute  ARRIM.RNPP_Execution @Full,  @histo

voir fichier **LancerExecution.sql**



</details>

<!--- TESTS------------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>3. Tests et contrôles</summary>


*Pour les tests, nous avons besoin d'installer préalablement DB_DIAG*

**Pour tester le transfert des demandes de modifications de l'Arrimage vers RNPP**

-   Il faut alimenter des données d'arrimage dans les strcuture 108, 109 et 110  
en utilisant la Web API. **http://arm-orbisbt.intra.rnpp-ci.org:8091**

    il faut utiliser le fichier [Insertion_Arimage_Test.sql](./Insertion_Arimage_Test.sql)  
Ce script permettra d'insérer des demandes dans les 3 structures.

- Il faut exécuter le transfert des données d'arrimage  
    le mode Full = 1 n'est pas nécessaire !

- il faut vérfier que les données d'ArrimageTest
    -   sont transférées dans RNPP
    -   sont historiséés dans ArrimageTest
    -   sont supprimées dans ArrimageTest
    
il faut utiliser le fichier [ControleDesDemandesTransferees.sql](./ControleDesDemandesTransferees.sql)




**Pour tester le transfert des données de RNPP vers Arrimage**  

- Lors de l'exécution,  
   il faut activer Full = 1  et Histo = 1


<div class="Yellow">

- Il faut modifier des dossiers dans RNPP 
    -   en activant un dossier  à Actif = 0         **-> Ajouter**  
    -   en modifiant un des 7 champs alphas transférés  
            DD_122  
            DD_123 ou DD_305  en fonction de DD_1286  
            DD_1286  
            DD_124  
            DD_127  
            DD_872  
            FK_908                                  **-> Modifier**  
    -   en désactivant un dossier  à Actif = 1      **-> Supprimer**

    il faut utiliser le fichier [XXX.sql](./XXXX.sql)

- Il faut exécuter le transfert des données d'arrimage  

- il faut vérfier que les données de RNPP 
    -   sont transférées dans ArrimageTest
    -   sont historiséés dans ArrimageTest  
        -   **Ajouter**       actif = 1		Date_Update = @DateUpdate		Desactivation = 0
        -   **Modifier**      actif = 1		Date_Update = @DateUpdate		Desactivation = 1
        -   **Supprimer**     actif = 0		Date_Update = @DateUpdate		Desactivation = 1
        
    il faut utiliser le fichier [XXX.sql](./XXXX.sql)
    
</div>

</details>

