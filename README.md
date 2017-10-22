# Echolink and WSPR node based on a Raspberry PI

### Requirements
- Raspberry PI (model doesn't matter)
- Raspbian 9 installed and working
- Internet access setup and working

### Required setup and software
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install g++ make libsigc++-1.2-dev libgsm1-dev libpopt-dev tcl8.5-dev libgcrypt-dev libspeex-dev libasound2-dev alsa-utils libqt4-dev
sudo apt-get install libsigc++ cmake groff 
```

### Echolink (Thru SVXLink)
```
sudo adduser svxlink
wget https://github.com/sm0svx/svxlink/archive/master.tar.gz
tar xvzf master.tar.gz
cd svxlink-master/src
mkdir build && cd build
sudo cmake -DCMAKE_INSTALL_PREFIX=/usr -DSYSCONF_INSTALL_DIR=/etc       -DLOCAL_STATE_DIR=/var -DUSE_QT=NO ..
make
make doc
sudo make install
sudo ldconfig
```
- Copy the etc/svxlink folder to your /etc/svxlink foder.
```
sudo cp -r etc/svxlink/* /etc/svxlink/
```
- Edit callsign and password (from Echolink Link/Repeater setup).
- Edit description.
- Check GPIO ports for Squelch and PTT.

### GPIO Setup
- Copy the etc/rc.local file to your /etc/rc.local
```
sudo cp etc/rc.local /etc/rc.local
```
- Check and match GPIO ports for Squelch and PTT.

### Software reset
- There is a Python script that handles Raspberry PI reboots from a hardware switch without killing power.
- Check the /etc/rc.local file and match the desired GPIO port for this task.
- Copy lib/systemd/system/reset.service to /lib/systemd/system/reset.service
```
sudo cp lib/systemd/system/reset.service to /lib/systemd/system/reset.service
chmod 644 /lib/systemd/system/reset.service
systemctl enable reset.service
systemctl start reset.service
```

### WSPR
```
git clone https://github.com/JamesP6000/WsprryPi.git
cd WsprryPi/
make
sudo make install
sudo wspr --test-tone 780e3
```
- Check if you hear the continuous test tone on 780Hz.
- Add to your .bashrc file: alias wspr='sudo wspr -r your-callsign your-grid-locator 10 20m' 
```
echo "alias wspr='sudo wspr -r your-callsign your-grid-locator 10 20m'" >> .bashrc
```
