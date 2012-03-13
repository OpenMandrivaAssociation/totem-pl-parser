%define major 17
%define gir_major 1.0
%define libname %mklibname totem-plparser %{major}
%define libmini %mklibname totem-plparser-mini %{major}
%define girname %mklibname totem-plparser-gir %{gir_major}
%define develname %mklibname -d totem-plparser

Summary: Playlist parser library from the Totem Movie Player
Name: totem-pl-parser
Version: 3.2.0
Release: 1
License: LGPLv2+
Group: System/Libraries
URL: http://www.hadess.net/totem.php3
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: pkgconfig(gmime-2.6)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libquvi)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)

%description
Shared library used by totem.

%package i18n
Summary: Playlist parser library from the Totem Movie Player
Group: System/Internationalization

%description i18n
This package contains the translations for %{name}.

%package -n %{libname}
Summary: Playlist parser library from the Totem Movie Player
Group: System/Libraries
Suggests: %{name}-i18n >= %{version}-%{release}

%description -n %{libname}
Shared library used by totem.

%package -n %{libmini}
Summary: Playlist parser library from the Totem Movie Player
Group: System/Libraries

%description -n %{libmini}
Shared library used by totem - minimal version.

%package -n %{girname}
Summary:    GObject Introspection interface description for %{name}
Group:      System/Libraries
Requires:   %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{develname}
Summary:	Development libraries, include files for totem playlist parser
Group:		Development/GNOME and GTK+
Provides:	totem-plparser-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libmini} = %{version}-%{release}
Conflicts: 	%{_lib}totem-plparser0-devel
Obsoletes:	%mklibname -d totem-plparser 7

%description -n	%{develname}
Development libraries, include files for totem playlist parser

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make LIBS='-lgcrypt -lgmodule-2.0'

%install
rm -rf %{buildroot} %{name}.lang
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}

%files i18n -f %{name}.lang
%doc README NEWS 

%files -n %{libname}
%{_libdir}/libtotem-plparser.so.%{major}*

%files -n %{libmini}
%{_libdir}/libtotem-plparser-mini.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/TotemPlParser-%{gir_major}.typelib

%files -n %{develname}
%doc ChangeLog AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/TotemPlParser-%{gir_major}.gir
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}

