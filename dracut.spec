# Variables must be defined
%define with_switch_root        1
%define with_nbd                1

# switchroot provided by util-linux-ng in F-12+
%if 0%{?fedora} > 11 || 0%{?rhel} >= 6
%define with_switch_root 0
%endif
# nbd in Fedora only
%if 0%{?rhel} >= 6
%define with_nbd 0
%endif

%if %{defined gittag}
%define rdist .git%{gittag}%{?dist}
%define dashgittag -%{gittag}
%else
%define rdist %{?dist}
%endif

Name: dracut
Version: 005
Release: 4%{?rdist}
Summary: Initramfs generator using udev
Group: System Environment/Base          
License: GPLv2+ 
URL: http://apps.sourceforge.net/trac/dracut/wiki
# Source can be generated by 
# http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=snapshot;h=%{?dashgittag};sf=tgz
Source0: dracut-%{version}%{?dashgittag}.tar.bz2

Patch1: 0001-dracut.8-fixed-LUKS-paragraph.patch
Patch2: 0002-Fix-ahci-detection-in-kernel-2.6.35.patch
Patch3: 0003-dracut.8-add-information-which-parameter-can-be-spec.patch
Patch4: 0004-dmraid-parse-different-error-messages.patch
Patch5: 0005-init-add-hacky-cdrom-polling-mechanism.patch
Patch6: 0006-add-module-btrfs.patch
Patch7: 0007-teach-dmsquash-live-root-to-use-rootflags.patch
Patch8: 0008-init-trigger-with-action-add.patch
Patch9: 0009-add-missing-paragraph-for-add-drivers.patch
Patch10: 0010-manpage-addition-for-kernel-drivers.patch
Patch11: 0011-dracut-add_drivers-from-the-command-line-should-add-.patch
Patch12: 0012-AUTHORS-updated.patch
Patch13: 0013-kernel-modules-hardcode-sr_mod.patch
Patch14: 0014-kernel-modules-only-remove-ocfs2-if-all-filesystems-.patch
Patch15: 0015-dracut.spec-add-btrfs-module.patch
Patch16: 0016-Use-pigz-for-gzipping-if-available.patch
Patch17: 0017-nfs-fixed-nsswitch.conf-parsing.patch
Patch18: 0018-network-removed-bogus-udev-rules.patch
Patch19: 0019-network-correct-rules-for-multiple-nics.patch
Patch20: 0020-nfs-add-missing-nfsidmap-libs.patch
Patch21: 0021-udev-rules-be-more-careful-about-md-devices-and-blki.patch
Patch22: 0022-dracut-lib-turn-of-shell-debug-mode-in-strstr-and-ge.patch
Patch23: 0023-mdraid-try-to-start-container-childs-manually-with-m.patch
Patch24: 0024-init-fix-cdrom-polling-loop.patch
Patch25: 0025-init-do-not-redirect-to.patch
Patch26: 0026-loginit-turn-off-debugging.patch
Patch27: 0027-TEST-12-RAID-DEG-create-root-filter-MD_UUID-only.patch
Patch28: 0028-run-qemu-add-usr-libexec-qemu-kvm-to-search.patch
Patch29: 0029-test-change-testsuite-to-local-tcp-rather-than-udp-m.patch
Patch30: 0030-add-rd_retry-kernel-command-line-parameter.patch
Patch31: 0031-test-nfs-correct-return-code-and-cleanup.patch
Patch32: 0032-NBD-kill-server-after-failed-test.patch
Patch33: 0033-test-TEST-50-MULTINIC-kill-server-after-failed-test.patch
Patch34: 0034-test-TEST-50-MULTINIC-install-all-nfsidmap-libs-for-.patch
Patch35: 0035-test-TEST-50-MULTINIC-install-sd_mod-and-ata_piix-ke.patch
Patch36: 0036-dracut.spec-removed-e2fsprogs-requirement.patch
Patch37: 0037-test-MULTINIC-kill-server-after-passing-all-tests.patch
Patch38: 0038-NEWS-update.patch
Patch39: 0039-test-NBD-check-for-nbd-kernel-module-first.patch
Patch40: 0040-Needs-btrfsctl-not-btrfs-module.patch
Patch41: 0041-btfrs-load-btrfs-module-and-updated-NEWS.patch
Patch42: 0042-kernel-modules-add-more-hardcoded-modules.patch
Patch43: 0043-dracut-functions-use-udevadm-to-get-ID_FS_.patch
Patch44: 0044-dracut.conf-use-as-default-for-config-variables.patch
Patch45: 0045-znet-use-ccw-init-and-ccw-rules-from-s390utils-in-dr.patch
Patch46: 0046-znet-renamed-rd_CCW-to-rd_ZNET.patch
Patch47: 0047-fcoe-add-sbin-vconfig-and-the-8021q-kernel-module.patch
Patch48: 0048-dracut.8-fix-rd_LVM_LV-description.patch
Patch49: 0049-plymouth-only-display-luksname-and-device-for-multip.patch
Patch50: 0050-dracut.spec-remove-elfutils-libelf-requirement.patch
Patch51: 0051-use-grep-directly-without-nm-to-drop-binutils-requir.patch
Patch52: 0052-plymouth-plymouth-populate-initrd-get-rid-of-awk.patch
Patch53: 0053-dracut-get-rid-of-the-file-command.patch
Patch54: 0054-dracut.spec-clean-up-the-requirements.patch
Patch55: 0055-90mdraid-dracut-functions-fix-md-raid-hostonly-detec.patch
Patch56: 0056-40network-parse-ip-opts.sh-add-ip-auto6-to-valid-opt.patch
Patch57: 0057-40network-dhclient-script-be-more-verbose.patch
Patch58: 0058-40network-ifup-be-more-verbose.patch
Patch59: 0059-TEST-50-MULTINIC-do-not-provide-a-cdrom-in-the-testc.patch
Patch60: 0060-95fcoe-fcoe-up-wait_for_if_up.patch
Patch61: 0061-get-rid-of-rdnetdebug.patch
Patch62: 0062-95znet-removed-55-ccw.rules-and-ccw_init.patch
Patch63: 0063-Makefile-make-more-clean.patch
Patch64: 0064-selinux-loadpolicy.sh-exit-for-selinux-0.patch
Patch65: 0065-dracut-functions-check-if-specific-dracut-module-is-.patch
Patch66: 0066-multipath-simplify-and-install-wwids-rhbz-595719.patch
Patch67: 0067-multipath-remove-multipath-udev-rules-if-no-multipat.patch
Patch68: 0068-90crypt-crypto_LUKS-identifier-corrected.patch
Patch69: 0069-selinux-move-selinux-to-a-separate-module.patch
Patch70: 0070-plymouth-cryptroot-ask.sh-beautify-password-prompt.patch
Patch71: 0071-network-depend-on-ifcfg-if-etc-sysconfig-network-scr.patch
Patch72: 0072-network-strip-pxelinux-hardware-type-field-from-BOOT.patch
Patch73: 0073-dracut.spec-moved-znet-to-dracut-network.patch
Patch74: 0074-Write-rules-for-symlinks-to-dev-.udev-rules.d-for-la.patch
Patch75: 0075-dracut-functions-set-LANG-C-for-ldd-output-parsing.patch
Patch76: 0076-dracut-functions-use-LC_ALL-C-rather-than-LANG-C.patch
Patch77: 0077-dmsquash-resume-do-not-name-the-dev-.udev-rules-like.patch
Patch78: 0078-dmsquash-live-mount-live-image-at-dev-.initramfs-liv.patch
Patch79: 0079-dmsquash-live-depend-on-dm-module.patch
Patch80: 0080-dmsquash-live-do-not-umount-dev-.initramfs-live-for-.patch
Patch81: 0081-plymouth-depend-on-crypt-if-cryptsetup-exists.patch
Patch82: 0082-dracut.spec-removed-duplicate-COPYING.patch
Patch83: 0083-Just-look-for-cryptroot-instead-of-sbin-cryptroot.patch
Patch84: 0084-Have-cryptroot-ask-load-dm_crypt-if-needed.patch
Patch85: 0085-crypt-assemble-70-luks.rules-dynamically.patch
Patch86: 0086-cryptroot-ask-s-getargs-rd_NO_CRYPTTAB-getarg-rd_NO_.patch
Patch87: 0087-crypt-parse-crypt.sh-fix-end-label-for-luks-udev-rul.patch
Patch88: 0088-crypt-wait-for-all-rd_LUKS_UUID-disks-to-appear.patch
Patch89: 0089-dracut-lib.sh-getarg-returns-the-value-of-the-last-a.patch
Patch90: 0090-dracut-fixed-stripping-of-kernel-modules.patch
Patch91: 0091-conffile-before-confdir.patch
Patch92: 0092-selinux-fixed-error-handling-for-load-policy.patch
Patch93: 0093-btrfs-add-hostonly-check.patch
Patch94: 0094-lvm-wait-for-all-rd_LVM_LV-and-rd_LVM_VG-specified-t.patch
Patch95: 0095-90crypt-keys-on-external-devices-support.patch
Patch96: 0096-crypt-remove-emergency-source-of-dracut-lib.sh.patch
Patch97: 0097-dracut-functions-fix-m-a-handling.patch
Patch98: 0098-removed-redundant-64-lvm.rules-install.patch
Patch99: 0099-crypt-strip-luks-from-rd_LUKS_UUID.patch
Patch100: 0100-crypt-loop-until-all-non-busy-crypt-devs-closed.patch
Patch101: 0101-dracut-functions-fix-check-255-logic-and-dependencie.patch
Patch102: 0102-crypt-fix-printf.patch
Patch103: 0103-mdraid-remove-local.patch
Patch104: 0104-mdraid-remove-mdadm.conf-on-rd_NO_MDADMCONF.patch
Patch105: 0105-dracut-lib.sh-fixed-getarg-for-nonexistent-parameter.patch
Patch106: 0106-mkdir-dev-.udev-rules.d-with-mode-0755.patch
Patch107: 0107-init-create-dev-.udev-rules.d-with-correct-permissio.patch
Patch108: 0108-dracut-functions-fixed-omit.patch
Patch109: 0109-Harden-check-for-used-modules-in-hostonly-mode.patch
Patch110: 0110-fips-udev-trigger-with-action-add.patch
Patch111: 0111-dracut-let-fwdir-be-specified-multiple-times.patch
Patch112: 0112-dracut-functions-use-proc-self-mountinfo-instead-of-.patch
Patch113: 0113-dracut-add-fstab-to-ignore-proc-self-mountinfo.patch
Patch114: 0114-plymouth-load-dm_crypt-module.patch
Patch115: 0115-crypt-depend-on-dm.patch
Patch116: 0116-plymouth-udev-trigger-with-action-add.patch
Patch117: 0117-dm-install-all-md-dm-kernel-modules.patch
Patch118: 0118-mkinitrd-do-not-call-dracut-in-host-only-mode.patch
Patch119: 0119-dmraid-switch-to-rd_NO_MDIMSM-if-no-mdadm-installed.patch
Patch120: 0120-mknod-with-mode-and-set-umask-for-the-rest.patch
Patch121: 0121-plymouth-do-not-create-hvc0.patch
Patch122: 0122-init-set-old-umask-before-switch_root.patch
Patch123: 0123-init-do-not-set-umask-yet.patch
Patch124: 0124-lvm-also-handle-LVM1-volumes.patch
Patch125: 0125-dracut-functions-filter_kernel_modules-search-in-ext.patch
Patch126: 0126-dracut-lib-and-usr-lib-dirs-detection.patch
Patch127: 0127-lvm-install-lvm-mirror-and-snaphot-libs.patch
Patch128: 0128-lvm-support-for-dynamic-LVM-SNAPSHOT-root-volume.patch
Patch129: 0129-95fstab-sys-mount-all-etc-fstab.sys-volumes-before-s.patch
Patch130: 0130-TEST-12-RAID-DEG-mark-test-failed-for-multiple-dummy.patch
Patch131: 0131-test-double-disk-space-for-root-images.patch
Patch132: 0132-network-kill-9-dhclient-if-normal-kill-does-not-succ.patch
Patch133: 0133-md-do-not-use-no-degraded-for-incremental-mode.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} > 12 || 0%{?rhel} >= 6
# no "provides", because dracut does not offer
# all functionality of the obsoleted packages
Obsoletes: mkinitrd <= 6.0.93
Obsoletes: mkinitrd-devel <= 6.0.93
Obsoletes: nash <= 6.0.93
Obsoletes: libbdevid-python <= 6.0.93
%endif
Obsoletes: dracut-kernel < 005
Provides:  dracut-kernel = %{version}-%{release}

