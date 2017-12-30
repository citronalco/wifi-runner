wifi-runner
===========

Run scripts when wifi connection (guided by connman) state is changed. 

The Connman connection manager on Sailfish unfortunately doesn't provide the ability
to run scripts after the wifi connection was established.

The purpose of this project is in adding this feature.
Here we have simple daemon that listening to connman's dbus interface.

Install
===========
Developer mode must be enabled on the phone to install the prerequisites.
Log in on the phone with ssh and become root by typing "devel-su".

Then install the required python modules:

``$ pkcon install dbus-python3``
``$ pkcon install python3-gobject``

MechanicalSoup is a handy module that makes scripting websites very easy. It is only required for the included WIFIonICE autologon script:
``$ pip3 install -Iv https://github.com/MechanicalSoup/MechanicalSoup/archive/v0.7.0.zip``


As normal user copy content of this repository's systemd folder including all subdirectories to ~/.config/systemd
and enable the service:

``$ systemctl --user enable wifi-runner.service``

After reboot this daemon will start automatically.

Configure
===========
There is a config file systemd/scripts/wifi-runner.conf .
It's name and path are hardcoded in wifi-runner.py so
after installation it's worth to check it is correct.

Each section name corresponds to SSID of the network.
Default section corresponds to scripts that runned for all wifi networks.
It's name consists of 42 charactes so it won't correspond to any correct SSID (the limit is 32).

For example if we want to start script ./test.py
when wifi with SSID 'TEST' stops and start.sh when it starts
we can just add in the end of the file

[TEST]

start = start.sh

stop  = test.py


Paths to scripts can be relative to config file or the absolute ones.

Script and configuration that auto authorize you in Moscow Metro Free Wifi and Deutsche Bahn's WIFIonICE are included.

