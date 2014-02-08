Name: amarok-scripts-zh_CN
Summary: Amarok scripts for Chinese users
Version: 0.8.11.29
Release: 8
License: GPLv2+
Url: http://www.kde-apps.org/index.php?xcontentmode=57
Group: Sound
Source0: http://www.kde-apps.org/CONTENT/content-files/91785-lyrics_CN.amarokscript.tar.gz
Source1: http://www.kde-apps.org/CONTENT/content-files/91784-amarok-radio-cn.amarokscript.tar.gz
Requires: amarok >= 3:1.98
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: kde4-macros

%description
This package contains several amarok scripts useful for Chinese users.

%prep
%setup -q -a1 -c -n %name

%install
rm -fr %buildroot
mkdir -p %buildroot%_kde_appsdir/amarok/scripts
cp -fr * %buildroot%_kde_appsdir/amarok/scripts/

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,-)
%_kde_appsdir/amarok/scripts/*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.11.29-5mdv2011.0
+ Revision: 662763
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.11.29-4mdv2011.0
+ Revision: 603177
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.11.29-3mdv2010.1
+ Revision: 521936
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.11.29-2mdv2010.0
+ Revision: 413026
- rebuild

* Sat Nov 29 2008 Funda Wang <fwang@mandriva.org> 0.8.11.29-1mdv2009.1
+ Revision: 308013
- New version

* Mon Nov 24 2008 Funda Wang <fwang@mandriva.org> 0.8.10.24-1mdv2009.1
+ Revision: 306326
- import amarok-scripts-zh_CN


