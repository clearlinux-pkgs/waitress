#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : waitress
Version  : 1.1.0
Release  : 50
URL      : http://pypi.debian.net/waitress/waitress-1.1.0.tar.gz
Source0  : http://pypi.debian.net/waitress/waitress-1.1.0.tar.gz
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
acceptable performance.  It has no dependencies except ones which live in the
        Python standard library.  It runs on CPython on Unix and Windows under Python
        2.7+ and Python 3.3+.  It is also known to run on PyPy 1.6.0+ on UNIX.  It
        supports HTTP/1.0 and HTTP/1.1.
        
        For more information, see the "docs" directory of the Waitress package or

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
%setup -q -n waitress-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541280641
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
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
