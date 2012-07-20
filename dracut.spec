%define dracutlibdir %{_prefix}/lib/dracut

# Variables must be defined
%define with_nbd                1

# nbd in Fedora only
%if 0%{?rhel} >= 6
%define with_nbd 0
%endif

Name: dracut
Version: 018
Release: 95.git20120720%{?dist}

Summary: Initramfs generator using udev
%if 0%{?fedora} || 0%{?rhel}
Group: System Environment/Base
%endif
%if 0%{?suse_version}
Group: System/Base
%endif
License: GPLv2+
URL: https://dracut.wiki.kernel.org/
# Source can be generated by
# http://git.kernel.org/?p=boot/dracut/dracut.git;a=snapshot;h=%{version};sf=tgz
Source0: http://www.kernel.org/pub/linux/utils/boot/dracut/dracut-%{version}.tar.bz2
Patch1: 0001-dracut-lib-add-str_ends-to-go-along-with-str_starts.patch
Patch2: 0002-run-setup_net-at-start-of-initqueue-online-hook.patch
Patch3: 0003-network-add-save_netinfo-fix-problems-with-nfs-NM-ta.patch
Patch4: 0004-Make-splitsep-work-as-documented-with-less-vars-than.patch
Patch5: 0005-shutdown-use-emergency_shell-from-dracut-lib.patch
Patch6: 0006-rootfs-block-avoid-remount-when-options-don-t-change.patch
Patch7: 0007-Debian-multiarch-support.patch
Patch8: 0008-dracut.sh-log-installed-modules-to-initdir-lib-dracu.patch
Patch9: 0009-lvm-disable-lvmetad.patch
Patch10: 0010-udev-rules-remove-01-ignore.rules.patch
Patch11: 0011-lsinitrd-support-symlinks.patch
Patch12: 0012-dracut.cmdline.7.asc-document-resume-option.patch
Patch13: 0013-dracut.spec-do-not-include-IMA-and-selinux-modules-w.patch
Patch14: 0014-Do-not-run-plymouth-hook-if-the-binary-is-missing.patch
Patch15: 0015-man-Fix-add-fstab-option-in-man-page.patch
Patch16: 0016-base-init.sh-mount-tmpfs-with-strictatime.patch
Patch17: 0017-99shutdown-shutdown.sh-export-PATH.patch
Patch18: 0018-Makefile-do-not-install-systemd-service-in-reboot.patch
Patch19: 0019-network-module-setup.sh-include-all-kernel-drivers-n.patch
Patch20: 0020-add-pre-pivot-cleanup-hook.patch
Patch21: 0021-move-cleanup-scripts-to-pre-pivot-cleanup-hook.patch
Patch22: 0022-network-parse-ip-opts.sh-remove-check-for-netroot.patch
Patch23: 0023-ifcfg-write-DNS1-.-for-nameserver-args-RHBZ-815369.patch
Patch24: 0024-url-lib-don-t-add-existing-handlers-multiple-times.patch
Patch25: 0025-url-lib-don-t-use-progress-bar-if-TERM-dumb-RHBZ-814.patch
Patch26: 0026-iscsi-module-setup.sh-fix-host-only-mount-checks.patch
Patch27: 0027-multipath-module-setup.sh-fix-host-only-mount-checks.patch
Patch28: 0028-fix-_getcmdline-arg-duplicating-bug-with-etc-cmdline.patch
Patch29: 0029-ifcfg-fix-resolv.conf.patch
Patch30: 0030-TEST-15-BTRFSRAID-add-one-more-partition-to-the-btrf.patch
Patch31: 0031-ifcfg-write-ifcfg.sh-use-PREFIX-for-prefix-netmask-f.patch
Patch32: 0032-Fail-to-boot-if-mediacheck-fails-817419.patch
Patch33: 0033-ifcfg-write-ifcfg.sh-add-s390-specific-configuration.patch
Patch34: 0034-Makefile-call-git2spec.pl-with-LANG-C.patch
Patch35: 0035-ARM-make-sure-that-we-get-the-storage-modules-into-t.patch
Patch36: 0036-Use-the-right-argument-for-dasd-module-options.patch
Patch37: 0037-Translate-dasd-arg-contents-into-proper-dasd.conf.patch
Patch38: 0038-Normalize-dasd-argument-content-for-dasd.conf.patch
Patch39: 0039-ifcfg-write-ifcfg.sh-fixed-IFS-resetting.patch
Patch40: 0040-Relax-the-rules-for-kdump-we-don-t-specify-netroot-i.patch
Patch41: 0041-url-lib-url-lib.sh-disable-curl-progress-bar.patch
Patch42: 0042-network-ifup.sh-do-not-default-to-dhcp-for-interface.patch
Patch43: 0043-network-do-not-arping-with-qeth-layer3-interfaces.patch
Patch44: 0044-dracut-shutdown.service-do-not-unpack-old-initramfs-.patch
Patch45: 0045-crypt-add-rd.luks.allow-discards-and-honor-options-i.patch
Patch46: 0046-dasd_mod-parse-dasd-mod.sh-fixed-dasd_mod-param-gene.patch
Patch47: 0047-fix-return-value-of-some-installkernel-functions.patch
Patch48: 0048-dracut.sh-do-not-rely-on-the-presence-of-lib64-check.patch
Patch49: 0049-Don-t-set-an-already-set-attribute-826357.patch
Patch50: 0050-add-filesystem-options-to-fsck_single.patch
Patch51: 0051-dasd_mod-change-rd.dasd-to-dasd_mod-kernel-parameter.patch
Patch52: 0052-dracut.spec-remove-typo-from-BuildRequires-for-suse.patch
Patch53: 0053-kernel-modules-module-setup.sh-include-omapdrm-in-th.patch
Patch54: 0054-network-ifup.sh-default-to-dhcp-for-BOOTIF.patch
Patch55: 0055-Revert-network-ifup.sh-default-to-dhcp-for-BOOTIF.patch
Patch56: 0056-Revert-network-ifup.sh-do-not-default-to-dhcp-for-in.patch
Patch57: 0057-resolve-conflict-between-cms-network-rules-and-defau.patch
Patch58: 0058-Add-vlan-support-in-network-module.patch
Patch59: 0059-Add-doc-for-vlan-cmdline.patch
Patch60: 0060-Add-doc-for-bond-cmdline.patch
Patch61: 0061-Add-doc-for-birdge-cmdline.patch
Patch62: 0062-Handle-multiple-underlying-devices-of-a-bridge.patch
Patch63: 0063-url-lib-url-lib.sh-use-silent-mode-for-curl-if-TERM-.patch
Patch64: 0064-dracut-functions-fixed-return-status-of-instmods.patch
Patch65: 0065-network-support-vlan-tagged-bonding.patch
Patch66: 0066-dracut-shutdown.service-fixed-ordering-to-be-before-.patch
Patch67: 0067-terminfo-module-setup.sh-speedup-install-of-all-term.patch
Patch68: 0068-network-module-setup.sh-fixed-installkernel-return-c.patch
Patch69: 0069-iscsi-module-setup.sh-speedup-installkernel.patch
Patch70: 0070-fs-lib-fs-lib.sh-removed-test-mounting-of-btrfs-and-.patch
Patch71: 0071-i18n-module-setup.sh-install_all_kbd-speedup-install.patch
Patch72: 0072-no-more-mknod-in-the-initramfs.patch
Patch73: 0073-dracut.sh-precopy-some-essential-device-nodes.patch
Patch74: 0074-dracut.sh-mkdir-initdir-lib-dracut.patch
Patch75: 0075-multipath-module-setup.sh-installkernel-fix-return-c.patch
Patch76: 0076-dracut.sh-do-not-copy-devices-nodes-mknod-them.patch
Patch77: 0077-i18n-module-setup.sh-do-not-install-systemd-vconsole.patch
Patch78: 0078-network-ifname-genrules.sh-no-rule-to-rename-other-i.patch
Patch79: 0079-mdraid-md-shutdown.sh-wait-until-md-devices-are-clea.patch
Patch80: 0080-fips-module-setup.sh-s-aes-xts-xts.patch
Patch81: 0081-fips-change-module-list.patch
Patch82: 0082-fips-fixed-module-list.patch
Patch83: 0083-Fix-fips-module-list.patch
Patch84: 0084-98usrmount-depend-on-fs-lib.patch
Patch85: 0085-man-pages-hostonly-mode-generates-host-specific-conf.patch
Patch86: 0086-Fixed-BOOTIF-for-converting-mac-addr-to-lowercase.patch
Patch87: 0087-modules.d-get-rid-of-tr.patch
Patch88: 0088-dracut-functions.sh-set-LC_ALL-C-to-get-correct-pars.patch
Patch89: 0089-resume-move-resume-process-to-initqueue.patch
Patch90: 0090-kernel-modules-module-setup.sh-also-install-lib-modp.patch
Patch91: 0091-nfs-install-modprobe-config-file.patch
Patch92: 0092-udev-rules-module-setup.sh-cope-with-systemd-udevd.patch
Patch93: 0093-Makefile-set-LC_MESSAGES-C-.-not-LANG.patch
Patch94: 0094-resume-move-resume-in-the-initqueue-finished-hook.patch


