# nextcloud-create-drop-dir

This repo contains a python script used to create an anonymous drop-dir at given nextcloud instance and return the link for sharing.

## Usage

```
$ python nextcloud-create-drop-dir.py -h
usage: nextcloud-create-drop-dir.py [-h] [-s SERVER] -u USER -p PASSWORD -n
                                    NAME [-d DIR]

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        Server instance
  -u USER, --user USER  Username
  -p PASSWORD, --password PASSWORD
                        Password
  -n NAME, --name NAME  Name of the directory
  -d DIR, --dir DIR     Path where to create a shared directory

```

## Examples

```
$ python nextcloud-create-drop-dir.py -u **** -p **** -n 'žluťoučký kůň pěl ďábelské ódy'
ZLUTOUCKY_KUN_PEL_DABELSKE_ODY : https://nextcloud.example.com/s/cMDoOkS2fO5EGRh

```
