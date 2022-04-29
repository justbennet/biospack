# Tricks and handy spack commands

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

