# A2071 - Robotique (Part 1) - 2024-2025
## Projet: Mini Robot Télécommandé

Binôme (B1)
- Xu Keng HE305064
- Fondimare Nathan HE304827
- de Meeus Justin HE304831
- Foyet Fondjo David HE305102

### Objectifs:
<!--- PRESENTATION------------------------------------------>
<!---------------------------------------------------------->

<details>
<summary>0. Objectif du projet</summary>

- Concevoir, construire et programmer un robot mobile radiocommandé.
- Le robot devra effectuer des mouvements, éviter des obstacles et exécuter des tâches simples.


<details>
<summary class="sum2">DB_DIAG contient les schémas suivants :</summary>

<div class="heatMap">

|Nom|Description|
|:--|:--|
|_Backup||
|_Data||
|_Extract||
|_Genkey||
|_HistoConfig||
|_ORBIS||
|_Root||
|_Schema||
|_TComp||
|_WebAPI||
|Docu||
</div>
</details>


<!--- ROOT------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>Root</i></summary>
<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|Backup_files||
|Configuration||
|Event||
|EventLog||
|TBL_COLUMNS||
</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_CreateCsvFileFromQuery||
|sp_CreateDirectory||
|sp_DeleteFile||
|sp_ExtractRoutines||
|sp_ReadFile||
|sp_ReadFileU||
|sp_SaveBlob||
|sp_SaveFile||
|sp_SaveFileU||
|sp_ShowJson||
|sp_ShowJson_UTF8||
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|fn_ConversionChaineEtendue||
|fn_ConversionChaineHTML||
|fn_ConvertBase64ToBin||
|fn_ConvertBinToBase64||
|fn_HashCode||
|fn_UTF8ToNvarchar||
|fn_NVARCHARtoUTF8||
|LPAD||
|RPAD||
|...||

</div>
</details>

</details>
<!--- FIN ROOT------------------------------------------>


<!--- ORBIS------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>ORBIS</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|DICO_OPERATION||
|Tempo_BIO||
|Tempo_HTML||
</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_CreationVueAlphas||
|sp_CreationVueFace||
|...||

</div>
</details>

</details>
 <!--- FIN ORBIS------------------------------------------>


<!--- BACKUP------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>BACKUP</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|BACKUP_FILES||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_Backup||
|sp_PurgeAllBackupFiles||
|sp_PurgeBackupFiles||
|sp_Restore||


</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN BACKUP------------------------------------------>



<!--- CONN------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>CONN</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_CreateSynonymsForTargetDatabase||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN CONN------------------------------------------>


<!--- HTTP------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>HTTP</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|Execution||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_ExecuteHTTPAuthExt||
|sp_ExecuteHTTPAuthExt_Bin||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN HTTP------------------------------------------>



<!--- WEBAPI------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>WEBAPI</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|WebAPI||
|.||
|.||
|.||
|.||
|.||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN WEBAPI------------------------------------------>



<!--- HistoConfig------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>HistoConfig</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN HistoConfig------------------------------------------>

<!--- AUTRES------------------------------------------>
<details  class="ex2" >
<summary  class="sum1"><i>AUTRES</i></summary>

<details class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN AUTRES------------------------------------------>

</details>


<!--- DEPLOIEMENT------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>1. Deploiement</summary>

Le déploiement s'effectue à l'aide de 3 fichiers SQL.  
<div class="heatMap">

|Description|Sript sql|
|--|--|
|Création de la DB et des schémas|[Deploy\Create_DB_DIAG.sql](./Deploy/Create_DB_DIAG.sql)|
|Procédures de base|[Deploy\Deploy.sql](./Deploy/Deploy.sql)|
|Procédures complétmentaires|[Deploy\Deploy_supp.sql](./Deploy/Deploy_supp.sql)|
</div>
Chacun des fichiers doit être ouvert dans SSMS, puis Executé.  

****  

**Deploy.sql** 

il faut personnaliser  : 	**@ROOT**

**Deploy_supp.sql**

il faut personnaliser  : **@DB_ORBIS**

** **

</details>


<!--- UTILISATION------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>2. Utilisation</summary>

```
eeeee
```

    eeee

ssss
 
** **

</details>

<!--- TESTS------------------------------------------------->
<!---------------------------------------------------------->

<details>
<summary>3. Test</summary>

*vvfrgev*



** **

</details>


<!--- CONTROLES--------------------------------------------->
<!---------------------------------------------------------->


<details>
<summary>4. Controles</summary>


** **

</details>

<!---------------------------------------------------------->





