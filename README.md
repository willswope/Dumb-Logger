# Dumb-Logger
An ultra-minimalist HTTP-based logging service.

Works on any linux w/ bash and busybox.

To run the service:
 - `cd ~/Desktop`
 - `git clone https://github.com/willswope/Dumb-Logger.git`
 - `chmod +x run.sh`
 - `./run.sh`

To use the service (localhost):

```
user@domain:~/Desktop$ curl -X 'POST' -d "hello, line 1" localhost:8080
curl: (52) Empty reply from server
user@domain:~/Desktop$ curl -X 'POST' -d "hello, line 2" localhost:8080
curl: (52) Empty reply from server
user@domain:~/Desktop$ curl -X 'POST' -d "hello, line 3" localhost:8080
curl: (52) Empty reply from server
user@domain:~/Desktop$ curl localhost:8080
hello, line 1
hello, line 2
hello, line 3
```
To use the service (remotely):
 - Reverse proxy this software and secure with TLS + basic auth. 
   - Ensure that files from your `www/cgi-bin` directory are not served as static files in your reverse proxy software's configuration.
 - *Do not use this software in sensitive contexts.*
