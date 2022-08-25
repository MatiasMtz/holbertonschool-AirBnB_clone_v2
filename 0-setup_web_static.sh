#!/usr/bin/env bash
# Script that sets up a web server for the deployment of web_static
sudo apt-get update -y && sudo apt upgrade -y
sudo apt-get install nginx -y
if [ ! -d /data/web_static/shared ]
then
	sudo mkdir -p /data/web_static/shared
fi
if [ ! -d /data/web_static/releases/test ]
then
	sudo mkdir -p /data/web_static/releases/test
fi
printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tFirst Web Deploy\n\t</body>\n</html>\n" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
grep -qxF $'\tlocation /hbnb_static/' /etc/nginx/sites-available/default || sed -i '/^\tserver_name/ a\\n\tlocation \/hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
