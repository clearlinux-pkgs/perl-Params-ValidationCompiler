#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-ValidationCompiler
Version  : 0.31
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-ValidationCompiler-0.31.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-ValidationCompiler-0.31.tar.gz
Summary  : 'Build an optimized subroutine parameter validator once, use it forever'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Params-ValidationCompiler-perl = %{version}-%{release}
Requires: perl(Class::XSAccessor)
Requires: perl(Eval::Closure)
Requires: perl(Exception::Class)
Requires: perl(Params::ValidationCompiler)
Requires: perl(Types::Standard)
BuildRequires : buildreq-cpan
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(Importer)
BuildRequires : perl(Specio)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Test2::V0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
Params::ValidationCompiler - Build an optimized subroutine parameter validator once, use it forever

%package dev
Summary: dev components for the perl-Params-ValidationCompiler package.
Group: Development
Provides: perl-Params-ValidationCompiler-devel = %{version}-%{release}
Requires: perl-Params-ValidationCompiler = %{version}-%{release}

%description dev
dev components for the perl-Params-ValidationCompiler package.


%package perl
Summary: perl components for the perl-Params-ValidationCompiler package.
Group: Default
Requires: perl-Params-ValidationCompiler = %{version}-%{release}

%description perl
perl components for the perl-Params-ValidationCompiler package.


%prep
%setup -q -n Params-ValidationCompiler-0.31
cd %{_builddir}/Params-ValidationCompiler-0.31

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Params::ValidationCompiler.3
/usr/share/man/man3/Params::ValidationCompiler::Compiler.3
/usr/share/man/man3/Params::ValidationCompiler::Exceptions.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
