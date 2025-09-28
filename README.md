# fontforge-stubs

This package provides PEP 561 type stubs and docstrings for
[FontForge](https://github.com/fontforge/fontforge)'s Python modules:

- `fontforge`
- `psMat`

The stubs and docstrings were created by referencing the official FontForge
Python Module documentation and -- when necessary -- the FontForge Python
extension source code.

## Motivation

FontForge provides powerful Python C extension modules. By nature, they do not
contain typing information. Combined with inconsistent naming conventions and
at times ambiguous documentation, FontForge Python scripting is unnecessarily
arduous.

Perhaps you can relate to:

- Never remembering if it's `glyph.name`, `glyph.glyphName`, or `glyph.glyph_name`
- Reading the docs and still not knowing whether `width` is an `int` or a `float`
- Parsing and re-parsing the documentation to figure out the structure of a
  feature-script-lang tuple

With type stubs, editors can provide autocompletion, and type checkers can
identify errors previously only discovered when running your script with
FontForge. Built-in documentation removes the need to constantly switch between
your editor and external documentation -- further increasing productivity.

## Installation

Install the package in your development environment:

```
pip install fontforge-stubs
```

Your editor/type-checker should automatically pick up the stubs.

## Versioning and Compatibility

This project uses YYYY.MM.DD [calendar versioning](https://calver.org/).

It aims to be compatible with FontForge 20230101 and later. Legacy and
deprecated FontForge Python APIs are not officially supported.

## Contributing

If you find any issues with the type stubs, please open an issue and/or pull request.

## License

This project is under the [MIT License](./LICENSE).

The stubs and docstrings in this project were closely derived from the
[FontForge source](https://github.com/fontforge/fontforge). In particular,
`fontforge.rst`, `psMat.rst`, and `python.c`. See [NOTICE](./NOTICE).
