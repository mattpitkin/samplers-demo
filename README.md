# samplers-demo

A demonstration of various Python MCMC samplers and Nested Sampling routines.

The website generated from this repository can be found [here](http://mattpitkin.github.io/samplers-demo/).

## Building the site

The [Makefile](Makefile) can be used to build the website locally with:

```
make publish
```

This should work if in a Conda environment generated with the [environment.yml](environment.yml) - in particular, note that nbconvert<=5.5.0 is required as the "basic" template has been removed in later versions. To publish the website to github use:

```
make publish-to-github
```
