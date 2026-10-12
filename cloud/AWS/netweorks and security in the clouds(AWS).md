# IAM

You can create **users**, **roles**, and **groups**.  
If you are reading this in 2025, you will notice that AWS is encouraging you to use **IAM Identity Center**.  

The idea is that this acts as a single login for all your AWS accounts and applications.  
**What’s the difference?**  
- If you need to switch between different accounts in one day (e.g., AWS Organizations), use the **Identity Center**.  
- If not, the “vanilla flavor” (classic IAM) is easier to learn while you get comfortable working in the cloud.

---

## Users, Groups, and Roles

- **Creating a user and a user group** is not very difficult.  
  As of 2025, the options are in the left panel.  

- **Roles** have no credentials. Think of them like a “hat” or a “job title” that can be assumed by anyone or anything.  
  - **Instance Role**: A role assumed by an instance. When you create instances of other services, this is essential for communication between them.  

With these three (users, groups, roles), we have covered the **“who” layer**.

---

## Policies

For the **“what” layer**, we have **policies**.  
- Written in **JSON** format.  
- Define **who can access what and when**.  
- Components include:  
  - **Version**  
  - **ID**  
  - **Statement** (which contains):  
    - `Sid` (statement ID)  
    - `Effect` (Allow or Deny)  
    - `Principal` (who the policy applies to)  
    - `Action`  
    - `Resource`  

---

## Best Practices

- Save your **root credentials** (the ones you created the account with) in a safe place.  
- Create an **IAM user with admin access policy** to use your account day-to-day.  
- It’s best practice to attach **policies to groups**, not individual users, and then assign users to groups.  

⚠️ **Reminder**: To log in as a user, you need the **account ID**.  
You can find it under **My Account** when logged in as the root user.

apart of all this you can use the  credentials report to  have an overview of the users we have attached to our aws account
and also have the access advisor it will show us all the permits by services in a granular lavel.


## networks in  the clouds

### vpc
	-regions, availability zones, private and public subnets
	-nat getways internet getways
# CIDR : clas inter domain routing
 nwhat does 0.0.0.0/24 mean?
## cloudfront : acts  as an intermediary between the client and the server  routes  request to the edge servers, 
 so it  ges you a low latancy because your request, "goes around the pool" insted of having to cross it when is crowded.

#route53
is a DNS host server inside amason cloud that allows you to route trafic to other ip adresses , domains, or resources inside AWS cloud
now you have Arecords to point to  ip adresses  CName records to point to  another domain and  the aliases that are use to point
to AWS resources like C3

Data governance and observability are also a bunch of services that we eill not cover in this series but  they escentiall

cloud formation work esentially as a .yml file where the infrastructure is define to save  and do version control and then build as it was a docker
cloud wach for monitoring services as the task administrator in windowws 10 ?
load balancer, when you have aouto scaling activated instance of your server will be dinamiclly created and erased, load balancer
balance the requests to this instances

#when creatting a  ec2 i encounter that with each ec2 a security group was crated, i first tougth they had some thing
to do with  iam policies but ni, they are the set ups of the firewalle between our instance and the world. at first 
i was having trouble conecting to my instance tougth the public ipv4 but this was because  i set the http  inbound rule for ipv4 directions and i guess i was using ipv6 in my pc. also i realized this was so important when the conection time out error apear on myssh conection atempts
