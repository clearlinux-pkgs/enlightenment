#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : enlightenment
Version  : 0.25.3
Release  : 17
URL      : https://download.enlightenment.org/rel/apps/enlightenment/enlightenment-0.25.3.tar.xz
Source0  : https://download.enlightenment.org/rel/apps/enlightenment/enlightenment-0.25.3.tar.xz
Summary  : Everything Module for Enlightenment
Group    : Development/Tools
License  : OFL-1.1
Requires: enlightenment-bin = %{version}-%{release}
Requires: enlightenment-data = %{version}-%{release}
Requires: enlightenment-filemap = %{version}-%{release}
Requires: enlightenment-lib = %{version}-%{release}
Requires: enlightenment-license = %{version}-%{release}
Requires: enlightenment-locales = %{version}-%{release}
Requires: enlightenment-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(eeze)
BuildRequires : pkgconfig(enlightenment)
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(xkeyboard-config)

%description
Enlightenment
-------------
Please report bugs and submit patches at https://phab.enlightenment.org

%package bin
Summary: bin components for the enlightenment package.
Group: Binaries
Requires: enlightenment-data = %{version}-%{release}
Requires: enlightenment-license = %{version}-%{release}
Requires: enlightenment-services = %{version}-%{release}
Requires: enlightenment-filemap = %{version}-%{release}

%description bin
bin components for the enlightenment package.


%package data
Summary: data components for the enlightenment package.
Group: Data

%description data
data components for the enlightenment package.


%package dev
Summary: dev components for the enlightenment package.
Group: Development
Requires: enlightenment-lib = %{version}-%{release}
Requires: enlightenment-bin = %{version}-%{release}
Requires: enlightenment-data = %{version}-%{release}
Provides: enlightenment-devel = %{version}-%{release}
Requires: enlightenment = %{version}-%{release}

%description dev
dev components for the enlightenment package.


%package filemap
Summary: filemap components for the enlightenment package.
Group: Default

%description filemap
filemap components for the enlightenment package.


%package lib
Summary: lib components for the enlightenment package.
Group: Libraries
Requires: enlightenment-data = %{version}-%{release}
Requires: enlightenment-license = %{version}-%{release}
Requires: enlightenment-filemap = %{version}-%{release}

%description lib
lib components for the enlightenment package.


%package license
Summary: license components for the enlightenment package.
Group: Default

%description license
license components for the enlightenment package.


%package locales
Summary: locales components for the enlightenment package.
Group: Default

%description locales
locales components for the enlightenment package.


%package services
Summary: services components for the enlightenment package.
Group: Systemd services

%description services
services components for the enlightenment package.


