#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : waitress
Version  : 1.4.4
Release  : 65
URL      : https://files.pythonhosted.org/packages/9a/32/90a74e5ab5fd4fa4bd051a51eb9a8f63bbbf3e00a00dc5cf73ebd4ddb46a/waitress-1.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/32/90a74e5ab5fd4fa4bd051a51eb9a8f63bbbf3e00a00dc5cf73ebd4ddb46a/waitress-1.4.4.tar.gz
Summary  : Waitress WSGI server
Group    : Development/Tools
License  : ZPL-2.1
Requires: waitress-bin = %{version}-%{release}
Requires: waitress-license = %{version}-%{release}
Requires: waitress-python = %{version}-%{release}
Requires: waitress-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
========

%package bin
Summary: bin components for the waitress package.
Group: Binaries
Requires: waitress-license = %{version}-%{release}

%description bin
bin components for the waitress package.


%package license
Summary: license components for the waitress package.
Group: Default

%description license
license components for the waitress package.


%package python
Summary: python components for the waitress package.
Group: Default
Requires: waitress-python3 = %{version}-%{release}

%description python
python components for the waitress package.


%package python3
Summary: python3 components for the waitress package.
Group: Default
Requires: python3-core
Provides: pypi(waitress)

%description python3
python3 components for the waitress package.


%prep
%setup -q -n waitress-1.4.4
cd %{_builddir}/waitress-1.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591116662
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/waitress
cp %{_builddir}/waitress-1.4.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/waitress/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/waitress-serve

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/waitress/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
