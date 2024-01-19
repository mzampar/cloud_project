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

another problem
Setting up Remote Access to your Next Cloud Server (AT&T)

dynamic dns provider:
https://www.youtube.com/watch?v=3NES2gFQ5ek

Nextcloud on the Internet with no router config or VPN with Cloudflare
https://www.youtube.com/watch?v=Vg1Wj5v7WFQ



idea: use cloudlared in docke-compose.yml
https://community.cloudflare.com/t/can-i-use-cloudflared-in-a-docker-compose-yml/407168


https://github.com/jonas-merkle/container-cloudflare-tunnel/blob/master/src/Dockerfile