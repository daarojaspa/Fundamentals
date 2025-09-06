IAM
you can create users, roles groups if you read this in 2025 you will find out  AWS is trying you to use  IAM identiry center.
The idea is that this is a single loging for all your AWS accounts an aplications whats the diferences?  if you need to switch between 
diferent accounts in one day eg AWS organizations ,  use the identyty center, if not  vanilla flavor is easier to learn
while you get  confortable working in cloud.

create a user and then a user group is not very dificult  rigth now  2025  the options re int he left panel. now roles have no credentials
is kind of a  had that or a job title can be asumme by anyone or  anything, role instance is a role were by and instance, when you create instance of other services this is undispensable
 for this instances to comunicate between them  with this  3 we have cover the (whom) layer 
now for the what we have polices, wich are writen in json format ant tell us who can acces what and when. now is good
practice to save your root credentials ( the ones u created the account with, in a safe  place, and create an IAM user 
with admin access policy to use   you acount from. althoug is best practice to attach policies to groups not users, and
then users to groups, so your call. just remember, you need to save the account ID to enter as a user is unther my acount in the root user.

amazon charges by usage, 
now there is a 12 moth  free tier, but not all services are free, and the ones that are , usually get limited usage, so
the next sensible thing to do is to set  spending alerts, so search  for billing and cost management in the search bar
after selecting it in the left panel you will find a budget option, it alowsyou to put allerts when your
 spending is getting out of the budget in a time span.


EC2 and computting

the E stands for Elastic, so you can grou or shrinck the  spesifications of the  instance of the EC2  you pick,
paying for the  time and resources you use, then you install operative systems and all programs you need.
there are diferent families they are: 
	-general porpuse (M,T)
	-compute specialization (C)
	-Storage related tasks (H-I)
	-Memory iptimise (R,x,z)

Then we have lambda functions, its a skedwall task, that is run  when the trigger  happens, the trigger can be any thing
(the most commund one is  atime in the day) you dont have to set ub ec2 instances, instal operating systems, just put your cod and set 
the trigger


Storage
tehre are 3 paradims of storage all cover by  a service on AWS

-folder based: works as the folder system in your pc, is herarchical not that much capacity  very little latency
is normaly used when need concurrency acces ( alot of people at once) EFS or amazonFSX for windows file server
-object base: the unit is the object, that can be any file type, wich is asociated to a meta data, like name, date unic ID
this meta data is what is use to retrive the onject more capacity, slower to acces Amazon, S3
- blocked base: Information is divided in blocks of a fix length (Mb) they are tagged with meta data too, but as little as posible
	best of both amazon EBS
 if you are creatting any of this  storage remember you can give  access to the oiblic  on the bucker (e.g S3 bucker with cli activated)
and the files still not be public, so eather you change the privacy settings of ech file or, you writte a policy file ussing the policy generator of AWS to set all this permissions at onece

Data Bases
	- Aurora: it supports aaround 6 data bases engines, like oracle,posgress,mariaDB,
	- RDS: It simplydfys everithing that has to do with maintanances config,  scaling and back up of  relational data bases
	- DynamoDB: For key value data bases (i magine it as a book of json files)
	- Elastic cache:it uses redis and mem cache
	- DocumentDB

ML services:I think these are greate to integrate accessibility features that allowed  your aplication to complain with the recently 
created WCAG 3 
	-recognition:  allows you to  detect harmfull objects, harmfull content, faces , and text in images and videos, so you can 
	integrate this ml service in your housted aplications, it uses json  as default output.
	- Polly: text to speech services
	- lex: for chatbot creation
	- Transcript: for speech to text creation
ofcourse there are more  and i imagine more will be created with the passed of time this is just a little pick

d
