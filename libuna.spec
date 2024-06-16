#
# Conditional build:
%bcond_without	tools	# unatools (disable for bootstrap)

# see m4/${libname}.m4 />= for required version of particular library
%define		libcdatetime_ver	20141018
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
Summary:	Library to support Unicode and ASCII (byte stream) conversions
Summary(pl.UTF-8):	Biblioteka obsługująca przekształcenia Unicode i ASCII (strumieni bajtów)
Name:		libuna
Version:	20240414
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libuna/releases
Source0:	https://github.com/libyal/libuna/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	1e492f9bdfc9b9e457737e101430213b
URL:		https://github.com/libyal/libuna/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
%if %{with tools}
BuildRequires:	libcdatetime-devel >= %{libcdatetime_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
%endif
Requires:	libcerror >= %{libcerror_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libuna is a library to support Unicode and ASCII (byte stream)
conversions.

%description -l pl.UTF-8
libuna to biblioteka obsługująca przekształcenia Unicode i ASCII
(strumieni bajtów).

%package devel
Summary:	Header files for libuna library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libuna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}

%description devel
Header files for libuna library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libuna.

%package static
Summary:	Static libuna library
Summary(pl.UTF-8):	Statyczna biblioteka libuna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libuna library.

%description static -l pl.UTF-8
Statyczna biblioteka libuna.

%package tools
Summary:	Unicode and ASCII (byte stream) conversion utilities
Summary(pl.UTF-8):	Narzędzia do konwersji Unicode i ASCII (strumieni bajtów)
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
Requires:	libcdatetime >= %{libcdatetime_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcfile >= %{libcfile_ver}

%description tools
Unicode and ASCII (byte stream) conversion utilities.

%description tools -l pl.UTF-8
Narzędzia do konwersji Unicode i ASCII (strumieni bajtów).

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libuna.la

%if %{without tools}
%{__rm} -f $RPM_BUILD_ROOT%{_bindir}/una* \
	$RPM_BUILD_ROOT%{_mandir}/man1/una*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libuna.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuna.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuna.so
%{_includedir}/libuna
%{_includedir}/libuna.h
%{_pkgconfigdir}/libuna.pc
%{_mandir}/man3/libuna.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libuna.a

%if %{with tools}
%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unabase
%attr(755,root,root) %{_bindir}/unaexport
%{_mandir}/man1/unaexport.1*
%endif