BuildArch: noarch
BuildRequires: dash bash git

%if 0%{?fedora} || 0%{?rhel}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif
%if 0%{?suse_version}
BuildRoot: %{_tmppath}/%{name}-%{version}-build
%endif

%if 0%{?fedora} || 0%{?rhel}
BuildRequires: docbook-style-xsl docbook-dtds libxslt
%endif

%if 0%{?suse_version}
BuildRequires: docbook-xsl-stylesheets libxslt
%endif

BuildRequires: asciidoc

%if 0%{?fedora} > 12 || 0%{?rhel}
# no "provides", because dracut does not offer
# all functionality of the obsoleted packages
Obsoletes: mkinitrd <= 6.0.93
Obsoletes: mkinitrd-devel <= 6.0.93
Obsoletes: nash <= 6.0.93
Obsoletes: libbdevid-python <= 6.0.93
%endif

%if 0%{?fedora} > 16 || 0%{?rhel} > 6
BuildRequires: systemd-units
%endif

%if 0%{?suse_version} > 9999
Obsoletes: mkinitrd < 2.6.1
Provides: mkinitrd = 2.6.1
%endif

Obsoletes: dracut-kernel < 005
Provides:  dracut-kernel = %{version}-%{release}

Requires: bash
Requires: coreutils
Requires: cpio
Requires: filesystem >= 2.1.0
Requires: findutils
Requires: grep
Requires: hardlink
Requires: gzip xz
Requires: module-init-tools >= 3.7-9
Requires: sed
Requires: udev > 166
%if 0%{?fedora} || 0%{?rhel} > 6
Requires: util-linux >= 2.21
%else
Requires: util-linux-ng >= 2.21
%endif

%if 0%{?fedora} || 0%{?rhel} > 6
Conflicts: initscripts < 8.63-1
Conflicts: plymouth < 0.8.0-0.2009.29.09.19.1
%endif

%description
Dracut contains tools to create a bootable initramfs for 2.6 Linux kernels.
Unlike existing implementations, dracut does hard-code as little as possible
into the initramfs. Dracut contains various modules which are driven by the
event-based udev. Having root on MD, DM, LVM2, LUKS is supported as well as
NFS, iSCSI, NBD, FCoE with the dracut-network package.

%package network
Summary: Dracut modules to build a dracut initramfs with network support
Requires: %{name} = %{version}-%{release}
Obsoletes: dracut-generic < 008
Provides:  dracut-generic = %{version}-%{release}