%prep
%setup -q -n enlightenment-0.25.3
cd %{_builddir}/enlightenment-0.25.3
pushd ..
cp -a enlightenment-0.25.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656712849
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/enlightenment
cp %{_builddir}/enlightenment-0.25.3/COPYING %{buildroot}/usr/share/package-licenses/enlightenment/ce9a4dfd1264bf1151044489c79f337217245a66
cp %{_builddir}/enlightenment-0.25.3/src/modules/wl_weekeyboard/themes/default/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/enlightenment/028166d82dc40a4d40716ea350a212c901956ade
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang enlightenment
## install_append content
chmod ug-s %{buildroot}/usr/lib64/enlightenment/modules/sysinfo/*/cpuclock_sysfs || :
chmod ug-s %{buildroot}/usr/lib64/enlightenment/modules/cpufreq/*/freqset  || :
chmod ug-s %{buildroot}/usr/lib64/enlightenment/utils/enlightenment_backlight  || :
chmod ug-s %{buildroot}/usr/lib64/enlightenment/utils/enlightenment_ckpasswd  || :
chmod ug-s %{buildroot}/usr/lib64/enlightenment/utils/enlightenment_sys  || :
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/enlightenment/modules/appmenu/e-module-appmenu.edj
/usr/lib64/enlightenment/modules/appmenu/module.desktop
/usr/lib64/enlightenment/modules/backlight/e-module-backlight.edj
/usr/lib64/enlightenment/modules/backlight/module.desktop
/usr/lib64/enlightenment/modules/battery/e-module-battery.edj
/usr/lib64/enlightenment/modules/battery/linux-gnu-x86_64-0.25.3/batget
/usr/lib64/enlightenment/modules/battery/module.desktop
/usr/lib64/enlightenment/modules/bluez5/e-module-bluez5.edj
/usr/lib64/enlightenment/modules/bluez5/module.desktop
/usr/lib64/enlightenment/modules/clock/e-module-clock.edj
/usr/lib64/enlightenment/modules/clock/module.desktop
/usr/lib64/enlightenment/modules/conf/e-module-conf.edj
/usr/lib64/enlightenment/modules/conf/module.desktop
/usr/lib64/enlightenment/modules/conf_applications/e-module-conf_applications.edj
/usr/lib64/enlightenment/modules/conf_applications/module.desktop
/usr/lib64/enlightenment/modules/conf_bindings/e-module-conf_bindings.edj
/usr/lib64/enlightenment/modules/conf_bindings/module.desktop
/usr/lib64/enlightenment/modules/conf_dialogs/e-module-conf_dialogs.edj
/usr/lib64/enlightenment/modules/conf_dialogs/module.desktop
/usr/lib64/enlightenment/modules/conf_display/e-module-conf_display.edj
/usr/lib64/enlightenment/modules/conf_display/module.desktop
/usr/lib64/enlightenment/modules/conf_interaction/e-module-conf_interaction.edj
/usr/lib64/enlightenment/modules/conf_interaction/module.desktop
/usr/lib64/enlightenment/modules/conf_intl/e-module-conf_intl.edj
/usr/lib64/enlightenment/modules/conf_intl/module.desktop
/usr/lib64/enlightenment/modules/conf_menus/e-module-conf_menus.edj
/usr/lib64/enlightenment/modules/conf_menus/module.desktop
/usr/lib64/enlightenment/modules/conf_paths/e-module-conf_paths.edj
/usr/lib64/enlightenment/modules/conf_paths/module.desktop
/usr/lib64/enlightenment/modules/conf_performance/e-module-conf_performance.edj
/usr/lib64/enlightenment/modules/conf_performance/module.desktop
/usr/lib64/enlightenment/modules/conf_randr/e-module-conf_randr.edj
/usr/lib64/enlightenment/modules/conf_randr/module.desktop
/usr/lib64/enlightenment/modules/conf_shelves/e-module-conf_shelves.edj
/usr/lib64/enlightenment/modules/conf_shelves/module.desktop
/usr/lib64/enlightenment/modules/conf_theme/e-module-conf_theme.edj
/usr/lib64/enlightenment/modules/conf_theme/module.desktop
/usr/lib64/enlightenment/modules/conf_window_manipulation/e-module-conf_window_manipulation.edj
/usr/lib64/enlightenment/modules/conf_window_manipulation/module.desktop
/usr/lib64/enlightenment/modules/conf_window_remembers/e-module-conf_window_remembers.edj
/usr/lib64/enlightenment/modules/conf_window_remembers/module.desktop
/usr/lib64/enlightenment/modules/connman/e-module-connman.edj
/usr/lib64/enlightenment/modules/connman/module.desktop
/usr/lib64/enlightenment/modules/cpufreq/e-module-cpufreq.edj
/usr/lib64/enlightenment/modules/cpufreq/module.desktop
/usr/lib64/enlightenment/modules/everything/e-module-everything-start.edj
/usr/lib64/enlightenment/modules/everything/e-module-everything.edj
/usr/lib64/enlightenment/modules/everything/module.desktop
/usr/lib64/enlightenment/modules/fileman/e-module-fileman.edj
/usr/lib64/enlightenment/modules/fileman/module.desktop
/usr/lib64/enlightenment/modules/fileman_opinfo/e-module-fileman_opinfo.edj
/usr/lib64/enlightenment/modules/fileman_opinfo/module.desktop
/usr/lib64/enlightenment/modules/gadman/e-module-gadman.edj
/usr/lib64/enlightenment/modules/gadman/module.desktop
/usr/lib64/enlightenment/modules/geolocation/e-module-geolocation.edj
/usr/lib64/enlightenment/modules/geolocation/module.desktop
/usr/lib64/enlightenment/modules/ibar/e-module-ibar.edj
/usr/lib64/enlightenment/modules/ibar/module.desktop
/usr/lib64/enlightenment/modules/ibox/e-module-ibox.edj
/usr/lib64/enlightenment/modules/ibox/module.desktop
/usr/lib64/enlightenment/modules/mixer/e-module-mixer.edj
/usr/lib64/enlightenment/modules/mixer/module.desktop
/usr/lib64/enlightenment/modules/mixer/sink-icons.txt
/usr/lib64/enlightenment/modules/msgbus/e-module-msgbus.edj
/usr/lib64/enlightenment/modules/msgbus/module.desktop
/usr/lib64/enlightenment/modules/music-control/e-module-music-control.edj
/usr/lib64/enlightenment/modules/music-control/module.desktop
/usr/lib64/enlightenment/modules/notification/e-module-notification.edj
/usr/lib64/enlightenment/modules/notification/module.desktop
/usr/lib64/enlightenment/modules/packagekit/e-module-packagekit.edj
/usr/lib64/enlightenment/modules/packagekit/module.desktop
/usr/lib64/enlightenment/modules/pager/e-module-pager.edj
/usr/lib64/enlightenment/modules/pager/module.desktop
/usr/lib64/enlightenment/modules/polkit/e-module-polkit.edj
/usr/lib64/enlightenment/modules/polkit/module.desktop
/usr/lib64/enlightenment/modules/procstats/e-module-procstats.edj
/usr/lib64/enlightenment/modules/procstats/module.desktop
/usr/lib64/enlightenment/modules/quickaccess/e-module-quickaccess.edj
/usr/lib64/enlightenment/modules/quickaccess/module.desktop
/usr/lib64/enlightenment/modules/shot/IndieFlower.ttf
/usr/lib64/enlightenment/modules/shot/Puk-Regular.ttf
/usr/lib64/enlightenment/modules/shot/Yantiq.ttf
/usr/lib64/enlightenment/modules/shot/e-module-shot.edj
/usr/lib64/enlightenment/modules/shot/intuitive.ttf
/usr/lib64/enlightenment/modules/shot/linux-gnu-x86_64-0.25.3/upload
/usr/lib64/enlightenment/modules/shot/module.desktop
/usr/lib64/enlightenment/modules/shot/shotedit.edj
/usr/lib64/enlightenment/modules/shot/shots.desktop
/usr/lib64/enlightenment/modules/start/e-module-start.edj
/usr/lib64/enlightenment/modules/start/module.desktop
/usr/lib64/enlightenment/modules/syscon/e-module-syscon.edj
/usr/lib64/enlightenment/modules/syscon/module.desktop
/usr/lib64/enlightenment/modules/systray/e-module-systray.edj
/usr/lib64/enlightenment/modules/systray/module.desktop
/usr/lib64/enlightenment/modules/tasks/e-module-tasks.edj
/usr/lib64/enlightenment/modules/tasks/module.desktop
/usr/lib64/enlightenment/modules/temperature/e-module-temperature.edj
/usr/lib64/enlightenment/modules/temperature/module.desktop
/usr/lib64/enlightenment/modules/tiling/e-module-tiling.edj
/usr/lib64/enlightenment/modules/tiling/module.desktop
/usr/lib64/enlightenment/modules/vkbd/dicts/English_US.dic
/usr/lib64/enlightenment/modules/vkbd/dicts/English_US_Small.dic
/usr/lib64/enlightenment/modules/vkbd/e-module-vkbd.edj
/usr/lib64/enlightenment/modules/vkbd/keyboards/Default.kbd
/usr/lib64/enlightenment/modules/vkbd/keyboards/Numbers.kbd
/usr/lib64/enlightenment/modules/vkbd/keyboards/Terminal.kbd
/usr/lib64/enlightenment/modules/vkbd/keyboards/alpha.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/backspace.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/down.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/enter.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/left.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/numeric.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/qwerty.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/right.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/shift.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/spanner.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/tab.png
/usr/lib64/enlightenment/modules/vkbd/keyboards/up.png
/usr/lib64/enlightenment/modules/vkbd/module.desktop
/usr/lib64/enlightenment/modules/vkbd/theme.edj
/usr/lib64/enlightenment/modules/winlist/e-module-winlist.edj
/usr/lib64/enlightenment/modules/winlist/module.desktop
/usr/lib64/enlightenment/modules/wizard/def-ibar.txt
/usr/lib64/enlightenment/modules/wizard/desktop/home.desktop
/usr/lib64/enlightenment/modules/wizard/desktop/root.desktop
/usr/lib64/enlightenment/modules/wizard/desktop/tmp.desktop
/usr/lib64/enlightenment/modules/xkbswitch/e-module-xkbswitch.edj
/usr/lib64/enlightenment/modules/xkbswitch/module.desktop
/usr/lib64/enlightenment/utils/enlightenment_alert
/usr/lib64/enlightenment/utils/enlightenment_ckpasswd
/usr/lib64/enlightenment/utils/enlightenment_elm_cfgtool
/usr/lib64/enlightenment/utils/enlightenment_fm
/usr/lib64/enlightenment/utils/enlightenment_fm_op
/usr/lib64/enlightenment/utils/enlightenment_sys
/usr/lib64/enlightenment/utils/enlightenment_system
/usr/lib64/enlightenment/utils/enlightenment_thumb
/usr/lib64/enlightenment/utils/enlightenment_wallpaper_gen

