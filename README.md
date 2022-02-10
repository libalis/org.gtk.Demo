# README
### Requirements
- flatpak
- flatpak-builder
- git
### Build & Install
    flatpak remote-add --if-not-exists gnome-nightly https://sdk.gnome.org/gnome-nightly.flatpakrepo
    flatpak install gnome-nightly org.gnome.Platform//master org.gnome.Sdk//master
    git clone https://github.com/libalis/repo.git
    cd repo/
    flatpak-builder build org.gtk.Demo.json --install --force-clean
    rm -rf build .flatpak-builder
### Uninstall
    flatpak remove org.gtk.Demo
### Run
    flatpak run org.gtk.Demo
