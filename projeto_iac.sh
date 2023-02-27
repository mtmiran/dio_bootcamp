#!/bin/bash


echo "=-=-=-=-= Excluindo diretórios e arquivos =-=-=-=-="

rm -rf ~/*

## ENTRE COMO ROOT 

echo "=-=-=-=-= Criando diretórios =-=-=-=-="

mkdir /publico
mkdir /adm
mkdir /ven
mkdir /sec

echo "=-=-=-=-= Criando grupos de usuários =-=-=-=-="

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "=-=-=-=-= Criando usuários =-=-=-=-="

# caso o openssl não esteja instalado
sudo apt install openssl -y

# grupo GRP_ADM
useradd carlos -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_ADM
useradd maria -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_ADM
useradd joao_ -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_ADM

# grupo GRP_VEN
useradd debora -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_VEN
useradd sebastiana -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_VEN
useradd roberto -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_VEN

# grupo GRP_SEC
useradd josefina -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_SEC
useradd amanda -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_SEC
useradd rogerio -m -s /bin/bash -p $(openssl passwd -crypt 123) -G GRP_SEC

echo "Especificando permissões dos diretórios...."

chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec

chmod 770 /adm
chmod 770 /ven
chmod 770 /sec
chmod 777 /publico
