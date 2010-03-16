Name: amarok-scripts-zh_CN
Summary: Amarok scripts for Chinese users
Version: 0.8.11.29
Release: %mkrel 3
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
