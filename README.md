# myraspberry

Este repositório mantém as configurações de meu rasp1-B, permitindo backup e restauração.

Pode servir como exemplo para outras pessoas adaptando às suas necessidades.

Baseado no rapbian stretch lite kernel versão 4.9


## Pacotes
libpcap-dev
fing
vim
git

## para webserver
apache2 php php-mysql mariadb-server 

## apache e tmpfs
tem de ajustar o arquivo /etc/systemd/system/multi-user.target.wants/apache2.service colocando

PrivateTmp=false

## php
apt install php-xml
