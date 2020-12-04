%define major 18
%define girmajor 1.0
%define libname %mklibname totem-plparser %{major}
%define libmini %mklibname totem-plparser-mini %{major}
%define girname %mklibname totem-plparser-gir %{girmajor}
%define develname %mklibname -d totem-plparser

Summary:	Playlist parser library from the Totem Movie Player
Name:		totem-pl-parser
Version:	3.26.5
Release:	3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.hadess.net/totem.php3
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem-pl-parser/3.10/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(gmime-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libquvi-0.9)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	meson

%description
Shared library used by totem.

%package i18n
Summary:	Playlist parser library from the Totem Movie Player
Group:		System/Internationalization

%description i18n
This package contains the translations for %{name}.

%package -n %{libname}
Summary:	Playlist parser library from the Totem Movie Player
Group:		System/Libraries
Suggests:	%{name}-i18n >= %{version}-%{release}

%description -n %{libname}
Shared library used by totem.

%package -n %{libmini}
Summary:	Playlist parser library from the Totem Movie Player
Group:		System/Libraries

%description -n %{libmini}
Shared library used by totem - minimal version.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{develname}
Summary:	Development libraries, include files for totem playlist parser
Group:		Development/GNOME and GTK+
Provides:	totem-plparser-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libmini} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Conflicts: 	%{_lib}totem-plparser0-devel
Obsoletes:	%{mklibname -d totem-plparser 7} < 3.4.2

%description -n	%{develname}
Development libraries, include files for totem playlist parser

%prep
%autosetup -p1

%build
%meson \
	-Denable-gtk-doc=true
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%{_libexecdir}/totem-pl-parser/99-totem-pl-parser-videosite-quvi

%files i18n -f %{name}.lang
%doc README NEWS

%files -n %{libname}
%{_libdir}/libtotem-plparser.so.%{major}*

%files -n %{libmini}
%{_libdir}/libtotem-plparser-mini.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/TotemPlParser-%{girmajor}.typelib

%files -n %{develname}
%doc NEWS AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/TotemPlParser-%{girmajor}.gir
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}
