%global debug_package %{nil}

%global commit d4ca559d1ff9f26dd6652df66ecc075aa14efdc2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           aerothemeplasma-desktop
Version:        0
Release:        1.git%{shortcommit}%{?dist}
Summary:        An alternative shell for KDE Plasma that aims to replicate the look and feel of Windows 7

License:        AGPLv3
URL:            https://gitgud.io/aeroshell/atp/aerothemeplasma
Source:         https://gitgud.io/aeroshell/atp/aerothemeplasma/-/archive/%{commit}/aerothemeplasma-%{shortcommit}.tar.gz

# Build requirements for C++ components
BuildRequires:  ninja-build

BuildRequires:  cmake make gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kpackage-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-ksvg-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-kiconthemes-devel 
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-kglobalaccel-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-kdeclarative-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-solid-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  gmp-ecm-devel 
BuildRequires:  kf6-knewstuff-devel 
BuildRequires:  kf6-knotifyconfig-devel 
BuildRequires:  kf6-attica-devel 
BuildRequires:  kf6-krunner-devel 
BuildRequires:  kf6-sonnet-devel 
BuildRequires:  kf6-kitemmodels-devel 
BuildRequires:  kf6-kstatusnotifieritem-devel
BuildRequires:  kf6-qqc2-desktop-style
# Plasma dependencies
BuildRequires:  plasma-workspace-devel
BuildRequires:  kwin-devel
BuildRequires:  kwin-x11-devel
BuildRequires:  kdecoration-devel
BuildRequires:  libplasma-devel 
BuildRequires:  plasma-activities-devel 
BuildRequires:  plasma-wayland-protocols 
BuildRequires:  kf5-plasma-devel
BuildRequires:  plasma5support-devel 
BuildRequires:  plasma-activities-stats-devel 
# Qt dependencies
BuildRequires:  qt-devel 
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qtdeclarative-devel 
BuildRequires:  qt6-qt5compat-devel 
BuildRequires:  qt6-qtwayland-devel
# Other dependencies
BuildRequires:  wayland-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libdrm-devel
BuildRequires:  polkit-qt6-1-devel 
BuildRequires:  curl

# Specific extras for the theme
Requires:       kvantum
Requires:       tar
Requires:       unzip
Requires:       kf6-frameworkintegration

%description
An alternative shell for KDE Plasma that aims to replicate the look and feel of Windows 7

%prep
%autosetup -n aerothemeplasma-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
kbuildsycoca6 &> /dev/null || :

%files
%{_sysconfdir}/xdg/aerothemeplasma/*
%{_sysconfdir}/xdg/autostart/x-atpootb.desktop
%{_bindir}/atpootb
%{_bindir}/startatp-wayland
%{_datadir}/plasma/desktoptheme/Seven-Black
%{_datadir}/plasma/shells/io.gitgud.wackyideas.desktop
%{_datadir}/plasma/look-and-feel/authui7
%{_datadir}/sddm/themes/sddm-theme-mod
%{_datadir}/plasma/plasmoids/io.gitgud.wackyideas.*
%{_datadir}/plasma/layout-templates
%{_datadir}/color-schemes/Aero.colors
%{_libexecdir}/kf6/kauth/ootbcursor_authhelper
%{_datadir}/Kvantum/*
%{_datadir}/aerothemeplasma/*
%{_datadir}/dbus-1/system-services/io.gitgud.wackyideas.ootb.service
%{_datadir}/dbus-1/system.d/io.gitgud.wackyideas.ootb.conf
%{_datadir}/polkit-1/actions/io.gitgud.wackyideas.ootb.policy
%{_datadir}/wayland-sessions/aerothemeplasma.desktop
# Compiled plasmoids
%{_libdir}/qt6/plugins/plasma/applets/io.gitgud.wackyideas.*.so
%{_libdir}/qt6/qml/io/gitgud/wackyideas/*


%changelog
%autochangelog