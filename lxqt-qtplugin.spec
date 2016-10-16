#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-qtplugin
Name:		lxqt-qtplugin
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d75b3566581dccea9d55de731c49d844
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libdbusmenu-qt5-devel
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-qtplugin.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/platformthemes
%attr(755,root,root) %{_libdir}/qt5/plugins/platformthemes/libqtlxqt.so
