# nfccli

Read and write nfc tags through the command line interface
`nfccli` works with the ACR1252U-A1 writer reader and NTAG215 nfc tags.
This program uses pyscard, which is only python 2 compatible.

## Dependencies

Assuming you run an archlinux, install `pcsc-tools` and start `pcscd.service`:

``` shell
$ sudo pacman -S pcsc-tools
$ sudo systemctl start pcscd.service
```

Use `yaourt` to install the acsccid driver:
``` shell
$ yaourt -S acsccid
```

## Installation and usage

1. Create a Python environment and activate it
   ``` shell
   $ virtualenv -p python2 .
   $ source nfccli/bin/activate
   ```
2. Install nfccli into the newly created environment:
   ``` shell
   $ (nfccli) pip install "git+https://github.com/escodebar/nfccli#egg=nfccli"
   ```
3. Use nfccli:
   ``` shell
   $ (nfccli) nfccli --help
   Usage:
      nfccli read [--continuous]
      nfccli write --string=<string>
      nfccli -h | --help
      nfccli --version

   Options:
      -h --help  Displays this message
      --version  Displays the version number
   ```


## Development environment

1. Clone the repository
   ``` shell
   $ git clone https://github.com/escodebar/nfccli.git
   $ cd nfccli
   ```
2. Create a Python environment and activate it
   ``` shell
   $ virtualenv -p python2 .
   $ source nfccli/bin/activate
   ```
3. Install the development environment:
   ``` shell
   $ (nfccli) pip install -e '.[dev]'
   ```