Requires: udev
Requires: util-linux-ng
Requires: module-init-tools >= 3.7-9
Requires: cpio
Requires: coreutils
Requires: findutils
Requires: binutils
Requires: grep
Requires: which
Requires: mktemp >= 1.5-5
Requires: mount
Requires: bash
Requires: dash
Requires: /bin/sh 
Requires: fileutils, gzip, tar
Requires: lvm2 >= 2.02.33-9
Requires: filesystem >= 2.1.0, cpio, device-mapper, initscripts >= 8.63-1
Requires: e2fsprogs >= 1.38-12, coreutils
Requires: mdadm
Requires(pre): plymouth >= 0.8.0-0.2009.29.09.19.1
Requires: plymouth >= 0.8.0-0.2009.29.09.19.1
Requires: cryptsetup-luks
Requires: file
Requires: bzip2
Requires: dmraid
Requires: kbd
Requires: plymouth-scripts

%if ! 0%{?with_switch_root}
Requires: util-linux-ng >= 2.16
BuildArch: noarch
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
Requires: rpcbind nfs-utils 
Requires: iscsi-initiator-utils
Requires: dhclient
%if %{with_nbd}
Requires: nbd
%endif
Requires: net-tools iproute
Requires: bridge-utils

%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

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

%package generic
Summary: Metapackage to build a generic initramfs with dracut
Requires: %{name} = %{version}-%{release}
Requires: %{name}-network = %{version}-%{release}

