#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstacksdk
Version  : 0.9.9
Release  : 19
URL      : http://tarballs.openstack.org/python-openstacksdk/openstacksdk-0.9.9.tar.gz
Source0  : http://tarballs.openstack.org/python-openstacksdk/openstacksdk-0.9.9.tar.gz
Summary  : An SDK for building applications to work with OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: openstacksdk-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
OpenStack Python SDK
====================
The ``python-openstacksdk`` is a collection of libraries for building
applications to work with OpenStack clouds. The project aims to provide
a consistent and complete set of interactions with OpenStack's many
services, along with complete documentation, examples, and tools.

%package python
Summary: python components for the openstacksdk package.
Group: Default

%description python
python components for the openstacksdk package.


%prep
%setup -q -n openstacksdk-0.9.9

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
