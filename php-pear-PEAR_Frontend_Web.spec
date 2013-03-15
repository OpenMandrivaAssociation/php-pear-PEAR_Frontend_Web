%define		_class		PEAR
%define		_subclass	Frontend
%define		upstream_name	%{_class}_%{_subclass}_Web

Name:		php-pear-%{upstream_name}
Version:	0.7.4
Release:	6
Summary:	HTML (Web) PEAR package manager
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PEAR_Frontend_Web/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Provides:	pear(Frontend)
BuildRequires:	php-pear
BuildArch:	noarch

%description
Web interface to the PEAR package manager. Needed only when you want
to use PEAR from their CVS.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/pearfrontendweb.php
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-5mdv2012.0
+ Revision: 742176
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-4
+ Revision: 679555
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-3mdv2011.0
+ Revision: 613748
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.4-2mdv2010.1
+ Revision: 467946
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2010.0
+ Revision: 441504
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.7.3-1mdv2009.1
+ Revision: 368332
- Update status to beta
- Update php pear PEAR_Frontend_Web to 0.7.3 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-3mdv2009.1
+ Revision: 322545
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-2mdv2009.0
+ Revision: 237042
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.7.0-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdv2008.0
+ Revision: 32739
- fix build
- 0.7.0

* Sat Apr 28 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdv2008.0
+ Revision: 18935
- 0.6.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdv2008.0
+ Revision: 15727
- 0.5.2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdv2007.0
+ Revision: 82501
- Import php-pear-PEAR_Frontend_Web

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdk
- 0.5.1

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdk
- initial Mandriva package (PLD import)

