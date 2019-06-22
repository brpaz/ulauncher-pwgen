# Ulauncher pwgen extension

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-pwgen)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-pwgen.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-pwgen)
![License](https://img.shields.io/github/license/brpaz/ulauncher-pwgen.svg?style=for-the-badge)

> [ulauncher](https://ulauncher.io/) Extension for generating strong passwords using `pwgen` python package.


## Usage

![demo](demo.gif)

* You can specify the lenght of your password like ```pwgen 32```.

## Requirements

* [ulauncher 5](https://ulauncher.io/)
* Python >= 3
* [pwgen](https://pypi.org/project/pwgen/) package - ```pip3 install pwgen```

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-pwgen```
 

## Development

```
git clone https://github.com/brpaz/ulauncher-pwgen
cd ulauncher-pwgen
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## TODO

* Make possible to configure other parameters of the password like including or not special characters

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


## License 

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