%description generic
This package requires everything which is needed to build a generic
all purpose initramfs with dracut.

%package tools
Summary: Dracut tools to build the local initramfs
Requires: coreutils cryptsetup-luks device-mapper
Requires: diffutils dmraid findutils gawk grep lvm2
Requires: module-init-tools sed
Requires: cpio gzip
Requires: %{name} = %{version}-%{release}

%description tools
This package contains tools to assemble the local initrd and host configuration.

%prep
%setup -q -n %{name}-%{version}%{?dashgittag}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1

%build
make WITH_SWITCH_ROOT=0%{?with_switch_root}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT sbindir=/sbin \
     sysconfdir=/etc mandir=%{_mandir} WITH_SWITCH_ROOT=0%{?with_switch_root}

echo %{name}-%{version}-%{release} > $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/10rpmversion/dracut-version
rm $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/01fips/check

mkdir -p $RPM_BUILD_ROOT/boot/dracut
mkdir -p $RPM_BUILD_ROOT/var/lib/dracut/overlay
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log
touch $RPM_BUILD_ROOT%{_localstatedir}/log/dracut.log

%if 0%{?fedora} <= 12 && 0%{?rhel} < 6
rm $RPM_BUILD_ROOT/sbin/mkinitrd
rm $RPM_BUILD_ROOT/sbin/lsinitrd
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS
/sbin/dracut
%if 0%{?with_switch_root}
/sbin/switch_root
%endif
%if 0%{?fedora} > 12 || 0%{?rhel} >= 6
/sbin/mkinitrd
/sbin/lsinitrd
%endif
%dir %{_datadir}/dracut
%{_datadir}/dracut/dracut-functions
%config(noreplace) /etc/dracut.conf
%dir /etc/dracut.conf.d
%{_mandir}/man8/dracut.8*
%{_mandir}/man5/dracut.conf.5*
%{_datadir}/dracut/modules.d/00dash
%{_datadir}/dracut/modules.d/10redhat-i18n
%{_datadir}/dracut/modules.d/10rpmversion
%{_datadir}/dracut/modules.d/50plymouth
%{_datadir}/dracut/modules.d/60xen
%{_datadir}/dracut/modules.d/90btrfs
%{_datadir}/dracut/modules.d/90crypt
%{_datadir}/dracut/modules.d/90dm
%{_datadir}/dracut/modules.d/90dmraid
%{_datadir}/dracut/modules.d/90dmsquash-live
%{_datadir}/dracut/modules.d/90kernel-modules
%{_datadir}/dracut/modules.d/90lvm
%{_datadir}/dracut/modules.d/90mdraid
%{_datadir}/dracut/modules.d/90multipath
%{_datadir}/dracut/modules.d/95debug
%{_datadir}/dracut/modules.d/95resume
%{_datadir}/dracut/modules.d/95rootfs-block
%{_datadir}/dracut/modules.d/95dasd
%{_datadir}/dracut/modules.d/95dasd_mod
%{_datadir}/dracut/modules.d/95zfcp
%{_datadir}/dracut/modules.d/95terminfo
%{_datadir}/dracut/modules.d/95udev-rules
%{_datadir}/dracut/modules.d/95uswsusp
%{_datadir}/dracut/modules.d/98selinux
%{_datadir}/dracut/modules.d/98syslog
%{_datadir}/dracut/modules.d/99base
# logfile needs no logrotate, because it gets overwritten
# for every dracut run
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log

