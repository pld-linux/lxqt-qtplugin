#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	lxqt-qtplugin
Name:		lxqt-qtplugin
Version:	0.7.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	dfb5d4030be3c00fde327969657fb12b
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.7.0
BuildRequires:	libqtxdg-devel >= 0.5.3
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-qtplugin.

%prep
%setup -q -c %{name}-%{version}

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
%dir %{_libdir}/qt4/plugins/gui_platform
%attr(755,root,root) %{_libdir}/qt4/plugins/gui_platform/libqtlxqt.so
