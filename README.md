# Warden

A tool to watch file creations in honeypot docker

[![alert(/xss/)](https://img.shields.io/badge/warden-arc-yellow.svg)]()

## Requirements

```
sudo apt-get install python-pip
sudo pip install watchdog
```

## Config

* watch: the paths to watch
* backup: copy the new file to backup path

## Usage

```
$ sudo python warden.py -h
Usage: warden.py [-c conifgfile]

Options:
  -h, --help            show this help message and exit
  -c FILE, --config=FILE
                        config file to load
```
