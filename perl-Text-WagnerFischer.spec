%define module  Text-WagnerFischer
%define name    perl-%{module}
%define version 0.04
%define release %mkrel 6

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        An implementation of the Wagner-Fischer edit distance
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module implements the Wagner-Fischer dynamic programming technique, used
here to calculate the edit distance of two strings. The edit distance is a
measure of the degree of proximity between two strings, based on ``edits'': the
operations of substitutions, deletions or insertions needed to transform the
string into the other one (and vice versa).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/*/*

