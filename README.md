# Android-Strings-Format

This script takes a strings resource as a model and a second one as a target.
It will format the target strings resource in order to keep the same tags and comments order as the model one.
Be aware that the target strings resource will be overwritten if no output file has been specified.
The script will also warn you if a resource is missing inside the target `strings.xml` file.

You need to run this script inside of the res directory of your Android project.
Example of usage: python android-strings-format.py --target fr --output formatted_strings.xml

Package is also available on PyPI:
https://pypi.python.org/pypi/android-strings-format/

## Getting started
Requirements:

* Python >= 2.7.*
* [Standard Android project structure](https://developer.android.com/tools/projects/index.html) for localized values-* folders in `res/` folder

To install run:
```bash
pip install android-strings-format
```

## Usage

`cd` into your `res/` folder, and run:

python android-strings-format.py [-h] [-m MODEL] -t TARGET
                                 [-o OUTPUT]

*  -h, --help            show this help message and exit

*  --model MODEL, -m MODEL
                        Language code of the strings resource to use as model (ex: en, fr...).
                        If not specified, strings.xml inside the default
                        values directory will be used as the model.

*  --target TARGET, -t TARGET
                        Language code of the strings resource to format (ex: en, fr).

*  --output OUTPUT, -o OUTPUT
                        Path to the output formatted strings resource (ex: output.xml). If not
                        specified, the target strings resource file will be
                        overwritten.

## Example

Target inside `values` directory
```xml
<?xml version="1.0" encoding="utf-8"?>

<!--
  Copyright 2016 Jonathan Odul
  Blablablabla
-->

<resources>
    <!-- Application name -->
    <string name="app_name">APP</string>

    <!-- Dialog texts -->
    <string name="loading">Loading…</string>
    <string name="loading_data">Loading data…</string>
    <string name="processing">Processing…</string>
    <string name="please_wait">Please wait…</string>

    <!-- Dialog button texts -->
    <string name="ok">Ok</string>
    <string name="refresh">Refresh</string>
    <string name="cancel">Cancel</string>
    <string name="quit">Quit</string>

    <!-- Error message -->
    <string name="no_sdcard">No SD card mounted.
    \nPlease mount a sd card to use this application.</string>

    <!-- Modes -->
    <string-array name="modes">
        <item>Single</item>
        <item>Shuffle</item>
        <item>Repeat</item>
    </string-array>

    <!-- Plurals: time_minute -->
    <plurals name="time_minute">
        <item quantity="one">%1$d minute</item>
        <item quantity="other">%1$d minutes</item>
    </plurals>

</resources>
```

Model inside `values-fr` directory
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Resources not formatted. What a disaster -->
    <string name="app_name">VG Music</string>

    <string name="loading">
        Chargement en cours…</string>
    <string name="loading_data">Chargement des données…</string>

    <string name="before_leaving">Avant de partir…</string>
    <string name="no_sdcard">Aucune carte SD détéctée.
    \nVeuillez obtenir une carte SD avant d\'utiliser cette application.</string>

    <string name="cancel">Annuler</string>
    <string name="quit">Quitter</string>
    <!-- Modes -->
<string-array name="modes">
        <item>Simple</item>
        <item>Aléatoire</item>
        <item>Répétition</item>
    </string-array>

    <string name="processing">Traitement en cours…</string>
<string name="please_wait">Veuillez patienter quelques instants…</string>

    <!-- Plurals: time_minute -->
    <plurals name="time_minute">
        <item quantity="one">%1$d minute</item>
        <item quantity="other">%1$d minutes</item>
    </plurals>

    <string name="refresh">Rafraîchir</string>

    <!-- To be deleted -->
    <string name="unused_resource">Omelette du fromage</string>
    </resources>
```

Running command
```bash
python android-strings-format.py --target fr --output formatted_strings.xml
```

Output
```xml
Processing with...
    model: values/strings.xml
    target: values-fr/strings.xml
Warning: resource 'ok' does not exist inside values-fr/strings.xml
Saved formatted strings resource to: formatted_strings.xml
```

formatted_strings.xml
```xml
<?xml version='1.0' encoding='UTF-8'?>
<!--
  Copyright 2016 Jonathan Odul
  Blablablabla
-->
<resources>
    <!-- Application name -->
    <string name="app_name">VG Music</string>

    <!-- Dialog texts -->
    <string name="loading">
        Chargement en cours…</string>
    <string name="loading_data">Chargement des données…</string>
    <string name="processing">Traitement en cours…</string>
    <string name="please_wait">Veuillez patienter quelques instants…</string>

    <!-- Dialog button texts -->
    <string name="ok">Ok</string>
    <string name="refresh">Rafraîchir</string>
    <string name="cancel">Annuler</string>
    <string name="quit">Quitter</string>

    <!-- Error message -->
    <string name="no_sdcard">Aucune carte SD détéctée.
    \nVeuillez obtenir une carte SD avant d\'utiliser cette application.</string>

    <!-- Modes -->
    <string-array name="modes">
        <item>Simple</item>
        <item>Aléatoire</item>
        <item>Répétition</item>
    </string-array>

    <!-- Plurals: time_minute -->
    <plurals name="time_minute">
        <item quantity="one">%1$d minute</item>
        <item quantity="other">%1$d minutes</item>
    </plurals>

</resources>
```

Much better, right?

