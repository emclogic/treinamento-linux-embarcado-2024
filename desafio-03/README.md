# Raspberry PI Zero 2W - Yocto Build

## TL-DR

Just run the commands bellow step by step:

```bash
$ mkdir -p ~/src/embarcados-desafio03
$ cd ~/src/embarcados-desafio03
$ git clone -b scarthgap git://git.yoctoproject.org/poky
$ git clone -b scarthgap git://git.openembedded.org/meta-openembedded
$ git clone -b scarthgap git://git.yoctoproject.org/meta-raspberrypi
$ cd poky
$ source oe-init-build-env build-desafio03
$ bitbake-layers add-layer ~/src/embarcados-desafio03/meta-raspberrypi
$ bitbake-layers add-layer ~/src/embarcados-desafio03/meta-openembedded/meta-oe
$ MACHINE=raspberrypi0-2w-64 bitbake core-image-full-cmdline --runall=fetch
$ MACHINE=raspberrypi0-2w-64 bitbake core-image-full-cmdline
```

## Playbook

Disponibilizei um playbook ansible que faz a preparacao do ambiente, exceto a adicao dos layers e compilacao do target.

```bash
ansible-playbook playbook-desafio03.yaml
```
