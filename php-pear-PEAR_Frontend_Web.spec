%define		_class		PEAR
%define		_subclass	Frontend
%define		upstream_name	%{_class}_%{_subclass}_Web

Summary:	HTML (Web) PEAR package manager
Name:		php-pear-%{upstream_name}
Version:	0.7.4
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
URL:		http://pear.php.net/package/PEAR_Frontend_Web/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Provides:	pear(Frontend)
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Web interface to the PEAR package manager. Needed only when you want
to use PEAR from their CVS.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/doc
rm -rf %{buildroot}%{_datadir}/pear/test

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/pearfrontendweb.php
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml
