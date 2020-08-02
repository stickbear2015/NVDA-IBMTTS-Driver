# IBMTTS driver, Add-on for NVDA #
  This add-on implements NVDA compatibility with the IBMTTS synthesizer.
  We can not distribute the IBMTTS libraries. So it is just the driver.
  If you want to improve this driver, feel free to send your pull requests!

# Download.
The latest release is available to [download in this link](https://davidacm.github.io/getlatest/gh/davidacm/NVDA-IBMTTS-Driver)

# Features:
* Voice, variant, rate, pitch, inflection and volume  setting support.
* Extra head size, Roughness, Breathiness parameters settings support. Create your own voice!
* Enable or disable backquote voice tags. Disable it to protect yourself from malisious codes from jokers, enable it to do many fun things with the synthesizer. Safe fun guaranteed!
* Rate boost. If the synthesizer does not speak very fast to  you, then enable it and get the maximum voice speech!
* auto language changes. Let the synthesizer to read texts in the correct language.
* Indexing support. The cursor will never be lost when using read all feature.
* anti crashing filter expressions. The driver filters known crashing expressions.

# Requirements.
## NVDA.
  You need NVDA 2018.4 or later. This driver is compatible with python 3, So you can use it with future NVDA versions. Once NVDA with python 3 is released, this driver will no longer be compatible with python 2.7. Please use the latest NVDA versions. Its free!

## IBMTTS synthesizer libraries.
  This is just the driver, you must   get the libraries from  somewhere else.

# Installation.
  Just install it as a NVDA add-on. Then open NVDA dialog settings, and set the IBMTTS folder files in the IBMTTS category.
  Also in this category you can copy the external IBMTTS files into an Add-on to use it locally.

# Packaging it for distribution.
  Open a command line, change to the Add-on root folder  and run the scons command. The created add-on, if there were no errors, is placed in the root directory.

## Notes:

* if the synthesizer is inside the add-on or in "eciLibraries" add-on, the driver will update the ini library paths automatically. So you can use it on portable NVDA versions.
* when you use the "Copy IBMTTS files in an  add-on" button, it will create a new add-on. So, if you want to uninstall IBMTTS, you'll need to uninstall two add-ons: "IBMTTS driver" and "Eci libraries".
* scons and gettext tools on this project are  compatible with python 3 only. Doesn't work with python 2.7.
* You can put the extra IBMTTS required files in the add-on (for personal use only). Just copy them in "addon\synthDrivers\ibmtts" folder. Adjust the default library name in "settingsDB.py" if necessary.

# References.
This driver is based on the IBM tts sdk, the documentation is available on:
[this link](http://www.wizzardsoftware.com/docs/tts.pdf)

Or you can get a copy on [this repo](https://github.com/david-acm/NVDA-IBMTTS-Driver)

See the files
[tts.pdf](https://cdn.jsdelivr.net/gh/davidacm/NVDA-IBMTTS-Driver/apiReference/tts.pdf)
or [tts.txt.](https://cdn.jsdelivr.net/gh/davidacm/NVDA-IBMTTS-Driver/apiReference/tts.txt)