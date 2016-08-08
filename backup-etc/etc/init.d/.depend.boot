TARGETS = mountkernfs.sh fake-hwclock hostname.sh udev mountdevsubfs.sh hwclock.sh checkroot.sh alsa-utils mountall.sh mountall-bootclean.sh mountnfs.sh mountnfs-bootclean.sh networking urandom bootmisc.sh procps checkroot-bootclean.sh checkfs.sh udev-finish raspi-config kmod
INTERACTIVE = udev checkroot.sh checkfs.sh
udev: mountkernfs.sh
mountdevsubfs.sh: mountkernfs.sh udev
hwclock.sh: mountdevsubfs.sh
checkroot.sh: hwclock.sh fake-hwclock mountdevsubfs.sh hostname.sh
alsa-utils: mountall.sh mountall-bootclean.sh mountnfs.sh mountnfs-bootclean.sh
mountall.sh: checkfs.sh checkroot-bootclean.sh
mountall-bootclean.sh: mountall.sh
mountnfs.sh: mountall.sh mountall-bootclean.sh networking
mountnfs-bootclean.sh: mountall.sh mountall-bootclean.sh mountnfs.sh
networking: mountkernfs.sh mountall.sh mountall-bootclean.sh urandom procps
urandom: mountall.sh mountall-bootclean.sh hwclock.sh
bootmisc.sh: mountall-bootclean.sh mountall.sh mountnfs.sh mountnfs-bootclean.sh udev checkroot-bootclean.sh
procps: mountkernfs.sh mountall.sh mountall-bootclean.sh udev
checkroot-bootclean.sh: checkroot.sh
checkfs.sh: checkroot.sh
udev-finish: udev mountall.sh mountall-bootclean.sh
raspi-config: udev mountkernfs.sh mountall.sh mountall-bootclean.sh mountnfs.sh mountnfs-bootclean.sh
kmod: checkroot.sh
