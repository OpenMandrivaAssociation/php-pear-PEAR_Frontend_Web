%define		_class		PEAR
%define		_subclass	Frontend
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_Web

Summary:	%{_pearname} - HTML (Web) PEAR package manager
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/PEAR_Frontend_Web/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Provides:	pear(Frontend)
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	recode
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Web interface to the PEAR package manager. Needed only when you want
to use PEAR from their CVS.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

# fix bad xml
recode -d latin-1..html < package.xml > package.xml~
mv package.xml~ package.xml

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Web

install %{_pearname}-%{version}/WebInstaller.php %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/Web.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Web/*.png %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.gif %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.html %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.css %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Web
install %{_pearname}-%{version}/%{_subclass}/Web/*.js %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Web

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Web
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Web/*.png
%{_datadir}/pear/%{_class}/%{_subclass}/Web/*.gif
%{_datadir}/pear/%{_class}/%{_subclass}/Web/*.html
%{_datadir}/pear/%{_class}/%{_subclass}/Web/*.css
%{_datadir}/pear/%{_class}/%{_subclass}/Web/*.js
%{_datadir}/pear/packages/%{_pearname}.xml


