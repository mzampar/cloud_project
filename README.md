# Cloud Basic Project

This project is based on Docker, a Docker-compose file, and then I customized Nextcloud form the administration settings, like user registration, configured mail for password recovery, email sst smtp...

First problem: find user registration, i had to install the Registration app, found a tutorial on the internet: 
https://www.youtube.com/watch?v=8tydyKqUPBY
Second problem: deal with emails:
another tutorial, 
https://www.youtube.com/watch?v=7NqL9ccYOlk
created a new google account and created app password: Nextcloud Password Recovery.
Then configured basic settings, 

problems with the confirmation emails
mail app downloaded and enabled, it wasn't this, mail was on the spam!

then tried to create a new account and tried password recovey, it worked!


## Address Scalability:
- Design the system to handle a growing number of users and files.

The system I designed is basically a Nextcloud connected with Mysql database.

We add an instance of Redis we could also implement caching mechanisms within Nextcloud to reduce the load on the MySQL database. Utilize in-memory caching solutions like Redis or Memcached to store frequently accessed data and improve response times.

A rudimental approach to handle a growing number of users and files would be a horizontal scaling in both the database and in the nextcloud instances trough proxies.

It is know that there are two different ways of scaling: horizontal and vertical and often the first approach is better in terms of costs and flexiblity, but can be more complex to organise.

To handle a growing number of users, we opt for a horizontal approach, we could create more instances of Nextlcoud and balance the traffic between them, 


Load Balancing:
Use load balancing for both Nextcloud instances and MySQL database servers. Distributing the load across multiple servers helps maintain system performance under increased traffic.

This worked! i see the same users using different ports, so it works.

To handle a growing number of files, we could choose both the approaches, enlarging the memory space or creating new instances of mysql databases.


Database Scaling:
MySQL can be scaled horizontally through techniques such as database sharding, where data is distributed across multiple database instances. This helps distribute the database load and ensures better performance as the user and file count increases.

We must note that these approaches are rudimental and it should be better to use autoscaling procedures.


- Discuss theoretically how you would handle increased load and traffic.


First of all, I would consider integrating object storage solutions like Amazon S3, Google Cloud Storage or Azure Blob Storage for storing files, because object storage is highly scalable and can handle large amounts of data, providing a more efficient solution for file storage. 
An infrastructure as a service like which takes care autonoumously of the storage and everything concerning it, like scalability, Optimized Database Queries, Asynchronous Processing.

Thanks to the concept of infinite resources availabilty we don't have to hurry about scaling, we only have to remembrer that, for the pay-as-you-go billing method, the more resources we use the more we pay!

Another interesting feature to handle load balancing and gloabl distribution is offered by cloudflared, a Content Delivery Network that has many servers all over the world, so it can improve the performances of the website in terms of latency.
Integrate a CDN like Cloudflare to cache and serve static content, reducing the load on your Nextcloud instances.

In this way, I think we are close to autoscaling, because both load and storage scale automatically.



## Address Security:

- Implement secure file storage and transmission.

    The first task I did to secure file storage is Server-side encryption: it is available directly from the Security section of Administration settings:
    Server-side encryption makes it possible to encrypt files which are uploaded to the server, it has a drawback in efficiency, since it reduces performance.

    As far as transmission, now I'm using Nextcloud locally, but if I had to set up remote access to my Next Cloud Server, I would employ secure communication protocols such as TLS/SSL for encrypting data in transit, that is I would use the https protocol: I would buy a domain and then use services like CloudFlared to create a tunnel between my local server and the domain. Cloudflared offers many advantages: I don't have to show my IP address, encrypts autonoumsly the connection and has many servers all over the world that can better the latency and deal with large amounts of accesses.


- Discuss how you would secure user authentication.

    In order to secure user authentication I would enable Two-Factor Authentication, available in the security section of administration settings: it works with a TOTP authenticator and can be enforced for all users or specific groups.

    I would also force the use of strong passwords enabling a monthly expire of the password, which can be done in the Security section of Administration settings.




    
- Discuss measures to prevent unauthorized access.

    First of all I would leverage the Nextcloud Security Scan -https://scan.nextcloud.com- to check for unknown vulnerabilities of my system.

    I would regularly look at the Activity and Logging sections of the admin page for any suspicious or unauthorized access patterns. I would create a "Suspicious" group of users to easily follow their behaviour.

    I would also use the Suspicious Login tool provided by Nextcloud, and I would set a small number of login attempts before the user account is blocked.



