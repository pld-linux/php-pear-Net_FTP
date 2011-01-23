%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	FTP
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
%define		subver	a2
%define		rel		2
Summary:	%{_pearname} - comfortable communication with FTP-servers
Summary(pl.UTF-8):	%{_pearname} - komfortowa komunikacja z serwerami FTP
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	3296b0ce4e2042cd29d7e60af1293e3a
URL:		http://pear.php.net/package/Net_FTP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-ftp
Requires:	php-pear
Obsoletes:	php-pear-Net_FTP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class allows you to communicate with FTP-servers more comfortable
that the ftp-functions of PHP. Especially you can up- and download
recursively.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta pozwala na bardziej komfortowa komunikację z serwerami FTP
niż jest to realizowane przez funkcje w PHP. Szczególnie łatwy jest
down- i upload rekursywny.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/data/Net_FTP/CHANGELOG .

mv docs/%{_pearname}/example examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log CHANGELOG
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{_examplesdir}/%{name}-%{version}
