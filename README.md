# cloud_project

First step: chose nextcloud as suggested and mysql as database.

First problem: find user registration, i had to install the Registration app, found a tutorial on the internet: 
https://www.youtube.com/watch?v=8tydyKqUPBY

Second problem: deal with emails:
another tutorial, 
https://www.youtube.com/watch?v=7NqL9ccYOlk
created a new google account and created app password: Nextcloud Password Recovery.
Then configured basic settings, email sst smtp...

problems with the confirmation emails
mail app downloaded and enabled, it wasn't this, mail was on the spam!

then tried to create a new account and tried password recovey, it worked!





Address Scalability:
- Design the system to handle a growing number of users and files.
- Discuss theoretically how you would handle increased load and traffic.

To address scalability in the given Docker Compose setup for Nextcloud with MySQL, you can make adjustments and introduce some theoretical considerations. Below are some suggestions:

Database Scaling:
MySQL can be scaled horizontally through techniques such as database sharding, where data is distributed across multiple database instances. This helps distribute the database load and ensures better performance as the user and file count increases.

Caching:
Implement caching mechanisms within Nextcloud to reduce the load on the MySQL database. Utilize in-memory caching solutions like Redis or Memcached to store frequently accessed data and improve response times.

done

Load Balancing:
Use load balancing for both Nextcloud instances and MySQL database servers. Distributing the load across multiple servers helps maintain system performance under increased traffic.

This worked! i see the same users using different ports, so it works.

Theoretically:

Asynchronous Processing:
Offload tasks that don't require immediate user feedback to asynchronous processing. For example, background processes for file indexing, thumbnail generation, and other non-critical tasks can be handled separately.

Object Storage for Files:
Consider integrating object storage solutions like Amazon S3 or Google Cloud Storage for storing files. Object storage is highly scalable and can handle large amounts of data, providing a more efficient solution for file storage.

Auto-Scaling:
Configure auto-scaling for both Nextcloud and MySQL instances based on predefined metrics. This ensures that resources are dynamically adjusted to handle varying workloads.

Backup and Restore Strategy:
Implement a robust backup and restore strategy for MySQL to ensure data integrity and availability. As the system scales, having reliable backup mechanisms becomes crucial.

Global Distribution:
If your user base is distributed globally, consider deploying Nextcloud and MySQL instances in multiple regions. This reduces latency and improves user experience for users in different geographical locations.

Optimized Database Queries:
Ensure that database queries executed by Nextcloud are optimized. Regularly review and optimize queries to prevent database performance bottlenecks.

Regular Performance Testing:
Conduct regular performance testing, simulating scenarios with a growing number of users and files. This helps identify potential bottlenecks and allows for proactive optimization.

Scalable Infrastructure:
Choose a cloud provider that offers scalable infrastructure. Cloud platforms like AWS, Azure, and Google Cloud provide tools and services for auto-scaling, load balancing, and global distribution.

5. Content Delivery Network (CDN):
Integrate a CDN like Cloudflare to cache and serve static content, reducing the load on your Nextcloud instances.

6. Global Distribution (Theoretical):
If the user base is global, deploy instances of Nextcloud in multiple regions to reduce latency and improve user experience.

7. Monitoring and Analytics:
Implement monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential bottlenecks. Set up alerts to respond to critical issues.

user usage report to have updates about the usage of the system.



Address Security:
- Implement secure file storage and transmission.
from nextlcoud
Server-side encryption
Server-side encryption makes it possible to encrypt files which are uploaded to this server. This comes with limitations like a performance penalty, so enable this only if needed.


now i'm using nc locally, but if i used it online i used it on https, so the connecton in encrypted
Employ secure communication protocols such as TLS/SSL for encrypting data in transit. This safeguards files during transmission between clients and the cloud storage system.

another problem
Setting up Remote Access to your Next Cloud Server (AT&T)

dynamic dns provider:
https://www.youtube.com/watch?v=3NES2gFQ5ek

Nextcloud on the Internet with no router config or VPN with Cloudflare
https://www.youtube.com/watch?v=Vg1Wj5v7WFQ





idea: use cloudlared in docker-compose.yml

to expose my local nextcloud system we could use cloudflared, using a tunnel to connect my remote system with the internet

https://community.cloudflare.com/t/can-i-use-cloudflared-in-a-docker-compose-yml/407168


https://github.com/jonas-merkle/container-cloudflare-tunnel/blob/master/src/Dockerfile


- Discuss how you would secure user authentication.
Two-Factor Authentication, avaible in the security section of administration settings
Two-factor authentication can be enforced for all users and specific groups. If they do not have a two-factor provider configured, they will be unable to log into the system.

- Discuss measures to prevent unauthorized access.
Access Logging and Monitoring:
Enable detailed access logging to track user activities. Regularly monitor these logs for any suspicious or unauthorized access patterns. This allows for quick identification and response to security incidents.



Discuss Cost-Efficiency:
- Consider the cost implications of your design.
- Discuss how you would optimize the system for cost efficiency.

Right-sizing storage and cost efficiency: While estimating the server needs for Nextcloud in terms of computation or a database is straightforward, right-sizing disk space is a challenge. Provision too much, and you will have to pay for unused capacity. Provision too little, and you will not be able to store all the files and content you want to work on. Adding a cloud provider storage extension, such as with Amazon S3, makes it possible to flexibly scale resources and avoid high fixed costs when space is no longer used.

We know that cloud serivices are based on the idea of "infinte resources" but at the same time we must keep in mind the pay-as-yo-go concept: it is important to balance these two sides, without being too hungry of resources not really needed: be wise and not hurry!

Right-sizing Instances: Choose cloud instances with appropriate sizes based on your actual resource requirements. Avoid over-provisioning, as this can lead to unnecessary costs. Regularly monitor resource usage and adjust instances accordingly.

Compression and Deduplication: Implement compression and deduplication techniques to reduce the amount of storage space required for files. This can lead to cost savings, especially when dealing with large datasets.

CDN Usage: If your system involves content delivery, leverage Content Delivery Networks (CDNs) to reduce data transfer costs. CDNs cache content closer to users, minimizing the need for data transfer over long distances.

Auto scaling and load balanicng were discussed earlier, but it is important to remembrer that they can help in reducing costs.

Auto-Scaling: Configure auto-scaling groups to automatically adjust the number of instances based on demand. This ensures that you have the right amount of resources to handle varying workloads, avoiding unnecessary costs during low-traffic periods.
Load Balancing: Distribute incoming traffic across multiple instances using load balancers. This ensures that resources are utilized efficiently and helps in maintaining a balanced workload.


Anyway, it is important to design well a system but the most important part is to keep updated and follow the develpoment of the system.


Deployment:
- Provide a deployment plan for your system in a containerized environment on your laptop based on docker and docker-compose.
- Discuss how you would monitor and manage the deployed system.
- Choose a cloud provider that could be used to deploy the system in production and justify your choice.



about scaling, what changes is that, as you have "infinte resources" you have no problems in scaling as regards memory, because the cloudprovider scales autonoumously, but we have to remember that as the system is pay as you go also cost scale!
 it could be a problem managing the flow and the number of users, not managed by the cloud provider if we use nextcloud. 


