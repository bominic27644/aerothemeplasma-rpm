%global debug_package %{nil}

%global commit b8d5ce100251b74a3a3c5b4a474cb3ff8df11bba
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           aerothemeplasma-icons
Version:        6.6.4
Release:        1.git%{shortcommit}%{?dist}
Summary:        Icon theme designed for AeroThemePlasma

License:        AGPLv3
URL:            https://gitgud.io/aeroshell/atp/aerothemeplasma-icons
Source:         https://gitgud.io/aeroshell/atp/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.zip

BuildRequires:  cmake make gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  git

%description
Icon theme designed for AeroThemePlasma

%prep
%autosetup -n %{name}-%{commit}
rm LICENSE
rm README.md

%build
%cmake

%install
%cmake_install


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
kbuildsycoca6 &> /dev/null || :

%files
%{_datadir}/icons/*

%changelog
%autochangelog