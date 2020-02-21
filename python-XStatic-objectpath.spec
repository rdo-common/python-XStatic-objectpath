%{?python_enable_dependency_generator}

%global pypi_name XStatic-objectpath

Name:           python-%{pypi_name}
Version:        1.2.1.0
Release:        2%{?dist}
Summary:        ObjectPath JavaScript library (XStatic packaging standard)

License:        MIT
URL:            https://github.com/mike-marcacci/objectpath
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/mike-marcacci/objectpath/master/license
BuildArch:      noarch

%description
ObjectPath JavaScript library packaged
for setuptools (easy_install) / pip.

Parse js object paths using both dot and bracket notation.
Stringify an array of properties into a valid path.

%package -n xstatic-objectpath-common
Summary: ObjectPath JavaScript library (XStatic packaging standard)

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-objectpath-common
ObjectPath JavaScript library packaged
for setuptools (easy_install) / pip.

This package contains the javascript files.

%package -n python3-%{pypi_name}
Summary: ObjectPath JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-objectpath-common = %{version}-%{release}

%description -n python3-%{pypi_name}
ObjectPath JavaScript library packaged
for setuptools (easy_install) / pip.

Parse js object paths using both dot and bracket notation.
Stringify an array of properties into a valid path.

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} LICENSE

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/objectpath'|" xstatic/pkg/objectpath/__init__.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
# Move static files
mkdir -p %{buildroot}/%{_jsdir}/objectpath
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/objectpath/data/ObjectPath.js %{buildroot}/%{_jsdir}/objectpath

rmdir %{buildroot}/%{python3_sitelib}/xstatic/pkg/objectpath/data/

%files -n xstatic-objectpath-common
%doc README.txt
%license LICENSE
%{_jsdir}/objectpath

%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{python3_sitelib}/xstatic/pkg/objectpath
%{python3_sitelib}/XStatic_objectpath-%{version}-py?.?.egg-info
%{python3_sitelib}/XStatic_objectpath-%{version}-py?.?-nspkg.pth

%changelog
* Fri Feb 21 2020 Yatin Karel <ykarel@redhat.com> - 1.2.1.0-2
- Drop python2 sub package

* Fri Aug 5 2016 David Moreau Simard <dmsimard@redhat.com> - 1.2.1.0-1
- First version