%files bin
%defattr(-,root,root,-)
/usr/bin/emixer
/usr/bin/enlightenment
/usr/bin/enlightenment_askpass
/usr/bin/enlightenment_filemanager
/usr/bin/enlightenment_fprint
/usr/bin/enlightenment_imc
/usr/bin/enlightenment_open
/usr/bin/enlightenment_paledit
/usr/bin/enlightenment_remote
/usr/bin/enlightenment_start
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/applications/emixer.desktop
/usr/share/applications/enlightenment_askpass.desktop
/usr/share/applications/enlightenment_filemanager.desktop
/usr/share/applications/enlightenment_fprint.desktop
/usr/share/applications/enlightenment_paledit.desktop
/usr/share/enlightenment/AUTHORS
/usr/share/enlightenment/COPYING
/usr/share/enlightenment/data/backgrounds/Bamboo.edj
/usr/share/enlightenment/data/backgrounds/Dunes.edj
/usr/share/enlightenment/data/backgrounds/Flat-Fan.edj
/usr/share/enlightenment/data/backgrounds/Flat-Stone-Pattern.edj
/usr/share/enlightenment/data/backgrounds/Foggy-Trees.edj
/usr/share/enlightenment/data/backgrounds/God-Rays.edj
/usr/share/enlightenment/data/backgrounds/Green-Maple.edj
/usr/share/enlightenment/data/backgrounds/Lichen-Branches.edj
/usr/share/enlightenment/data/backgrounds/Mountain.edj
/usr/share/enlightenment/data/backgrounds/Paper-Flower.edj
/usr/share/enlightenment/data/backgrounds/Peaks.edj
/usr/share/enlightenment/data/backgrounds/Red-Maple.edj
/usr/share/enlightenment/data/backgrounds/Sea-of-Lanterns.edj
/usr/share/enlightenment/data/backgrounds/Snow-Trees.edj
/usr/share/enlightenment/data/backgrounds/Spruce-Needles.edj
/usr/share/enlightenment/data/backgrounds/Squiggle-Dark.edj
/usr/share/enlightenment/data/backgrounds/Squiggle-Light.edj
/usr/share/enlightenment/data/backgrounds/Squiggle-Mid.edj
/usr/share/enlightenment/data/backgrounds/Squiggle.edj
/usr/share/enlightenment/data/backgrounds/Sunset-Clouds.edj
/usr/share/enlightenment/data/backgrounds/Sunset-Hills.edj
/usr/share/enlightenment/data/backgrounds/White-Flower.edj
/usr/share/enlightenment/data/backgrounds/Yellow-Flower.edj
/usr/share/enlightenment/data/config/default/e.cfg
/usr/share/enlightenment/data/config/default/e_bindings.cfg
/usr/share/enlightenment/data/config/profile.cfg
/usr/share/enlightenment/data/config/standard/e.cfg
/usr/share/enlightenment/data/config/standard/e_bindings.cfg
/usr/share/enlightenment/data/config/standard/enlightenment-standard.png
/usr/share/enlightenment/data/config/standard/module.battery.cfg
/usr/share/enlightenment/data/config/standard/module.conf.cfg
/usr/share/enlightenment/data/config/standard/module.cpufreq.cfg
/usr/share/enlightenment/data/config/standard/module.fileman.cfg
/usr/share/enlightenment/data/config/standard/module.ibar.cfg
/usr/share/enlightenment/data/config/standard/module.ibox.cfg
/usr/share/enlightenment/data/config/standard/module.pager.cfg
/usr/share/enlightenment/data/config/standard/module.temperature.cfg
/usr/share/enlightenment/data/config/standard/profile.desktop
/usr/share/enlightenment/data/config/tiling/e.cfg
/usr/share/enlightenment/data/config/tiling/e_bindings.cfg
/usr/share/enlightenment/data/config/tiling/enlightenment-tiling.png
/usr/share/enlightenment/data/config/tiling/module.battery.cfg
/usr/share/enlightenment/data/config/tiling/module.conf.cfg
/usr/share/enlightenment/data/config/tiling/module.cpufreq.cfg
/usr/share/enlightenment/data/config/tiling/module.fileman.cfg
/usr/share/enlightenment/data/config/tiling/module.ibar.cfg
/usr/share/enlightenment/data/config/tiling/module.ibox.cfg
/usr/share/enlightenment/data/config/tiling/module.pager.cfg
/usr/share/enlightenment/data/config/tiling/module.temperature.cfg
/usr/share/enlightenment/data/config/tiling/module.tiling.cfg
/usr/share/enlightenment/data/config/tiling/profile.desktop
/usr/share/enlightenment/data/favorites/.order
/usr/share/enlightenment/data/favorites/desktop.desktop
/usr/share/enlightenment/data/favorites/home.desktop
/usr/share/enlightenment/data/favorites/root.desktop
/usr/share/enlightenment/data/favorites/tmp.desktop
/usr/share/enlightenment/data/flags/ad_flag.png
/usr/share/enlightenment/data/flags/af_flag.png
/usr/share/enlightenment/data/flags/al_flag.png
/usr/share/enlightenment/data/flags/am_flag.png
/usr/share/enlightenment/data/flags/ar_flag.png
/usr/share/enlightenment/data/flags/ara_flag.png
/usr/share/enlightenment/data/flags/at_flag.png
/usr/share/enlightenment/data/flags/az_flag.png
/usr/share/enlightenment/data/flags/ba_flag.png
/usr/share/enlightenment/data/flags/bd_flag.png
/usr/share/enlightenment/data/flags/be_flag.png
/usr/share/enlightenment/data/flags/bg_flag.png
/usr/share/enlightenment/data/flags/br_flag.png
/usr/share/enlightenment/data/flags/brai_flag.png
/usr/share/enlightenment/data/flags/bt_flag.png
/usr/share/enlightenment/data/flags/bw_flag.png
/usr/share/enlightenment/data/flags/by_flag.png
/usr/share/enlightenment/data/flags/ca_flag.png
/usr/share/enlightenment/data/flags/cat_flag.png
/usr/share/enlightenment/data/flags/cd_flag.png
/usr/share/enlightenment/data/flags/ch_flag.png
/usr/share/enlightenment/data/flags/cm_flag.png
/usr/share/enlightenment/data/flags/cn_flag.png
/usr/share/enlightenment/data/flags/cz_flag.png
/usr/share/enlightenment/data/flags/de_flag.png
/usr/share/enlightenment/data/flags/dk_flag.png
/usr/share/enlightenment/data/flags/ee_flag.png
/usr/share/enlightenment/data/flags/epo_flag.png
/usr/share/enlightenment/data/flags/es_flag.png
/usr/share/enlightenment/data/flags/et_flag.png
/usr/share/enlightenment/data/flags/fi_flag.png
/usr/share/enlightenment/data/flags/fo_flag.png
/usr/share/enlightenment/data/flags/fr_flag.png
/usr/share/enlightenment/data/flags/gb_flag.png
/usr/share/enlightenment/data/flags/ge_flag.png
/usr/share/enlightenment/data/flags/gh_flag.png
/usr/share/enlightenment/data/flags/gn_flag.png
/usr/share/enlightenment/data/flags/gr_flag.png
/usr/share/enlightenment/data/flags/hr_flag.png
/usr/share/enlightenment/data/flags/hu_flag.png
/usr/share/enlightenment/data/flags/ie_flag.png
/usr/share/enlightenment/data/flags/il_flag.png
/usr/share/enlightenment/data/flags/in_flag.png
/usr/share/enlightenment/data/flags/iq_flag.png
/usr/share/enlightenment/data/flags/ir_flag.png
/usr/share/enlightenment/data/flags/is_flag.png
/usr/share/enlightenment/data/flags/it_flag.png
/usr/share/enlightenment/data/flags/jp_flag.png
/usr/share/enlightenment/data/flags/ke_flag.png
/usr/share/enlightenment/data/flags/kg_flag.png
/usr/share/enlightenment/data/flags/kh_flag.png
/usr/share/enlightenment/data/flags/kr_flag.png
/usr/share/enlightenment/data/flags/ku_flag.png
/usr/share/enlightenment/data/flags/kz_flag.png
/usr/share/enlightenment/data/flags/la_flag.png
/usr/share/enlightenment/data/flags/lang-system.png
/usr/share/enlightenment/data/flags/latam_flag.png
/usr/share/enlightenment/data/flags/lk_flag.png
/usr/share/enlightenment/data/flags/lt_flag.png
/usr/share/enlightenment/data/flags/lv_flag.png
/usr/share/enlightenment/data/flags/ma_flag.png
/usr/share/enlightenment/data/flags/mao_flag.png
/usr/share/enlightenment/data/flags/md_flag.png
/usr/share/enlightenment/data/flags/me_flag.png
/usr/share/enlightenment/data/flags/mk_flag.png
/usr/share/enlightenment/data/flags/ml_flag.png
/usr/share/enlightenment/data/flags/mm_flag.png
/usr/share/enlightenment/data/flags/mn_flag.png
/usr/share/enlightenment/data/flags/mt_flag.png
/usr/share/enlightenment/data/flags/mv_flag.png
/usr/share/enlightenment/data/flags/my_flag.png
/usr/share/enlightenment/data/flags/ng_flag.png
/usr/share/enlightenment/data/flags/nl_flag.png
/usr/share/enlightenment/data/flags/no_flag.png
/usr/share/enlightenment/data/flags/np_flag.png
/usr/share/enlightenment/data/flags/ph_flag.png
/usr/share/enlightenment/data/flags/pk_flag.png
/usr/share/enlightenment/data/flags/pl_flag.png
/usr/share/enlightenment/data/flags/pt_flag.png
/usr/share/enlightenment/data/flags/ro_flag.png
/usr/share/enlightenment/data/flags/rs_flag.png
/usr/share/enlightenment/data/flags/ru_flag.png
/usr/share/enlightenment/data/flags/se_flag.png
/usr/share/enlightenment/data/flags/si_flag.png
/usr/share/enlightenment/data/flags/sk_flag.png
/usr/share/enlightenment/data/flags/sn_flag.png
/usr/share/enlightenment/data/flags/sy_flag.png
/usr/share/enlightenment/data/flags/th_flag.png
/usr/share/enlightenment/data/flags/tj_flag.png
/usr/share/enlightenment/data/flags/tm_flag.png
/usr/share/enlightenment/data/flags/tr_flag.png
/usr/share/enlightenment/data/flags/tw_flag.png
/usr/share/enlightenment/data/flags/tz_flag.png
/usr/share/enlightenment/data/flags/ua_flag.png
/usr/share/enlightenment/data/flags/unknown_flag.png
/usr/share/enlightenment/data/flags/us_flag.png
/usr/share/enlightenment/data/flags/uz_flag.png
/usr/share/enlightenment/data/flags/vn_flag.png
/usr/share/enlightenment/data/flags/za_flag.png
/usr/share/enlightenment/data/fonts/Topaz_a500_v1.0.ttf
/usr/share/enlightenment/data/icons/audio_player.png
/usr/share/enlightenment/data/icons/audio_player2.png
/usr/share/enlightenment/data/icons/image_viewer.png
/usr/share/enlightenment/data/icons/mail_client.png
/usr/share/enlightenment/data/icons/text_editor.png
/usr/share/enlightenment/data/icons/video_player.png
/usr/share/enlightenment/data/icons/web_browser.png
/usr/share/enlightenment/data/icons/xterm.png
/usr/share/enlightenment/data/images/enlightenment.png
/usr/share/enlightenment/data/images/test.edj
/usr/share/enlightenment/data/images/test.jpg
/usr/share/enlightenment/data/images/test.png
/usr/share/enlightenment/data/images/test.svg
/usr/share/enlightenment/data/input_methods/fcitx.imc
/usr/share/enlightenment/data/input_methods/gcin.imc
/usr/share/enlightenment/data/input_methods/hime.imc
/usr/share/enlightenment/data/input_methods/ibus.imc
/usr/share/enlightenment/data/input_methods/iiimf.imc
/usr/share/enlightenment/data/input_methods/scim.imc
/usr/share/enlightenment/data/input_methods/uim.imc
/usr/share/enlightenment/doc/FDO.txt
/usr/share/enlightenment/doc/cache.txt
/usr/share/enlightenment/doc/documentation.html
/usr/share/enlightenment/doc/enlightenment.png
/usr/share/enlightenment/doc/illume2.html
/usr/share/enlightenment/doc/illume2.png
/usr/share/enlightenment/themes/enlightenment_fprint.edj
/usr/share/icons/hicolor/128x128/apps/emixer.png
/usr/share/icons/hicolor/128x128/apps/enlightenment_fprint.png
/usr/share/icons/hicolor/128x128/apps/enlightenment_paledit.png
/usr/share/icons/hicolor/512x512/apps/enlightenment.png
/usr/share/icons/hicolor/512x512/apps/enlightenment_badge-symbolic.png
/usr/share/icons/hicolor/512x512/places/enlightenment.png
/usr/share/icons/hicolor/512x512/places/enlightenment_badge-symbolic.png
/usr/share/icons/hicolor/scalable/apps/enlightenment.svg
/usr/share/icons/hicolor/scalable/apps/enlightenment_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/enlightenment.svg
/usr/share/icons/hicolor/scalable/places/enlightenment_badge-symbolic.svg
/usr/share/pixmaps/enlightenment-askpass.png
/usr/share/xsessions/enlightenment.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/enlightenment/config.h
/usr/include/enlightenment/e.h
/usr/include/enlightenment/e_Efx.h
/usr/include/enlightenment/e_about.h
/usr/include/enlightenment/e_acpi.h
/usr/include/enlightenment/e_actions.h
/usr/include/enlightenment/e_alert.h
/usr/include/enlightenment/e_atoms.h
/usr/include/enlightenment/e_auth.h
/usr/include/enlightenment/e_backlight.h
/usr/include/enlightenment/e_bg.h
/usr/include/enlightenment/e_bindings.h
/usr/include/enlightenment/e_client.h
/usr/include/enlightenment/e_client.x
/usr/include/enlightenment/e_client_volume.h
/usr/include/enlightenment/e_color.h
/usr/include/enlightenment/e_color_dialog.h
/usr/include/enlightenment/e_comp.h
/usr/include/enlightenment/e_comp_canvas.h
/usr/include/enlightenment/e_comp_cfdata.h
/usr/include/enlightenment/e_comp_object.h
/usr/include/enlightenment/e_comp_x.h
/usr/include/enlightenment/e_comp_x_devices.h
/usr/include/enlightenment/e_comp_x_randr.h
/usr/include/enlightenment/e_config.h
/usr/include/enlightenment/e_config_data.h
/usr/include/enlightenment/e_config_dialog.h
/usr/include/enlightenment/e_configure.h
/usr/include/enlightenment/e_confirm_dialog.h
/usr/include/enlightenment/e_datastore.h
/usr/include/enlightenment/e_dbusmenu.h
/usr/include/enlightenment/e_desk.h
/usr/include/enlightenment/e_deskenv.h
/usr/include/enlightenment/e_desklock.h
/usr/include/enlightenment/e_deskmirror.h
/usr/include/enlightenment/e_desktop_editor.h
/usr/include/enlightenment/e_dialog.h
/usr/include/enlightenment/e_dnd.h
/usr/include/enlightenment/e_dpms.h
/usr/include/enlightenment/e_entry_dialog.h
/usr/include/enlightenment/e_env.h
/usr/include/enlightenment/e_error.h
/usr/include/enlightenment/e_exec.h
/usr/include/enlightenment/e_exehist.h
/usr/include/enlightenment/e_filereg.h
/usr/include/enlightenment/e_flowlayout.h
/usr/include/enlightenment/e_fm.h
/usr/include/enlightenment/e_fm_custom.h
/usr/include/enlightenment/e_fm_device.h
/usr/include/enlightenment/e_fm_mime.h
/usr/include/enlightenment/e_fm_op.h
/usr/include/enlightenment/e_fm_op_registry.h
/usr/include/enlightenment/e_fm_prop.h
/usr/include/enlightenment/e_fm_shared_codec.h
/usr/include/enlightenment/e_fm_shared_device.h
/usr/include/enlightenment/e_fm_shared_types.h
/usr/include/enlightenment/e_focus.h
/usr/include/enlightenment/e_font.h
/usr/include/enlightenment/e_gadcon.h
/usr/include/enlightenment/e_gadcon_popup.h
/usr/include/enlightenment/e_gesture.h
/usr/include/enlightenment/e_grab_dialog.h
/usr/include/enlightenment/e_grabinput.h
/usr/include/enlightenment/e_hints.h
/usr/include/enlightenment/e_icon.h
/usr/include/enlightenment/e_ilist.h
/usr/include/enlightenment/e_import_config_dialog.h
/usr/include/enlightenment/e_import_dialog.h
/usr/include/enlightenment/e_includes.h
/usr/include/enlightenment/e_init.h
/usr/include/enlightenment/e_int_client_locks.h
/usr/include/enlightenment/e_int_client_menu.h
/usr/include/enlightenment/e_int_client_prop.h
/usr/include/enlightenment/e_int_client_remember.h
/usr/include/enlightenment/e_int_config_modules.h
/usr/include/enlightenment/e_int_gadcon_config.h
/usr/include/enlightenment/e_int_menus.h
/usr/include/enlightenment/e_int_shelf_config.h
/usr/include/enlightenment/e_int_toolbar_config.h
/usr/include/enlightenment/e_intl.h
/usr/include/enlightenment/e_intl_data.h
/usr/include/enlightenment/e_ipc.h
/usr/include/enlightenment/e_ipc_codec.h
/usr/include/enlightenment/e_layout.h
/usr/include/enlightenment/e_livethumb.h
/usr/include/enlightenment/e_log.h
/usr/include/enlightenment/e_macros.h
/usr/include/enlightenment/e_maximize.h
/usr/include/enlightenment/e_menu.h
/usr/include/enlightenment/e_mmx.h
/usr/include/enlightenment/e_module.h
/usr/include/enlightenment/e_mouse.h
/usr/include/enlightenment/e_moveresize.h
/usr/include/enlightenment/e_msg.h
/usr/include/enlightenment/e_msgbus.h
/usr/include/enlightenment/e_notification.h
/usr/include/enlightenment/e_obj_dialog.h
/usr/include/enlightenment/e_object.h
/usr/include/enlightenment/e_order.h
/usr/include/enlightenment/e_pan.h
/usr/include/enlightenment/e_path.h
/usr/include/enlightenment/e_pixmap.h
/usr/include/enlightenment/e_place.h
/usr/include/enlightenment/e_pointer.h
/usr/include/enlightenment/e_powersave.h
/usr/include/enlightenment/e_prefix.h
/usr/include/enlightenment/e_randr2.h
/usr/include/enlightenment/e_remember.h
/usr/include/enlightenment/e_resist.h
/usr/include/enlightenment/e_scale.h
/usr/include/enlightenment/e_screensaver.h
/usr/include/enlightenment/e_scrollframe.h
/usr/include/enlightenment/e_sha1.h
/usr/include/enlightenment/e_shelf.h
/usr/include/enlightenment/e_signals.h
/usr/include/enlightenment/e_slidecore.h
/usr/include/enlightenment/e_slider.h
/usr/include/enlightenment/e_slidesel.h
/usr/include/enlightenment/e_spectrum.h
/usr/include/enlightenment/e_startup.h
/usr/include/enlightenment/e_sys.h
/usr/include/enlightenment/e_system.h
/usr/include/enlightenment/e_test.h
/usr/include/enlightenment/e_theme.h
/usr/include/enlightenment/e_theme_about.h
/usr/include/enlightenment/e_thumb.h
/usr/include/enlightenment/e_toolbar.h
/usr/include/enlightenment/e_update.h
/usr/include/enlightenment/e_user.h
/usr/include/enlightenment/e_utils.h
/usr/include/enlightenment/e_video.h
/usr/include/enlightenment/e_watchdog.h
/usr/include/enlightenment/e_widget.h
/usr/include/enlightenment/e_widget_aspect.h
/usr/include/enlightenment/e_widget_bgpreview.h
/usr/include/enlightenment/e_widget_button.h
/usr/include/enlightenment/e_widget_check.h
/usr/include/enlightenment/e_widget_color_well.h
/usr/include/enlightenment/e_widget_config_list.h
/usr/include/enlightenment/e_widget_entry.h
/usr/include/enlightenment/e_widget_filepreview.h
/usr/include/enlightenment/e_widget_flist.h
/usr/include/enlightenment/e_widget_font_preview.h
/usr/include/enlightenment/e_widget_framelist.h
/usr/include/enlightenment/e_widget_frametable.h
/usr/include/enlightenment/e_widget_fsel.h
/usr/include/enlightenment/e_widget_ilist.h
/usr/include/enlightenment/e_widget_image.h
/usr/include/enlightenment/e_widget_label.h
/usr/include/enlightenment/e_widget_list.h
/usr/include/enlightenment/e_widget_preview.h
/usr/include/enlightenment/e_widget_radio.h
/usr/include/enlightenment/e_widget_scrollframe.h
/usr/include/enlightenment/e_widget_slider.h
/usr/include/enlightenment/e_widget_spectrum.h
/usr/include/enlightenment/e_widget_table.h
/usr/include/enlightenment/e_widget_textblock.h
/usr/include/enlightenment/e_widget_toolbar.h
/usr/include/enlightenment/e_widget_toolbook.h
/usr/include/enlightenment/e_win.h
/usr/include/enlightenment/e_xinerama.h
/usr/include/enlightenment/e_xkb.h
/usr/include/enlightenment/e_xsettings.h
/usr/include/enlightenment/e_zone.h
/usr/include/enlightenment/e_zoomap.h
/usr/include/enlightenment/evry_api.h
/usr/include/enlightenment/evry_types.h
/usr/lib64/pkgconfig/enlightenment.pc
/usr/lib64/pkgconfig/everything.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-enlightenment

