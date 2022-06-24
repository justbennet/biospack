# Setting Spack up

Rightly or not, we use a Spack 'sandbox' to test installations and
make sure that the dependencies pulled are sane, and all errors
in installation have been resolved prior to installing into the
production environment.

Spack is set up mostly the same way regardless whether it is the
sandbox or a new production version (as on a new cluster).  Some
configuration files will be different to account for different
paths, but that should be the only difference.

The production environment, as of 24 June, 2022, is used only to
install and manage a set of bioinformatics packages.  The root
of the installation is at `/sw/spack/bio`.  The structure under
that is:

```
/sw/spack/bio
    /local-packages   # locally modified Spack packages
    /modules          # Spack installed module files
    /pkgs             # Spack installed software
    /spack            # Spack itself
```

We recommend changing only the root and keeping a parallel
structure underneath.  In this example, we will use
`/var/software/$USER/bio` as the root for the sandbox and
the path above as the production path.  NOTE:  Spack also
has a `$user` variable; we will use the all uppercase version
to mean the shell variable and the all lowercase version to
mean the Spack variable.

# Spack configuration

The first configuration step is to set

```
SPACK_USER_CACHE_PATH=/tmp/$USER/spack-cache
SPACK_DISABLE_LOCAL_CONFIG=true
```

Create the directories needed.

```
$ for dir in local-packages modules pkgs ; do
    mkdir -p /var/software/$USER/bio/$dir
done
```

Clone Spack source.

```
$ cd /var/software/$USER/bio
$ git clone git@github.com:spack/spack.git
```

Clone this repository if you have not already.  We will
assume that `biospack` and `bio` are in the same directory
hereafter.

```
$ cd /var/software/$USER
$ git clone git@github.com:justbennet/biospack.git
```

Copy the configuration files from `biospack` to `bio` and
modify for your configuration.

```
$ cd bio/spack/etc/spack
$ cp /var/software/$USER/biospack/spack/etc/spack/*.yaml .
```

Modify `config.yaml` by choosing the correct `root:` attribute for
`install_tree:` and the correct `lmod:` for the `module_roots:`.

