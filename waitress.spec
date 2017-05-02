#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : waitress
Version  : 1.0.2
Release  : 31
URL      : http://pypi.debian.net/waitress/waitress-1.0.2.tar.gz
Source0  : http://pypi.debian.net/waitress/waitress-1.0.2.tar.gz
Summary  : Waitress WSGI server
Group    : Development/Tools
License  : ZPL-2.1
Requires: waitress-bin
Requires: waitress-python
Requires: Sphinx
Requires: coverage
Requires: docutils
Requires: nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Waitress is meant to be a production-quality pure-Python WSGI server with very
acceptable performance.  It has no dependencies except ones which live in the
Python standard library.  It runs on CPython on Unix and Windows under Python
2.7+ and Python 3.3+.  It is also known to run on PyPy 1.6.0+ on UNIX.  It
supports HTTP/1.0 and HTTP/1.1.

%package bin
Summary: bin components for the waitress package.
Group: Binaries

%description bin
bin components for the waitress package.


%package python
Summary: python components for the waitress package.
Group: Default

%description python
python components for the waitress package.


%prep
%setup -q -n waitress-1.0.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489025565
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1489025565
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/waitress-serve

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
