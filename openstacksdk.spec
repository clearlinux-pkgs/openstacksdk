#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : openstacksdk
Version  : 0.17.2
Release  : 28
URL      : https://tarballs.openstack.org/openstacksdk/openstacksdk-0.17.2.tar.gz
Source0  : https://tarballs.openstack.org/openstacksdk/openstacksdk-0.17.2.tar.gz
Source99 : https://tarballs.openstack.org/openstacksdk/openstacksdk-0.17.2.tar.gz.asc
Summary  : An SDK for building applications to work with OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: openstacksdk-bin
Requires: openstacksdk-python3
Requires: openstacksdk-license
Requires: openstacksdk-python
Requires: PyYAML
Requires: Sphinx
Requires: appdirs
Requires: beautifulsoup4
Requires: cryptography
Requires: decorator
Requires: docutils
Requires: dogpile.cache
Requires: futures
Requires: ipaddress
Requires: iso8601
Requires: jmespath
Requires: jsonpatch
Requires: keystoneauth1
Requires: netifaces
Requires: openstackdocstheme
Requires: pbr
Requires: reno
Requires: requestsexceptions
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
============
        
        openstacksdk is a client library for building applications to work
        with OpenStack clouds. The project aims to provide a consistent and
        complete set of interactions with OpenStack's many services, along with
        complete documentation, examples, and tools.
        
        It also contains an abstraction interface layer. Clouds can do many things, but
        there are probably only about 10 of them that most people care about with any
        regularity. If you want to do complicated things, the per-service oriented
        portions of the SDK are for you. However, if what you want is to be able to
        write an application that talks to clouds no matter what crazy choices the
        deployer has made in an attempt to be more hipster than their self-entitled
        narcissist peers, then the Cloud Abstraction layer is for you.
        
        A Brief History
        ---------------
        
        .. TODO(shade) This history section should move to the docs. We can put a
           link to the published URL here in the README, but it's too long.

%package bin
Summary: bin components for the openstacksdk package.
Group: Binaries
Requires: openstacksdk-license

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
Requires: openstacksdk-python3

%description python
python components for the openstacksdk package.


%package python3
Summary: python3 components for the openstacksdk package.
Group: Default
Requires: python3-core

%description python3
python3 components for the openstacksdk package.


%prep
%setup -q -n openstacksdk-0.17.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533787831
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/openstacksdk
cp LICENSE %{buildroot}/usr/share/doc/openstacksdk/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openstack-inventory

%files license
%defattr(-,root,root,-)
/usr/share/doc/openstacksdk/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
