%define major 17
%define minimajor 17
%define libname %mklibname totem-plparser %major
%define libnamedev %mklibname -d totem-plparser
%define minilibname %mklibname totem-plparser-mini %minimajor

Summary: Playlist parser library from the Totem Movie Player
Name: totem-pl-parser
Version: 2.32.6
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
License: LGPLv2+
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://www.hadess.net/totem.php3
BuildRequires: gmime-devel
BuildRequires: libxml2-devel
BuildRequires: libsoup-devel
BuildRequires: gobject-introspection-devel >= 0.9.5
BuildRequires: intltool
BuildRequires: gtk-doc gnome-common

%description
Shared library used by totem.

%package i18n
Summary: Playlist parser library from the Totem Movie Player
Group: System/Internationalization

%description i18n
This package contains the translations for %name.

%package -n %libname
Summary: Playlist parser library from the Totem Movie Player
Group: System/Libraries
Requires: %name-i18n >= %version

%description -n %libname
Shared library used by totem.

%package -n %minilibname
Summary: Playlist parser library from the Totem Movie Player
Group: System/Libraries

%description -n %minilibname
Shared library used by totem - minimal version.

%package -n	%{libnamedev}
Summary:	Static libraries, include files for totem playlist parser
Group:		Development/GNOME and GTK+
Provides:	totem-plparser-devel = %{version}
Provides:	libtotem-plparser-devel = %{version}
Requires:	%{libname} = %{version}
Requires:	%{minilibname} = %{version}
Conflicts: 	%{_lib}totem-plparser0-devel
Obsoletes:	%mklibname -d totem-plparser 7

%description -n	%{libnamedev}
Static libraries, include files for totem playlist parser

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make 

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{minilibname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{minilibname} -p /sbin/ldconfig
%endif


%files i18n -f %name.lang
%defattr(-,root,root)

%files -n %{libname}
%defattr(-,root,root)
%doc README NEWS 
%{_libdir}/libtotem-plparser.so.%{major}*
%_libdir/girepository-1.0/TotemPlParser-1.0.typelib

%files -n %{minilibname}
%defattr(-,root,root)
%{_libdir}/libtotem-plparser-mini.so.%{minimajor}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%doc %_datadir/gtk-doc/html/*
%{_libdir}/*.so
%_datadir/gir-1.0/TotemPlParser-1.0.gir
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%_includedir/%name



