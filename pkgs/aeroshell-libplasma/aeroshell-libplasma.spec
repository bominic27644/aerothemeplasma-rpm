%global debug_package %{nil}

%global commit 5636741b56ba90b60f71d2505de6bc2d2e609ced
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           aeroshell-libplasma
Version:        6.6.3
Release:        1%{?dist}
Summary:        Plasma library and runtime components, with AeroShell patches

License:        LGPLv2
URL:            https://gitgud.io/aeroshell/libplasma
Source:         https://gitgud.io/aeroshell/libplasma/-/archive/%{commit}/libplasma-%{shortcommit}.tar.gz

# Build requirements for C++ components
BuildRequires:  ninja-build
BuildRequires:  kf6-rpm-macros

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
# Plasma dependenciesPlasma library and runtime components, with AeroShell patches
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

Requires:       kf6-filesystem

	
Obsoletes:      libplasma <= %{version}-%{release}
Provides:       libplasma = %{version}-%{release}
Obsoletes:      kf6-plasma < 1:%{version}-%{release}
Provides:       kf6-plasma = 1:%{version}-%{release}

%description
Plasma library and runtime components, with AeroShell patches

%prep
%autosetup -n libplasma-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install
# create/own dirs
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde/private

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
kbuildsycoca6 &> /dev/null || :

%files
%dir %{_kf6_qmldir}/org/
%dir %{_kf6_qmldir}/org/kde/
%dir %{_kf6_qmldir}/org/kde/private/
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/plasma/
%{_kf6_datadir}/qlogging-categories6/*plasma*
%{_libdir}/libPlasma.so.*
%{_libdir}/libPlasmaQuick.so.*
%{_kf6_plugindir}/kirigami/
%{_kf6_plugindir}/packagestructure
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/kirigami/styles/Plasma/AbstractApplicationHeader.qml
%dir %{_kf6_datadir}/kdevappwizard/
%{_kf6_datadir}/kdevappwizard/templates/
%{_includedir}/Plasma/
%{_includedir}/PlasmaQuick/
%{_libdir}/cmake/Plasma/
%{_libdir}/cmake/PlasmaQuick/
%{_libdir}/libPlasma.so
%{_libdir}/libPlasmaQuick.so
%{_datadir}/locale/*/LC_MESSAGES/libplasma6.mo

%changelog
%autochangelog