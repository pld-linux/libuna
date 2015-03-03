#
# Conditional build:
%bcond_without	tools	# unatools (disable for bootstrap)

Summary:	Library to support Unicode and ASCII (byte stream) conversions
Summary(pl.UTF-8):	Biblioteka obsługująca przekształcenia Unicode i ASCII (strumieni bajtów)
Name:		libuna
Version:	20150101
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libuna/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	36e8c89a1a8e516b65359ed6340fa455
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libuna/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
%if %{with tools}
BuildRequires:	libcdatetime-devel >= 20141018
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libcsystem-devel >= 20141018
%endif
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
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
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425

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
Requires:	libcdatetime >= 20141018
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcfile >= 20140503
Requires:	libcsystem >= 20141018

%description tools
Unicode and ASCII (byte stream) conversion utilities.

%description tools -l pl.UTF-8
Narzędzia do konwersji Unicode i ASCII (strumieni bajtów).

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_tools:--without-tools}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libuna.la

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
