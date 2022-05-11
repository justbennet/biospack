# Tricks and handy spack commands

To get a list of avaialble versions not the full `info` (see below), use

```
$ spack versions samtools
==> Safe versions (already checksummed):
  1.13  1.12  1.10  1.9  1.8  1.7  1.6  1.5  1.4  1.3.1  1.2  0.1.8
==> Remote versions (not yet checksummed):
  1.15.1  1.15  1.14  1.11
```

Show the `specs` of installed packages

```
$ spack find
==> 60 installed packages
-- linux-rhel8-skylake_avx512 / gcc@8.4.1 -----------------------
autoconf@2.69                gcc@10.3.0       m4@1.4.19      readline@8.1
. . . .
```

Regenerate module files to update content or layout with `refresh`.
Use --delete-tree to delete the module file tree before refresh.
Add -y option if you are sure and don't want to be prompted to confirm

```
$ spack module lmod refresh --delete-tree
```

Garbage Collector command: uninstall all unneeded packages

```
$  spack gc
```

These two were gleaned from Slack.  Someone wanted to run `spack uninstall
--all` and was getting an error.

```
$ spack clean -a
$ spack reindex
```

were suggested to get things back on track.

To get detailed information about a package use `spack info package_name`.

```
$ spack info blat
```
[Full output](./blat_info.md)

To see the depencies of a package, use
```
$ spack dependencies -i plink-ng
==> Dependencies of plink-ng@220503%gcc@10.3.0/zgl226z
-- linux-rhel8-haswell / gcc@10.3.0 -----------------------------
3ntlyrq cblas@2015-06-06  d5sydgn zlib@1.2.11
mslmaxc openblas@0.3.18   z6it5pz zstd@1.5.0
```

To see what depends on a package (its dependents), use
```
$ spack dependents -i openblas@0.3.18
==> Dependents of openblas@0.3.18%gcc@10.3.0/mslmaxc
-- linux-rhel8-haswell / gcc@10.3.0 -----------------------------
3ntlyrq cblas@2015-06-06  zgl226z plink-ng@220503
```

To refresh modules, we currently have to blast the module tree and regenerate,
```
spack module lmod refresh -y --delete-tree
```
There is a bug that gives `permission denied` to anyone who didn't create the
tree.
