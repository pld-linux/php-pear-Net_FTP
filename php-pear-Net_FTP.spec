%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	FTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - comfortable communication with FTP-servers
Summary(pl):	%{_pearname} - komfortowa komunikacja z serwerami FTP
Name:		php-pear-%{_pearname}
Version:	1.3.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fce386d6029e1171ab8f46c7568f2637
URL:		http://pear.php.net/package/Net_FTP/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-ftp
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class allows you to communicate with FTP-servers more comfortable
that the ftp-functions of PHP. Especially you can up- and download
recursively.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta pozwala na bardziej komfortowa komunikacjê z serwerami FTP
ni¿ jest to realizowane przez funkcje w PHP. Szczególnie ³atwy jest
down- i upload rekursywny.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/example
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
