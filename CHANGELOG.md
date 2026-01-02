# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project uses YYYY.MM.DD [calendar versioning](https://calver.org/).

## Unreleased

### Added

- Several missing `fontforge` classes:
  - `awglyph`
  - `awcontext`
  - `references`
  - `mathKern`
  - `layer_array`
  - `math.device_table`
  - `cvt`
  - `layerinfo`
  - `layerinfo_array`

### Changed

- `GlyphMathKerning` to `mathKern`
  - `mathKern` attributes to be optional
- `glyph.activeLayer` to a property with more accurate typing
- `glyph.references` to a property with more accurate typing
- `math` "DeviceTable" attributes to properties with more accurate typing
- `FontLayerInfo` to `layerinfo`
- `font.cvt` to a property with more accurate typing

### Fixed

- Typing of `registerGlyphSeparationHook` `hook` parameter

## 2025.12.1 - 2025-12-01

### Added

- Missing `no-mac-names` flag for `font.generateTtc`

### Changed

- Several class attributes to properties to:
  - Handle setters that accept a wider range of types than returned by their
    getters
  - Represent attributes that are read-only
- Widen typing of flags to accept a string for a single flag or a sequence
  of strings

### Fixed

- `font.gasp` to be a tuple of arbitrary length

## 2025.11.28 - 2025-11-28

### Added

- Missing `no-mac-names` flag for `font.generate`
- More variants of the `point` initializer
- `point` comparison methods
- `contour.__delitem__` by `slice`
- Optional `layer` parameter of `glyph.boundingBox`

### Changed

- `font.addLookup` docstring to document mark sets
- `font.__contains__` to accept a glyph encoding (`int`)
- `feature_script_lang_tuple` parameter of `font.addLookup` to accept a single
  string for the languages

### Fixed

- `font.markClasses` to be a tuple of arbitrary length
- `glyph.anchorPoints` to be a tuple of arbitrary length
- `glyph.anchorPointsWithSel` to be a tuple of arbitrary length
- `hvcurve` flag in `glyph.setLayer`
- Remove nonexistent parameter of `UnicodeBlockCountFromLib`
- Return type of `contour.moveTo` to `Self`
- `font.mergeFeature` boolean parameter to have a default value

## 2025.11.10 - 2025-11-10

### Added

- Several missing `fontforge` module members:
  - `userConfigPath`
  - `onAppClosing`
  - `getConvexNib`
  - `setConvexNib`
  - `layer.reverseDirection`
  - `glyph.codepoint`
  - `glyph.xBoundsAtY`
  - `glyph.yBoundsAtX`
  - `selection.font`
  - `font.creationtime`
  - `font.markClasses`
  - `font.os2_winascent_add`
  - `font.os2_windescent_add`
  - `font.xuid`
  - `font.clearSpecialData`

### Fixed

- Return type of `glyph.getPosSub`
- `gsub_reversecchain` lookup type in `font.addLookup`

## 2025.10.13 - 2025-10-13

### Added

- Various undocumented method overloads and parameters

### Fixed

- Various typos in docstrings
- Return types of several class methods from `None` to `Self`

## 2025.9.30 - 2025-09-30

### Added

- Initial stubs for `fontforge` and `psMat`
