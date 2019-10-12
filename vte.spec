#
# Conditional build:
%bcond_with	gtk4	# GTK+ 4 based library [doesn't build with 3.90]

Summary:	VTE terminal widget library
Summary(pl.UTF-8):	Biblioteka z kontrolką terminala VTE
Name:		vte
Version:	0.58.2
Release:	1
# some files have LGPL v2.1+ signature, but some LGPL v3+
License:	LGPL v3+ (library), GPL v3+ (app)
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vte/0.58/%{name}-%{version}.tar.xz
# Source0-md5:	dadbf2c1d9864d3ea185738f97ab63af
Patch0:		%{name}-wordsep.patch
BuildRequires:	cairo-gobject-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fribidi-devel >= 1.0.0
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnutls-devel >= 3.2.7
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gperf
BuildRequires:	gtk+3-devel >= 3.8.0
%{?with_gtk4:BuildRequires:	gtk+4-devel >= 4.0.0}
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	intltool >= 0.40.0
# C++17 support (-std=gnu++17, with constexpr lambdas support)
BuildRequires:	libstdc++-devel >= 6:7.0
BuildRequires:	libxml2-progs >= 2
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pcre2-8-devel >= 10.21
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	fribidi >= 1.0.0
Requires:	glib2 >= 1:2.40.0
Requires:	gnutls >= 3.2.7
Requires:	gtk+3 >= 3.8.0
Requires:	pango >= 1:1.22.0
Obsoletes:	vte-common < 0.42.0
Obsoletes:	vte-glade < 0.58.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.8.0
Requires:	pango-devel >= 1:1.22.0
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
This package contains header files for GTK+ 3 based vte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
biblioteki vte opartej na GTK+ 3.

%package -n vala-vte
Summary:	Vala API for VTE library
Summary(pl.UTF-8):	API języka Vala dla biblioteki VTE
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.24
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
%patch0 -p1

%build
%meson build \
	-Ddocs=true \
	-Dgtk3=true \
	-Dgtk4=%{__true_false gtk4}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}-2.91

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f vte-2.91.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
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

%files -n vala-vte
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/vte-2.91.deps
%{_datadir}/vala/vapi/vte-2.91.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/vte-2.91
