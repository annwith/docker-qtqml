# qtqml-docker
Docker capaz de rodar aplicações Qt/QML com interface para o usuário.

## Como utilizar o Docker com a interface
* To open the Container terminal and enable the display:

docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -a stdin -a stdout -i -t jumidlej/qtqml /bin/bash

* To test with files in examples folder:

docker run -e DISPLAY -u $(id -u $USER):$(id -g $USER) -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v your_dir/examples:/examples -a stdin -a stdout -i -t jumidlej/qtqml /bin/bash

* To fix: Error: No protocol specified QXcbConnection: Could not connect to display

docker run -e DISPLAY -u $(id -u $USER):$(id -g $USER) -v /tmp/.X11-unix:/tmp/.X11-unix:rw -a stdin -a stdout -i -t jumidlej/qtqml /bin/bash

Link: http://wiki.ros.org/docker/Tutorials/GUI

## Versões das bibliotecas
* QtQuick 2.7
* QtQuick.Window 2.2

## Instalação do Qt/QML no Raspberry
* PyQt5

sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5

sudo apt-get install qt5-default

* qmlscene

sudo apt-get update -y

sudo apt-get install -y qmlscene

sudo apt install qml-module-qtquick-dialogs

sudo apt install qml-module-qtquick-controls

sudo apt install qml-module-qtquick-layouts

sudo apt install qml-module-qtquick-window2