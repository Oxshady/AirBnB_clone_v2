#!/usr/bin/env bash
#configuring my web server to deploy my static app
sudo apt update -y -qq > /dev/null
sudo apt install nginx -y -qq > /dev/null
my_app="/data/web_static/releases/test/"
if [ ! -d $my_app ]; then
	sudo mkdir -p $my_app
fi
if [ ! -f "$my_app/index.html" ]; then
	sudo touch "$my_app/index.html"
	sudo chmod 755 "$my_app/index.html"
fi
data="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo echo "$data" | sudo tee "$my_app/index.html" > /dev/null
sym_lin="/data/web_static/current"
dir_to_lin="/data/web_static/releases/test/"
sudo ln -sf "$dir_to_lin" "$sym_lin"
sudo chown -R "ubuntu":"ubuntu" /data/
sudo chmod -R 755 /data
sudo sed -i '59i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
sudo nginx -s reload
