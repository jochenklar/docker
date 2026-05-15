docker
======

Docker compose setups for various services, to be used in development. The idea is to use
them with [copier](https://copier.readthedocs.io), e.g.:

```bash
mkdir ~/code/docker/postgres
copier copy ~/code/templates/docker/postgres .
make
```
