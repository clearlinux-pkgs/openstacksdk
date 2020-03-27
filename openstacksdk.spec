#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : openstacksdk
Version  : 0.45.0
Release  : 70
URL      : https://tarballs.openstack.org/openstacksdk/openstacksdk-0.45.0.tar.gz
Source0  : https://tarballs.openstack.org/openstacksdk/openstacksdk-0.45.0.tar.gz
Source1  : https://tarballs.openstack.org/openstacksdk/openstacksdk-0.45.0.tar.gz.asc
Summary  : An SDK for building applications to work with OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: openstacksdk-bin = %{version}-%{release}
Requires: openstacksdk-license = %{version}-%{release}
Requires: openstacksdk-python = %{version}-%{release}
Requires: openstacksdk-python3 = %{version}-%{release}
Requires: PyYAML
Requires: appdirs
Requires: cryptography
Requires: decorator
Requires: dogpile.cache
Requires: ipaddress
Requires: iso8601
Requires: jmespath
Requires: jsonpatch
Requires: keystoneauth1
Requires: munch
Requires: netifaces
Requires: os-service-types
Requires: pbr
Requires: requestsexceptions
Requires: six
BuildRequires : PyYAML
BuildRequires : appdirs
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : decorator
BuildRequires : dogpile.cache
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : jmespath
BuildRequires : jsonpatch
BuildRequires : keystoneauth1
BuildRequires : munch
BuildRequires : netifaces
BuildRequires : os-service-types
BuildRequires : pbr
BuildRequires : requestsexceptions
BuildRequires : six

%description
openstacksdk
============
openstacksdk is a client library for building applications to work
with OpenStack clouds. The project aims to provide a consistent and
complete set of interactions with OpenStack's many services, along with
complete documentation, examples, and tools.

%package bin
Summary: bin components for the openstacksdk package.
Group: Binaries
Requires: openstacksdk-license = %{version}-%{release}

%description bin
bin components for the openstacksdk package.


%package license
Summary: license components for the openstacksdk package.
Group: Default

%description license
license components for the openstacksdk package.


%package python
Summary: python components for the openstacksdk package.
Group: Default
Requires: openstacksdk-python3 = %{version}-%{release}

%description python
python components for the openstacksdk package.


%package python3
Summary: python3 components for the openstacksdk package.
Group: Default
Requires: python3-core
Provides: pypi(openstacksdk)
Requires: pypi(decorator)
Requires: pypi(jsonpatch)
Requires: pypi(dogpile.cache)
Requires: pypi(os_service_types)
Requires: pypi(six)
Requires: pypi(iso8601)
Requires: pypi(pbr)
Requires: pypi(netifaces)
Requires: pypi(appdirs)
Requires: pypi(requestsexceptions)
Requires: pypi(jmespath)
Requires: pypi(munch)
Requires: pypi(cryptography)
Requires: pypi(pyyaml)
Requires: pypi(keystoneauth1)

%description python3
python3 components for the openstacksdk package.


%prep
%setup -q -n openstacksdk-0.45.0
cd %{_builddir}/openstacksdk-0.45.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585315949
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openstacksdk
cp %{_builddir}/openstacksdk-0.45.0/LICENSE %{buildroot}/usr/share/package-licenses/openstacksdk/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openstack-inventory

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openstacksdk/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
