%{?scl:%scl_package nodejs-lru-cache}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-lru-cache
Version:    2.5.0
Release:    1.sc1%{?dist}
Summary:    A least recently used cache object for Node.js
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/node-lru-cache
Source0:    http://registry.npmjs.org/lru-cache/-/lru-cache-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A cache object that deletes the least recently used items.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/lru-cache
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/lru-cache

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/lru-cache
%doc CONTRIBUTORS README.md LICENSE

%changelog
* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 2.5.0-1
- New upstream release 2.5.0
- AUTHORS renamed to CONTRIBUTORS

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 2.3.0-3
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.0-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.3.0-1
- new upstream release 2.3.0

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.2-1
- new upstream release 2.2.2

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.1-2
- add missing build section
- improve summary/description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.1-1
- new upstream release 2.2.1
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2
- fix BuildRequires not present on <F17

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1
- New upstream release 1.1.0

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.6-1
- new upstream release 1.0.6

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-1
- new upstream release 1.0.5

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-2
- add Group to make EL5 happy

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-1
- initial package
