#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : links
Version  : 2.28
Release  : 28
URL      : http://links.twibright.com/download/links-2.28.tar.bz2
Source0  : http://links.twibright.com/download/links-2.28.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: links-bin = %{version}-%{release}
Requires: links-license = %{version}-%{release}
Requires: links-man = %{version}-%{release}
BuildRequires : gpm-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(openssl)
BuildRequires : xz-dev
BuildRequires : zstd-dev

%description
Links
=====
Contents
--------
1. About
2. Installation
3. Usage
4. Braille terminal support
5. More features

%package bin
Summary: bin components for the links package.
Group: Binaries
Requires: links-license = %{version}-%{release}

%description bin
bin components for the links package.


%package license
Summary: license components for the links package.
Group: Default

%description license
license components for the links package.


%package man
Summary: man components for the links package.
Group: Default

%description man
man components for the links package.


%prep
%setup -q -n links-2.28
cd %{_builddir}/links-2.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664805445
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664805445
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/links
cp %{_builddir}/links-%{version}/COPYING %{buildroot}/usr/share/package-licenses/links/095cd2f9a1768387960b0df92d8c168fea492af2 || :
%make_install
## install_append content
ln -sv links %{buildroot}/usr/bin/elinks
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/elinks
/usr/bin/links

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/links/095cd2f9a1768387960b0df92d8c168fea492af2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/links.1
