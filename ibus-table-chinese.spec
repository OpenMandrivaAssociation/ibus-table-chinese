Summary:	ibus-chinese - table-based engine
Name:		ibus-table-chinese
Epoch:		1
Version:	1.4.6
Release:	1
License:	GPLv3+
Group:		System/Internationalization
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
Source1:	https://fedorahosted.org/releases/c/m/cmake-fedora/cmake-fedora-modules-only-latest.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(ibus-table)
BuildArch:	noarch

%description
ibus-table-chinese provide the following input method tables for IBus-Table.

#----------------------------------------------------------------------------

%package -n ibus-table-array30
Summary:	ibus-array30 - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-array30
Array30 input method on IBus Table under IBus framework.

%files -n ibus-table-array30
%{_datadir}/ibus-table/icons/array30-big.png
%{_datadir}/ibus-table/icons/array30.png
%{_datadir}/ibus-table/tables/array30-big.db
%{_datadir}/ibus-table/tables/array30.db

#----------------------------------------------------------------------------

%package -n ibus-table-cangjie
Summary:	ibus-cangjie - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-cangjie
CangJie input methods on IBus Table under IBus framework.

%files -n ibus-table-cangjie
%{_datadir}/ibus-table/icons/cangjie-big.png
%{_datadir}/ibus-table/icons/cangjie3.svg
%{_datadir}/ibus-table/icons/cangjie5.svg
%{_datadir}/ibus-table/icons/easy-big.png
%{_datadir}/ibus-table/icons/quick-classic.png
%{_datadir}/ibus-table/icons/quick3.png
%{_datadir}/ibus-table/icons/quick5.png
%{_datadir}/ibus-table/icons/scj6.svg
%{_datadir}/ibus-table/tables/cangjie-big.db
%{_datadir}/ibus-table/tables/cangjie3.db
%{_datadir}/ibus-table/tables/cangjie5.db
%{_datadir}/ibus-table/tables/easy-big.db
%{_datadir}/ibus-table/tables/quick-classic.db
%{_datadir}/ibus-table/tables/quick3.db
%{_datadir}/ibus-table/tables/quick5.db
%{_datadir}/ibus-table/tables/scj6.db

#----------------------------------------------------------------------------

%package -n ibus-table-cantonese
Summary:	ibus-cantonese - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-cantonese
Cantonese input method on IBus Table under IBus framework.

%files -n ibus-table-cantonese
%{_datadir}/ibus-table/icons/cantonese.png
%{_datadir}/ibus-table/icons/cantonhk.png
%{_datadir}/ibus-table/icons/jyutping.png
%{_datadir}/ibus-table/tables/cantonese.db
%{_datadir}/ibus-table/tables/cantonhk.db
%{_datadir}/ibus-table/tables/jyutping.db

#----------------------------------------------------------------------------

%package -n ibus-table-erbi
Summary:	ibus-erbi - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-erbi
ErBi input method on IBus Table under IBus framework.

%files -n ibus-table-erbi
%{_datadir}/ibus-table/icons/erbi*
%{_datadir}/ibus-table/tables/erbi*.db

#----------------------------------------------------------------------------

%package -n ibus-table-stroke5
Summary:	ibus-stroke5 - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-stroke5
Stroke5 input method on IBus Table under IBus framework.

%files -n ibus-table-stroke5
%{_datadir}/ibus-table/icons/stroke5*
%{_datadir}/ibus-table/tables/stroke5*.db

#----------------------------------------------------------------------------

%package -n ibus-table-wu
Summary:	ibus-wu - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-wu
Wu input method on IBus Table under IBus framework.

%files -n ibus-table-wu
%{_datadir}/ibus-table/icons/wu.png
%{_datadir}/ibus-table/tables/wu.db

#----------------------------------------------------------------------------

%package -n ibus-table-wubi
Summary:	ibus-wubi - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-wubi
Wubi86 input method on IBus Table under IBus framework.

%files -n ibus-table-wubi
%{_datadir}/ibus-table/icons/wubi*86.svg
%{_datadir}/ibus-table/tables/wubi*86.db

#----------------------------------------------------------------------------

%package -n ibus-table-yong
Summary:	ibus-yong - table-based engine
Group:		System/Internationalization
Requires:	ibus-table

%description -n ibus-table-yong
Yong input method on IBus Table under IBus framework.

%files -n ibus-table-yong
%{_datadir}/ibus-table/icons/yong*
%{_datadir}/ibus-table/tables/yong*.db

#---------------------------------------------------------------------------0

%prep
%setup -q -n %{name}-%{version}-Source -a1

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DDATA_DIR:PATH=%{_datadir}
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_datadir}/doc

