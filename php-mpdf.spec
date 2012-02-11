# TODO
# - external http://apps.sourceforge.net/trac/hyphenator4php/
# - classes/barcode.php - adopted from tcpdf
# - external iccprofiles/
# - external utils/UnicodeData.txt
%define		php_min_version 5.2.7
%define		pkgname	mpdf
%include	/usr/lib/rpm/macros.php
Summary:	A PHP class to generate PDF files from HTML with Unicode/UTF-8 and CJK support
Name:		php-%{pkgname}
Version:	5.3
Release:	0.2
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://mpdf1.com/repos/download.php?file=MPDF53#/MPDF53.zip
# Source0-md5:	db4ab1585e97b597ec35e48ee2914e29
Patch0:	backslash-fix.patch
URL:		http://www.mpdf1.com/mpdf/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php-bcmath
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-ctype
Requires:	php-date
Requires:	php-gd
Requires:	php-mbstring
Requires:	php-pcre
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{pkgname}

# bad depsolver
%define		_noautopear	pear

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
mPDF is a PHP class which generates PDF files from UTF-8 encoded HTML.
It is based on FPDF and HTML2FPDF, with a number of enhancements.

%package examples
Summary:	mPDF example programs
Summary(pl.UTF-8):	mPDF programy przykładowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
mPDF example programs.

%description examples -l pl.UTF-8
mPDF - przykładowe programy.

%prep
%setup -q -n MPDF53
%undos -f php,txt
%patch0 -p1

%{__rm} tmp/dummy.txt
%{__rm} ttfontdata/dummy.txt
%{__rm} graph_cache/dummy.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a *.css $RPM_BUILD_ROOT%{_appdir}
cp -a classes includes utils $RPM_BUILD_ROOT%{_appdir}
cp -a font iccprofiles mpdfi patterns ttfontdata ttfonts $RPM_BUILD_ROOT%{_appdir}
cp -a graph_cache tmp $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ADDED\ INFO\ FONTS.txt CHANGELOG.txt CREDITS.txt FONT\ INFO.txt README.txt
%{_appdir}/*.php
%{_appdir}/*.css
%{_appdir}/classes
%{_appdir}/includes
%{_appdir}/utils
%{_appdir}/font
%{_appdir}/iccprofiles
%{_appdir}/mpdfi

%{_appdir}/ttfonts
%{_appdir}/patterns

%dir %{_appdir}/graph_cache
%dir %{_appdir}/ttfontdata
%dir %{_appdir}/tmp

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