%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

%if 0%{?fedora} || 0%{?rhel} >= 6
%package fips
Summary: Dracut modules to build a dracut initramfs with an integrity check
Requires: %{name} = %{version}-%{release}
Requires: hmaccalc
%if 0%{?rhel} > 5
# For Alpha 3, we want nss instead of nss-softokn
Requires: nss
%else
Requires: nss-softokn
%endif
Requires: nss-softokn-freebl

%description fips
This package requires everything which is needed to build an
all purpose initramfs with dracut, which does an integrity check.
%endif

%package fips-aesni
Summary: Dracut modules to build a dracut initramfs with an integrity check with aesni-intel
Requires: %{name}-fips = %{version}-%{release}

%description fips-aesni
This package requires everything which is needed to build an
all purpose initramfs with dracut, which does an integrity check
and adds the aesni-intel kernel module.

%package caps
Summary: Dracut modules to build a dracut initramfs which drops capabilities
Requires: %{name} = %{version}-%{release}
Requires: libcap

%description caps
This package requires everything which is needed to build an
all purpose initramfs with dracut, which drops capabilities.

%package tools
Summary: Dracut tools to build the local initramfs
Requires: %{name} = %{version}-%{release}

%description tools
This package contains tools to assemble the local initrd and host configuration.

%prep
%setup -q -n %{name}-%{version}

%if %{defined PATCH1}
git init
git config user.email "dracut-maint@redhat.com"
git config user.name "Fedora dracut team"
git add .
git commit -a -q -m "%{version} baseline."

# Apply all the patches.
git am -p1 %{patches}
%endif

%build
make all

%install
%if 0%{?fedora} || 0%{?rhel}
rm -rf $RPM_BUILD_ROOT
%endif
make install DESTDIR=$RPM_BUILD_ROOT \
     libdir=%{_prefix}/lib \
     bindir=%{_bindir} \
%if %{defined _unitdir}
     systemdsystemunitdir=%{_unitdir} \
%endif
     sysconfdir=/etc mandir=%{_mandir}

echo %{name}-%{version}-%{release} > $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/10rpmversion/dracut-version

%if 0%{?fedora} == 0 && 0%{?rhel} == 0
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/01fips
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/02fips-aesni
%endif

# remove gentoo specific modules
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/50gensplash

%if %{defined _unitdir}
# with systemd IMA and selinux modules do not make sense
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/96securityfs
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/97masterkey
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/98integrity
rm -fr $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/98selinux
%endif

mkdir -p $RPM_BUILD_ROOT/boot/dracut
mkdir -p $RPM_BUILD_ROOT/var/lib/dracut/overlay
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log
touch $RPM_BUILD_ROOT%{_localstatedir}/log/dracut.log
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/initramfs

%if 0%{?fedora} || 0%{?rhel}
install -m 0644 dracut.conf.d/fedora.conf.example $RPM_BUILD_ROOT/etc/dracut.conf.d/01-dist.conf
install -m 0644 dracut.conf.d/fips.conf.example $RPM_BUILD_ROOT/etc/dracut.conf.d/40-fips.conf
%endif

%if 0%{?suse_version}
install -m 0644 dracut.conf.d/suse.conf.example   $RPM_BUILD_ROOT/etc/dracut.conf.d/01-dist.conf
%endif

%if 0%{?fedora} <= 12 && 0%{?rhel} < 6 && 0%{?suse_version} <= 9999
rm $RPM_BUILD_ROOT%{_bindir}/mkinitrd
rm $RPM_BUILD_ROOT%{_bindir}/lsinitrd
%endif

mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m 0644 dracut.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/dracut_log

# create compat symlink
mkdir -p $RPM_BUILD_ROOT/sbin
ln -s /usr/bin/dracut $RPM_BUILD_ROOT/sbin/dracut

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS dracut.html dracut.png dracut.svg
%{_bindir}/dracut
# compat symlink
/sbin/dracut
%if 0%{?fedora} > 12 || 0%{?rhel} >= 6 || 0%{?suse_version} > 9999
%{_bindir}/mkinitrd
%{_bindir}/lsinitrd
%endif
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/dracut-functions.sh
%{dracutlibdir}/dracut-functions
%{dracutlibdir}/dracut-logger.sh
%{dracutlibdir}/dracut-initramfs-restore
%config(noreplace) /etc/dracut.conf
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%config /etc/dracut.conf.d/01-dist.conf
%endif
%dir /etc/dracut.conf.d
%{_mandir}/man8/dracut.8*
%{_mandir}/man7/dracut.kernel.7*
%{_mandir}/man7/dracut.cmdline.7*
%{_mandir}/man5/dracut.conf.5*
%{dracutlibdir}/modules.d/00bootchart
%{dracutlibdir}/modules.d/00dash
%{dracutlibdir}/modules.d/05busybox
%{dracutlibdir}/modules.d/10i18n
%{dracutlibdir}/modules.d/10rpmversion
%{dracutlibdir}/modules.d/30convertfs
%{dracutlibdir}/modules.d/45url-lib
%{dracutlibdir}/modules.d/50plymouth
%{dracutlibdir}/modules.d/80cms
%{dracutlibdir}/modules.d/90btrfs
%{dracutlibdir}/modules.d/90crypt
%{dracutlibdir}/modules.d/90dm
%{dracutlibdir}/modules.d/90dmraid
%{dracutlibdir}/modules.d/90dmsquash-live
%{dracutlibdir}/modules.d/90kernel-modules
%{dracutlibdir}/modules.d/90lvm
%{dracutlibdir}/modules.d/90mdraid
%{dracutlibdir}/modules.d/90multipath
%{dracutlibdir}/modules.d/91crypt-gpg
%{dracutlibdir}/modules.d/95debug
%{dracutlibdir}/modules.d/95resume
%{dracutlibdir}/modules.d/95rootfs-block
%{dracutlibdir}/modules.d/95dasd
%{dracutlibdir}/modules.d/95dasd_mod
%{dracutlibdir}/modules.d/95fstab-sys
%{dracutlibdir}/modules.d/95zfcp
%{dracutlibdir}/modules.d/95terminfo
%{dracutlibdir}/modules.d/95udev-rules
%if %{undefined _unitdir}
%{dracutlibdir}/modules.d/96securityfs
%{dracutlibdir}/modules.d/97masterkey
%{dracutlibdir}/modules.d/98selinux
%{dracutlibdir}/modules.d/98integrity
%endif
%{dracutlibdir}/modules.d/97biosdevname
%{dracutlibdir}/modules.d/98ecryptfs
%{dracutlibdir}/modules.d/98pollcdrom
%{dracutlibdir}/modules.d/98syslog
%{dracutlibdir}/modules.d/98usrmount
%{dracutlibdir}/modules.d/99base
%{dracutlibdir}/modules.d/99fs-lib
%{dracutlibdir}/modules.d/99img-lib
%{dracutlibdir}/modules.d/99shutdown
%config(noreplace) /etc/logrotate.d/dracut_log
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log
%dir %{_sharedstatedir}/initramfs
%if %{defined _unitdir}
%{_unitdir}/*.service
%{_unitdir}/*/*.service
%endif

