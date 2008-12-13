# the weird-looking versioning for snapshots is necessary, because we
# don't know when upstream will bump rootver and when it will do a new
# release but just bump releasedate - AdamW 2008/12

%define rootver		0.6.0
%define cvs		20081211
%define releasedate	0
%define ver		1
%define rel		2

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
URL:		http://livecd.berlios.de/
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

