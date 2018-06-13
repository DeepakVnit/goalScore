python3-pip
virtualenv
sudo apt-get install mysql-server
sudo apt-get install libmariadbclient-dev
sudo /etc/init.d/mysql start
sudo /etc/init.d/mysql stop

# change mysql password: https://support.rackspace.com/how-to/mysql-resetting-a-lost-mysql-root-password/
sudo mysqld --skip-grant-tables &
mysql -u root mysql
# remove sudo for mysql connect https://stackoverflow.com/questions/37239970/connect-to-mysql-server-without-sudo/37241990


sudo apt-get install wget curl build-essential tcl -y
sudo apt-get install redis-server -y

gcloud compute --project "fifaworldcup2018-207005" ssh --zone "asia-south1-c" "fifaworldcup2018"
gcloud compute scp file.txt fifaworldcup2018:~/