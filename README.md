# Cloud Basic Project

This project is based on Docker, a Docker-compose file, and then I customized Nextcloud from the administration settings, like user registration, Configure SMTP server for email for password recovery and email notifications.


## Address Scalability:
- Design the system to handle a growing number of users and files.

    The system I designed is basically a Nextcloud connected with Mysql database.

    We add an instance of Redis to implement caching mechanisms within Nextcloud to reduce the load on the MySQL database, this can improve response times.

    A rudimental approach to handle a growing number of users and files would be a horizontal scaling in both the database and in the nextcloud instances trough proxies: this approach can to scaling can save money but can be harder to implement respct to a vertical scaling in wich we simply buy a bigger -and more expensive- disk block.

    To handle a growing number of users, we opt for a horizontal approach, we could create more instances of Nextlcoud and distribute the load between them.

    To handle a growing number of files, we could implement database sharding, where data is distributed across multiple database instances. This helps distribute the database load and ensures better performance as the user and file count increases.


- Discuss theoretically how you would handle increased load and traffic.

    My system works locally, to implement remote access one solution could be to buy a domain and set a tunnel between my local port and the domain.

    Trough an Application Load Balancer we could also handle an increasing traffic on my domain.

    Another step to do is using a data storage serivce offered by a cloud provider, so that we don't have to worry about scaling our database, but thanks to the concept of infinite resources paradigm we can use all the resources needed, being aware of the pay-as-you-go policy, the more memory we allocate, the more we will spend!

    The last step to improve performance may be using a Content Delivery Network.

    Another step that can be performed is to deploy the system trough a Container directly on the Cloud Provider.

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

    I would regularly look at the Activity and Logging sections of the admin page for any suspicious or unauthorized access patterns.

    I would also use the Suspicious Login tool provided by Nextcloud, and I would set a small number of login attempts before the user account is blocked.


## Discuss Cost-Efficiency:
- Consider the cost implications of your design.

    The costs of my desgin are: the domain, the Object Storage service and eventually the Application Load Balancer and Content delivery network.

    The cost of a domain is often fixed, but AWS policy is pay-as-you-go also for this, it depends on Hosted Zones, Queries and others.

    We can choose different pricing for the Object Storage service, like S3 Standard - General purpose storage for any type of data, typically used for frequently accessed data or
    S3 Intelligent - Tiering * - Automatic cost savings for data with unknown or changing access patterns and many others. The choice strongly depends on how we will use our system.

    As far as the Applicaton Load Balancer, it has a fixed cost per hour, plus an additional cost varying on the number of connections.

    It is important to note that as your system scales, so do the costs! That is why it is important to have an estimate of the cost a single user has and the profit he can provide: if the system is not weel developed, you could have millions of customers but still lose money!


- Discuss how you would optimise the system for cost efficiency.

    The first problem to face is right-sizing storage and cost efficiency: "while estimating the server needs for Nextcloud in terms of computation or a database is straightforward, right-sizing disk space is a challenge. Provision too much, and you will have to pay for unused capacity. Provision too little, and you will not be able to store all the files and content you want to work on."
    What I would do is, depending on the needs and the money available, to have an hybrid approach:  investing in some basic disk space for every-day tasks and going to the cloud when extra resources are needed.
    We must admit that this approach can save money, but it requires attention and domain expertise, since when the resources are again avaialable in the base storage we have to be able to safely move back the resources from the cloud to our base storage.

    Another choice aimed to improve cost/efficiency is to choose Object File Storage instead of traditional storage because it's much cheaper: cents/gb vs dollar/gb.

    Another aspect that helps in reducing costs is surely autoscaling, and we can say that our design is close to it, thanks to the fact that the cloud provider that gives us the storage and the Application Load Balancing scale authomatically and have an intelligent way of pricing: the pay-as-you-go policy.

## Deployment:
- Provide a deployment plan for your system in a containerized environment on your laptop based on docker and docker-compose.

    The deployment of the system is avialable on my GitHub repository, with the docker-compose and Dockerfile.

    For a more developed project we colud implement what we discussed theoretically in section `Address Scalability`.


