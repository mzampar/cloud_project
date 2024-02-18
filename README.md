The only softare needed to install and run this project is Docker-Desktop.

Since I kept the two containers of Nextcloud and Locust separetaed, the first thing to do is to create a docker network named my_network and the execute the 2 docker-compose files.

```bash
docker network create --driver bridge my_network
docker-compose -f docker-compose-nc.yml up -d
docker-compose -f test/docker-compose-locust.yml up -d # --scale worker=1, to create various workers
```

Since I got a warning for the bz2 package not installed, we can install it directly form the shell of Nextcloud Container (exec section).

```bash
apt-get update
apt-get install -y libbz2-dev
docker-php-ext-install bz2
php -m | grep -i bz2 # verify it has been correctly installed
```

Then restart the container

```bash
docker restart nextcloud
```

Before starting with the tests, we have to add nextcloud to the trusted domains:

```bash
docker exec -u 33 nextcloud php occ config:system:set trusted_domains 1 --value=nextcloud
```


```bash
chmod +x CreateUsers.sh
./test/CreateUsers.sh
```

To run the test, turn on the Locust container , open http://localhost:8089 and start swarming.


Some commands that may be useful:

```bash
# create a new user
curl -X POST -u ADMIN:PASSWORD -H "OCS-APIRequest: true" http://nextcloud-nfs.local/ocs/v1.php/cloud/users -d userid="user1" -d password="abc123abc!"

# to delete a file
curl -X DELETE -u USERNAME:PASSWORD "http://localhost:8080/remote.php/dav/files/USERNAME/path/to/your/file.txt"

# to turn-off maintanence mode
docker exec -u www-data nextcloud php occ maintenance:mode --off

docker exec -u www-data nextcloud php occ upgrade

docker exec -u www-data nextcloud php occ twofactorauth:enforce --off

docker exec -u www-data nextcloud php occ twofactor:disable marcoz totp

docker exec -u www-data nextcloud php occ app:update --all

docker exec -u www-data nextcloud php occ app:disable twofactor_totp

```
