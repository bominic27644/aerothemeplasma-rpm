%global debug_package %{nil}

%global commit 55d2f5fd15f53cccbbb13388941b930442db1159
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           aerothemeplasma-sounds
Version:        0
Release:        %autorelease
Summary:        Collection of sound themes designed for AeroThemePlasma

License:        AGPLv3
URL:            https://gitgud.io/aeroshell/atp/aerothemeplasma-sounds
Source:         https://gitgud.io/aeroshell/atp/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.zip

BuildRequires:  cmake make gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  git

%description
Collection of sound themes designed for AeroThemePlasma

%prep
%autosetup -n %{name}-%{commit}
rm LICENSE
rm README.md

%build
%cmake

%install
%cmake_install

%files
%{_datadir}/sounds/*

%changelog
%autochangelog