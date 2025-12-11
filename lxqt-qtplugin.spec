#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Qt plugin framework for LXQt Desktop Suite
Summary(pl.UTF-8):	Struktura wtyczek Qt dla pakietu LXQt Desktop Suite
Name:		lxqt-qtplugin
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-qtplugin/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	aa2106968922a96b4205c80f6cbbc542
URL:		http://www.lxqt.org/
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	libdbusmenu-lxqt-devel >= 0.3.0
BuildRequires:	libfm-qt-devel >= 2.3.0
BuildRequires:	libqtxdg-devel >= 4.3.0
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt plugin framework for LXQt Desktop Suite.

%description -l pl.UTF-8
Struktura wtyczek Qt dla pakietu LXQt Desktop Suite.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt6/plugins/platformthemes
%{_libdir}/qt6/plugins/platformthemes/libqtlxqt.so
