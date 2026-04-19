%global debug_package %{nil}

%global commit f9621f0d7e7bc9a52009cb714f66140ae72a4bea
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libplasma
Version:        6.6.4
Release:        51%{?dist}
Summary:        Plasma library and runtime components, with AeroShell patches

License:        LGPLv2
URL:            https://gitgud.io/aeroshell/libplasma
Source:         https://gitgud.io/aeroshell/libplasma/-/archive/%{commit}/libplasma-%{shortcommit}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
 
# Qt
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6GuiPrivate)
 
# KDE Frameworks
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6DBusAddons)
 
# Plasma
BuildRequires:  cmake(PlasmaActivities)
 
# Wayland
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  pkgconfig(wayland-client)
 
# autotests
BuildRequires:  cmake(KF6Archive)
 
# examples
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)
 
Requires:       kf6-filesystem
	
Provides:       kf6-plasma = 1:%{version}-%{release}
Obsoletes:      kf6-plasma < 1:%{version}-%{release}

%description
Plasma library and runtime components, with AeroShell patches

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Qml)
Requires:       cmake(Qt6Gui)
Requires:       cmake(KF6Package)
Requires:       cmake(KF6KirigamiPlatform)
Requires:       cmake(KF6WindowSystem)
Obsoletes:      kf6-plasma-devel < 1:%{version}-%{release}
Provides:       kf6-plasma-devel = 1:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n libplasma-%{commit}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-man --all-name

# create/own dirs
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde/private

%files -f %{name}.lang
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
 
%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%{_kf6_datadir}/kdevappwizard/templates/
%{_includedir}/Plasma/
%{_includedir}/PlasmaQuick/
%{_libdir}/cmake/Plasma/
%{_libdir}/cmake/PlasmaQuick/
%{_libdir}/libPlasma.so
%{_libdir}/libPlasmaQuick.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
%autochangelog