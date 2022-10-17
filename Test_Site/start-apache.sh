command sudo cp -r apache2.conf /etc/apache2
command sudo cp -r serve-cgi-bin.conf /etc/apache2/conf-available/serve-cgi-bin.conf
command sudo cp -r 000-default.conf /etc/apache2/sites-available/
command sudo a2enmod cgi
command sudo a2enmod rewrite
command sudo service apache2 start
command sudo service apache2 restart