%files lib
%defattr(-,root,root,-)
/usr/lib64/enlightenment/modules/appmenu/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/backlight/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/battery/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/bluez5/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/clock/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_applications/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_bindings/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_dialogs/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_display/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_interaction/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_intl/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_menus/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_paths/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_performance/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_randr/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_shelves/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_theme/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_window_manipulation/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/conf_window_remembers/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/connman/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/cpufreq/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/everything/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/fileman/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/fileman_opinfo/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/gadman/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/geolocation/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/ibar/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/ibox/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/lokker/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/mixer/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/msgbus/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/music-control/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/notification/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/packagekit/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/pager/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/polkit/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/procstats/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/quickaccess/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/shot/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/start/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/syscon/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/systray/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/tasks/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/temperature/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/tiling/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/vkbd/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/winlist/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/module.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_000.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_010.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_011.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_020.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_030.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_040.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_050.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_060.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_070.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_080.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_090.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_100.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_110.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_115.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_120.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_130.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_150.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_160.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_170.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_180.so
/usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-0.25.3/page_200.so
/usr/lib64/enlightenment/modules/xkbswitch/linux-gnu-x86_64-0.25.3/module.so
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/enlightenment/028166d82dc40a4d40716ea350a212c901956ade
/usr/share/package-licenses/enlightenment/ce9a4dfd1264bf1151044489c79f337217245a66

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/enlightenment.service

%files locales -f enlightenment.lang
%defattr(-,root,root,-)

