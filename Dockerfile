FROM navikey/raspbian-buster

USER root

RUN apt-get purge -y libreoffice*
RUN apt-get clean
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get autoremove -y

# PyQt5
RUN apt-get install -y \ 
    libqtgui4 \
    libqtwebkit4 \
    libqt4-test \
    python3-pyqt5

# qmlscene
RUN apt-get install -y \
    qmlscene \
    qml-module-qtquick-dialogs \
    qml-module-qtquick-controls \
    qml-module-qtquick-layouts \
    qml-module-qtquick-window2

RUN apt-get install -y qt5-default
RUN apt-get install -y qtcreator
RUN apt-get install -y qtdeclarative5-* \
    qml-module-qtquick* \
    qtquickcontrols5-* \
    qml-module-qtquick2