# Songlist-Converter

## Summary

This is a tool that converts the songlist of QQ music to Netease Music. The repo is based on [xMusicWeb](https://github.com/comwrg/xMusicWeb). It has some bugs and stops maintaining. I fix  the bugs and add instruction on how to run the code in this repo. 

## Environment

* Ubuntu
* python2

## Usage

### Init

First, clone the repo and install necessary packages.

```bash
https://github.com/crh19970307/Songlist-Converter.git
cd Songlist-Converter
./init.sh
```

### Start the server

Replace the host ip in `run.sh` to your ip address. Note that the ip address is your Intranet IP if you are using NAT. You can view it in `ifconfig`. Choose the port and do port mapping.

Then run the code to start server.

```
./run.sh
```

### Visit the Website

Now you can visit the website through host:port.


### Export the QQ Music Songlist

Open [QQ music website](http://music.qq.com), and enter the sonlist that you want to convert. Copy the url, e.g. `https://y.qq.com/n/yqq/playlist/3363492195.html` and paste it in website. Then you will get a kwl file. Download it. Note that the songlist of QQ should be public, or you can not get the kwl file.

### Import the Songlist

Download an old version of Netease Music because the newest version does not support import songlist. Then import the kwl file which is the format of Kuwo Music. Then just wait.

### Compare Differences

Some music can not be found in Netease Music so you can compare differences in the website. Paste the url of QQ music and Netease Music and the website will show the differences. You can add the song in hand.

---

If you have questions, just create an issue.