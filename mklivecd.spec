# the weird-looking versioning for snapshots is necessary, because we
# don't know when upstream will bump rootver and when it will do a new
# release but just bump releasedate - AdamW 2008/12

%define rootver		0.6.0
%define cvs		20081211
%define releasedate	1
%define ver		1
%define rel		4

%if %cvs
%define release		%mkrel 0.%{cvs}.%{rel}
%define version		%{rootver}.%{cvs}
%define distname	%{name}-%{cvs}.tar.lzma
%define dirname		%{name}
%else
%define release		%mkrel %{rel}
%define version		%{rootver}.%{releasedate}
%define distname	%{name}-%{rootver}-%{releasedate}.tar.bz2
%define dirname		%{name}-%{rootver}-%{releasedate}
%endif

%define Summary	Builds a LiveCD from an existing Mandriva Linux installation

Summary:	%{Summary}
Name:		mklivecd
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		System/Configuration/Boot and Init
URL:		https://livecd.berlios.de/
Source0:	http://download.berlios.de/livecd/%{distname}
Patch3:     	mklivecd-0.6.0-20071202-no-more-hotplug.patch
Patch4:     	mklivecd-0.6.0-20071202-quiet-umount.patch
Patch7:     	mklivecd-0.5.9-quiet-mode.patch
Patch8:		mklivecd-0.6.0-20071202-mandriva.patch
Requires:	busybox
Requires:	cloop-utils
Requires:	mkisofs
Requires:	drakxtools-newt
Requires:	squashfs-tools
Requires:	mediacheck
Requires:	syslinux
Requires:	zisofs-tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:	noarch

%description
%{Summary}.

%prep
%setup -q -n %{dirname}
%patch3 -p1 -b .hotplug
# (tv) conflict with rc.sysinit:
%patch4 -p1 -b .umount
%patch7 -p0 -b .quiet
%patch8 -p1 -b .mandriva

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG FAQ README* TODO
%{_sbindir}/hwdetect
%{_sbindir}/%{name}
%{_datadir}/%{name}



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0.20081211-0.20081211.4mdv2011.0
+ Revision: 620371
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0.20081211-0.20081211.3mdv2010.0
+ Revision: 440008
- rebuild

* Sat Dec 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0.20081211-0.20081211.2mdv2009.1
+ Revision: 313854
- fix a bit of the patch I screwed up

* Thu Dec 11 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0.20081211-0.20081211.1mdv2009.1
+ Revision: 313432
- add mandriva.patch from Simon Blandford to work with current Mandriva
- bump to current CVS snapshot

* Mon Dec 08 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0.20071202-1mdv2009.1
+ Revision: 312021
- drop a workaround for kernel 2.6.10
- upstream now uses our preferred default resolution so don't set it manually
- drop keep-menu.patch and splash.patch (merged upstream)
- rediff quiet-unmount.patch and make it do what the changelog claims it should
  (the original version actually just stopped the unmount happening at all, it
  didn't make it quiet)
- rediff no-more-hotplug.patch
- new license policy
- new version 0.6.0-20071202
- small cleanups

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.5.9-0.13mdv2009.0
+ Revision: 140954
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.5.9-0.13mdv2008.1
+ Revision: 130031
- kill re-definition of %%buildroot on Pixel's request
- import mklivecd


* Thu Feb 23 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.5.9-0.13mdk
- new snapshot (20060109)
- remove patches 1, 2 & 10 now that draklive supercedes mklivecd and package
  hwdetect again (#20977)
- drop patch 6 (i'm tired of maintaining patches adding hw support that
  upstream won't apply)
- ditto for patch 8

* Thu Oct 13 2005 Pascal Terjan <pterjan@mandriva.org> 0.5.9-0.12mdk
- patch 10: allow aulologin with something else than KDE (or disabling
  autologin).

* Fri Sep 09 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.5.9-0.11mdk
- requires zisofs-tools
- don't package hwdetect, harddrake is enabled at boot and does a better job
  (hwdetect just broke snd_intel8x0 for example) (blino)
- use 800x600 as default resolution like DrakX since some machines
  dislike 1024x768 (blino)
- patch 3: fix build w/o hotplug since it's no more mandatory
- patch 4: quiet umount of /proc
- patch 5: keep builded menus on live image
- patch 6:
  o handle more SATA controllers
  o add sata support for ahci/ata_piix in initrd as well (blino)
  o don't break scsi modules list with misplaced comments (blino)
  o don't try to use inexistent qlogicisp (blino)
- patch 7: let perl be quiet by default
- patch 8: don't break XKB and XDM
- patch 9: allow splash=silent and splash=verbose options
  (splash=yes didn't make much sense) (blino)

* Wed Jun 01 2005 Lenny Cartier <lenny@mandriva.com> 0.5.9-0.10mdk
- fix summary & desc (thx Zero_Dogg)

* Tue May 31 2005 Lenny Cartier <lenny@mandriva.com> 0.5.9-0.9mdk
- requires syslinux

* Tue Mar 22 2005 Nicolas L�cureuil <neoclust@mandrake.org> 0.5.9-0.8mdk
- rebuild

* Tue Mar 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5.9-0.7mdk
- update docs

* Tue Mar 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5.9-0.6mdk
- add another missing dependency; mediacheck
- update from cvs

* Tue Mar 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5.9-0.5mdk
- update url
- add missing dependency on squashfs-tools

* Thu Feb 10 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.9-0.4mdk
- 20050208 CVS snapshot (fix shell)

* Tue Feb 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.9-0.3mdk
- 20050208 CVS snapshot (sata update, sync with udev)
- fix cdrom now build into kernel core
- rediff patch 1
- merge patch 3 into patch 1

* Fri Dec 24 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.5.9-0.2mdk
- fix undefined variable

* Fri Dec 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.9-0.1mdk
- CVS snapshot (mdk10.x aware)
- kill useless patch 0
- patch 1: preconfigure keyboard, i18n, user, ... so that harddrake is able to
  autoconfigure everything
- patch 2: let harddrake service work

* Thu Jun 17 2004 Michael Scherer <misc@mandrake.org> 0.5.6-5mdk
- fix Summary
 
* Tue May 04 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.6-4mdk
- patch 0: fix deps killed by latest drakxtools

* Mon Dec 22 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.6-3mdk
- rebuild for new deps

* Wed Dec 03 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5.6-2mdk
- spec fixes
- fix unowned dir

* Mon Oct  6 2003 Jaco Greeff <jaco@linuxminicd.org> 0.5.6-1mdk
- version 0.5.6
- spec fixes by Buchan Milne <bgmilne@cae.co.za>

* Sat Sep 27 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.5.5-2mdk
- rebuild

* Thu Sep 25 2003 Jaco Greeff <jaco@linuxminicd.org> 0.5.5-1mdk
- version 0.5.5

* Wed Sep 24 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.5.4-2mdk
- spec fixes

* Tue Sep 23 2003 Jaco Greeff <jaco@linuxminicd.org> 0.5.4-1mdk
- version 0.5.4
- removed patch0, fixed upstream

* Mon Sep 22 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.5.3-1mdk
- initial import into contrib, based on spec file from Jaco Greeff
- fixed requires (mkisofs)
- temporary locale fix to correct calculate initrd size
- correct mdk group name
- some macroszification
