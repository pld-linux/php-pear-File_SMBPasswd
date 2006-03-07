%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	SMBPasswd
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class for managing SAMBA style password files
Summary(pl):	%{_pearname} - klasa do zarz±dzania plikami z has³ami SAMBY
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	2
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dcb06b21db84f1bf64cf94eb364d8fb9
URL:		http://pear.php.net/package/File_SMBPasswd/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-mhash
Requires:	php-pear
Requires:	php-pear-Crypt_CHAP >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this package, you can maintain smbpasswd-files, usualy used by
SAMBA.

In PEAR status of this package is: %{_status}.

%description -l pl
Przy u¿yciu tego pakietu mo¿na zarz±dzaæ plikami smbpasswd, u¿ywanymi
zwykle przez SAMBÊ.

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
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