%files network
%defattr(-,root,root,0755)
%{dracutlibdir}/modules.d/40network
%{dracutlibdir}/modules.d/95fcoe
%{dracutlibdir}/modules.d/95iscsi
%{dracutlibdir}/modules.d/90livenet
%{dracutlibdir}/modules.d/95nbd
%{dracutlibdir}/modules.d/95nfs
%{dracutlibdir}/modules.d/95ssh-client
%{dracutlibdir}/modules.d/45ifcfg
%{dracutlibdir}/modules.d/95znet

%if 0%{?fedora} || 0%{?rhel}
%files fips
%defattr(-,root,root,0755)
%{dracutlibdir}/modules.d/01fips
%config(noreplace) /etc/dracut.conf.d/40-fips.conf
%endif

%files fips-aesni
%defattr(-,root,root,0755)
%doc COPYING
%{dracutlibdir}/modules.d/02fips-aesni

%files caps
%defattr(-,root,root,0755)
%{dracutlibdir}/modules.d/02caps

%files tools
%defattr(-,root,root,0755)
%{_mandir}/man8/dracut-catimages.8*
%{_bindir}/dracut-catimages
%dir /boot/dracut
%dir /var/lib/dracut
%dir /var/lib/dracut/overlay

%changelog
* Fri Jul 20 2012 Harald Hoyer <harald@redhat.com> 018-95.git20120720
- fixed some more race condition in resume

* Thu Jul 19 2012 Harald Hoyer <harald@redhat.com> 018-93.git20120719
- do not rename network interfaces
- wait until md raids are clean on shutdown
- fips module fixes
- fixed BOOTIF case sensitive
- fixed resume from hibernate
- nfs module fixes

* Fri Jun 22 2012 Harald Hoyer <harald@redhat.com> 018-78.git20120622
- speedup install
- fixed installkernel() return codes
- removed test mounting of btrfs and xfs (was fsck replacement)
- no more "mknod" in the initramfs, fixes plymouth on s390
- no systemd-vconsole-setup installation (unused currently anyway)

* Fri Jun 22 2012 Harald Hoyer <harald@redhat.com> 018-67.git20120622
- add tagged bonding
Resolves: rhbz#833057
- fixed shutdown service
Resolves: rhbz#831634

* Tue Jun 12 2012 Harald Hoyer <harald@redhat.com> 018-65.git20120612
- revert to "ip=dhcp" by default

* Mon Jun 11 2012 Harald Hoyer <harald@redhat.com> 018-55.git20120611
- default to dhcp for BOOTIF

* Tue Jun 05 2012 Dennis Gilmore <dennis@ausil.us> 018-53.git20120605
- include omapdrm in the arm modules to include

* Tue Jun 05 2012 Harald Hoyer <harald@redhat.com> 018-52.git20120605
- change rd.dasd to dasd_mod kernel parameter

* Mon Jun 04 2012 Harald Hoyer <harald@redhat.com> 018-51.git20120604
- fix network rules for kdump
Resolves: rhbz#822750
- disable curl progress bar
Resolves: rhbz#817301 rhbz#824883
- do not default to dhcp for interfaces without ip=
- do not arping with qeth layer3 interfaces
Resolves: rhbz#825783
- do not unpack the initramfs, if the old initramfs still exists
- add rd.luks.allow-discards and honor options in crypttab
- fixed dasd_mod param generation
- fix return value of some installkernel() functions
- do not rely on the presence of lib64, check with ldd
- dasd: don't set an already set attribute
Resolves: rhbz#826357
- add filesystem options to fsck_single()

* Tue May 22 2012 Harald Hoyer <harald@redhat.com> 018-40.git20120522
- fixed s390 dasd handling
- fixed DNS bug for s390

* Thu May 17 2012 Dennis Gilmore <dennis@ausil.us> 018-36.git20120510
- add patch for arm storage modules

* Thu May 10 2012 Harald Hoyer <harald@redhat.com> 018-35.git20120510
- fix s390 ifcfg configuration
Resolves: rhbz#811521

* Thu May 10 2012 Harald Hoyer <harald@redhat.com> 018-33.git20120510
- fix mediacheck
Resolves: rhbz#817419

* Wed May 09 2012 Harald Hoyer <harald@redhat.com> 018-32.git20120509
- use PREFIX for netmask prefixes
Resolves: rhbz#820185

