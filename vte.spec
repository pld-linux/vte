#
# Conditional build:
%bcond_without	glade	# Glade catalog

Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.46.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.46/%{name}-%{version}.tar.xz
# Source0-md5:	e8f4393b9f1ec2e2f3cdb3fd4f5a16de
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
%{?with_glade:BuildRequires:	glade-devel >= 3}
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnutls-devel >= 3.2.7
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.8.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	gtk-doc-automake >= 1.13
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-progs >= 2
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pcre2-8-devel >= 10.21
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
# for test application
#BuildRequires:	vala >= 2:0.18
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	glib2 >= 1:2.40.0
Requires:	gnutls >= 3.2.7
Requires:	gtk+3 >= 3.8.0
Requires:	pango >= 1:1.22.0
Obsoletes:	vte-common < 0.42.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+ 3.x. It's used by
gnome-terminal among other programs.

%description -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 3.x. Jest używany
przez gnome-terminal oraz inne programy.

%package common
Summary:	Common files for vte and vte0
Summary(pl.UTF-8):	Pliki wspólne dla vte i vte0
Group:		X11/Libraries
Requires(pre):	utempter

%description common
Common files for GTK+ 3 based vte and GTK+ 2 based vte0.

%description common -l pl.UTF-8
Pliki wspólne dla vte opartego na GTK+ 3 oraz vte0 opartego na GTK+ 2.

%package devel
Summary:	Header files for VTE for GTK+ 3
Summary(pl.UTF-8):	Pliki nagłówkowe VTE dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gnutls-devel >= 3.2.7
Requires:	gtk+3-devel >= 3.8.0
Requires:	ncurses-devel
Requires:	pango-devel >= 1:1.22.0
Requires:	pcre2-8-devel >= 10.21
Requires:	zlib-devel
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
This package contains header files for GTK+ 3 based vte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK+ 3.

%package static
Summary:	Static VTE library for GTK+ 3
Summary(pl.UTF-8):	Statyczna biblioteka VTE dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of VTE library for GTK+ 3.

%description static -l pl.UTF-8
Statyczna wersja biblioteki VTE dla GTK+ 3.

%package glade
Summary:	VTE catalog file for Glade
Summary(pl.UTF-8):	Plik katalogu VTE dla Glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glade >= 3

%description glade
VTE catalog file for Glade.

%description glade -l pl.UTF-8
Plik katalogu VTE dla Glade.

%package -n vala-vte
Summary:	Vala API for VTE library
Summary(pl.UTF-8):	API języka Vala dla biblioteki VTE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-vte
Vala API for VTE library.

%description -n vala-vte -l pl.UTF-8
API języka Vala dla biblioteki VTE.

%package apidocs
Summary:	VTE API documentation (GTK+ 3 version)
Summary(pl.UTF-8):	Dokumentacja API VTE (wersja dla GTK+ 3)
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
VTE API documentation (GTK+ 3 version).

%description apidocs -l pl.UTF-8
Dokumentacja API VTE (wersja dla GTK+ 3).

%prep
%setup -q

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	%{?with_glade:--enable-glade-catalogue} \
	--enable-gtk-doc \
	--enable-introspection \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}-2.91

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte-2.91.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/vte-2.91
%attr(755,root,root) %{_libdir}/libvte-2.91.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte-2.91.so.0
%{_libdir}/girepository-1.0/Vte-2.91.typelib
%config(noreplace) %verify(not md5 mtime size) /etc/profile.d/vte.sh

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte-2.91.so
%{_includedir}/vte-2.91
%{_pkgconfigdir}/vte-2.91.pc
%{_datadir}/gir-1.0/Vte-2.91.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libvte-2.91.a

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%{_datadir}/glade/catalogs/vte-2.91.xml
%{_datadir}/glade/pixmaps/hicolor/16x16/actions/widget-vte-terminal.png
%{_datadir}/glade/pixmaps/hicolor/22x22/actions/widget-vte-terminal.png
%endif

%files -n vala-vte
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/vte-2.91.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.91
