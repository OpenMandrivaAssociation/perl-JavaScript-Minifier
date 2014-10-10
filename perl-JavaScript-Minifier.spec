%define upstream_name    JavaScript-Minifier
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for minifying JavaScript code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/JavaScript/JavaScript-Minifier-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
This module removes unnecessary whitespace from JavaScript code. The
primary requirement developing this module is to not break working code: if
working JavaScript is in input then working JavaScript is output. It is ok
if the input has missing semi-colons, snips like '++ +' or '12
.toString()', for example. Internet Explorer conditional comments are
copied to the output but the code inside these comments will not be
minified.

The ECMAScript specifications allow for many different whitespace
characters: space, horizontal tab, vertical tab, new line, carriage return,
form feed, and paragraph separator. This module understands all of these as
whitespace except for vertical tab and paragraph separator. These two types
of whitespace are not minimized.

For static JavaScript files, it is recommended that you minify during the
build stage of web deployment. If you minify on-the-fly then it might be a
good idea to cache the minified file. Minifying static files on-the-fly
repeatedly is wasteful.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Sep 11 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 699423
- import perl-JavaScript-Minifier


