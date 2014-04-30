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




