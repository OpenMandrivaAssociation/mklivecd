%define fver	0.6.0-20071202

%define Summary	Builds a LiveCD from an existing Mandriva Linux installation

Summary:	%{Summary}
Name:		mklivecd
Version:	0.6.0.20071202
Release:	%{mkrel 1}
License:	GPLv2+
Group:		System/Configuration/Boot and Init
URL:		http://livecd.berlios.de/
Source0:	http://download.berlios.de/livecd/%{name}-%{fver}.tar.bz2
Patch3:     	mklivecd-0.6.0-20071202-no-more-hotplug.patch
Patch4:     	mklivecd-0.6.0-20071202-quiet-umount.patch
Patch7:     	mklivecd-0.5.9-quiet-mode.patch
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
%setup -q -n %{name}-%{fver}
%patch3 -p1 -b .hotplug
# (tv) conflict with rc.sysinit:
%patch4 -p1 -b .umount
%patch7 -p0 -b .quiet

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

