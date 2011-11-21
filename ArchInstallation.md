<!-- Name: ArchInstallation -->
<!-- Version: 1 -->
<!-- Last-Modified: 2010/10/27 19:40:25 -->
<!-- Author: ajashton -->
# Installing Mapnik on Arch Linux

## Stable version

The stable release of Mapnik (and all of its dependencies, of course) are available from the Arch Community repository. Install it with Pacman:


    $ sudo pacman -S mapnik

## Mapnik Trunk (aka Mapnik2)

Installing Mapnik2 will require building a couple packages from source. It is highly recommended you do this using the Arch Build System. If you are unfamiliar with this process read more about it on the Arch Wiki: https://wiki.archlinux.org/index.php/Arch_Build_System . With the ABS and tools like Yaourt, building custom packages for Arch is usually an easy process.

### Installation from AUR with Yaourt

If you use Yaourt (or perhaps a similar AUR frontend) installation is greatly simplified. Just install the 'mapnik2-svn' package and Yaourt will handle building and installing Mapnik and its dependencies:


    $ yaourt -S mapnik2-svn

This will build a custom version of Boost against ICU, and pull any other uninstalled dependencies from the Arch 'extra' and 'community' repositories. More info about Yaourt can be found here: https://wiki.archlinux.org/index.php/Yaourt

### Manual ABS installation

Details coming soon. For now look at these packages in the AUR:

 * boost-icu: https://aur.archlinux.org/packages.php?ID=42259
 * mapnik2-svn: https://aur.archlinux.org/packages.php?ID=42260
