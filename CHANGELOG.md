Prospector Changelog
=======
## Version 0.6

* Module and package finding has been centralised into a `finder.py` module, from which all tools take the list of files to be inspected. This helps unify which files get inspected, as previously there were several times when tools were not correctly ignoring files.
* Frosted [cannot handle non-utf-8 encoded files](https://github.com/timothycrosley/frosted/issues/56) so a workaround has been added to simply ignore encoding errors raised by Frosted until the bug is fixed. This was deemed okay as it is very similar to pyflakes in terms of what it finds, and pyflakes does not have this problem.
* [#43](https://github.com/landscapeio/prospector/issues/43) - the blender is now smarter, and considers that a message may be part of more than one 'blend'. This means that some messages are no longer duplicated.
* [#42](https://github.com/landscapeio/prospector/issues/42) - a few more message pairs were cleaned up, reducing ambiguity and redundancy
* [#33](https://github.com/landscapeio/prospector/issues/33) - there is now an output format called `pylint` which mimics the pylint `--parseable` output format, with the slight difference that it includes the name of the tool as well as the code of the message.
* [#37](https://github.com/landscapeio/prospector/issues/37) - profiles can now use the extension `.yml` as well as `.yaml`
* [#34](https://github.com/landscapeio/prospector/issues/34) - south migrations are ignored if in the new south name of `south_migrations` (ie, this is compatible with the post-Django-1.7 world)

## Version 0.5.6 / 0.5.5

* The pylint path handling was slightly incorrect when multiple python modules were in the same directory and importing from each other, but no `__init__.py` package was present. If modules in such a directory imported from each other, pylint would crash, as the modules would not be in the `sys.path`. Note that 0.5.5 was released but this bugfix was not correctly merged before releasing. 0.5.6 contains this bugfix.

## Version 0.5.4

* Fixing a bug in the handling of relative/absolute paths in the McCabe tool

## Version 0.5.3

##### New Features

* Python 3.4 is now tested for and supported

##### Bug Fixes

* Module-level attributes can now be documented with a string without triggering a "String statement has no effect" warning
* [#28](https://github.com/landscapeio/prospector/pull/28) Fixed absolute path bug with Frosted tool

## Version 0.5.2

##### New Features

* Support for new error messages introduced in recent versions of `pep8` and `pylint` was included.

## Version 0.5.1

##### New Features

* All command line arguments can now also be specified in a `tox.ini` and `setup.cfg` (thanks to [Jason Simeone](https://github.com/jayclassless))
* `--max-line-length` option can be used to override the maximum line length specified by the chosen strictness

##### Bug Fixes

* [#17](https://github.com/landscapeio/prospector/issues/17) Prospector generates messages if in a path containing a directory beginning with a `.` - ignore patterns were previously incorrectly being applied to the absolute path rather than the relative path.
* [#12](https://github.com/landscapeio/prospector/issues/12) Library support for Django now extends to all tools rather than just pylint
* Some additional bugs related to ignore paths were squashed.

## Version 0.5
 
* Files and paths can now be ignored using the `--ignore-paths` and `--ignore-patterns` arguments.

* Full PEP8 compliance can be turned on using the `--full-pep8` flag, which overrides the defaults in the strictness profile.
* The PEP8 tool will now use existing config if any is found in `.pep8`, `tox.ini`, `setup.cfg` in the path to check, or `~/.config/pep8`. These will override any other configuration specified by Prospector. If none are present, Prospector will fall back on the defaults specified by the strictness.
* A new flag, `--external-config`, can be used to tweak how PEP8 treats external config. `only`, the default, means that external configuration will be preferred to Prospector configuration. `merge` means that Prospector will combine external configuration and its own 
values. `none` means that Prospector will ignore external config.

* The `--path` command line argument is no longer required, and Prospector can be called with `prospector path_to_check`.

* Pylint version 1.1 is now used.

* Prospector will now run under Python3.

## Version 0.4.1

* Additional blending of messages - more messages indicating the same problem from different tools are now merged together
* Fixed the maximum line length to 160 for medium strictness, 100 for high and 80 for very high. This affects both the pep8 tool and pylint.

## Version 0.4

* Added a changelog
* Added support for the [dodgy](https://github.com/landscapeio/dodgy) codebase checker
* Added support for pep8 (thanks to [Jason Simeone](https://github.com/jayclassless))
* Added support for pyflakes (thanks to [Jason Simeone](https://github.com/jayclassless))
* Added support for mccabe (thanks to [Jason Simeone](https://github.com/jayclassless))
* Replaced Pylint W0312 with a custom checker. This means that warnings are only generated for inconsistent indentation characters, rather than warning if spaces were not used.
* Some messages will now be combined if Pylint generates multiple warnings per line for what is the same cause. For example, 'unused import from wildcard import' messages are now combined rather than having one message per unused import from that line.
* Messages from multiple tools will be merged if they represent the same problem.
* Tool failure no longer kills the Prospector process but adds a message instead.
* Tools can be enabled or disabled from profiles.
* All style warnings can be suppressed using the `--no-style-warnings` command line switch.
* Uses a newer version of [pylint-django](https://github.com/landscapeio/pylint-django) for improved analysis of Django-based code.
