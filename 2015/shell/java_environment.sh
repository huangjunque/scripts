#!/bin/bash
#---------script----------------
#   Name:JAVA_environment
#   Version Number:1.0
#   Language:bash shell
#   Date:2014-09-29
#   Author:syd_python
#--------------------------------

Date=`date +%Y%m%d%H`
Log=/var/log/JAVA_environment.log.$Date
java_soft_dir=`pwd`
JAVA_install_home=/usr/local/

yum_install()
{
    yum -y install $1 > $Log
    if [ $? -eq 1 ];then
        echo "install error please is check"
    fi
    mv /etc/localtime{,.bak}
    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    /usr/sbin/ntpdate pool.ntp.org
    echo "0 */2 * * * /usr/sbin/ntpdate pool.ntp.org" >> /var/spool/cron/root

}

java_install()
{
#java and tomcat install
cd $java_soft_dir
rpm -ivh jdk-6u12-linux-i586.rpm
tar zxvf apache-tomcat-6.0.18.tar.gz
cp -a apache-tomcat-6.0.18 $JAVA_install_home/tomcat

echo "export JAVA_HOME=/usr/java/jdk1.6.0_12" >> /etc/profile 
echo "export CLASSPATH=\JAVA_HOME/lib/dt.jar:\$JAVA_HOME/jre/lib/tools.jar" >> /etc/profile 
echo "export PATH=.:\$PATH:\$JAVA_HOME/bin" >> /etc/profile 
echo "export CATALINA_HOME=/usr/local/tomcat" >> /etc/profile 
. /etc/profile 
#start tomcat
/usr/local/tomcat/bin/startup.sh
}

nginx_web_install()
{
 /usr/sbin/useradd www
 cd $java_soft_dir
 tar zxvf nginx-1.2.1.tar.gz
 cd nginx-1.2.1 
 ./configure --prefix=/usr/local/nginx && make && make install
 mv $JAVA_install_home/nginx/conf/nginx.conf{,.bak}
 yes|cp -a ../nginx.conf $JAVA_install_home/nginx/conf/
}

nginx_load_install()
{
/usr/sbin/useradd www
cd $java_soft_dir
tar zxvf nginx-1.2.1.tar.gz
tar zxvf nginx-upstream-jvm-route-0.1.tar.gz
cp -a nginx_upstream_jvm_route ../
cd nginx-1.2.1 
patch -p0 < /usr/local/src/nginx_upstream_jvm_route/jvm_route.patch
./configure --user=www --group=www --prefix=/usr/local/nginx --with-http_stub_status_module \
--add-module=/usr/local/src/nginx_upstream_jvm_route \
make && make install 
mv $JAVA_install_home/nginx/conf/nginx.conf{,.bak}
}
mysql5.5_install()
{
mysql_basedir=/usr/local/mysql5.5 
mysql_datadir=/var/mysql 
cd $java_soft_dir
/usr/sbin/useradd mysql 
mkdir $mysql_basedir
mkdir $mysql_datadir 
chown mysql.mysql -R $mysql_basedir
tar zxvf mysql-5.5.25.tar.gz
cd mysql-5.5.25 
cmake . -DCMAKE_INSTALL_PREFIX=$mysql_basedir -DMYSQL_DATADIR=$mysql_datadir -DMYSQL_UNIX_ADDR=$mysql_datadir/mysqld.sock -DWITH_INNOBASE_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DMYSQL_TCP_PORT=3308 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_READLINE=on -DDEFAULT_CHARSET=utf8  -DWITH_DEBUG=true -DEXTRA_CHARSETS=all && make && make install 
cp -a support-files/my-medium.cnf /etc/my.cnf
cp -a support-files/mysql.server /etc/init.d/mysqld
chmod 755 /etc/init.d/mysqld 
/usr/local/mysql5.5/scripts/mysql_install_db --user=mysql --basedir=$mysql_basedir --datadir=$mysql_datadir
/etc/init.d/mysqld start 
}

case "$1" in 

    yum_install)

    for var in pcre-devel  gcc-c++ openssl openssl-devel ncurses-devel cmake  patch ntp 
    do
    yum_install $var
    done 
    exit 1
    ;;
    java_install)
    java_install 
    ;;
    nginx_web_install)
    nginx_web_install
    ;;
    nginx_load_install)
    nginx_load_install 
    ;;
    mysql5.5_install)
    mysql5.5_install
    ;;
    *)

     echo  "Usage: $SCRIPTNAME {yum_install|java_install|nginx_web_install|nginx_load_install|mysql5.5_install}"
     exit 1
     ;;
esac

exit 0

