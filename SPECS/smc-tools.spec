Name:           smc-tools
Version:        1.8.3
Release:        3%{?dist}
Summary:        Shared Memory Communication Tools

License:        EPL-1.0
URL:            https://www.ibm.com/developerworks/linux/linux390/smc-tools.html

Requires:       man
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  bash-completion

Source0:        https://github.com/ibm-s390-linux/%{name}/archive/refs/tags/%{version}.tar.gz

Patch0:         smc-tools-1.6.0-smc_chk-py3.patch
Patch1:         1-0b965ae9b5ad.patch
Patch2:         2-61129ccb308b.patch
Patch3:         3-3cb6fbb2afac.patch
Patch4:         4-108d5124b837.patch
Patch5:         5-a60b96821be3.patch

%description
The Shared Memory Communication Tools (smc-tools) package enables usage of SMC
sockets in Linux.

%prep
%forgesetup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%make_build CFLAGS="%{build_cflags} -I%{_includedir}/libnl3" LDFLAGS="%{build_ldflags}" V=1

%install
%make_install V=1

%files
%license LICENSE
%doc README.md
%{_datadir}/bash-completion/
%{_mandir}/man7/af_smc.7.gz
%{_mandir}/man8/smc*
%{_bindir}/smc_pnet
%{_bindir}/smc_run
%{_bindir}/smcss
%{_bindir}/smcd
%{_bindir}/smcr
%{_bindir}/smc_dbg
%ifarch s390x
%{_bindir}/smc_rnics
%{_bindir}/smc_chk
%endif
%{_bindir}/smc_dbg
%{_libdir}/libsmc-preload.so*

%changelog
* Tue Aug 04 2026 Čestmír Kalina <ckalina@redhat.com> - 1.8.3-3
- Resolves: RHEL-224216
- fix rpminspect license and debuginfo errors

* Tue Jun 23 2026 Čestmír Kalina <ckalina@redhat.com> - 1.8.3-2
- Resolves: RHEL-159089
- smc-tools: smc_rnics is not listing the NetH/NetD cards inside the guest

* Mon Oct 09 2023 Čestmír Kalina <ckalina@redhat.com> - 1.8.3-1
- Resolves: RHEL-11417 Upgrade smc-tools to latest version
- smc_stats: Fix man page name
- Bump version.

* Mon Dec 05 2022 Čestmír Kalina <ckalina@redhat.com> - 1.8.2-1
- Resolves: #2110414 Upgrade smc-tools to latest version

* Thu Jun 23 2022 Čestmír Kalina <ckalina@redhat.com> - 1.8.1-1
- Upgrade smc-tools to latest version
- Add User-defined EID (Enterprise ID) Support
- Resolves: #1919228
- Resolves: #2043841

* Mon Oct 18 2021 Čestmír Kalina <ckalina@redhat.com> - 1.6.1-1
- Upgrade smc-tools to latest version
- Resolves: #1984975

* Fri Jul 16 2021 Čestmír Kalina <ckalina@redhat.com> - 1.6.0-3
- Patch stats.c to fix overruns
- Patch stats.c to fix leaks
- Patch stats.c to fix fallback counter values
- Resolves: #1993469

* Fri Jul 16 2021 Čestmír Kalina <ckalina@redhat.com> - 1.6.0-2
- Patch smc_chk to use platform-python
- Resolves: #1981727

* Fri Jul 02 2021 Čestmír Kalina <ckalina@redhat.com> - 1.6.0-1
- Resolves: #1869292 Statistics Support - smc-tools part
- Resolves: #1919225 Add SMC-D Setup Check (smc-tools)
- Resolves: #1919240 Upgrade smc-tools to latest version
* Wed Feb 10 2021 Čestmír Kalina <ckalina@redhat.com> - 1.5.0-2
- Resolves: #1924787
- Add python3/man requires
* Mon Feb 08 2021 Čestmír Kalina <ckalina@redhat.com> - 1.5.0-1
- Resolves: #1924787
- Upgrade to 1.5.0
* Mon Jan 04 2021 Čestmír Kalina <ckalina@redhat.com> - 1.4.0-3
- Resolves: #1879128
- Add bash-completion to build requires

* Mon Jan 04 2021 Čestmír Kalina <ckalina@redhat.com> - 1.4.0-1
- Resolves: #1851143
- Update to 1.4.0
- Explicitly state libnl3 in include path

* Tue Jun 23 2020 Čestmír Kalina <ckalina@redhat.com> - 1.3.0-1
- Resolves: #1780304
- Update to 1.3.0

* Wed Nov 06 2019 Čestmír Kalina <ckalina@redhat.com> - 1.2.2-3
- Resolves: rhbz#1726264
- Release bump to force brew rebuild due to tagging failure.

* Wed Nov 06 2019 Čestmír Kalina <ckalina@redhat.com> - 1.2.2-2
- Resolves: rhbz#1726264
- update to 1.2.2

* Mon May 20 2019 Čestmír Kalina <ckalina@redhat.com> - 1.2.1-2
- Resolves: rhbz#1706015
- guards smc_rnics man with %ifarch s390x to avoid build failure

* Mon May 20 2019 Čestmír Kalina <ckalina@redhat.com> - 1.2.1-1
- Resolves: rhbz#1706015

* Tue Apr 02 2019 Čestmír Kalina <ckalina@redhat.com> - 1.2.0-2
- Resolves: rhbz#1683274
- guards smc_rnics with %ifarch s390x

* Tue Apr 02 2019 Čestmír Kalina <ckalina@redhat.com> - 1.2.0-1
- Resolves: rhbz#1683274
- update to 1.2.0

* Mon Jul 09 2018 Dan Horák <dan@danny.cz> - 1.1.0-1
- update to 1.1.0

* Mon Apr 16 2018 Dan Horák <dan@danny.cz> - 1.0.0-4
- fix LDFLAGS injection (#1567902)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Dan Horák <dan@danny.cz> - 1.0.0-2
- use make macro
- comment patches
- use distro LDFLAGS in build

* Mon Jan  8 2018 Dan Horák <dan@danny.cz> - 1.0.0-1
- initial Fedora version
