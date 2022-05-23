# Docker 101
## Docker 101 Crash Course - companion repository

## Introduction

This repository contains a `Vagrantfile` that will spin up a `Ubuntu 20.04` virtual machine, upload the `docker101-apps` folder containing files utilized in the course and install `Docker` and other required packages.

## Requirements

You'll need [Vagrant](https://www.vagrantup.com/) with the [vagrant-vmware-desktop plugin](https://www.vagrantup.com/docs/providers/vmware/installation) if using vmware fusion, for [vmware fusion](https://www.vmware.com/go/getfusion) you will need to register to get a [free personal license from vmware](https://www.vmware.com/go/getfusionplayer). If you are running Linux use [virtualbox](https://www.virtualbox.org/wiki/Linux_Downloads).

## Directory Structure

```
docker101
├── LICENSE
├── README.md
├── Vagrantfile
├── docker101-apps
│   ├── example-voting-app
│   └── flask-app
├── docker_install.sh
└── gifs
```

## Use

1) Clone this repository to your local machine
  - `git clone https://github.com/jisorondo/docker101.git`
2) Change into the project directory
  - `cd docker101`
3) `vagrant up --provider $PROVIDER` for OSX use `vmware_desktop` and for Linux `virtualbox`
4) Once the vm has finished deploying connect to it via `ssh` with `vagrant ssh`
