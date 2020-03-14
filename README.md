### Setup
- Install `pipenv` for whatever OS you use, and run `pipenv install` in the project root
- `cd scripts/` and run `./run_server.sh`

### Running the nginx server
- Install nginx 1.13.1 from source
  - https://www.vultr.com/docs/how-to-compile-nginx-from-source-on-ubuntu-16-04
  - https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/
- Patch the source code with `hpack.patch`
  - http://manpages.ubuntu.com/manpages/bionic/en/man1/patch.1.html
  - https://github.com/cloudflare/sslconfig/issues/72
- Setting up the certificate
  - https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
