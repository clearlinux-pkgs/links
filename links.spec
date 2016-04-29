#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : links
Version  : 1.03
Release  : 6
URL      : http://www.jikos.cz/~mikulas/links/download/links-1.03.tar.gz
Source0  : http://www.jikos.cz/~mikulas/links/download/links-1.03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: links-bin
Requires: links-doc
BuildRequires : openssl-dev
BuildRequires : pkgconfig(openssl)
BuildRequires : zlib-dev

%description
Links
Lynx-like text WWW browser
Usage: links [options] <url>
See end of file default.c for list of options. Most options can be set in luser
interface or config file, so you do not need to care about them.

%package bin
Summary: bin components for the links package.
Group: Binaries

%description bin
bin components for the links package.


%package doc
Summary: doc components for the links package.
Group: Documentation

%description doc
doc components for the links package.


%prep
%setup -q -n links-1.03

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
ln -sv links %{buildroot}/usr/bin/elinks
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/elinks
/usr/bin/links

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
