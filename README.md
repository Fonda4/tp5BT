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
    .heatMap tr {
        vertical-align: top;
    }
    .heatMap tr:nth-child(1) {  background: #e1f5fe ; }
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

    .ex1 {
    margin: auto;
    background: gold;
    width: 66%;
    }
    .ex2 {
            margin: 0px 0px 0px 20px;
    }

    details {  
        border:5px solid #ffffff;
        background: #ffffff;
        color: #000000;
    }

    summary {
        font-size: 24px;
        font-weight: bold;
    
    }

    .sum1 {
        font-size: 20px;
        font-weight: bold;
    }    

    .sum2 {
        font-size: 16px;
        font-weight: normal;
    
    }
</style> 




<!--- PRESENTATION------------------------------------------>
<!---------------------------------------------------------->

<details open>
<summary>0. Présentation</summary>

Pour répondre à différents besoins liés à ORBIS et toutes les données enregsitrées dans sa DB,
nous avons conçu une DB de Diagnostic.
Elle contient différentes ... tables, procédures stockées et fonctions .. rangées dans plusieurs schémas.

Pour accéder à la DB d'ORBIS, une procdure permet de disposer de synonymes ayant les mêmes noms que les tables d'ORBIS ... les données sont accessibles comme si nous étions dans la DB d'ORBIS.
 


<details open >
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
<details  open class="ex2" >
<summary  class="sum1"><i>Root</i></summary>
<details open class="ex2" >
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
<details open class="ex2" >
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
<details open class="ex2" >
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


<!--- CONN------------------------------------------>
<details open class="ex2" >
<summary  class="sum1"><i>Conn</i></summary>

<details open class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_StatDbOrbis <br>[src](./Deploy/conn/sp_StatDbOrbis.sql)|Cette procédure permet de rechercher toutes les DB ORBIS <br>présentent sur le serveur SQL|
|sp_CreateSynonymsForTargetDatabase <br>[src](./Deploy/conn/CreateSynonymsForTargetDatabase.sql)|Cette procédure permet de se connecter à une DB ORBIS<br>**Parametre 1 : @databaseName** Nom de la DB ORBIS|


</div>
</details>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Table|Colonne|Type|
|:--|:--|:--|
|STAT_DB_ORBIS<br>[src](./Deploy/conn/TB_STAT_DB_ORBIS.sql)|Nom<br>DateCreation<br>ConfigFileVersion<br>DbRevision<br>LastSchemaUpdate<br>LastEvent|varchar(100)<br>datetime<br>varchar(100)<br>varchar(100)<br>datetime<br>datetime|

</div>
</details>

</details>
 <!--- FIN CONN------------------------------------------>


<!--- ORBIS------------------------------------------>
<details open class="ex2" >
<summary  class="sum1"><i>ORBIS</i></summary>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|DICO_OPERATION||
|Tempo_BIO||
|Tempo_HTML||
</div>
</details>
<details open class="ex2" >
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
<details open class="ex2" >
<summary  class="sum1"><i>BACKUP</i></summary>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|BACKUP_FILES||

</div>
</details>
<details open class="ex2" >
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
<details open class="ex2" >
<summary class="sum2"><i>Fonctions</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
</details>
 <!--- FIN BACKUP------------------------------------------>



<!--- HTTP------------------------------------------>
<details open class="ex2" >
<summary  class="sum1"><i>HTTP</i></summary>


<details open class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|sp_ExecuteHTTPAuthExt <br>[src](./Deploy/http/EXECUTE_HTTP_AuthExt.sql)|Cette procédure pemet de soumettre une requête HTPP<br> et d'obtenir une réponse Texte <br>**parametre 1 : @URL**  <br>**parametre 2 : @UserName**  <br>**parametre 3 : @Password**  <br>**parametre 4 :	@Type**  <br>**parametre 5 : @iFormat**  <br>**parametre 6 : @Param**  <br>**parametre 7 : @Body**  <br>**parametre 8 : @Status**  <br>**parametre 9 : @StatusText**  <br>**parametre 10 : @Response**|
|sp_ExecuteHTTPAuthExt_Bin <br>[src](./Deploy/http/EXECUTE_HTTP_AuthExt_Bin.sql)|Cette procédure pemet de soumettre une requête HTPP<br> et d'obtenir une réponse Binaire <br>**parametre 1 : @URL**  <br>**parametre 2 : @UserName**  <br>**parametre 3 : @Password**  <br>**parametre 4 :	@Type**  <br>**parametre 5 : @iFormat**  <br>**parametre 6 : @Param**  <br>**parametre 7 : @Body**  <br>**parametre 8 : @Status**  <br>**parametre 9 : @StatusText**  <br>**parametre 10 : @Response**|
|||

</div>
</details>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Table|Colonne|Type|
|:--|:--|:--|
|Execution <br> [src](./Deploy/http/TB_Execution.sql)|IdAuto<br>DateExecution<br>EndPoint<br>Username<br>Password<br>TypeRequest<br>ApplicationType<br>Param<br>Body<br>Status<br>StatusText<br>Response<br>IdAutoPrecedent<br>Redo_Status<br>Redo_Reponse|int identity (1,1)<br>datetime default getdate()<br>varchar(1000)<br>varchar(1000)<br>varchar(1000)<br>varchar(10)<br>varchar(100)<br>varchar(MAX)<br>varchar(MAX)<br>varchar(32)<br>varchar(32)<br>varchar(MAX)<br>int<br>int<br>int|

</div>
</details>



</details>
 <!--- FIN HTTP------------------------------------------>



<!--- WEBAPI------------------------------------------>
<details open class="ex2" >
<summary  class="sum1"><i>WEBAPI</i></summary>

<details open class="ex2" >
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
<details open class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details open class="ex2" >
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
<details open class="ex2" >
<summary  class="sum1"><i>HistoConfig</i></summary>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details open class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details open class="ex2" >
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
<details open class="ex2" >
<summary  class="sum1"><i>AUTRES</i></summary>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>
<div class="heatMap">  
    
|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details open class="ex2" >
<summary class="sum2"><i>Procédures</i></summary>
<div class="heatMap">

|Nom|Description|
|:--|:--|
|...||

</div>
</details>
<details open class="ex2" >
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

<details open >
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

<details open >
<summary>2. Utilisation</summary>


 <!--- Root------------------------------------------>
<details open  class="ex2" >
<summary  class="sum1"><i>Root</i></summary>

</details>
 <!--- FIN Root------------------------------------------>


<!--- Conn------------------------------------------>
<details open  class="ex2" >
<summary  class="sum1"><i>Conn</i></summary>


<details open class="ex2" >
<summary class="sum2"><i>sp_StatDbOrbis</i></summary>

[source](./Use/conn/Use%20sp_StatDbOrbis.sql)

</details>

<details open class="ex2" >
<summary class="sum2"><i>sp_CreateSynonymsForTargetDatabase</i></summary>

[source](./Use/conn/CreateSynonymsForTargetDatabase.sql)

</details>

</details>
 <!--- FIN Conn------------------------------------------>


 <!--- Http------------------------------------------>
<details open  class="ex2" >
<summary  class="sum1"><i>Http</i></summary>


<details open class="ex2" >
<summary class="sum2"><i>MinimalAPI
</i></summary>

[source](./Use/http/WebApi_MinimalAPI.sql)

</details>

</details>
 <!--- FIN Http------------------------------------------>


<!--- AUTRES------------------------------------------>
<details open  class="ex2" >
<summary  class="sum1"><i>AUTRES</i></summary>

<details open class="ex2" >
<summary class="sum2"><i>Tables</i></summary>

</details>

</details>
 <!--- FIN AUTRES------------------------------------------>

</details>

<!--- TESTS------------------------------------------------->
<!---------------------------------------------------------->

<details open >
<summary>3. Test</summary>

*vvfrgev*



** **

</details>


<!--- CONTROLES--------------------------------------------->
<!---------------------------------------------------------->


<details open >
<summary>4. Controles</summary>


** **

</details>

<!---------------------------------------------------------->





