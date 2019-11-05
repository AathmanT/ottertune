#!/usr/bin/env bash
sudo -u postgres /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -w restart
cd /etc/postgresql/10/main/
sudo cp postgresql.conf.ottertune.bak postgresql.conf
sudo service postgresql restart