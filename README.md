orgie
=====

Orgue de barbarie 2.0?

Le système fonctionne avec une raspicam et simplecv, une surcouche python d'opencv

Il faut installer une version récente d'opencv
Des instructions sont disponibles ici http://tothinkornottothink.com/post/59305587476/raspberry-pi-simplecv-opencv-raspicam-csi-camera

La compilation d'opencv a pris une dizaine d'heure...
Il y a quelques modifications à apporter aux informations données sur le site tothinkornottothink

Il faut lancer la commande suivante pour supprimer les anciennes librairies
apt-get remove libopencv-core2.3

Il faut également ajouter la ligne suivante dans le fichier ~/.bashrc
export PYTHONPATH=/usr/local/lib/python2.7/site-packages/

Installer simplecv en suivant les instruction sde tothinkornottothink
Il faut ajouter une dépendence qui a été rajoutée dans simplecv
sudo pip install svgwrite

Concernant les drivers, j'ai d'abord essayé d'installer UV4L CSI driver http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14  

Cela a bien marché sur un de mes raspberry, mais cela freezait le raspberry sur un autre.

La solution semble d'utiliser les drivers officiels disponibles depuis décembre 2013 http://www.ics.com/blog/raspberry-pi-camera-module#.U2DM0vg5o6U

Tester la raspicam

raspistill -t 5000

Gestion de la puissance
Le script power.py doit être lancer au démarrage.
Il va mettre la pin GPIO 16 à une valeur haute, pour conserver l'alimentation du raspberry.
Lorsque la batterie devient faible, ou après un timer, un signal est envoyé au raspberry sur la pin 12.
A ce moment, l'extinction logicielle du pi est lancée. Lorque le pi s'éteint, la ping GPIO 16 retombe à zéro, et l'alimentation peut-être coupée.
Le lancement du script en service pose problème.
Il faut du coup utiliser cron
crontab -e:"sudo python /home/pi/orgie/power.py"