* Fri May 04 2012 Harald Hoyer <harald@redhat.com> 018-31.git20120504
- fix anaconda installer bug
Resolves: rhbz#818707

* Tue Apr 24 2012 Harald Hoyer <harald@redhat.com> 018-26.git20120424
- fixed progress bar for TERM=dumb
Resolves: rhbz#814713
- add DNS to ifcfg for NM takeover 
Resolves: rhbz#815369

* Thu Apr 19 2012 Harald Hoyer <harald@redhat.com> 018-23.git20120419
- fixed vnc installation
- do not ignore ram devices in udev
- lsinitrd support for symlinks
- manpage fixes
- do not include IMA and selinux dracut modules (systemd does that)
- removed dracut shutdown service from reboot
- include all phy network kernel modules
- cleanups now after pre-pivot hook

* Mon Apr 16 2012 Harald Hoyer <harald@redhat.com> 018-12.git20120416
- new upstream version, which fixes various anaconda loader issues

* Thu Apr 05 2012 Harald Hoyer <harald@redhat.com> 018-1
- version 018

* Thu Mar 22 2012 Harald Hoyer <harald@redhat.com> 017-62.git20120322
- fixed /run prefix copying

* Wed Mar 21 2012 Harald Hoyer <harald@redhat.com> 017-59.git20120321
- new upstream version, which fixes various anaconda loader issues

* Mon Mar 12 2012 Harald Hoyer <harald@redhat.com> 017-43.git20120312
- live image: fixed image uncompression
- live updates for livenet

* Thu Mar 08 2012 Harald Hoyer <harald@redhat.com> 017-40.git20120308
- add s390 ctcm network kernel module

* Thu Mar 08 2012 Harald Hoyer <harald@redhat.com> 017-39.git20120308
- kill dhclient silently
- cleanup and fix network config writeout to /run/initramfs/state
Resolves: rhbz#799989
- various cleanups

* Fri Mar 02 2012 Harald Hoyer <harald@redhat.com> 017-22.git20120302
- nfs path fixes for live image over nfs
  root=live:nfs://10.10.10.10:/srv/all/install.img ip=dhcp rd.neednet

* Thu Mar 01 2012 Harald Hoyer <harald@redhat.com> 017-19.git20120301
- fixed include of some kernel modules

* Wed Feb 29 2012 Harald Hoyer <harald@redhat.com> 017-17.git20120229
- update to latest git
- fixes for convertfs (/usr-move)

* Fri Feb 24 2012 Harald Hoyer <harald@redhat.com> 017-1
- version 017

* Fri Feb 17 2012 Harald Hoyer <harald@redhat.com> 016-9.git20120217
- update to latest git

* Wed Feb 15 2012 Harald Hoyer <harald@redhat.com> 016-1
- version 016

* Mon Feb 13 2012 Harald Hoyer <harald@redhat.com> 015-9.git20120213
- update to latest git

* Sun Feb 12 2012 Kay Sievers <kay@redhat.com> - 015-9.git20120210
- fix dependency loop in systemd service files

* Fri Feb 10 2012 Harald Hoyer <harald@redhat.com> 015-8.git20120210
- update to latest git

* Thu Feb 09 2012 Harald Hoyer <harald@redhat.com> 015-7.git20120209
- update to latest git

* Thu Feb 09 2012 Harald Hoyer <harald@redhat.com> 015-4.git20120209
- update to latest git

* Wed Feb 08 2012 Harald Hoyer <harald@redhat.com> 015-3.git20120208
- update to latest git

* Tue Feb 07 2012 Harald Hoyer <harald@redhat.com> 015-1
- version 015

* Thu Feb 02 2012 Harald Hoyer <harald@redhat.com> 014-81.git20120202
- update to latest git

* Thu Feb 02 2012 Harald Hoyer <harald@redhat.com> 014-80.git20120202
- update to latest git

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-77.git20120126.1
- rebuild for rawhide

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-77.git20120126
- update to latest git

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-76.git20120126
- update to latest git

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-75.git20120126
- update to latest git

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-74.git20120126
- update to latest git

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-73.git20120126
- update to latest git

* Thu Jan 26 2012 Harald Hoyer <harald@redhat.com> 014-72.git20120126
- update to latest git

* Mon Jan 23 2012 Harald Hoyer <harald@redhat.com> 014-65.git20120123
- update to latest git

* Mon Jan 23 2012 Harald Hoyer <harald@redhat.com> 014-61.git20120123
- update to latest git

* Tue Jan 17 2012 Harald Hoyer <harald@redhat.com> 014-38.git20120117
- update to latest git

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 014-10.git20111215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Harald Hoyer <harald@redhat.com> 014-9.git20111215
- update to latest git
- lots of patch changes

* Fri Oct 21 2011 Harald Hoyer <harald@redhat.com> 013-100.git20111021
- update to latest git

* Thu Oct 20 2011 Harald Hoyer <harald@redhat.com> 013-93.git20111020
- update to latest git

* Wed Oct 19 2011 Harald Hoyer <harald@redhat.com> 013-85.git20111019
- update to latest git

* Tue Oct 04 2011 Harald Hoyer <harald@redhat.com> 013-15
- fixed mdraid container handling
Resolves: rhbz#743240

* Thu Sep 22 2011 Harald Hoyer <harald@redhat.com> 013-13
- fixed mdraid issues
- fixed btrfsck
Resolves: rhbz#735602

* Wed Sep 21 2011 Harald Hoyer <harald@redhat.com> 013-12
- removed patch backup files
- reintroduced /dev/live

* Tue Sep 20 2011 Harald Hoyer <harald@redhat.com> 013-11
- move mounting of securitfs to a seperate module
Resolves: rhbz#737140

* Tue Sep 20 2011 Harald Hoyer <harald@redhat.com> 013-10
- mount securitfs with the correct source
Resolves: rhbz#737140

* Tue Sep 20 2011 Harald Hoyer <harald@redhat.com> 013-9
- do not carry over initramfs udev rules
Resolves: rhbz#734096

* Fri Sep 02 2011 Harald Hoyer <harald@redhat.com> 013-8
- hopefully fixed one part of a loop/udev and loop/mount race
Resolves: rhbz#735199

* Wed Aug 31 2011 Harald Hoyer <harald@redhat.com> 013-7
- add /lib/udev/input_id to the initramfs
- fix hmac install

* Tue Aug 30 2011 Harald Hoyer <harald@redhat.com> 013-6
- fixed environment passing to real init
Resolves: rhbz#733674
- fixed lvm on md

* Mon Aug 29 2011 Harald Hoyer <harald@redhat.com> 013-5
- fixed rhel/fedora version checks

* Wed Aug 17 2011 Harald Hoyer <harald@redhat.com> 013-4
- fixed crash with livenet installed

* Wed Aug 17 2011 Harald Hoyer <harald@redhat.com> 013-3
- fixed live iso mounting
Resolves: rhbz#730579

* Fri Aug 12 2011 Harald Hoyer <harald@redhat.com> 013-1
- fixed symlink creation for lorax

* Wed Aug 10 2011 Harald Hoyer <harald@redhat.com> 011-41.git20110810
- fixed getargs() for empty args

* Wed Aug 10 2011 Harald Hoyer <harald@redhat.com> 011-40.git20110810
- fixed symbolic link creation in the initramfs
Resolves: rhbz#728863

* Wed Jul 20 2011 Harald Hoyer <harald@redhat.com> 011-15.git20110720
- "eject" is optional now
- refined shutdown procedure

* Mon Jul 18 2011 Harald Hoyer <harald@redhat.com> 011-1
- version 011

* Fri May 20 2011 Harald Hoyer <harald@redhat.com> 011-0.1%{?rdist}
- git snapshot of pre-version 011

* Fri Apr 01 2011 Harald Hoyer <harald@redhat.com> 010-1
- version 010

* Thu Mar 31 2011 Harald Hoyer <harald@redhat.com> 009-5
- fixed PATH and kmsg logging

* Thu Mar 31 2011 Harald Hoyer <harald@redhat.com> 009-4
- fixed dmsquash rule generation
- fixed fips boot arg parsing
- fixed plymouth pid generation

* Wed Mar 30 2011 Harald Hoyer <harald@redhat.com> 009-3
- fixed dhcp
- added /lib/firmware/updates to firmware directories 
- fixed LiveCD /dev/.initramfs fallback
- fixed cdrom polling
- dropped net-tools dependency

* Tue Mar 29 2011 Harald Hoyer <harald@redhat.com> 009-2
- fixed empty output file argument handling:
  "dracut '' <kernel version>" 

* Mon Mar 28 2011 Harald Hoyer <harald@redhat.com> 009-1
- version 009

* Thu Mar 17 2011 Harald Hoyer <harald@redhat.com> 009-0.1
- version 009 prerelease

* Tue Feb 22 2011 Harald Hoyer <harald@redhat.com> 008-7
- fixed lvm version parsing

* Tue Feb 22 2011 Harald Hoyer <harald@redhat.com> 008-6
- fixed lvm version parsing

* Mon Feb 21 2011 Harald Hoyer <harald@redhat.com> 008-5
- fixed i18n unicode setting
- set cdrom in kernel polling

* Fri Feb 18 2011 Harald Hoyer <harald@redhat.com> 008-4
- readded dist tag

* Fri Feb 18 2011 Harald Hoyer <harald@redhat.com> 008-3
- fixed i18n
- turned off selinux by default

* Wed Feb 09 2011 Harald Hoyer <harald@redhat.com> 008-2
- do not write dracut.log to /tmp under any circumstances
- touch /dev/.systemd/plymouth after plymouth started

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 008-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Harald Hoyer <harald@redhat.com> 008-1
- version 008-1

* Mon Jan 17 2011 Harald Hoyer <harald@redhat.com> 008-0.11
- removed "mount" requirement

* Thu Nov 18 2010 Harald Hoyer <harald@redhat.com> - 008-0.10
- dracut-008 pre git snapshot
- fixes /dev/dri permissions
Resolves: rhbz#626559

* Fri Nov 12 2010 Harald Hoyer <harald@redhat.com> 008-0.9
- dracut-008 pre git snapshot
- fixes /dev/.udev permissions
Resolves: rhbz#651594

* Wed Nov  3 2010 Harald Hoyer <harald@redhat.com> - 008-0.8
- fixed fsck -a option

* Fri Oct 29 2010 Harald Hoyer <harald@redhat.com> 008-0.7
- added fsck to initramfs

* Fri Oct 29 2010 Harald Hoyer <harald@redhat.com> 008-0.6
- fixed rpm macros

* Fri Oct 29 2010 Harald Hoyer <harald@redhat.com> 008-0.5
- dracut-008 pre git snapshot

* Mon Aug 09 2010 Harald Hoyer <harald@redhat.com> 007-1
- version 007

* Thu Jun 17 2010 Harald Hoyer <harald@redhat.com> 006-1
- version 006

* Fri Jun 11 2010 Harald Hoyer <harald@redhat.com>
- Remove requirements, which are not really needed
Resolves: rhbz#598509
- fixed copy of network config to /dev/.initramfs/ (patch 146)
Resolves: rhbz#594649
- more password beauty (patch 142)
Resolves: rhbz#561092
- support multiple iSCSI disks (patch 143)
Resolves: rbhz#580190
- fixed selinux=0 (patch 130)
Resolves: rhbz#593080
- add support for booting LVM snapshot root volume (patch 145)
Resolves: rbhz#602723
- remove hardware field from BOOTIF= (patch 148)
Resolves: rhbz#599593
- add aes kernel modules and fix crypt handling (patch 137, patch 140 and patch 147)
Resolves: rhbz#600170

