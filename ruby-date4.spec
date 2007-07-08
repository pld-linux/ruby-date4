Summary:	Enhanced Date class
Summary(pl.UTF-8):	Klasa Enhanced Date (rozszerzonej daty)
Name:		ruby-date4
Version:	0.1.18
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://www.funaba.org/en/archive/date4-%{version}.tar.gz
# Source0-md5:	05ba7c1c44d0424e968a0cbed3d8e679
Source1:	setup.rb
URL:		http://www.funaba.org/en/ruby.html#date4
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
Requires:	ruby-tzinfo
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
date4 is a derivative of date2 that is for some experiments.

Supports timezone handling, provides a new class Delta, and some minor
changes.

%description -l pl.UTF-8
date4 to pochodna date2 przeznaczona do pewnych eksperymentów.

Obsługuje strefy czasowe, udostępnia nową klasę Delta i pewne
pomniejsze modyfikacje.

%prep
%setup -q -n date4-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
#rm $RPM_BUILD_ROOT%{ruby_ridir}/created.rid

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/date4.rb
%{ruby_rubylibdir}/date4
%{ruby_rubylibdir}/date4asdate.rb
