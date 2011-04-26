Name:      ibus-table-chinese
Summary:   ibus-chinese - table-based engine
Epoch:     1
Version:   1.3.0.20101126
Release:   %mkrel 2
Group:     System/Internationalization
License:   GPLv3+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
Patch0:    ibus-table-chinese-1.3.0.20101126-out-of-source-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ibus-table-devel >= 1.3.0
BuildRequires: ibus-devel >= 1.3.9-5
BuildRequires: cmake
BuildArch:	noarch

%description
ibus-table-chinese provide the following input method tables for IBus-Table.

%package -n ibus-table-erbi
Group: System/Internationalization
Summary: ibus-erbi - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-erbi
ibus-table-erbi provides ErBi input method on IBus Table under IBus framework.

%post -n ibus-table-erbi
%post_ibus_register_engine erbi-qs zh_CN
%post_ibus_register_engine erbi zh_CN

%preun -n ibus-table-erbi
%preun_ibus_unregister_engine erbi-qs
%preun_ibus_unregister_engine erbi

%files -n ibus-table-erbi
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/erbi*
%{_datadir}/ibus-table/tables/erbi*.db

%package -n ibus-table-wu
Group: System/Internationalization
Summary: ibus-wu - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-wu
ibus-table-wu provides wu input method on IBus Table under IBus framework.

%post -n ibus-table-wu
%post_ibus_register_engine wu zh_CN

%preun -n ibus-table-wu
%preun_ibus_unregister_engine wu

%files -n ibus-table-wu
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/wu.png
%{_datadir}/ibus-table/tables/wu.db

%package -n ibus-table-wubi
Group: System/Internationalization
Summary: ibus-wubi - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-wubi
ibus-table-wubi provides wubi86 input method on IBus Table under IBus framework.

%post -n ibus-table-wubi
%post_ibus_register_engine wubi-haifeng86 zh_CN
%post_ibus_register_engine wubi-jidian86 zh_CN

%preun -n ibus-table-wubi
%preun_ibus_unregister_engine wubi-haifeng86
%preun_ibus_unregister_engine wubi-jidian86

%files -n ibus-table-wubi
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/wubi*86.svg
%{_datadir}/ibus-table/tables/wubi*86.db

%package -n ibus-table-yong
Group: System/Internationalization
Summary: ibus-yong - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-yong
ibus-table-yong provides yong input method on IBus Table under IBus framework.

%post -n ibus-table-yong
%post_ibus_register_engine yong zh_CN

%preun -n ibus-table-yong
%preun_ibus_unregister_engine yong

%files -n ibus-table-yong
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/yong*
%{_datadir}/ibus-table/tables/yong*.db

%package -n ibus-table-stroke5
Group: System/Internationalization
Summary: ibus-stroke5 - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-stroke5
ibus-table-stroke5 provides stroke5 input method on IBus Table under IBus framework.

%post -n ibus-table-stroke5
%post_ibus_register_engine stroke5 zh_TW

%preun -n ibus-table-stroke5
%preun_ibus_unregister_engine stroke5

%files -n ibus-table-stroke5
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/stroke5*
%{_datadir}/ibus-table/tables/stroke5*.db

%package -n ibus-table-cangjie
Group: System/Internationalization
Summary: ibus-cangjie - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2
Obsoletes: ibus-table-quick < 1.2.0.20100106

%description -n ibus-table-cangjie
ibus-table-cangjie provide CangJie input methods on IBus Table under IBus framework.

%post -n ibus-table-cangjie
%post_ibus_register_engine cangjie-big zh_TW
%post_ibus_register_engine cangjie3 zh_TW
%post_ibus_register_engine cangjie5 zh_TW
%post_ibus_register_engine easy-big zh_TW
%post_ibus_register_engine quick-classic zh_TW
%post_ibus_register_engine quick3 zh_TW
%post_ibus_register_engine quick5 zh_TW
%post_ibus_register_engine scj6 zh_TW

%preun -n ibus-table-cangjie
%preun_ibus_unregister_engine cangjie-big
%preun_ibus_unregister_engine cangjie3
%preun_ibus_unregister_engine cangjie5
%preun_ibus_unregister_engine easy-big
%preun_ibus_unregister_engine quick-classic
%preun_ibus_unregister_engine quick3
%preun_ibus_unregister_engine quick5
%preun_ibus_unregister_engine scj6

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
Requires(post,preun): GConf2

%description -n ibus-table-cantonese
ibus-table-cantonese provides cantonese input method on IBus Table under IBus framework.

%post -n ibus-table-cantonese
%post_ibus_register_engine cantonese zh_HK
%post_ibus_register_engine cantonhk zh_HK
%post_ibus_register_engine jyutping zh_HK

%preun -n ibus-table-cantonese
%preun_ibus_unregister_engine cantonese
%preun_ibus_unregister_engine cantonhk
%preun_ibus_unregister_engine jyutping

%files -n ibus-table-cantonese
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/cantonese.png
%{_datadir}/ibus-table/icons/cantonhk.png
%{_datadir}/ibus-table/icons/jyutping.png
%{_datadir}/ibus-table/tables/cantonese.db
%{_datadir}/ibus-table/tables/cantonhk.db
%{_datadir}/ibus-table/tables/jyutping.db

%package -n ibus-table-array30
Group: System/Internationalization
Summary: ibus-array30 - table-based engine
Requires: ibus-table >= 1.3.0
Requires(post,preun): GConf2

%description -n ibus-table-array30
ibus-table-array30 provides array30 input method on IBus Table under IBus framework.

%post -n ibus-table-array30
%post_ibus_register_engine array30 zh_TW
%post_ibus_register_engine array30-big zh_TW

%preun -n ibus-table-array30
%preun_ibus_unregister_engine array30
%preun_ibus_unregister_engine array30-big

%files -n ibus-table-array30
%defattr(-,root,root)
%{_datadir}/ibus-table/icons/array30-big.png
%{_datadir}/ibus-table/icons/array30.png
%{_datadir}/ibus-table/tables/array30-big.db
%{_datadir}/ibus-table/tables/array30.db

#---------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-Source
%patch0 -p0

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

rm -rf %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT
