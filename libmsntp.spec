%define	major 1
%define libname	%mklibname msntp %{major}

Summary:	Full-featured, compact, portable SNTP library
Name:		libmsntp
Version:	1.6a
Release:	%mkrel 8
Group:		System/Libraries
License:	GPL
URL:		http://snarfed.org/space/libmsntp
Source0:	http://ryan.barrett.name/%{name}-%{version}.tar.bz2
Patch0:		libmsntp-1.6a-shared.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libmsntp is a full-featured, compact, portable SNTP library.

libmsntp provides SNTP client and server functionality in a shared
library with a simple API. SNTP (RFC 2030) is a simplified version
of NTP, which allows precise synchronization of system clocks over
a best-effort network. 

%package -n	%{libname}
Summary:	Full-featured, compact, portable SNTP library
Group:          System/Libraries

%description -n	%{libname}
libmsntp is a full-featured, compact, portable SNTP library.

libmsntp provides SNTP client and server functionality in a shared
library with a simple API. SNTP (RFC 2030) is a simplified version
of NTP, which allows precise synchronization of system clocks over
a best-effort network. 

%package -n	%{libname}-devel
Summary:	Static library and header files for the libmsntp library
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
libmsntp is a full-featured, compact, portable SNTP library.

libmsntp provides SNTP client and server functionality in a shared
library with a simple API. SNTP (RFC 2030) is a simplified version
of NTP, which allows precise synchronization of system clocks over
a best-effort network. 

This package contains the static libevent library and its header files
needed to compile applications such as stegdetect, etc.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build

%make \
    CFLAGS="%{optflags} -fPIC -DPIC" \
    shared static

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}

install -m0755 libmsntp.so.%{major} %{buildroot}%{_libdir}/
install -m0644 libmsntp.a %{buildroot}%{_libdir}/
ln -s libmsntp.so.%{major} %{buildroot}%{_libdir}/libmsntp.so
install -m0644 libmsntp.h %{buildroot}%{_includedir}/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc Copyright.msntp LICENSE README*
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc example.c
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6a-8mdv2011.0
+ Revision: 620154
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6a-7mdv2010.0
+ Revision: 429813
- rebuild

* Sat Jul 26 2008 Thierry Vignaud <tv@mandriva.org> 1.6a-6mdv2009.0
+ Revision: 250260
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.6a-4mdv2008.1
+ Revision: 170950
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.6a-3mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.6a-3mdv2007.1
+ Revision: 138898
- use the %%mkrel macro
- bunzip patches
- Import libmsntp

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6a-2mdk
- rebuild

* Tue Jan 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0a-1mdk
- initial mandrake package

