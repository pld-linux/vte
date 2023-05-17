#
# Conditional build:
%bcond_without	apidocs	# API documentation
%bcond_without	glade	# Glade catalog
%bcond_without	gtk4	# GTK+ 4 based library

Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.72.1
Release:	2
# some files have LGPL v2.1+ signature, but some LGPL v3+
License:	LGPL v3+ (library), GPL v3+ (app)
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/vte/0.72/%{name}-%{version}.tar.xz
# Source0-md5:	56f66f6049aab6a35eee20174d961e80
Patch0:		%{name}-wordsep.patch
URL:		https://wiki.gnome.org/Apps/Terminal/VTE
BuildRequires:	cairo-gobject-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fribidi-devel >= 1.0.0
# C11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.52.0
BuildRequires:	gnutls-devel >= 3.2.7
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gperf
BuildRequires:	gtk+3-devel >= 3.24.0
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0.1}
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libicu-devel >= 4.8
# C++20 support (-std=gnu++2a, char8_t)
BuildRequires:	libstdc++-devel >= 6:9.0
BuildRequires:	libxml2-progs >= 2
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pcre2-8-devel >= 10.21
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	systemd-devel >= 1:220
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	fribidi >= 1.0.0
Requires:	glib2 >= 1:2.52.0
Requires:	gnutls >= 3.2.7
Requires:	gtk+3 >= 3.24.0
Requires:	libicu >= 4.8
Requires:	pango >= 1:1.22.0
Requires:	systemd-libs >= 1:220
Obsoletes:	vte-common < 0.42.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The vte package contains a terminal widget for GTK+ 3.x. It's used by
gnome-terminal among other programs.

%description -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK+ 3.x. Jest używany
przez gnome-terminal oraz inne programy.

%package devel
Summary:	Header files for VTE for GTK+ 3
Summary(pl.UTF-8):	Pliki nagłówkowe VTE dla GTK+ 3
License:	LGPL v3+
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.52.0
Requires:	gtk+3-devel >= 3.24.0
Requires:	pango-devel >= 1:1.22.0
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
This package contains header files for GTK+ 3 based vte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK+ 3.

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
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.24
BuildArch:	noarch

%description -n vala-vte
Vala API for VTE library.

%description -n vala-vte -l pl.UTF-8
API języka Vala dla biblioteki VTE.

%package apidocs
Summary:	VTE API documentation (GTK+ 3 version)
Summary(pl.UTF-8):	Dokumentacja API VTE (wersja dla GTK+ 3)
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
VTE API documentation (GTK+ 3 version).

%description apidocs -l pl.UTF-8
Dokumentacja API VTE (wersja dla GTK+ 3).

%package gtk4
Summary:	VTE terminal widget library (GTK 4 version)
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE (wersja dla GTK 4)
Group:		Libraries
Requires:	fribidi >= 1.0.0
Requires:	glib2 >= 1:2.52.0
Requires:	gnutls >= 3.2.7
Requires:	gtk4 >= 4.0.1
Requires:	libicu >= 4.8
Requires:	pango >= 1:1.22.0
Requires:	systemd-libs >= 1:220
# for common files
Suggests:	%{name} = %{version}-%{release}

%description gtk4
The vte package contains a terminal widget for GTK 4.x. It's used by
gnome-terminal among other programs.

%description gtk4 -l pl.UTF-8
Ten pakiet zawiera kontrolkę terminala dla GTK 4. Jest używany przez
gnome-terminal oraz inne programy.

%package gtk4-devel
Summary:	Header files for VTE for GTK 4
Summary(pl.UTF-8):	Pliki nagłówkowe VTE dla GTK 4
License:	LGPL v3+
Group:		X11/Development/Libraries
Requires:	%{name}-gtk4 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.52.0
Requires:	gtk4-devel >= 4.0.1
Requires:	pango-devel >= 1:1.22.0

%description gtk4-devel
This package contains header files for GTK 4 based vte library.

%description gtk4-devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK 4.

%package -n vala-vte-gtk4
Summary:	Vala API for VTE library (GTK 4 version)
Summary(pl.UTF-8):	API języka Vala dla biblioteki VTE (wersja dla GTK 4)
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}
Requires:	vala >= 2:0.24
BuildArch:	noarch

%description -n vala-vte-gtk4
Vala API for VTE library (GTK 4 version).

%description -n vala-vte-gtk4 -l pl.UTF-8
API języka Vala dla biblioteki VTE (wersja dla GTK 4).

%package gtk4-apidocs
Summary:	VTE API documentation (GTK 4 version)
Summary(pl.UTF-8):	Dokumentacja API VTE (wersja dla GTK 4)
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description gtk4-apidocs
VTE API documentation (GTK 4 version).

%description gtk4-apidocs -l pl.UTF-8
Dokumentacja API VTE (wersja dla GTK 4).

%prep
%setup -q
%patch0 -p1

# it seems 9.0 with -std=gnu++2a is sufficient for 0.68.x (-std=gnu++20 option was added in 10.0)
%{__sed} -i -e '/cxx_req_std/ s/gnu++20/gnu++2a/; /gxx_req_version/ s/10\.0/9.0/' meson.build
# ...except for single test, which wants consteval and constinit
%{__sed} -i -e 's/consteval //;s/constinit //' src/pastify-test.cc

%build
%meson build \
	%{?with_apidocs:-Ddocs=true} \
	%{!?with_glade:-Dglade=false} \
	-Dgtk3=true \
	-Dgtk4=%{__true_false gtk4}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with apidocs}
# FIXME: where to package gi-docgen generated docs?
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/vte-2.91* $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%find_lang %{name}-2.91

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk4 -p /sbin/ldconfig
%postun	gtk4 -p /sbin/ldconfig

%files -f vte-2.91.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/vte-2.91
# gtk-version neutral, move to common?
%attr(755,root,root) %{_libexecdir}/vte-urlencode-cwd
%attr(755,root,root) %{_libdir}/libvte-2.91.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvte-2.91.so.0
%{_libdir}/girepository-1.0/Vte-2.91.typelib
%config(noreplace) %verify(not md5 mtime size) /etc/profile.d/vte.csh
%config(noreplace) %verify(not md5 mtime size) /etc/profile.d/vte.sh
%dir %{systemduserunitdir}/vte-spawn-.scope.d
%{systemduserunitdir}/vte-spawn-.scope.d/defaults.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte-2.91.so
%{_includedir}/vte-2.91
%{_pkgconfigdir}/vte-2.91.pc
%{_datadir}/gir-1.0/Vte-2.91.gir

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%{_datadir}/glade/catalogs/vte-2.91.xml
%{_datadir}/glade/pixmaps/hicolor/*x*/actions/widget-vte-terminal.png
%endif

%files -n vala-vte
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/vte-2.91.deps
%{_datadir}/vala/vapi/vte-2.91.vapi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.91
%endif

%if %{with gtk4}
%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vte-2.91-gtk4
%attr(755,root,root) %{_libdir}/libvte-2.91-gtk4.so.0
%{_libdir}/girepository-1.0/Vte-3.91.typelib

%files gtk4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvte-2.91-gtk4.so
%{_includedir}/vte-2.91-gtk4
%{_pkgconfigdir}/vte-2.91-gtk4.pc
%{_datadir}/gir-1.0/Vte-3.91.gir

%files -n vala-vte-gtk4
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/vte-2.91-gtk4.deps
%{_datadir}/vala/vapi/vte-2.91-gtk4.vapi

%if %{with apidocs}
%files gtk4-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.91-gtk4
%endif
%endif
