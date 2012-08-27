%define		_state		stable
%define		orgname		kmouth
%define		qtver		4.8.1

Summary:	K Desktop Environment - A program that speaks for you
Name:		kde4-%{orgname}
Version:	4.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	3a29f2ef9e2d792afc895256bbd7d752
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	perl
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xorg-lib-libX11-devel
Requires:	kde4-kaccessible >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program that allows people who have lost their voice to let their
computer speak for them.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_desktopdir}/kde4/kmousetool.desktop
%{_datadir}/apps/kmousetool
%{_iconsdir}/hicolor/*/actions/kmousetool_off.png
%{_iconsdir}/hicolor/*/actions/kmousetool_on.png
%{_iconsdir}/hicolor/*/apps/kmousetool.png
%{_docdir}/kde/HTML/en/kmousetool
%{_mandir}/man1/kmousetool.1*
