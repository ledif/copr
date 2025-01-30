%global srcname Openterface_QT

Name:           openterface-qt
Version:        0.0.6
Release:        %autorelease
Summary:        Openterface Mini-KVM host application

License:        AGPL-3.0-only
URL:            https://github.com/TechxArtisanStudio/Openterface_QT
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qtsvg-devel

%description
This is the host application to control an Openterface Mini-KVM.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%qmake_qt6
%make_build

%install
%make_install
install -Dpm0755 -t %{buildroot}%{_bindir} build/install/openterfaceQT

%files
%license LICENSE
%doc README.md
%{_bindir}/openterfaceQT

%changelog
%autochangelog
