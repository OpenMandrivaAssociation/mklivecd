# $Id: mklivecd.spec.in,v 1.12 2003/10/04 10:03:28 jaco Exp $

%define name	mklivecd
%define version	0.5.9
%define release	%mkrel 0.13

%define Summary	Builds a LiveCD from an existing Mandriva Linux installation

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Boot and Init
URL:		http://livecd.berlios.de/
Source0:	%{name}-%{version}.tar.bz2
Patch3:     	mklivecd-0.5.9-no-more-hotplug.patch.bz2
Patch4:     	mklivecd-0.5.9-quiet-umount.patch.bz2
Patch5:     	mklivecd-0.5.9-keep-menu.patch.bz2
Patch7:     	mklivecd-0.5.9-quiet-mode.patch.bz2
Patch9:     	mklivecd-0.5.9-splash.patch.bz2
Requires:	busybox cloop-utils mkisofs drakxtools-newt
Requires:	squashfs-tools mediacheck syslinux zisofs-tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:	noarch

%description
%{Summary}

%prep
%setup -q -n %{name}
%patch3 -p0 -b .hotplug
# (tv) conflict with rc.sysinit:
%patch4 -p1 -b .umount
%patch5 -p0 -b .menu
%patch7 -p0 -b .quiet
%patch9 -p1 -b .splash

%build
# use 800x600 as default resolution like DrakX (some machines dislike 1024x768)
%make DEF_RESOLUTION=800x600 DEF_VGAMODE=788

%install
rm -rf %{buildroot}
# fix cdrom.ko lookup when building with kernel < 2.6.10-1mdk
perl -pi -e 's! drivers/cdrom/cdrom ! !' dist/mklivecd
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG FAQ README* TODO
%{_sbindir}/hwdetect
%{_sbindir}/mklivecd
%{_datadir}/mklivecd/