* Thu May 27 2010 Harald Hoyer <harald@redhat.com> 
- fixed Requirements
- fixed autoip6 
Resolves: rhbz#538388
- fixed multipath
Resolves: rhbz#595719

* Thu May 06 2010 Harald Hoyer <harald@redhat.com> 
- only display short password messages
Resolves: rhbz#561092

* Thu May 06 2010 Harald Hoyer <harald@redhat.com>
- fixed dracut manpages 
Resolves: rhbz#589109
- use ccw-init and ccw rules from s390utils
Resolves: rhbz#533494
- fixed fcoe
Resolves: rhbz#486244
- various other bugfixes seen in Fedora

* Tue Apr 20 2010 Harald Hoyer <harald@redhat.com> 
- fixed network with multiple nics
- fixed nfsidmap paths
- do not run blkid on non active container raids
- fixed cdrom polling mechanism
- update to latest git

* Thu Apr 15 2010 Harald Hoyer <harald@redhat.com>
- fixed dracut manpages
- dmraid parse different error messages
- add cdrom polling mechanism for slow cdroms
- add module btrfs
- teach dmsquash live-root to use rootflags
- trigger udev with action=add
- fixed add_drivers handling 
- add sr_mod
- use pigz instead of gzip, if available

* Thu Mar 25 2010 Harald Hoyer <harald@redhat.com> 
- removed firmware requirements (rhbz#572634)
- add /etc/dracut.conf.d
- Resolves: rhbz#572634

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 
- version 005

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 
- fixed rpmlint errors (rhbz#570547)
- removed firmware package from dracut-kernel (rhbz#572634)
- add dcb support to dracut's FCoE support (rhbz#563794)
- force install some modules in hostonly mode (rhbz#573094)
- various other bugfixes
- Resolves: rhbz#570547, rhbz#572634, rhbz#563794, rhbz#573094

* Thu Feb 18 2010 Harald Hoyer <harald@redhat.com> 004-15
- fixed "selinux=0" booting (rhbz#566376)
- fixed internal IFS handling
- Resolves: rhbz#566376

* Fri Jan 29 2010 Harald Hoyer <harald@redhat.com> 004-5
- fixed firmware.sh bug (#559975 #559597)

* Tue Jan 26 2010 Harald Hoyer <harald@redhat.com> 004-4
- add multipath check

* Tue Jan 26 2010 Harald Hoyer <harald@redhat.com> 004-3
- fix selinux handling if .autorelabel is present
- Resolves: rhbz#557744

* Wed Jan 20 2010 Harald Hoyer <harald@redhat.com> 004-2
- fix emergency_shell argument parsing
- Related: rhbz#543948

* Fri Jan 15 2010 Harald Hoyer <harald@redhat.com> 004-1
- version 004
- Resolves: rhbz#529339 rhbz#533494 rhbz#548550 
- Resolves: rhbz#548555 rhbz#553195

* Wed Jan 13 2010 Harald Hoyer <harald@redhat.com> 003-3
- add Obsoletes of mkinitrd/nash/libbdevid-python
- Related: rhbz#543948

* Wed Jan 13 2010 Warren Togami <wtogami@redhat.com> 003-2
- nbd is Fedora only

* Fri Nov 27 2009 Harald Hoyer <harald@redhat.com> 003-1
- version 003

* Mon Nov 23 2009 Harald Hoyer <harald@redhat.com> 002-26
- add WITH_SWITCH_ROOT make flag
- add fips requirement conditional
- add more device mapper modules (bug #539656)

* Fri Nov 20 2009 Dennis Gregorovic <dgregor@redhat.com> - 002-25.1
- nss changes for Alpha 3

* Thu Nov 19 2009 Harald Hoyer <harald@redhat.com> 002-25
- add more requirements for dracut-fips (bug #539257)

* Tue Nov 17 2009 Harald Hoyer <harald@redhat.com> 002-24
- put fips module in a subpackage (bug #537619)

* Tue Nov 17 2009 Harald Hoyer <harald@redhat.com> 002-23
- install xdr utils for multipath (bug #463458)

* Thu Nov 12 2009 Harald Hoyer <harald@redhat.com> 002-22
- add module 90multipath
- add module 01fips
- renamed module 95ccw to 95znet (bug #533833)
- crypt: ignore devices in /etc/crypttab (root is not in there)
- dasd: only install /etc/dasd.conf in hostonly mode (bug #533833)
- zfcp: only install /etc/zfcp.conf in hostonly mode (bug #533833)
- kernel-modules: add scsi_dh scsi_dh_rdac scsi_dh_emc (bug #527750)
- dasd: use dasdconf.sh from s390utils (bug #533833)

* Fri Nov 06 2009 Harald Hoyer <harald@redhat.com> 002-21
- fix rd_DASD argument handling (bug #531720)
- Resolves: rhbz#531720

* Wed Nov 04 2009 Harald Hoyer <harald@redhat.com> 002-20
- fix rd_DASD argument handling (bug #531720)
- Resolves: rhbz#531720

* Tue Nov 03 2009 Harald Hoyer <harald@redhat.com> 002-19
- changed rd_DASD to rd_DASD_MOD (bug #531720)
- Resolves: rhbz#531720

* Tue Oct 27 2009 Harald Hoyer <harald@redhat.com> 002-18
- renamed lvm/device-mapper udev rules according to upstream changes
- fixed dracut search path issue

* Mon Oct 26 2009 Harald Hoyer <harald@redhat.com> 002-17
- load dm_mod module (bug #530540)

* Fri Oct 09 2009 Jesse Keating <jkeating@redhat.com> - 002-16
- Upgrade plymouth to Requires(pre) to make it show up before kernel

* Thu Oct 08 2009 Harald Hoyer <harald@redhat.com> 002-15
- s390 ccw: s/layer1/layer2/g

* Thu Oct 08 2009 Harald Hoyer <harald@redhat.com> 002-14
- add multinic support
- add s390 zfcp support
- add s390 network support

* Wed Oct 07 2009 Harald Hoyer <harald@redhat.com> 002-13
- fixed init=<command> handling
- kill loginit if "rdinitdebug" specified
- run dmsquash-live-root after udev has settled (bug #527514)

* Tue Oct 06 2009 Harald Hoyer <harald@redhat.com> 002-12
- add missing loginit helper
- corrected dracut manpage

* Thu Oct 01 2009 Harald Hoyer <harald@redhat.com> 002-11
- fixed dracut-gencmdline for root=UUID or LABEL

* Thu Oct 01 2009 Harald Hoyer <harald@redhat.com> 002-10
- do not destroy assembled raid arrays if mdadm.conf present
- mount /dev/shm 
- let udevd not resolve group and user names
- preserve timestamps of tools on initramfs generation
- generate symlinks for binaries correctly
- moved network from udev to initqueue
- mount nfs3 with nfsvers=3 option and retry with nfsvers=2
- fixed nbd initqueue-finished
- improved debug output: specifying "rdinitdebug" now logs
  to dmesg, console and /init.log
- stop udev before killing it
- add ghost /var/log/dracut.log
- dmsquash: use info() and die() rather than echo
- strip kernel modules which have no x bit set
- redirect stdin, stdout, stderr all RW to /dev/console
  so the user can use "less" to view /init.log and dmesg

* Tue Sep 29 2009 Harald Hoyer <harald@redhat.com> 002-9
- make install of new dm/lvm udev rules optionally
- correct dasd module typo

* Fri Sep 25 2009 Warren Togami <wtogami@redhat.com> 002-8
- revert back to dracut-002-5 tarball 845dd502
  lvm2 was reverted to pre-udev

* Wed Sep 23 2009 Harald Hoyer <harald@redhat.com> 002-7
- build with the correct tarball

* Wed Sep 23 2009 Harald Hoyer <harald@redhat.com> 002-6
- add new device mapper udev rules and dmeventd 
  bug 525319, 525015

* Wed Sep 23 2009 Warren Togami <wtogami@redaht.com> 002-5
- Revert back to -3, Add umount back to initrd
  This makes no functional difference to LiveCD.  See Bug #525319

* Mon Sep 21 2009 Warren Togami <wtogami@redhat.com> 002-4
- Fix LiveCD boot regression

* Mon Sep 21 2009 Harald Hoyer <harald@redhat.com> 002-3
- bail out if selinux policy could not be loaded and 
  selinux=0 not specified on kernel command line 
  (bug #524113)
- set finished criteria for dmsquash live images

* Fri Sep 18 2009 Harald Hoyer <harald@redhat.com> 002-2
- do not cleanup dmraids
- copy over lvm.conf

* Thu Sep 17 2009 Harald Hoyer <harald@redhat.com> 002-1
- version 002
- set correct PATH
- workaround for broken mdmon implementation

* Wed Sep 16 2009 Harald Hoyer <harald@redhat.com> 001-12
- removed lvm/mdraid/dmraid lock files
- add missing ifname= files

* Wed Sep 16 2009 Harald Hoyer <harald@redhat.com> 001-11
- generate dracut-version during rpm build time

* Tue Sep 15 2009 Harald Hoyer <harald@redhat.com> 001-10
- add ifname= argument for persistent netdev names
- new /initqueue-finished to check if the main loop can be left
- copy mdadm.conf if --mdadmconf set or mdadmconf in dracut.conf

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-9
- added Requires: plymouth-scripts

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-8
- plymouth: use plymouth-populate-initrd
- add add_drivers for dracut and dracut.conf
- do not mount /proc and /selinux manually in selinux-load-policy

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-7
- add scsi_wait_scan to be sure everything was scanned

* Tue Sep 08 2009 Harald Hoyer <harald@redhat.com> 001-6
- fixed several problems with md raid containers
- fixed selinux policy loading

* Tue Sep 08 2009 Harald Hoyer <harald@redhat.com> 001-5
- patch does not honor file modes, fixed them manually

* Mon Sep 07 2009 Harald Hoyer <harald@redhat.com> 001-4
- fixed mdraid for IMSM

* Mon Sep 07 2009 Harald Hoyer <harald@redhat.com> 001-3
- fixed bug, which prevents installing 61-persistent-storage.rules (bug #520109)

* Thu Sep 03 2009 Harald Hoyer <harald@redhat.com> 001-2
- fixed missing grep for md
- reorder cleanup

* Wed Sep 02 2009 Harald Hoyer <harald@redhat.com> 001-1
- version 001
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Aug 14 2009 Harald Hoyer <harald@redhat.com> 0.9-1
- version 0.9

* Thu Aug 06 2009 Harald Hoyer <harald@redhat.com> 0.8-1
- version 0.8 
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Jul 24 2009 Harald Hoyer <harald@redhat.com> 0.7-1
- version 0.7
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Wed Jul 22 2009 Harald Hoyer <harald@redhat.com> 0.6-1
- version 0.6
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Jul 17 2009 Harald Hoyer <harald@redhat.com> 0.5-1
- version 0.5
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Sat Jul 04 2009 Harald Hoyer <harald@redhat.com> 0.4-1
- version 0.4
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Thu Jul 02 2009 Harald Hoyer <harald@redhat.com> 0.3-1
- version 0.3
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Wed Jul 01 2009 Harald Hoyer <harald@redhat.com> 0.2-1
- version 0.2

* Fri Jun 19 2009 Harald Hoyer <harald@redhat.com> 0.1-1
- first release

* Thu Dec 18 2008 Jeremy Katz <katzj@redhat.com> - 0.0-1
- Initial build
