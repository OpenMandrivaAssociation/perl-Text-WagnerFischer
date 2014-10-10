%define upstream_name    Text-WagnerFischer
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An implementation of the Wagner-Fischer edit distance
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements the Wagner-Fischer dynamic programming technique, used
here to calculate the edit distance of two strings. The edit distance is a
measure of the degree of proximity between two strings, based on ``edits'': the
operations of substitutions, deletions or insertions needed to transform the
string into the other one (and vice versa).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/*/*

%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 405717
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-8mdv2009.0
+ Revision: 242063
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-6mdv2008.0
+ Revision: 87050
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-5mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-4mdk
- Fix SPEC according to Perl Policy
    - Source URL
- use mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdk 
- better url
- spec cleanup
- don't ship useless empty directories
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.04-2mdk
- fix buildrequires in a backward compatible way

* Thu Jun 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.04-1mdk 
- first mdk release