%files network
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS
%{_datadir}/dracut/modules.d/40network
%{_datadir}/dracut/modules.d/95fcoe
%{_datadir}/dracut/modules.d/95iscsi
%{_datadir}/dracut/modules.d/95nbd
%{_datadir}/dracut/modules.d/95nfs
%{_datadir}/dracut/modules.d/45ifcfg
%{_datadir}/dracut/modules.d/95znet

%files fips
%defattr(-,root,root,0755)
%{_datadir}/dracut/modules.d/01fips

%files generic
%defattr(-,root,root,0755)
%doc README.generic

%files tools 
%defattr(-,root,root,0755)
%{_mandir}/man8/dracut-gencmdline.8*
%{_mandir}/man8/dracut-catimages.8*
/sbin/dracut-gencmdline
/sbin/dracut-catimages
%dir /boot/dracut
%dir /var/lib/dracut
%dir /var/lib/dracut/overlay

%changelog
* Wed Sep 22 2010 Harald Hoyer <harald@redhat.com> 005-4
- backported a lot of bugfixes from git 

* Tue Apr 20 2010 Harald Hoyer <harald@redhat.com> 005-3
- fixed network with multiple nics
- fixed nfsidmap paths
- do not run blkid on non active container raids
- fixed cdrom polling mechanism
- update to latest git

* Thu Apr 15 2010 Harald Hoyer <harald@redhat.com> 005-2
- fixed dracut manpages
- dmraid parse different error messages
- add cdrom polling mechanism for slow cdroms
- add module btrfs
- teach dmsquash live-root to use rootflags
- trigger udev with action=add
- fixed add_drivers handling 
- add sr_mod
- use pigz instead of gzip, if available

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 005-1
- version 005

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

