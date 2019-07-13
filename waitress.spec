#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : waitress
Version  : 1.3.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/43/50/9890471320d5ad22761ae46661cf745f487b1c8c4ec49352b99e1078b970/waitress-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/50/9890471320d5ad22761ae46661cf745f487b1c8c4ec49352b99e1078b970/waitress-1.3.0.tar.gz
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
Waitress
========
.. image:: https://img.shields.io/pypi/v/waitress.svg
:target: https://pypi.org/project/waitress/
:alt: latest version of waitress on PyPI

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

%description python3
python3 components for the waitress package.


%prep
%setup -q -n waitress-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557022898
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/waitress
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/waitress/LICENSE.txt
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
/usr/share/package-licenses/waitress/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
