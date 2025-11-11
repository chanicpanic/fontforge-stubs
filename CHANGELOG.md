# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project uses YYYY.MM.DD [calendar versioning](https://calver.org/).

## Unreleased

### Added

- Several missing module members:
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
