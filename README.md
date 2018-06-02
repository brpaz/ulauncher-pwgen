# Ulauncher pwgen extension

> [ulauncher](https://ulauncher.io/) Extension for generating strong passwords using `pwgen` python package.

## Usage

![demo](demo.gif)

* You can specify the lenght of your password like ```pwgen 32```.

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7
* [pwgen](https://pypi.org/project/pwgen/) package - ```pip install pwgen```

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-pwgen```
 

## Development

```
git clone https://github.com/brpaz/ulauncher-pwgen
cd ~/.cache/ulauncher_cache/extensions/ulauncher-pwgen
ln -s <repo_location> ulauncher-pwgen
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## TODO

* Make possible to configure other parameters of the password like including or not special characters

## License 

MIT
