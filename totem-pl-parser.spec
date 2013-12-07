%define major 17
%define girmajor 1.0
%define libname %mklibname totem-plparser %{major}
%define libmini %mklibname totem-plparser-mini %{major}
%define girname %mklibname totem-plparser-gir %{girmajor}
%define develname %mklibname -d totem-plparser

Summary:	Playlist parser library from the Totem Movie Player
Name:		totem-pl-parser
Version:	3.4.4
Release:	4
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.hadess.net/totem.php3
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem-pl-parser/3.4/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libquvi)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libgcrypt)

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
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make LIBS='-lgcrypt -lgmodule-2.0'

%install
%makeinstall_std

%find_lang %{name}

%files i18n -f %{name}.lang
%doc README NEWS

%files -n %{libname}
%{_libdir}/libtotem-plparser.so.%{major}*

%files -n %{libmini}
%{_libdir}/libtotem-plparser-mini.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/TotemPlParser-%{girmajor}.typelib

%files -n %{develname}
%doc ChangeLog AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/TotemPlParser-%{girmajor}.gir
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}



%changelog
* Mon Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.4.3-1
- update to 3.4.3

* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799411
- update to new version 3.4.2

* Thu May 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 795590
- new version 3.4.1

* Wed Mar 14 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0-1
+ Revision: 784901
- new version 3.2.0
- added additional BRs

* Thu Dec 08 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.32.6-2
+ Revision: 739169
- rebuild
- split out gir pkg
- removed .la files
- disabled static build
- removed defattr, clean section, mkrel, BuildRoot
- removed pre 200900 scriptlets
- cleaned up spec

* Tue Sep 20 2011 Götz Waschk <waschk@mandriva.org> 2.32.6-1
+ Revision: 700596
- new version
- xz tarball

* Tue May 10 2011 Götz Waschk <waschk@mandriva.org> 2.32.5-1
+ Revision: 673355
- update to new version 2.32.5

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 2.32.4-2
+ Revision: 652111
- rebuild for updated libsoup libtool archive

* Mon Mar 21 2011 Götz Waschk <waschk@mandriva.org> 2.32.4-1
+ Revision: 647379
- update to new version 2.32.4

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.32.3-2
+ Revision: 640006
- rebuild

* Mon Feb 21 2011 Götz Waschk <waschk@mandriva.org> 2.32.3-1
+ Revision: 639194
- new version
- drop patch

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 2.32.2-2
+ Revision: 633889
- fix linkage

* Sat Jan 29 2011 Götz Waschk <waschk@mandriva.org> 2.32.2-1
+ Revision: 633875
- new version
- don't build with --no-undefined

* Mon Oct 18 2010 Götz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 586628
- update to new version 2.32.1

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581882
- update to new version 2.32.0

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 578816
- new version
- drop patch

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 2.30.3-1mdv2011.0
+ Revision: 578196
- new version
- fix introspection build (b.g.o #629342)

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-2mdv2011.0
+ Revision: 568245
- rebuild for new libproxy

* Wed Aug 04 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 565868
- update build deps
- update to new version 2.30.2

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 2.30.1-2mdv2011.0
+ Revision: 563907
- rebuild for new gobject-introspection

* Wed May 12 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-1mdv2010.1
+ Revision: 544601
- Release 2.30.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528904
- update to new version 2.30.0

* Mon Mar 15 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 520295
- new version
- update file list

  + Funda Wang <fwang@mandriva.org>
    - linkage patch not needed

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 497199
- new version
- new major
- update build deps
- enable introspection

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 476373
- update to new version 2.28.2

* Tue Sep 29 2009 Götz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.0
+ Revision: 450968
- update to new version 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446472
- update to new version 2.28.0

* Tue Sep 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 443022
- update to new version 2.27.92

* Thu Jul 23 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 399059
- new version
- update build deps

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374161
- new version

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 370844
- New version 2.26.2

* Tue Mar 31 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 362899
- new version

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355754
- new version
- fix linking
- update build deps

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347809
- update to new version 2.25.92

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 337016
- new version
- drop patch

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.1-3mdv2009.1
+ Revision: 336623
- rebuild

* Fri Dec 19 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-2mdv2009.1
+ Revision: 316263
- fix exported symbols again (upstream bug #556719)

* Mon Dec 08 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 311777
- update to new version 2.25.1

* Mon Dec 08 2008 Götz Waschk <waschk@mandriva.org> 2.24.3-1mdv2009.1
+ Revision: 311769
- update to new version 2.24.3

* Sat Nov 08 2008 Götz Waschk <waschk@mandriva.org> 2.24.2-3mdv2009.1
+ Revision: 301149
- rebuild for new libxcb

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 2.24.2-2mdv2009.1
+ Revision: 299495
- rebuild for new evolution-data-server

* Thu Oct 30 2008 Götz Waschk <waschk@mandriva.org> 2.24.2-1mdv2009.1
+ Revision: 298744
- new version
- drop patch

* Mon Oct 20 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-3mdv2009.1
+ Revision: 295653
- rebuild

* Sat Oct 18 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-2mdv2009.1
+ Revision: 294972
- fix python binding (bug #43622)

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 291932
- new version
- drop patch

* Thu Oct 02 2008 Frederic Crozat <fcrozat@mandriva.com> 2.24.0-2mdv2009.0
+ Revision: 290752
- Patch0 (SVN): bug fixes from SVN

* Sun Sep 21 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286361
- new version

* Fri Aug 29 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 277464
- new version

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 2.23.3-3mdv2009.0
+ Revision: 241879
- rebuild for missing packages

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 2.23.3-2mdv2009.0
+ Revision: 240200
- rebuild

* Mon Jul 14 2008 Götz Waschk <waschk@mandriva.org> 2.23.3-1mdv2009.0
+ Revision: 234534
- fix buildrequires
- new version
- drop patch and all build workarounds

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.2-1mdv2009.0
+ Revision: 231097
- patch to make it build
- new version
- new major
- fix build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 193794
- new version
- drop patch

* Wed Apr 02 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.1-3mdv2008.1
+ Revision: 191630
- Patch0: various parsing fixes from SVN

* Wed Mar 26 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-2mdv2008.1
+ Revision: 190454
- rebuild

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2008.1
+ Revision: 183427
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174560
- new version

* Wed Jan 30 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-2mdv2008.1
+ Revision: 160401
- rebuild

* Tue Jan 22 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 156135
- new version
- add devel docs

* Mon Jan 07 2008 Götz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 146326
- new version
- update deps

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Götz Waschk <waschk@mandriva.org> 2.21.6-1mdv2008.1
+ Revision: 115989
- new version
-new major

* Tue Dec 04 2007 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 115195
- import totem-pl-parser


* Tue Dec  4 2007 G�tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
- initial package
