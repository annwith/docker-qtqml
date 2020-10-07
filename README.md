# qtqml-docker
Docker capaz de rodar aplicações Qt/QML com interface para o usuário.

## Como utilizar o Docker com a interface
* To run the Container: 

docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY image

* To open the container terminal:

docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -a stdin -a stdout -i -t jumidlej/qtqml /bin/bash

* To fix Error: No protocol specified QXcbConnection: Could not connect to display

xhost +local:docker

## Instalação do Qt/QML no Raspberry
* Pacotes necessários

sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5

* PySide2

sudo apt-get install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qt python3-pyside2.qttools python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns python3-pyside2uic

* qmlscene

sudo apt-get update -y

sudo apt-get install -y qmlscene

sudo apt install qml-module-qtquick-dialogs

sudo apt install qml-module-qtquick-controls

sudo apt install qml-module-qtquick-layouts

sudo apt install qml-module-qtquick-window2


