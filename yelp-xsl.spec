#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yelp-xsl
Version  : 3.38.1
Release  : 17
URL      : https://download.gnome.org/sources/yelp-xsl/3.38/yelp-xsl-3.38.1.tar.xz
Source0  : https://download.gnome.org/sources/yelp-xsl/3.38/yelp-xsl-3.38.1.tar.xz
Summary  : Yelp XSLT Stylesheets
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: yelp-xsl-data = %{version}-%{release}
Requires: yelp-xsl-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : perl(XML::Parser)

%description
ABOUT
=====
yelp-xsl is a collection of programs and data files to help you build,
maintain, and distribute documentation. It provides XSLT stylesheets
that can be built upon for help viewers and publishing systems. These
stylesheets output JavaScript and CSS content, and reference images
provided by yelp-xsl. This package also redistributes copies of the
jQuery and jQuery.Syntax JavaScript libraries.

%package data
Summary: data components for the yelp-xsl package.
Group: Data

%description data
data components for the yelp-xsl package.


%package dev
Summary: dev components for the yelp-xsl package.
Group: Development
Requires: yelp-xsl-data = %{version}-%{release}
Provides: yelp-xsl-devel = %{version}-%{release}
Requires: yelp-xsl = %{version}-%{release}

%description dev
dev components for the yelp-xsl package.


%package license
Summary: license components for the yelp-xsl package.
Group: Default

%description license
license components for the yelp-xsl package.


%prep
%setup -q -n yelp-xsl-3.38.1
cd %{_builddir}/yelp-xsl-3.38.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601834610
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1601834610
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yelp-xsl
cp %{_builddir}/yelp-xsl-3.38.1/COPYING %{buildroot}/usr/share/package-licenses/yelp-xsl/3db6c7b240e7ee09baf9426dc9ed4aacb6904dbb
cp %{_builddir}/yelp-xsl-3.38.1/COPYING.GPL %{buildroot}/usr/share/package-licenses/yelp-xsl/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/yelp-xsl-3.38.1/COPYING.LGPL %{buildroot}/usr/share/package-licenses/yelp-xsl/545f380fb332eb41236596500913ff8d582e3ead
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/yelp-xsl/js/highlight.pack.js
/usr/share/yelp-xsl/xslt/common/color.xsl
/usr/share/yelp-xsl/xslt/common/domains/yelp-xsl.xml
/usr/share/yelp-xsl/xslt/common/html.xsl
/usr/share/yelp-xsl/xslt/common/icons.xsl
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-advanced.svg
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-bug.svg
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-important.svg
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-note.svg
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-package.svg
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-tip.svg
/usr/share/yelp-xsl/xslt/common/icons/yelp-note-warning.svg
/usr/share/yelp-xsl/xslt/common/l10n-numbers.xsl
/usr/share/yelp-xsl/xslt/common/l10n.xsl
/usr/share/yelp-xsl/xslt/common/ttml.xsl
/usr/share/yelp-xsl/xslt/common/utils.xsl
/usr/share/yelp-xsl/xslt/docbook/common/db-chunk.xsl
/usr/share/yelp-xsl/xslt/docbook/common/db-common.xsl
/usr/share/yelp-xsl/xslt/docbook/common/db-profile.xsl
/usr/share/yelp-xsl/xslt/docbook/common/db-selectors.mod
/usr/share/yelp-xsl/xslt/docbook/common/db-title.xsl
/usr/share/yelp-xsl/xslt/docbook/common/db-xref.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-bibliography.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-block.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-callout.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-classsynopsis.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-cmdsynopsis.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-css.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-division.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-ebnf.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-footnote.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-funcsynopsis.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-index.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-inline.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-links.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-list.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-math.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-media.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-refentry.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-suppressed.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-table.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html-xref.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2html.xsl
/usr/share/yelp-xsl/xslt/docbook/html/db2xhtml.xsl
/usr/share/yelp-xsl/xslt/mallard/cache/mal-cache.xsl
/usr/share/yelp-xsl/xslt/mallard/common/mal-gloss.xsl
/usr/share/yelp-xsl/xslt/mallard/common/mal-if.xsl
/usr/share/yelp-xsl/xslt/mallard/common/mal-link.xsl
/usr/share/yelp-xsl/xslt/mallard/common/mal-sort.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-api.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-block.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-gloss.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-inline.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-links.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-list.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-math.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-media.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-page.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-svg.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-table.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html-ui.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2html.xsl
/usr/share/yelp-xsl/xslt/mallard/html/mal2xhtml.xsl

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/yelp-xsl.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yelp-xsl/3db6c7b240e7ee09baf9426dc9ed4aacb6904dbb
/usr/share/package-licenses/yelp-xsl/545f380fb332eb41236596500913ff8d582e3ead
/usr/share/package-licenses/yelp-xsl/b47456e2c1f38c40346ff00db976a2badf36b5e3
