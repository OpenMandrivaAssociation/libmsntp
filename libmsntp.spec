%define	major 1
%define libname	%mklibname msntp %{major}

Summary:	Full-featured, compact, portable SNTP library
Name:		libmsntp
Version:	1.6a
Release:	%mkrel 3
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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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


