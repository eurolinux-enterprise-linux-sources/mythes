Name:      mythes
Summary:   A thesaurus library
Version:   1.2.3
Release:   7%{?dist}
Source:    http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
Group:     System Environment/Libraries
URL:       http://hunspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   BSD and MIT
BuildRequires: hunspell-devel
Patch0: mythes-aarch64.patch

%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return 
information on part of speech, meanings, and synonyms.

%package devel
Requires: mythes = %{version}-%{release}, pkgconfig
Summary: Files for developing with mythes
Group: Development/Libraries

%description devel
Includes and definitions for developing with mythes

%prep
%setup -q
%patch0 -p1 -b .aarch64

%build
%configure --disable-rpath --disable-static
make %{?_smp_mflags}

%check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING AUTHORS
%{_libdir}/*.so.*
%{_datadir}/mythes

%files devel
%defattr(-,root,root,-)
%doc data_layout.txt
%{_includedir}/mythes.hxx
%{_libdir}/*.so
%{_libdir}/pkgconfig/mythes.pc
%{_bindir}/th_gen_idx.pl

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.2.3-7
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.3-6
- Mass rebuild 2013-12-27

* Thu Apr 04 2013 Caolán McNamara <caolanm@redhat.com> - 1.2.3-5
- Resolves: rhbz#926191 support aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Caolán McNamara <caolanm@redhat.com> - 1.2.3-3
- tarball contains MIT-alike licensed wordnet-derived sample thesaurus data

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Caolán McNamara <caolanm@redhat.com> - 1.2.3-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Caolán McNamara <caolanm@redhat.com> - 1.2.2-1
- latest version
- drop integrated mythes-1.2.1-rhbz675806.patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Caolán McNamara <caolanm@redhat.com> - 1.2.1-2
- Resolves: rhbz#675806 fix crash if thesarus is busted

* Mon Jun 21 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Thu Mar 11 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.0-1
- initial version