## Discuss Cost-Efficiency:
- Consider the cost implications of your design.

The costs of my desgin are: the domain, Content Delivery Network and the Object Storage service.


- Discuss how you would optimise the system for cost efficiency.

    Let's assume I'm the director of a company, the first thing in which I would invest is cloud data storage, and here comes the trouble:
    
    Right-sizing storage and cost efficiency: While estimating the server needs for Nextcloud in terms of computation or a database is straightforward, right-sizing disk space is a challenge. Provision too much, and you will have to pay for unused capacity. Provision too little, and you will not be able to store all the files and content you want to work on. Adding a cloud provider storage extension, such as with Amazon S3, makes it possible to flexibly scale resources and avoid high fixed costs when space is no longer used.

We know that cloud serivices are based on the idea of "infinte resources" but at the same time we must keep in mind the pay-as-yo-go concept: it is important to balance these two sides, without being too hungry of resources not really needed: be wise and not hurry!

Right-sizing Instances: Choose cloud instances with appropriate sizes based on your actual resource requirements. Avoid over-provisioning, as this can lead to unnecessary costs. Regularly monitor resource usage and adjust instances accordingly.

Compression and Deduplication: Implement compression and deduplication techniques to reduce the amount of storage space required for files. This can lead to cost savings, especially when dealing with large datasets.

Auto scaling and load balanicng were discussed earlier, but it is important to remembrer that they can help in reducing costs.

Auto-Scaling: Configure auto-scaling groups to automatically adjust the number of instances based on demand. This ensures that you have the right amount of resources to handle varying workloads, avoiding unnecessary costs during low-traffic periods.
Load Balancing: Distribute incoming traffic across multiple instances using load balancers. This ensures that resources are utilized efficiently and helps in maintaining a balanced workload.


Anyway, it is important to design well a system but the most important part is to keep updated and follow the develpoment of the system.


## Deployment:
- Provide a deployment plan for your system in a containerized environment on your laptop based on docker and docker-compose.

The deployment of the system is avialable on my GitHub repository, with the docker-compose and Dockerfile.

- Discuss how you would monitor and manage the deployed system.

A basic tool is the user usage report of Nextlcoud

- Choose a cloud provider that could be used to deploy the system in production and justify your choice.

I would choose Amazon Web Services as the Cloud Provider, precisely the Amazon S3 Object File Storage System, which in many blogs and sites is referred to as the best provider in terms of costs, reliability, and scalability for object storage solutions, paired to the low-latency access.

The pay-as-you-go pricing model of AWS, coupled with the ability to scale storage resources seamlessly, aligns well with the requirements of our cloud-based file storage system.

As regards the CDN, a valid option is Amazon CloudFront. Amazon CloudFront is a global CDN service that accelerates the delivery of content (such as web pages, images, videos, and other assets) to end-users. It uses a network of edge locations worldwide to cache and serve content from locations that are closer to the end-users, reducing latency and improving the overall performance of web applications.

Global Reach: CloudFront has a large network of edge locations strategically distributed around the world, enabling fast and low-latency content delivery.
Integration with AWS Services: CloudFront seamlessly integrates with other AWS services, including Amazon S3, Amazon EC2, AWS Lambda, and more. This makes it easy to distribute content stored in AWS and deliver dynamic or static content from various sources.
Security: CloudFront provides features such as HTTPS support, field-level encryption, and integration with AWS Identity and Access Management (IAM) for secure content delivery.
Scalability: The service scales automatically to handle varying levels of traffic, ensuring that content is delivered efficiently even during traffic spikes.
Customization: CloudFront allows for customizations such as setting cache behaviors, configuring access controls, and enabling features like signed URLs or cookies for secure content delivery.

Concerning the domain, there is plenty of offers and possibilities to consider.


## Test your infrastructure:
- Consider the performance of your system in terms of load and IO operations

Regular Performance Testing:
Conduct regular performance testing, simulating scenarios with a growing number of users and files. This helps identify potential bottlenecks and allows for proactive optimization.
7. Monitoring and Analytics:
Implement monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential bottlenecks. Set up alerts to respond to critical issues.

user usage report to have updates about the usage of the system.

