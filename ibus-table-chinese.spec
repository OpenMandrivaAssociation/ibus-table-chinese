%define	version 1.2.0.20100305
%define	release %mkrel 2

Name:      ibus-table-chinese
Summary:   ibus-chinese - table-based engine
Version:   1.3.0.20100527
Release:   %mkrel 1
Group:     System/Internationalization
License:   GPLv3+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ibus-table-devel >= 1.3.0
BuildRequires: ibus-table-extraphrase >= 1.2.0
BuildArch:	noarch

%description
ibus-table-chinese provide the following input method tables for IBus-Table.

%package -n ibus-table-erbi
Group: System/Internationalization
Summary: ibus-erbi - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-erbi
ibus-table-erbi provides ErBi input method on IBus Table under IBus framework.

%files -n ibus-table-erbi
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/erbi*
%{_datadir}/ibus-table/tables/erbi*.db

%package -n ibus-table-wu
Group: System/Internationalization
Summary: ibus-wu - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-wu
ibus-table-wu provides wu input method on IBus Table under IBus framework.

%files -n ibus-table-wu
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/wu*
%{_datadir}/ibus-table/tables/wu*.db

%package -n ibus-table-yong
Group: System/Internationalization
Summary: ibus-yong - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-yong
ibus-table-yong provides yong input method on IBus Table under IBus framework.

%files -n ibus-table-yong
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/yong*
%{_datadir}/ibus-table/tables/yong*.db

%package -n ibus-table-zhuyin
Group: System/Internationalization
Summary: ibus-zhuyin - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-zhuyin
ibus-table-zhuyin provides zhuyin input method on IBus Table under IBus framework.

%files -n ibus-table-zhuyin
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/zhuyin*
%{_datadir}/ibus-table/tables/zhuyin*.db

%package -n ibus-table-ziranma
Group: System/Internationalization
Summary: ibus-ziranma - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-ziranma
ibus-table-ziranma provides ziranma input method on IBus Table under IBus framework.

%files -n ibus-table-ziranma
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/ziranma*
%{_datadir}/ibus-table/tables/ziranma*.db

%package -n ibus-table-xinhua
Group: System/Internationalization
Summary: ibus-xinhua - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-xinhua
ibus-table-xinhua provides Xinhua input method on IBus Table under IBus framework.

%files -n ibus-table-xinhua
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/xinhua*
%{_datadir}/ibus-table/tables/xinhua*.db

%package -n ibus-table-stroke5
Group: System/Internationalization
Summary: ibus-stroke5 - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-stroke5
ibus-table-stroke5 provides stroke5 input method on IBus Table under IBus framework.

%files -n ibus-table-stroke5
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/stroke5*
%{_datadir}/ibus-table/tables/stroke5*.db

%package -n ibus-table-zhengma
Group: System/Internationalization
Summary: ibus-zhengma - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-zhengma
ibus-table-zhengma provides zhengma input method on IBus Table under IBus framework.

%files -n ibus-table-zhengma
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/zhengma*
%{_datadir}/ibus-table/tables/zhengma*.db

%package -n ibus-table-cangjie
Group: System/Internationalization
Summary: ibus-cangjie - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-cangjie
ibus-table-cangjie provide CangJie input methods on IBus Table under IBus framework.

%files -n ibus-table-cangjie
%defattr(-,root,root)
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

%package -n ibus-table-cantonese
Group: System/Internationalization
Summary: ibus-cantonese - table-based engine
Requires: ibus-table >= 1.3.0

%description -n ibus-table-cantonese
ibus-table-cantonese provides cantonese input method on IBus Table under IBus framework.

%files -n ibus-table-cantonese
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/cantonese.png
%{_datadir}/ibus-table/icons/cantonhk.png
%{_datadir}/ibus-table/icons/jyutping.png
%{_datadir}/ibus-table/tables/cantonese.db
%{_datadir}/ibus-table/tables/cantonhk.db
%{_datadir}/ibus-table/tables/jyutping.db

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --enable-extra-phrases
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT
