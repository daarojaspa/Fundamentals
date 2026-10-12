The old way was,  each company bougth their server, that server is never turn of and if you needed a 
bigger server, move your headquarters, well abig tsk ahead, the virtual machines got really popular and developed,
if you had a lot of money you could make a  humungus  invertion  in buldings and servers  build virtual machines 
on those servers and then rent those virtual machines, thats how cloud computing was born, the cloud is just a bunch
of servers that you can use but that arent yours. avrage joe normaly just uses storage services, like drive,
 google photos,netflix,gmail,dropbox.
but you can use computing services, eg running your programs  on some one else computer using the internet 
as  comunication sistem, unlike the 50s were you used someone else computer (main frame) but had to be there to use it.

this business model allow small  players to have acces to  top of the line hardware, at a lower cost, in a 
easy to scale fashion. now some extrange  acronims

-IaS: you pay for the virtual machines but you are in charge of  managing how u use them(os, storage,networks)
like a EC2 from AWS, use it  when need to train big models, or  have to do hevy computing (trainning)
-PaaS: the provider also handels os storage setings security patches, is like hiring a  catering service,the provide the kitchen,
 the cooking and the ingridients, you pik the menu (what to run in that envroment) use it when need to serve models as APIs quikly(deploying)
-SaaS:You go out to a restaurant the menu is set, you pick what you want for example,  you pay for a
 prebuild monitoring services for a  ml that you have runin in a PaaS service and that ws train in a IaaS  virtual machine.

Now if you go to AWS and create a new account for the first time, you will probably be over well because is a huge site,
with a lot of options panels and it changes depending on  some factors, not very  comprensible really,
 i will say WAAG 2.2  is not   met (accesibility guide lines). They  have more than 200 services, and they are not the only 
cloud provider, so i asked for a easy to map clasification of the services to gpt so its almost 1 to one mapping with the 
other 2 big cloud providers (GCP and  Azure).

-	Networking and security services: Is about connecting all otheer resources with  safty precaution, managing
	users and group permissions,like you would do in a  pc or a local network.
	- AWS: VPC (networks), CloudFront (CDN), Route 53 (DNS), IAM (identity).

	- Azure: Virtual Network, Front Door/CDN, DNS, Active Directory.

	- GCP: VPC, Cloud CDN, Cloud DNS, IAM. 
-	Compute : Is about where your code runs
	- AWS: EC2 (VMs), Lambda (serverless), ECS/EKS (containers, Kubernetes).

	- Azure: Virtual Machines, Azure Functions, AKS.

	- GCP: Compute Engine, Cloud Functions, GKE.
-	Storage:Any kind of data, like a folder in your local pc,it has a flat structure,use key or path to upload/download
	- AWS: S3 (object storage), EBS (block storage), Glacier (archival).

	- Azure: Blob Storage, Disk Storage, Archive Storage.

	- GCP: Cloud Storage, Persistent Disk, Nearline/Coldline.
-	Databases and analitics: Structure or semi structured data they are build for eficiency on information acces 
	and are not flat, i guees if you are a data analyst this is your nich of services.
	- AWS: RDS (SQL), DynamoDB (NoSQL), Redshift (data warehouse), Athena (querying).

	- Azure: SQL Database, Cosmos DB, Synapse Analytics.

	- GCP: Cloud SQL, Firestore, BigQuery.
- 	AI,ML dev tools:ML pipelines, Ai services  and tools to manage apps
	- AWS: SageMaker (ML), Rekognition (vision), Comprehend (NLP), CodePipeline, CloudWatch.

	- Azure: Azure ML, Cognitive Services, DevOps.

	- GCP: Vertex AI, Vision/NLP APIs, Cloud Build, Cloud Monitoring.
	

now you have a broder and consistent pictore of the services in the cloud  in a way you can generalize to all major 
providers,lets talk about regions

They represent the physical locations where the data centeers are, depending on the region and services  prices will change,
this also happens for all providers, so when picking region you want to  select the one that have athe services you need and 
 best prices but also near your clients. Here a tip to know wich servises will be global (available in all regions) and wich ones no.

If it's networking and identity (IAM, DNS or billing) its gonna be  global, all others are region based, 
some can be access globally eather paying extra or using then in convbination with other networking services (so paying extra).
the AWS web page chages depending in wich reagion you have it set up (The web page is normally called AWS console),
so you will find usefull to:
	- if you are experimenting for the first time pick us-est-1 region it has the wildest availability
	- Use the search bar, it does not filter by region , and its faster some times
	- when you find what you are looking book mark the page
	- learn AWS CLI or SDK if UI changes messes with you  a lot (like if u use a screen reader).

finally a Cheat sheet for ML engineers that are starting in cloud and don't know where to start.

| **Category**                   | **AWS** (most known for ML beginners ⭐)                             | **Azure**              | **GCP**         |
| ------------------------------ | ------------------------------------------------------------------- | ---------------------- | --------------- |
| **Compute (Run code)**         | **Lambda** ⭐ (serverless, easy to deploy small models/APIs)         | Azure Functions        | Cloud Functions |
| **Storage (Save data/models)** | **S3** ⭐ (store datasets, models, logs)                             | Blob Storage           | Cloud Storage   |
| **Databases & Analytics**      | **RDS** ⭐ (managed SQL, great for ML feature storage)               | SQL Database           | Cloud SQL       |
| **Networking & Security**      | **IAM** ⭐ (manage roles/permissions, critical for safe deployments) | Azure Active Directory | IAM             |
| **AI/ML & Dev Tools**          | **SageMaker** ⭐ (train, deploy, monitor ML models)                  | Azure ML               | Vertex AI       |


I am the only one that got a little frustrated when traing to  work with cloud services  for the first time? i mean, is not intuitive, althougth i untherstand the paradigms is build on, so i decided to start a series of  easy to read texts that i wuld like to have in hand to paint me the big picture so the learnning resistance wass less. does not matter if you are a Ai lernner or not this could be helpful