<!-- Name: ArchInstallation -->
<!-- Version: 1 -->
<!-- Last-Modified: 2010/10/27 19:40:25 -->
<!-- Author: ajashton -->
# Installing Mapnik on Arch Linux

## Mapnik 2 from Git

Mapnik 2 must be built from source. A package description is available in the Arch User Repository for easy building with ABS: [mapnik-git](https://aur.archlinux.org/packages.php?ID=53270) (this will compile the latest development version from the Git master branch).

If you use [Yaourt](https://wiki.archlinux.org/index.php/Yaourt) or a similar [AUR helper](https://wiki.archlinux.org/index.php/AUR_Helpers), just install the 'mapnik-git' package:

    $ yaourt -S mapnik-git

This will handle downloading, building and installing Mapnik with dependencies from the 'extra' and 'community' repositories.

## 0.7.x (Deprecated version)

Mapnik 0.7.1 is available from the Arch Community repository. Install it with Pacman:

    $ sudo pacman -S mapnik
