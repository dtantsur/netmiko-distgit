%global srcname netmiko
%global sum Multi-vendor library to simplify Paramiko SSH connections to network devices

Name:           python-%{srcname}
Version:        1.4.1
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python3-devel

%description
%{sum}


%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python2-paramiko >= 1.13.0
Requires:       python2-scp >= 0.10.0
Requires:       PyYAML
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{sum} - package for Python 2.


%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-paramiko >= 1.13.0
Requires:       python3-scp >= 0.10.0
Requires:       python3-PyYAML
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum} - package for Python 3.

# FIXME: build the documentation, when upstream starts shipping its sources:
# https://github.com/ktbyers/netmiko/issues/507


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
# FIXME: run unit tests, when upstream starts shipping them:
# https://github.com/ktbyers/netmiko/issues/508


%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*


%changelog
* Mon Jun 26 2017 Dmitry Tantsur <divius.inside@gmail.com> - 1.4.1-1
- Initial packaging
