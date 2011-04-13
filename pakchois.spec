Summary:	PaKChoiS - PKCS#11 wrapper library
Summary(pl.UTF-8):	PaKChoiS - biblioteka obudowująca PKCS#11
Name:		pakchois
Version:	0.4
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.manyfish.co.uk/pakchois/%{name}-%{version}.tar.gz
# Source0-md5:	218ad0256e514989299acdf4e86aaf3d
URL:		http://www.manyfish.co.uk/pakchois/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PaKChoiS is just another PKCS#11 wrapper library. It aims to provide a
thin wrapper over the PKCS#11 interface. The goals are:

- to offer a modern object-oriented C interface wrapper for PKCS#11
- to not hide or abstract away any details of the PKCS#11 interface
  itself except where absolutely necessary
- to handle the details of loading DSOs
- to allow the caller to avoid caring about where on the system,
  PKCS#11 modules might be stored, or exactly how they are named
- to avoid any dependency on a particular cryptography toolkit.

%description -l pl.UTF-8
PaKChoiS to jeszcze jedna biblioteka obudowująca PKCS#11. Ma na celu
jest dostarczenie lekkiego obudowania interfejsu PKCS#11:

- oferującego współczesny, zorientowany obiektowo interfejs w C
- nie ukrywającego szczegółów interfejsu PKCS#11 poza miejscami, gdzie
  jest to konieczne
- obsługującego szczegóły wczytywania DSO
- pozwalającego wywołującemu pominąć szczegóły dotyczące
  umiejscowienia czy nazw modułów PKCS#11 w systemie
- zapobiegającego zależności od konkretnej biblioteki
  kryptograficznej.

%package devel
Summary:	Header files for pakchois library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pakchois
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pakchois library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pakchois.

%package static
Summary:	Static pakchois library
Summary(pl.UTF-8):	Statyczna biblioteka pakchois
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pakchois library.

%description static -l pl.UTF-8
Statyczna biblioteka pakchois.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpakchois.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libpakchois.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpakchois.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpakchois.so
%{_includedir}/pakchois
%{_pkgconfigdir}/pakchois.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpakchois.a
