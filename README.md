# Biospack

These are files that provide local customization for the Spack installation
that is used to provide Bioinformatics packages on the Great Lakes and
Armis clusters.  This was all intended for use on Red Hat 8 systems, and
the Spack installation will cohabit software installed in the traditional
manner.  We are consciously restricting ourselves to non-MPI software,
and only for Bioinformatics.

The presumption is that these will be used to set up the test Spack for a
new contributor, so all the settings in the configuration files presume a
root directory of `/var/software/$USER`, and that all Spack created files
(including temporary files) will be in directories beneath it.

The files in the repository can be modified to create a Spack installation
to provide the production installation intended for real users.  The targets
should be

Software:  `/sw/pkgs/bio`
Modules:  `/sw/modules/bio/spack`

To set up a new installation, first run the `start_new_biospack` script.
That will create the `/var/software/$USER/bio` directory, clone Spack
itself into it, prompt you for the version of Spack to set, create the
directories used for Spack temporary and cache files.