- Discuss how you would monitor and manage the deployed system.

    A basic tool is the User usage report of Nextlcoud.

    First of all, I would regularly keep track of the users, the data storage and the activities.
    It is important to note that because of the pay-as-you-go policy, the more resources you allocate, the larger the monthly bill! 
    A way to manage the system could be setting a maximum storage space for every user, and creating various groups of users like base-premium to differentiate the storage space availability.

    I would also execute regular tests on the performace of my system to make the right adjustements where needed: another aspect in favour of using a cloud provider is that it facilitates the process of testing.


- Choose a cloud provider that could be used to deploy the system in production and justify your choice.

    I would choose Amazon Web Services as the Cloud Provider, precisely the Amazon S3 Object File Storage System, which in many blogs and sites is referred to as the best provider in terms of costs, reliability, and scalability for object storage solutions, paired to the low-latency access.

    The pay-as-you-go pricing model of AWS aligns well with the requirements of our cloud-based file storage system.

    The second ingredient is a domain to gurantee remote access. There is plenty of solutions, but if we want to keep a seamless integration we could stick with AWS, in particular AWS Route 53.

    And then we need a tunnel between my local port and the domain. This can be done also with AWS by leveraging services such as AWS Elastic Load Balancer (ELB) or AWS API Gateway, which provide secure and scalable options for exposing local services to the internet.

    We could also do better! If we are distributing our serivce all over the world and we want to reduce the latency, we could add a Content Delivery Network, like Amazon CloudFront: it is a global CDN service that accelerates the delivery of content (such as web pages, images, videos, and other assets) to end-users. It uses a network of edge locations worldwide to cache and serve content from locations that are closer to the end-users.

    We note that there is plenty of solutions but I decided to stick with AWS to operate seamlessly in the same enviroment.


## Test your infrastructure:
- Consider the performance of your system in terms of load and IO operations


create an external network to make communicate nextcloud and locust. 

docker stats nextcloud for IO operations


Regular Performance Testing:
Conduct regular performance testing, simulating scenarios with a growing number of users and files. This helps identify potential bottlenecks and allows for proactive optimization.
7. Monitoring and Analytics:
Implement monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential bottlenecks. Set up alerts to respond to critical issues.



where i found the docker compose for locust
https://github.com/locustio/locust/blob/master/examples/docker-compose/docker-compose.yml

bettere this:
https://github.com/MorrisJobke/load-testing/blob/master/locust/locustfile.py

tell how to compile the docker-compose.yml

docker-compose -f docker-compose-nc.yml up -d
docker-compose -f test/docker-compose-locust.yml up -d

curl -X POST -u ADMIN:PASSWORD -H "OCS-APIRequest: true" http://nextcloud-nfs.local/ocs/v1.php/cloud/users -d userid="user1" -d password="abc123abc\!"

to fix maintanence mode
docker exec -u www-data nextcloud php occ maintenance:mode --off

docker exec -u www-data nextcloud php occ upgrade

docker exec -u www-data nextcloud php occ twofactorauth:enforce --off

docker exec -u www-data nextcloud php occ twofactor:disable marcoz totp

docker exec -u www-data nextcloud php occ app:update --all

docker exec -u www-data nextcloud php occ app:disable twofactor_totp

docker exec -u 33 nextcloud php occ config:system:set trusted_domains 1 --value=test-master-1

docker exec -it nextcloud cat /var/www/html/config/config.php 


created a network,
connected nextcloud and locust


curl -X POST -u marcoz:Willie75 -H "OCS-APIRequest: true" http://localhost:8080/ocs/v1.php/cloud/config -d key="trusted_domains" -d value="['localhost', 'test-master-1']"


curl -X POST -u marcoz:Willie75 -H "OCS-APIRequest: true" http://localhost:8080/ocs/v1.php/cloud/users -d userid="user1" -d password="abc123abc\!"