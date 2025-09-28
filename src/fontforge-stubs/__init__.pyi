"""
The primary module for interacting with FontForge
"""

from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
from typing import (
    Any,
    Final,
    Literal,
    NoReturn,
    TypeAlias,
    TypedDict,
    TypeVar,
    overload,
    override,
)

from typing_extensions import (
    NotRequired,
    Unpack,
    deprecated,
)

T = TypeVar("T")

# Module attributes

class GlobalHooks(TypedDict):
    newFontHook: Callable[[font], None]
    """
    This function will be called when a new font has been created.
    """

    loadFontHook: Callable[[font], None]
    """
    This function will be called when a font is loaded from disk.
    (if a font has an "initScriptString" entry in its persistent
    dictionary, that script will be invoked before this function).
    """

hooks: GlobalHooks
"""
A dictionary which the user may fill to associate certain FontForge
events with a python function to be run when those events happen.
The function will be passed the font (or possibly glyph) for which
the relevant event occurred.
"""

splineCorner: Final = 0
"""A point type enumeration of value 0"""

splineCurve: Final = 1
"""A point type enumeration of value 1"""

splineHVCurve: Final = 2
"""A point type enumeration of value 2"""

splineTangent: Final = 3
"""A point type enumeration of value 3"""

spiroG4: Final = 1
"""A spiro point type enumeration of value 1.

A Spiro G4 curve point"""

spiroG2: Final = 2
"""
A spiro point type enumeration of value 2.

A Spiro G2 curve point
"""

spiroCorner: Final = 3
"""
A spiro point type enumeration of value 3.

A Spiro corner point
"""

spiroLeft: Final = 4
"""
A spiro point type enumeration of value 4.

A Spiro left "tangent" point
"""

spiroRight: Final = 5
"""
A spiro point type enumeration of value 5.

A Spiro right "tangent" point
"""

spiroOpen: Final = 6
"""
A spiro point type enumeration of value 6.

This may only be used on the first point in a spiro tuple. It indicates that
the tuple describes an open contour.
"""

unspecifiedMathValue: Final
"""A constant, used when the value is unspecified"""

# Module functions

def getPrefs(pref_name: str) -> Any:
    """returns the value of the named preference item"""
    ...

def setPrefs(pref_name: str, value: Any) -> None:
    """sets the value of the named preference item"""
    ...

def hasSpiro() -> bool:
    """Returns a boolean, ``True`` if Raph Levien's spiro package is available for use in FontForge."""
    ...

def savePrefs() -> None:
    """Saves the current preference settings"""
    ...

def loadPrefs() -> None:
    """Loads the user's default preference settings. Not done automatically in a script."""
    ...

def defaultOtherSubrs() -> None:
    """Sets the type1 PostScript OtherSubrs to the default value"""
    ...

def readOtherSubrsFile(filename: str) -> None:
    """Sets the type1 PostScript OtherSubrs to the stuff found in the file."""
    ...

def loadEncodingFile(filename: str, encname: str | None = None) -> str | None:
    """
    Loads an encoding file, returns the name of the encoding or ``None``. When
    loading encodings in Unicode consortium format, an encname has to be specified
    or the encoding will be ignored and ``None`` will be returned.
    """
    ...

def loadNamelist(filename: str) -> None:
    """Loads a namelist"""
    ...

def loadNamelistDir(dirname: str) -> None:
    """Loads all namelist files in the directory"""
    ...

def preloadCidmap(filename: str, registry: str, order: str, supplement: int) -> None:
    """Loads a FontForge cidmap file"""
    ...

def printSetup(
    type: Literal["lp", "lpr", "ghostview", "command", "ps-file", "pdf-file"],
    printer_or_cmd_or_file: str | None = None,
    width: float | None = None,
    height: float | None = None,
) -> None:
    """
    Prepare to print a font sample.
    The first argument may be one of:

    lp:

      Queues postscript output to the printer using lp.
      You may use the optional second argument to specify the printer name.

    lpr:

      Queues postscript output to the printer using lpr.
      You may use the optional second argument to specify the printer name.

    ghostview:

      Displays the output using ghostview (or gv). The second argument is ignored.

    command:

      Use a custom shell command to print the output.
      The second argument should contain the command and its arguments.

    ps-file:

      Dump the postscript output to a file. The second argument specifies the filename.

    pdf-file:

      Dump the output as pdf to a file. The second argument specifies the filename.

    The third and fourth arguments are optional and specify the page size
    (in points) for the output. The third argument is the page width and the
    fourth is the height. These settings remain until changed.
    """
    ...

def nameFromUnicode(uni: int, namelist: str | None = None) -> str:
    """
    Finds the glyph name associated with a given unicode codepoint. If a
    namelist is specified the name will be taken from that.
    """
    ...

def UnicodeAnnotationFromLib(n: int) -> str:
    """
    Returns the Unicode Annotations for this value as described by
    www.unicode.org. If there is no unicode annotation for this value, or no
    library available, then return empty string "". It can execute with no
    current font.
    """
    ...

def UnicodeBlockCountFromLib(n: int) -> int:
    """
    Return the number of Unicode Blocks as described by www.unicode.org.
    Currently, the blocks are {0..233}, spanning unicode values {uni0..uni10FFFF}.
    If there is no value, then return -1. This can execute with no current font.
    """
    ...

def UnicodeBlockEndFromLib(n: int) -> int:
    """
    Returns the Unicode Block end value as described by www.unicode.org.
    Currently, the blocks are {0..233}, spanning unicode values {uni0..uni10FFFF}.
    If there is no value, then return -1. This can execute with no current font.
    """
    ...

def UnicodeBlockNameFromLib(n: int) -> str:
    """
    Returns the Unicode Block Name as described by www.unicode.org.
    Currently, the blocks are {0..233}, spanning unicode values {uni0..uni10FFFF}.
    If there is no value, then return empty string "". This can execute with no
    current font.
    """
    ...

def UnicodeBlockStartFromLib(n: int) -> int:
    """
    Returns the Unicode Block start value as described by www.unicode.org.
    Currently, the blocks are {0..233}, spanning unicode values {uni0..uni10FFFF}.
    If there is no value, then return -1. This can execute with no current font.
    """
    ...

def unicodeFromName(glyphname: str) -> int:
    """
    Looks up glyph name in its dictionary and if it is associated with a unicode
    code point returns that number. Otherwise it returns -1
    """
    ...

def UnicodeNameFromLib(n: int) -> str:
    """
    Returns the Unicode Name for this value as described by www.unicode.org.
    If there is no unicode name for this value, then return empty string "".
    It can execute with no current font.
    """
    ...

def UnicodeNamesListVersion() -> str:
    """
    Return the Unicode Nameslist Version (as described by www.unicode.org).

    This can execute with no current font.
    """
    ...

def UnicodeNames2FromLib(val: int) -> str:
    """
    Errors and corrections happen, therefore names can be corrected in the next
    Unicode Nameslist version. This function returns the formal alias for the
    unicode value given, or an empty string if there is no such alias.
    """
    ...

def scriptFromUnicode(n: int) -> str:
    """
    Return the script tag for the given Unicode codepoint. So, for ``ord('Q')``,
    it would return ``latn``. This is most useful with :meth:`font.addLookup()`,
    like: ::

       # Add a `mark` lookup for an arbitrary glyph...
       script = fontforge.scriptFromUnicode(glyph.unicode)
       font.addLookup("l1", "gpos_mark2base", None, (("mark",((script,("dflt")),)),))
       font.addLookupSubtable("l1", "l1-1")
       font.addAnchorClass("l1-1", "top")
    """
    ...

def SpiroVersion() -> str:
    """
    Returns the version of LibSpiro available to FontForge. Versions 0.1 to 0.5
    do not have a method to indicate version numbers, but there is a limited
    method to estimate versions {'0.0'..'0.5'}. '0.0' if FontForge has no LibSpiro
    available. '0.1' if LibSpiro 20071029 is available. '0.2' if LibSpiro 0.2 to
    0.5 is available. LibSpiro 0.6 and higher reports back its version available.
    """
    ...

def version() -> str:
    """Returns FontForge's version number. This will be a large number like 20070406."""
    ...

def loadPlugins() -> None:
    """
    Discovers and loads FontForge python plugins according to the current
    configuration, if not already loaded. This is primarily intended when
    importing FontForge into a python process but can also be when loading
    is delayed by the ``-skippyplug`` command-line flag.
    """
    ...

class PluginInfo(TypedDict):
    """
    Information describing configured and/or discovered plugins.

    Some of these values will be ``None`` if the plugin has not been loaded
    and a few more will be ``None`` if the plugin was not discovered.
    """

    name: str | None
    """
    The name of the plugin as defined by its author.
    """

    enabled: Literal["On", "Off", "New"] | None
    """
    "On" if the plugin is enabled, "Off" if it is disabled, "New" if the
    user has not yet configured this plugin.
    """

    status: Literal["Not Found", "Couldn't Load", "Couldn't Start", "Unloaded"] | None
    """
    "Not Found" if the plugin is configured but was not discovered.
    "Couldn't Load" if the plugin was discovered and its load status is
    "On" but the relevant module could not be imported. "Couldn't Start"
    if the module could be imported but the initialization function
    was missing or returned an error. "Unloaded" if the plugin was discovered
    and its load status is "On" but loading has not been attempted (most
    likely because of a configuration change or startup flag). ``None``
    if the plugin was discovered but has load status "Off" or New" or if
    it was loaded successfully.
    """

    package_name: str | None
    """
    The name of the Python package containing the plugin.
    """

    module_name: str | None
    """
    The name of the Python module carrying the initialization function.
    """

    attrs: Any | None
    """
    Additional sub-objects or properties of the module needed to pick
    out the location of the initialization function (if any).
    """

    prefs: bool | None
    """
    A boolean indicating whether the plugin has configurable preferences.
    """

    package_url: str | None
    """
    The "Home-page" URL listed in the package, if any.
    """

    summary: str | None
    """
    The "Summary" line in the package's metadata with a brief description
    of the plugin.
    """

def getPluginInfo() -> list[PluginInfo]:
    """
    Returns a list of dictionary objects describing configured and/or discovered
    plugins. Configured plugins are listed first in loading order followed by
    any newly discovered plugins.
    """
    ...

class PluginConfiguration(TypedDict):
    name: str
    """
    The name of the plugin as defined by its author.
    """

    enabled: Literal["On", "Off"]
    """
    "On" if the plugin is enabled, "Off" if it is disabled.
    """

def configurePlugins(plugins: Iterable[PluginConfiguration]) -> None:
    """
    This method allows plugins to be reconfigured using the Python API. It
    accepts a list (or any other iterable object) of dictionaries similar to
    those provided by ``getPluginInfo()`` except that only the ``name`` and
    ``enabled`` fields are examined. The ``name`` value must be the name of a
    known (currently configured or discovered) plugin.  The ``enabled`` value
    must be "On" or "Off". The configuration will be updated to correspond to
    the listed plugins in the specified order.

    If a plugin that was *not* discovered is missing from the list it will be
    removed from the configuration. Any missing but discovered plugins will
    be added to the end of the configuration list with load status "New".
    """
    ...

def runInitScripts() -> None:
    """
    Runs the system or user initialization scripts, if not already run. This is
    primarily intended when importing FontForge into a python process.
    """
    ...

def scriptPath() -> tuple[str, ...]:
    """Returns a tuple listing the directory paths which are searched for python scripts during FontForge initialization."""
    ...

def fonts() -> tuple[font, ...]:
    """Returns a tuple of all fonts currently loaded into FontForge for editing"""
    ...

def activeFont() -> font | None:
    """
    If the script were invoked from the File->Execute Script... dialog, or
    invoked by a menu item in the font view, this returns the font that was
    active at the time. Otherwise it returns ``None``.
    """
    ...

def activeGlyph() -> glyph | None:
    """
    If the script were invoked from the File->Execute Script... dialog or a menu
    item from an outline glyph window or a glyph import/export command this
    returns the glyph that was active at the time. Otherwise it returns ``None``.
    """
    ...

def activeLayer() -> int:
    """
    This returns the currently active layer as an integer between 0 (inclusive)
    and the font/glyph's layer count (exclusive). It may also be set to -1 if the
    current glyph window is displaying the font's guideline layer.
    """
    ...

def fontsInFile(filename: str) -> tuple[str, ...]:
    """
    Returns a tuple of all font names found in the specified file. The tuple may
    be empty if FontForge couldn't find any.
    """
    ...

def open(
    filename: str,
    flags: tuple[
        Literal[
            "fstypepermitted", "allglyphsinttc", "fontlint", "hidewindow", "alltables"
        ],
        ...,
    ]
    | int
    | None = None,
) -> "font":
    """
    Opens a filename and returns the font it contains (if any). The optional
    ``flags`` argument can be string tuple or integer combination of the
    following flags:

    fstypepermitted (1)

      The user has the appropriate license to examine the font no matter what
      the fstype setting is.

    allglyphsinttc (4)

      Load all glyphs from the 'glyf' table of a ttc font (rather than only the
      glyphs used in the font picked).

    fontlint (8)

      Report more error conditions.

    hidewindow (16)

      Do not create a view window for this font even if the UI is active.

      Note:

        This option supports efficient bulk processing of fonts in scripts run
        through the UI but using it can be tricky. Open fonts will be listed at
        the bottom of the "Window" menu but choosing them will have no effect.

        If some fonts are not closed you may need to "force-quit" the
        application using your OS.

    alltables (32)

      Retain all recognized font tables that do not have a native format.
    """
    ...

def parseTTInstrs(string: str) -> bytes:
    """
    Returns a binary string each byte of which corresponds to a truetype
    instruction. The input string should contain a set of instruction names as ::

       "SRP0 MIRP[min,rnd,black]"
    """
    ...

def unParseTTInstrs(sequence: bytes) -> str:
    """Reverse of parseTTInstrs. Converts a binary string into a human readable string."""
    ...

def unitShape(n: int) -> contour:
    """
    Returns a closed contour which is a regular n-gon. The contour will be
    inscribed in the unit circle. If n is negative, then the contour will be
    circumscribed around the unit circle. A value of 0 will produce a unit circle.
    If n==1 it is treated as if n were -4 -- a circumscribed square where each
    side is 2 units long (this is for historical reasons). Behavior is undefined
    for n=2,-1,-2.
    """
    ...

def registerGlyphSeparationHook(
    hook: Callable[[glyph, glyph, Any, T | None], int] | None = None,
    arg: T | None = None,
) -> None:
    """
    The GlyphSeparationHook is a python routine which FontForge will call when
    it wants to figure out the optical separation between two glyphs. If you
    never call this, or if you call it with a value of ``None`` FontForge will
    use a built-in default. This routine gets called during AutoWidth, AutoKern,
    and computing the optical left and right side bearings (for 'lfbd' and 'rtbd'
    features).
    """
    ...

# User Interface Module Functions

def hasUserInterface() -> bool:
    """Returns ``True`` if this session of FontForge has a user interface"""
    ...

@overload
def registerMenuItem(
    callback: Callable[[T | None, glyph | font], None],
    enable: Callable[[T | None, glyph | font], bool] | None,
    data: T | None,
    context: Literal["Font", "Glyph"] | tuple[Literal["Font"], Literal["Glyph"]],
    hotkey: str | None,
    *submenu_names: str | tuple[str, str] | tuple[str, str, str],
    name: str | tuple[str, str] | tuple[str, str, str],
) -> None: ...
@overload
def registerMenuItem(
    callback: Callable[[T | None, glyph | font], None],
    enable: Callable[[T | None, glyph | font], bool] | None = None,
    data: T | None = None,
    context: Literal["Font", "Glyph"] | tuple[Literal["Font"], Literal["Glyph"]] = ...,
    hotkey: str | None = None,
    name: str | tuple[str, str] | tuple[str, str, str] = ...,
    *,
    submenu: str
    | tuple[str, str]
    | tuple[str, str, str]
    | list[str | tuple[str, str] | tuple[str, str, str]]
    | None = None,
    keyword_only: bool = False,
) -> None: ...
@overload
def registerMenuItem(
    *,
    context: Literal["Font", "Glyph"] | tuple[Literal["Font"], Literal["Glyph"]],
    divider: Literal[True],
    submenu: str
    | tuple[str, str]
    | tuple[str, str, str]
    | list[str | tuple[str, str] | tuple[str, str, str]]
    | None = None,
) -> None:
    """
    If FontForge has a user interface this will add this menu item to the
    FontForge menu(s) specified by the ``context`` parameter. This second
    keyword interface is explained in the ``divider`` section.

    Note: The positional interface is forward-compatible with earlier
    verions of FontForge.

    callback:

      This is the function that will be called when the menu item is activated.
      It will be passed two arguments, the first is the data value specified
      here (which defaults to ``None``) and the second is a :class:`fontforge.glyph`
      or :class:`fontforge.font` object (depending on the ``context``).
      The callback's return value is ignored.

    enable:

      When specified this function is called with the same arguments as ``callback``
      right before the menu or submenu is diplayed. When it returns ``True``
      the menu item will be enabled and when it returns ``False`` it will be
      disabled. (When ``enable`` is ``None`` the menu item is always enabled.)

    data:

      ``data`` can be whatever you want; it defaults to ``None``. FontForge
      passes it to both of the above functions. It can be used to provide
      context or default arguments for the function (so that one function can
      be used for multiple menu items.)

    context:

      Currently this can the string ``"Font"``, the string ``"Glyph"``
      or the tuple ``("Font", "Glyph")``). ``"Font"`` will add the menu item
      to the FontView "Tools" menu or its submenu, while ``"Glyph"`` will
      add it to the CharView tools menu or its submenu.

    hotkey:

      ``hotkey`` must be either ``None`` or a string in hotkey format
      Because hotkeys are a "limited resource" this string is only a `suggestion`;
      it has no effect when the specified HotKey is already taken.
      Therefore, before picking a candidate HotKey you should at least verify
      that it is not already used by the relevant window in FontForge.

      Even when the specified HotKey is taken a user can still specify their
      own in the HotKeys file. You can make this easier to do, now and in the
      future, by providing the full triplet of names for each "level" using
      the current interface.

    name:

      ``name`` can be a string but ideally it is a tuple of three strings
      ``(localized_name, english_name, identifier_string)`` or of two strings
      ``(english_name, identifier_string)``. Use the three-tuple version when
      your plugin or other extension is localized and the two-tuple version
      when it is not localized or the user has configured the base locale.

      Note: The ``english_name`` and ``localized_name`` can and should
      include a *mnemonic*, picked out by a leading underscore. However,
      mnemonics at the top level (so the first ``submenu`` name or the ``name``
      if ``submenu`` is ``None``) are taken as a suggestion, similar to the
      ``hotkey`` argument.

      The ``identifier_string`` should be a single alphanumeric (plus
      underscores, but no spaces) string to identify this menu item. In the
      future this will serve as the representation of the menu item in menu
      configuration files, allowing a user or administrator to put the item
      where they like. It should include the name of your plugin or an
      abbreviation of it. For a plugin called "Feature File Helpers" and an
      item with (English) name "Save Fragment" a reasonable option would be
      "FeatFileHelp_SaveFragment". (This is for the future, as configurable
      menus are not yet supported by FontForge.)

    submenu:

      Note: ``submenu`` is a keyword-only argument.

      ``submenu`` can be any of: ``None``, a string, a two-tuple or three-tuple
      as with ``name``, or a Python *list* of any of these, with each
      specifying a level of sub-menu. (You cannot specify muitple levels of
      submenu with a tuple, as this would be ambiguous.) The tuple elements are
      analogous to ``name``: a three-tuple of ``(localized_name, english_name,
      identifier_string)``, a two-tuple of ``(english_name,
      identifier_string)``, or a string which is treated as the
      ``localized_name``. Submenus can and should also specify a *mnemonic*.

      In the future the ``identfier_string`` will allow a whole submenu to be
      moved to a different location in the menu hierarchy.

    submenu_names:

      When using the positional interface, each of these "intermediate" entries
      can be a three-tuple, two-tuple, or string, corresponding to an entry
      in the ``submenu`` list.

    keyword_only:

      When ``keyword_only`` is ``False`` (the default) the function will attempt
      to fall back to the positional interface and any reported errors will be
      relative to that interface. If you're having trouble with keyword parameters
      set ``keyword_only`` to ``True`` to see a more specific error message.

    divider:

      This special form of the function adds a horizontal line to the menu.
      The ``context`` keyword is required and ``divider`` must be set to ``True``.
      If the ``submenu`` keyword is omitted the divider is added to the top level.
    """
    ...

def registerImportExport(
    import_function: Callable[[T | None, glyph, str, bool], None] | None,
    export_function: Callable[[T | None, glyph, str], None] | None,
    data: T | None,
    name: str,
    extension: str,
    extension_list: str | None = None,
) -> None:
    """
    This will add the capability to import or export files of a given type,
    presumably a way of specifying the splines in a given glyph.

    import_function:

       The function to call to import a file into a glyph. It will be called
       with: The data argument (specified below), A pointer to the glyph into
       which the import is to happen, A filename, A flag indicating whether the
       import should go to the background layer or foreground. This function may
       be ``None``. In which case there is no import method for this file type.

    export_function:

       The function to call to export a glyph into a file. It will be called
       with: The data argument (see below), a pointer to the glyph, and a
       filename. This function may be ``None``, in which case there is no export
       method for this file type.

    data:

       Anything you like (including ``None``). It will be passed to the
       import/export routines and can provide them with context if they need that.

    name:

       The name to be displayed in the user interface for this file type.
       This may just be the extension, or it might be something more informative.

    extension:

       This is the default extension for this file type. It is used by the
       export dialog to pick an extension for the generated filename.

    extension_list:

       Some file types have more than one common extension. The import dialog
       needs to filter all possible filenames of this file type. This argument
       should be a comma separated list of extensions. It may be omitted, in
       which case it defaults to being the same as the "extension" argument above.
    """
    ...

def logWarning(msg: str) -> None:
    """
    Adds the message (a string) to FontForge's Warnings window. (if you wish to
    display a % character you must represent it as two percents). If there is no
    user interface the output will go to stderr.
    """
    ...

def postError(win_title: str, msg: str) -> None:
    """
    Creates a popup dialog to display the message (a string) in that dlg. (if you
    wish to display a % character you must represent it as two percents). If
    there is no user interface the output will go to stderr.
    """
    ...

def postNotice(win_title: str, msg: str) -> None:
    """
    Creates a little window which will silently vanish after a minute or two and
    displays the message (a string) in that window. (if you wish to display a %
    character you must represent it as two percents). If there is no user
    interface the output will go to stderr.
    """
    ...

def openFilename(
    question: str,
    def_name: str | None = None,
    filter: str | None = None,
) -> str | None:
    """
    All arguments are strings. The first is a question asked to the user (for
    which a filename to open is presumed to be the answer). The second is
    optional and provides a default filename. The third is optional and provides
    a filter (like "*.sfd")

    The result is either a filename or ``None`` if the user canceled the dialog.

    Throws an exception if there is no user interface.
    """
    ...

def saveFilename(
    question: str,
    def_name: str | None = None,
    filter: str | None = None,
) -> str | None:
    """
    All arguments are strings. The first is a question asked to the user (for
    which a filename to save something to is presumed to be the answer). The
    second is optional and provides a default filename. The third is optional and
    provides a filter (like "*.sfd")

    The result is either a filename or ``None`` if the user canceled the dialog.

    Throws an exception if there is no user interface.
    """

    ...

def ask(
    title: str,
    question: str,
    answers: tuple[str, ...],
    default: int | None = None,
    cancel: int | None = None,
) -> int:
    """
    Allows you to ask the user a multiple choice question. It pops up a dialog
    posing the question with a list of buttons ranged underneath it -- one for
    each answer.

    The first argument is the dialog's title, the second is the question to be
    asked, the third is a tuple of strings -- each string will become a button,
    the fourth and fifth arguments are optional, the fourth is the index in the
    answer array that will be the default answer (the one invoked if the user
    presses the [Return] key), and the fifth is the answer invoked if the user
    presses the [Escape] key. If omitted the default answer will be the first,
    and the cancel answer will be the last.

    The function returns the index in the answer array of the answer chosen by
    the user.

    Throws an exception if there is no user interface.
    """
    ...

@overload
def askChoices(
    title: str,
    question: str,
    answers: tuple[str, ...],
    default: int | None = None,
    multiple: Literal[False] = False,
) -> int: ...
@overload
def askChoices(
    title: str,
    question: str,
    answers: tuple[str, ...],
    default: int | tuple[bool, ...] | None = None,
    multiple: Literal[True] = True,
) -> int:
    """
    Allows you to ask the user a multiple choice question. It pops up a dialog
    posing the question with a scrollable list of choices -- one for each answer.

    The first argument is the dialog's title, the second is the question to be
    asked, the third is a tuple of strings -- each string will become a button,
    the fourth and fifth arguments are optional, the fourth is the index in the
    answer array that will be the default answer (the one invoked if the user
    presses the [Return] key). If omitted the default answer will be the first.

    The fifth argument means that multiple options can be selected. If true,
    the fourth argument should be a tuple of Boolean values or a single integer
    index into the answer tuple. So, if there are three options, it should look
    like ``(True, False, True)``, which would select the first and last option.

    The function returns the index in the answer array of the answer chosen by
    the user. If the user cancels the dialog, a -1 is returned.

    Throws an exception if there is no user interface.
    """
    ...

def askString(
    title: str,
    question: str,
    def_string: str | None = None,
) -> str | None:
    """
    Allows you to ask the user a question for which a string is the answer.

    The first argument is the dialog's title, the second is the question to be
    asked, the third is optional and specified a default answer.

    The function returns the string the user typed or ``None`` if they cancelled
    the dialog.

    Throws an exception if there is no user interface.
    """
    ...

class BaseQuestion(TypedDict):
    """
    Represents common keys for questions passed to ``askMulti``.

    At least ``question`` or ``tag`` must have a value.
    """

    question: str | None
    """
    The label string which is displayed before the answer field.
    This key must be present but the value can be ``None`` if no label is needed.
    """

    tag: NotRequired[Hashable]
    """
    The value that will be used as the key corresponding to this question in
    the ``askMulti`` result dictionary. If not provided, the ``question`` value
    will be used.
    """

    align: NotRequired[object]
    """
    A boolean-evaluable value (ideally ``True`` or ``False``) that indicates whether,
    when the dialog is being laid out, the label for this question should be
    aligned with the other labels of the same category. When absent the default
    is ``True``. (This has no effect when the ``question`` value is ``None``,
    so if you want an aligned, empty label use a space as the ``question`` value.)
    """

class StringQuestion(BaseQuestion):
    """
    Represents a string question that displays the label followed by a text
    entry field.
    """

    type: Literal["string"]

    default: NotRequired[str]
    """The initial value of the answer entry field."""

class Answer(TypedDict):
    """Represents potential answer for a ``ChoiceQuestion``."""

    name: str
    """The string the user will choose among."""

    tag: NotRequired[object]
    """
    The value used to report the answer in the ``askMulti`` result dictionary.
    If not present, the ``name`` string will be used.
    """

    default: NotRequired[object]
    """
    A boolean-evaluable value that indicates whether the answer is selected
    when the dialog is presented.
    """

class ChoiceQuestion(BaseQuestion):
    """
    Represents a choice question that asks the user to pick a subset of given
    answers.
    """

    type: Literal["choice"]

    answers: list[Answer]
    """A list of potential answers."""

    multiple: NotRequired[object]
    """
    A boolean-evaluable value that indicates whether the user must choose exactly
    one answer or can choose multiple, or potentially, no answers. When absent,
    the default is ``False``. When ``multiple`` is ``False`` there must be at
    most one answer for which ``default`` is ``True``.
    """

    checks: NotRequired[object]
    """
    A boolean-evaluable value that defaults to ``False``. By default a choice
    question is presented with a (potentially) scrolling vertical list similar
    to a pop-up menu. When ``checks`` is ``True`` and ``multiple`` is ``False``
    the answers are presented as radio buttons. When ``checks`` is ``True`` and
    ``multiple`` is ``True`` the answers are presented as checkboxes.
    """

class PathnameQuestion(BaseQuestion):
    """
    Represents open pathname and save pathname questions that display an entry
    field followed by a button to raise a browser.
    """

    type: Literal["openpath", "savepath"]

    default: NotRequired[str]
    """An initial pathname value."""

    filter: NotRequired[str]
    """Optional file filter."""

Question: TypeAlias = StringQuestion | ChoiceQuestion | PathnameQuestion
"""A question that may be passed to ``askMulti``."""

class Category(TypedDict):
    """Represents a group of questions."""

    category: str | None
    """A label to display to the user."""

    questions: list[Question]
    """A list of questions."""

def askMulti(
    title: str,
    specification: Question | list[Question] | Category | list[Category],
) -> dict[Hashable, object | tuple[object, ...]] | None:
    """
    This method raises a dialog with multiple questions for the user, optionally
    organized into separate tabs.  The answers can be choices (similar to
    :func:`fontforge.askChoices()`) a string (similar to
    :func:`fontforge.askString()`) an existing filename (similar to
    :func:`fontforge.openFilename()`) or a save filename (similar to
    :func:`fontforge.saveFilename()`.

    The method throws an exception if there is no user interface or the
    specification is not valid. Otherwise it either returns a dictionary of answers
    or ``None`` if the user chose "Cancel" or closed the dialog without choosing "OK".
    """
    ...

# Point class
class point:
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        on_curve: bool = True,
        type: Literal[0, 1, 2, 3] = 0,
        selected: bool = False,
    ) -> None:
        """
        Creates a new point. Optionally specifying its x,y location, on-curve status
        and selected status. x and y must be supplied together.
        """
        ...

    x: float
    """The x location of the point"""

    y: float
    """The y location of the point"""

    on_curve: bool
    """Whether this is an on curve point or an off curve point (a control point)"""

    selected: bool
    """
    The value of this member also determines the selected status in the UI on
    setting a layer. FontForge usually retains the selection status of any point
    between and that of an on-curve point when saving, whether or not a UI is present.
    """

    type: Literal[0, 1, 2, 3]
    """
    For an on-curve point, its FontForge point type.

    There are four types: :data:`fontforge.splineCorner`, :data:`fontforge.splineCurve`,
    :data:`fontforge.splineHVCurve` and :data:`fontforge.splineTangent`.

    A new point will have type :data:`splineCorner`. When assigning a layer to
    :attr:`glyph.layers`, :attr:`glyph.background` or :attr:`glyph.foreground`
    the type value is ignored. To influence the type FontForge will associate
    with an on-curve point use :meth:`glyph.setLayer`.
    """

    interpolated: bool
    """
    ``True`` if FontForge treats this (quadratic, on-curve) point as interpolated.
    All interpolated points should be mid-way between their off-curve points,
    but some such points are not treated as interpolated. This flag is ignored
    when setting a layer.

    Older versions of FontForge omitted interpolated points. This was equivalent
    to executing the following on a contour: ::

       c[:] = [ p for p in c if not p.interpolated ]

    This member will be false for a point marked "Never interpolate" in FontForge
    but there is currently no way of setting or preserving that mark when a layer
    is replaced using the Python interfaces. A "round trip" through a Python
    contour therefore clears that mark on any points that have it, and FontForge
    treats mid-placed and omitted :attr:`on_curve` points as equivalent.
    """

    name: str
    """The point name (generally there is no name)"""

    def dup(self) -> point:
        """Returns a copy of the current point."""
        ...

    def transform(
        self, matrix: tuple[float, float, float, float, float, float]
    ) -> None:
        """Transforms the point by the transformation matrix"""
        ...

PointInitializer: TypeAlias = (
    tuple[()]
    | tuple[float, float]
    | tuple[float, float, bool]
    | tuple[float, float, bool, Literal[0, 1, 2, 3]]
    | tuple[float, float, bool, Literal[0, 1, 2, 3], bool]
)
"""Represents a tuple of parameters that could be passed to the ``point`` initializer."""

# Contour class
class contour(Sequence[point]):
    """
    A contour is a collection of points. A contour may be either based on cubic or
    quadratic splines.

    If based on cubic splines there should be either 0 or 2 off-curve points
    between every two on-curve points. If there are no off-curve points then
    we have a line between those two points. If there are 2 off-curve points
    we have a cubic bezier curve between the two end points.

    If based on quadratic splines things are more complex. Again, two
    adjacent on-curve points yield a line between those points. Two on-curve
    points with an off-curve point between them yields a quadratic bezier
    curve. However if there are two adjacent off-curve points then an
    on-curve point will be interpolated between them. (This should be
    familiar to anyone who has read the truetype 'glyf' table docs).

    A contour may be open in which case it is just a long wiggly line, or
    closed when it is more like a circle with an inside and an outside.
    Unless you are making stroked fonts all your contours should eventually
    be closed.

    Contours may also be expressed in terms of Raph Levien's spiro points.
    This is an alternate representation for the contour, and is not always
    available (Only if :func:`fontforge.hasSpiro()` is ``True``. If
    available the spiro member will return a tuple of spiro control points,
    while assigning to this member will change the shape of the contour to
    match the new spiros.

    Two contours may be compared to see if they describe similar paths.
    """

    def __init__(self, is_quadratic: bool = ...) -> None:
        """Creates a new contour."""
        ...

    is_quadratic: bool
    """
    Whether the contour should be interpreted as a set of quadratic or cubic
    splines. Setting this value has the side effect of converting the point list
    to the appropriate format.
    """

    closed: bool
    """Whether the contour is open or closed."""

    name: str
    """The contour name (generally there is no name)."""

    spiros: tuple[tuple[float, float, int, int], ...]
    """
    This is an alternate representation of a curve. This member is only
    available if :meth:`fontforge.hasSpiro()` is ``True``. Returns a tuple
    of spiro control points. Each of these is itself a tuple of four
    elements; an x,y location, a type field, and a set of flags. The type
    field takes on values (which are predefined constants in the
    :mod:`fontforge` module):

    * :data:`fontforge.spiroG4`
    * :data:`fontforge.spiroG2`
    * :data:`fontforge.spiroCorner`
    * :data:`fontforge.spiroLeft`
    * :data:`fontforge.spiroRight`
    * :data:`fontforge.spiroOpen`

    For more information on what these point types mean see
    Raph Levien's work https://www.levien.com/spiro.

    The flags argument is treated as a bitmap of which currently one bit (0x1)
    is defined. This indicates that this point is selected in the UI.

    When you assign a tuple of spiro control points to this member, the point
    list for the Bezier interpretation of the contour will change. And when you
    change the Bezier interpretation the set of spiro points will change.
    """

    def dup(self) -> contour:
        """
        Returns a deep copy of the contour. That is, it copies the points that make
        up the contour.
        """
        ...

    def isEmpty(self) -> bool:
        """Returns whether the contour is empty (contains no points)"""
        ...

    def boundingBox(self) -> tuple[float, float, float, float]:
        """
        Returns a tuple representing a rectangle ``(xmin,ymin, xmax,ymax)`` into
        which the contour fits. It is not guaranteed to be the smallest such
        rectangle, but it will often be.
        """
        ...

    def getSplineAfterPoint(
        self, pos: int
    ) -> tuple[tuple[float, float, float, float], tuple[float, float, float, float]]:
        """
        Returns a tuple of two four-element tuples. These tuples are x and y splines
        for the curve after the specified point.
        """
        ...

    def draw(self, pen: glyphPen) -> None:
        """Draw the contour to the pen argument."""
        ...

    @override
    def __iter__(self) -> Iterator[point]: ...
    @override
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int) -> point: ...
    @overload
    def __getitem__(self, key: slice) -> contour: ...
    @overload
    def __setitem__(self, key: int, value: point | PointInitializer) -> None: ...
    @overload
    def __setitem__(
        self, key: slice, value: contour | Sequence[point | PointInitializer]
    ) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    def __add__(
        self,
        other: contour | Sequence[point | PointInitializer] | point | PointInitializer,
    ) -> contour: ...
    def __iadd__(
        self,
        other: contour | Sequence[point | PointInitializer] | point | PointInitializer,
    ) -> contour: ...
    @overload
    def __contains__(self, p: point | tuple[float, float]) -> bool: ...
    @overload
    def __contains__(self, p: object) -> bool: ...
    def moveTo(self, x: float, y: float) -> None:
        """Adds an initial, on-curve point at ``(x,y)`` to the contour"""
        ...

    def lineTo(self, x: float, y: float, pos: int | None = None) -> None:
        """
        Adds a line to the contour. If the optional third argument is given, the
        line will be added after the pos'th point, otherwise it will be at the end
        of the contour.
        """
        ...

    def cubicTo(
        self,
        cp1: tuple[float, float],
        cp2: tuple[float, float],
        end: tuple[float, float],
        pos: int | None = None,
    ) -> None:
        """
        Adds a cubic curve to the contour. If the optional fourth argument is given,
        the curve will be added after the pos'th point, otherwise it will be at the
        end of the contour.
        """
        ...

    def quadraticTo(
        self,
        cp: tuple[float, float],
        end: tuple[float, float],
        pos: int | None = None,
    ) -> None:
        """
        Adds a quadratic curve to the contour. If the optional third argument is
        given, the curve will be added after the pos'th point, otherwise it will be at
        the end of the contour.
        """
        ...

    def insertPoint(
        self, point: point | PointInitializer, pos: int | None = None
    ) -> None:
        """
        Adds a point to the contour. If the optional second argument is given, the point
        will be added after the pos'th point, otherwise it will be at the end of the
        contour.
        """
        ...

    def makeFirst(self, pos: int) -> None:
        """Rotate the point list so that the pos'th point becomes the first point"""
        ...

    def isClockwise(self) -> int:
        """
        Returns whether the contour is drawn in a clockwise direction. A return
        value of -1 indicates that no consistent direction could be found (the
        contour self-intersects).
        """
        ...

    def reverseDirection(self) -> None:
        """
        Reverse the order in which the contour is drawn (turns a clockwise contour
        into a counter-clockwise one). See also :meth:`layer.correctDirection`.
        """
        ...

    def similar(self, other_contour: contour, error: float = 0.5) -> bool:
        """
        Checks whether this contour is similar to the other one where error is the
        maximum distance (in em-units) allowed for the two contours to diverge.

        This is like the comparison operator, but that doesn't allow you to specify
        an error bound.
        """
        ...

    def xBoundsAtY(
        self,
        ybottom: float,
        ytop: float | None = None,
    ) -> tuple[float, float] | None:
        """
        Finds the minimum and maximum x positions attained by the contour when y is
        between ybottom and ytop (if ytop is not specified it is assumed the same as
        ybottom). If the contour does not have any y values in the specified range
        then ff will return ``None``.
        """
        ...

    def yBoundsAtX(
        self,
        xleft: float,
        xright: float | None = None,
    ) -> tuple[float, float] | None:
        """
        Finds the minimum and maximum y positions attained by the contour when x is
        between xleft and xright (if xright is not specified it is assumed the same
        as xleft). If the contour does not have any x values in the specified range
        then ff will return ``None``.
        """
        ...

    def addExtrema(
        self,
        flags: Literal["all", "only_good", "only_good_rm"] = "only_good",
        emsize: int = 1000,
    ) -> None:
        """
        Extrema should be marked by on-curve points. If a curve lacks a point at an
        extrema this command will add one. Flags may be one of the following strings:

        all:

          Add all missing extrema

        only_good:

          Only add extrema on longer splines (with respect to the em-size)

        only_good_rm:

          As above but also merge away on-curve points which are very close to, but
          not on, an added extremum
        """
        ...

    def cluster(
        self,
        within: float = 0.1,
        max: float = 0.5,
    ) -> None:
        """
        Moves clustered coordinates to a standard central value.

        See also :meth:`contour.round()`.
        """
        ...

    def merge(self, pos: int | tuple[int, ...]) -> None:
        """
        Removes the on-curve point at the given position and rearranges the other
        points to make the curve as similar to the original as possible. (pos may
        also be a tuple of positions, all of which will be removed)

        See also :meth:`contour.simplify()`.
        """
        ...

    def round(self, factor: float = 1) -> None:
        """
        Rounds the x and y coordinates. If factor is specified then ::

           new_coord = round(factor*old_coord)/factor

        See also :meth:`contour.cluster()`.
        """
        ...

    def selfIntersects(self) -> bool:
        """Returns whether this contour intersects itself."""
        ...

    def simplify(
        self,
        error_bound: float = 1,
        flags: tuple[
            Literal[
                "ignoreslopes",
                "ignoreextrema",
                "smoothcurves",
                "choosehv",
                "forcelines",
                "nearlyhvlines",
                "mergelines",
                "setstarttoextremum",
                "removesingletonpoints",
            ],
            ...,
        ] = (),
        tan_bounds: float = 0.2,
        linefixup: float = 2,
        linelenmax: float = 10,
    ) -> None:
        """
        Tries to remove excess points on the contour if doing so will not perturb
        the curve by more than error-bound. Flags is a tuple of the following strings:

        ignoreslopes:

          Allow slopes to change

        ignoreextrema:

          Allow removal of extrema

        smoothcurves:

          Allow curve smoothing

        choosehv:

          Snap to horizontal or vertical

        forcelines:

          flatten bumps on lines

        nearlyhvlines:

          Make nearly horizontal/vertical lines be so

        mergelines:

          Merge adjacent lines into one

        setstarttoextremum:

          Rotate the point list so that the start point is on an extremum

        removesingletonpoints:

          If the contour contains just one point then remove it

        See also :meth:`contour.merge()`.
        """
        ...

    def transform(
        self, matrix: tuple[float, float, float, float, float, float]
    ) -> None:
        """Transforms the contour by the matrix"""
        ...

    def addInflections(self) -> None:
        """
        If the curvature of a spline in the contour changes sign then break the
        spline so that there will be a point at all points of inflection.
        """
        ...

    def balance(self) -> None:
        """
        For all cubic bezier splines of the contour make the line between the control
        points parallel to the chord such that the area is preserved. This is an
        improved version of the algorithm known as "tunnify".
        """
        ...

    def harmonize(self) -> None:
        """
        For all bezier splines of the contour move the smooth on-curve points between
        its adjacent control points such that the adjacent curvatures become equal.
        """
        ...

class StrokeOptions(TypedDict, total=False):
    "Additional options for stroke operations."

    removeinternal: bool
    """
    When a contour is closed and clockwise, only the smaller "inside" contour
    is retained. When a contour is closed and counter-clockwise only the
    larger "outside" contour is retained. Default: False
    """

    removeexternal: bool
    """
    When a contour is closed and clockwise, only the larger "outside" contour
    is retained. When a contour is closed and counter-clockwise only the
    smaller "inside" contour is retained. Default: False
    """

    extrema: bool
    """When true, any missing extrema on the stroked paths are added. Default: True"""

    simplify: bool
    """
    When true, simplify is called on the path before it is returned. The
    ``error-bound`` is set to the ``accuracy`` value. Default: True
    """

    removeoverlap: Literal["layer", "contour", "none"]
    """
    Specifies whether, and on what basis, remove-overlap should be run.
    "layer" corresponds to running remove-overlap on the :class:`layer` as a
    whole. "contour" corresponds to running remove-overlap on individual
    contours. "none" corresponds to not running remove-overlap. Note that
    because the stroke facility relies on remove-overlap to eliminate cusps
    and other artifacts, "none" is an unusual choice and available primarily
    for debugging purposes. Default: "layer"
    """

    accuracy: float
    """
    This is a target (but not a guarantee) for the allowed error, in em-units,
    of the output relative to the input path and nib geometries. Higher values
    allow more error will typically yield contours with fewer points.
    Default: 0.25
    """

    jlrelative: bool
    """See ``joinlimit`. Default: True"""

    joinlimit: float
    """
    Specifies the maximum length of a "miter", "miterclip", or "arcs" join.
    For "miter" joins that would be longer will fall back to "bevel". With
    "miterclip" and "arcs" a longer join will be trimmed to the specified
    length. Note, however, that no join is trimmed past the "bevel line" and
    therefore lower values do not guarantee a given length.

    When ``jlrelative`` is false the value is interpreted as a length in
    em-units. Otherwise the value is interpreted as a multiple of
    "stroke-widths": the average of the spans of the nib at the incoming
    and outgoing join angles.

    Default: 20
    """

    ecrelative: bool
    """
    See ``extendcap``. Default: True
    """

    extendcap: float
    """
    When the contour being stroked is open and the ``cap`` style is "butt" or
    "round", this parameter adds area between the end of that contour and the
    cap. The length of that area will never be less than the specified value
    but may be more, depending on the geometry of the nib and the join.
    (However, it will always be exact for circular nibs.)

    When ``ecrelative`` is false the value is interpreted as a length in
    em-units. Otherwise the value is interpreted as a multiple of
    "stroke-widths": the span of the stroked path at the angle at the cap.

    Default: 0
    """

    arcsclip: Literal["svg2", "ratio", "auto"]
    """
    When using the "arcs" join style this parameter influences the algorithm
    used to clip joins that exceed the ``joinlimit``. The value "svg2"
    specifies the standard SVG algorithm while the value "ratio" specifies an
    alternative algorithm that works better for longer and thinner nibs at
    shorter limits. The default value "auto" chooses the "ratio" algorithm
    for oblong elliptical and calligraphic nibs and
    ``jlrelative joinlimit`` < 4 and the "svg2" algorithm otherwise.
    Default: "auto"
    """

# Layer class
class layer(Sequence[contour]):
    """
    A layer is a collection of contours. All the contours must be the same order
    (all quadratic or all cubic). Currently layers do not contain references.

    Layers may be compared to see if their contours are similar.
    """

    def __init__(self) -> None:
        """Creates a new layer"""
        ...

    def is_quadratic(self) -> bool:
        """
        Whether the contours should be interpreted as a set of quadratic cubic
        splines. Setting this value has the side effect of converting the contour
        list to the appropriate format.
        """
        ...

    @override
    def __iter__(self) -> Iterator[contour]:
        """Returns an iterator for the layer which will return the contours in order."""
        ...

    def dup(self) -> "layer":
        """
        Returns a deep copy of the layer. That is, it will copy all the contours and
        all the points as well as copying the layer object itself.
        """
        ...

    def isEmpty(self) -> bool:
        """Returns whether the layer is empty (contains no contour)"""
        ...

    def addExtrema(
        self,
        flags: Literal["all", "only_good", "only_good_rm"] = "only_good",
        emsize: int = 1000,
    ) -> None:
        """
        Extrema should be marked by on-curve points. If a curve lacks a point at an
        extrema this command will add one. Flags may be one of the following strings:

        all:

          Add all missing extrema

        only_good:

          Only add extrema on longer splines (with respect to the em-size)

        only_good_rm:

          As above but also merge away on-curve points which are very close to, but
          not on, an added extremum
        """
        ...

    def cluster(
        self,
        within: float = 0.1,
        max: float = 0.5,
    ) -> None:
        """
        Moves clustered coordinates to a standard central value.

        See also :meth:`layer.round()`.
        """
        ...

    def correctDirection(self) -> None:
        """
        Moves clustered coordinates to a standard central value.

        See also :meth:`layer.round()`.
        """
        ...

    def export(
        self,
        filename: str,
        *,
        usetransform: bool = False,
        usesystem: bool = False,
        asksystem: bool = False,
    ) -> None:
        """
        Exports the current layer (in outline format) to a file. The type of file is
        determined by the extension.

        The following optional keywords modify the export process for various formats:

        usetransform:

          Flip the Y-axis of exported SVGs with a transform element rather than
          modifying the individual Y values.

        usesystem:

          Ignore the above keyword settings and use the values set by the user
          in the Import options dialog.

        asksystem:

          If the UI is present show the Import options dialog to the user
          and use the chosen values (does nothing otherwise).
        """
        ...

    def exclude(self, excluded_layer: layer) -> None:
        """
        Removes the excluded area from the current contours. See also
        :meth:`layer.removeOverlap()` and :meth:`layer.intersect()`.
        """
        ...

    def intersect(self) -> None:
        """
        Leaves only areas in the intersection of contours. See also
        :meth:`layer.removeOverlap()` and :meth:`layer.exclude()`.
        """
        ...

    def removeOverlap(self) -> None:
        """
        Removes overlapping areas. See also :meth:`layer.intersect()` and
        :meth:`layer.exclude()`.
        """
        ...

    def interpolateNewLayer(self, other_layer: layer, amount: float) -> layer:
        """
        Creates (and returns) a new layer which contains splines interpolated from
        the current layer and the first argument. If amount is 0 the result will
        look like the current layer, if 1 then like the first argument.
        """
        ...

    def round(self, factor: float = 1) -> None:
        """
        Rounds the x and y coordinates. If factor is specified then ::

           new_coord = round(factor*old_coord)/factor

        See also :meth:`layer.cluster()`.
        """
        ...

    def selfIntersects(self) -> bool:
        """
        Returns whether any of the contours on this layer intersects any other
        contour (including itself).
        """
        ...

    def similar(self, other_layer: layer, error: float = 0.5) -> bool:
        """
        Checks whether this layer is similar to the other one where error is the
        maximum distance (in em-units) allowed for any two corresponding contours
        in the layers to diverge.

        This is like the comparison operator, but that doesn't allow you to specify
        an error bound.
        """
        ...

    def simplify(
        self,
        error_bound: float = 1,
        flags: tuple[
            Literal[
                "ignoreslopes",
                "ignoreextrema",
                "smoothcurves",
                "choosehv",
                "forcelines",
                "nearlyhvlines",
                "mergelines",
                "setstarttoextremum",
                "removesingletonpoints",
            ],
            ...,
        ] = (),
        tan_bounds: float = 0.2,
        linefixup: float = 2,
        linelenmax: float = 10,
    ) -> None:
        """
        Tries to remove excess points on the contour if doing so will not perturb the
        curve by more than error-bound. Flags is a tuple of the following strings:

        ignoreslopes:

          Allow slopes to change

        ignoreextrema:

          Allow removal of extrema

        smoothcurves:

          Allow curve smoothing

        choosehv:

          Snap to horizontal or vertical

        forcelines:

          flatten bumps on lines

        nearlyhvlines:

          Make nearly horizontal/vertical lines be so

        mergelines:

          Merge adjacent lines into one

        setstarttoextremum:

          Rotate the point list so that the start point is on an extremum

        removesingletonpoints:

          If the contour contains just one point then remove it
        """
        ...

    def stemControl(
        self,
        stem_width_scale: float,
        hscale: float = 1,
        stem_height_scale: float | None = None,
        vscale: float | None = None,
        xheight: float | None = None,
    ) -> None:
        """
        Allows you to scale counters and stems independently of each other.
        ``stem_width_scale`` specifies by how much the widths of stems should be
        scaled (this should be a number around 1).

        If omitted, ``hscale`` defaults to 1, otherwise it will indicate the
        horizontal scaling factor for the glyph as a whole.

        If omitted, ``stem_height_scale`` defaults to ``stem_width_scale``,
        otherwise it specifies the scaling for stem heights.

        If omitted, ``vscale`` defaults to ``hscale``, otherwise it specifies the
        vertical scale factor for the glyph as a whole. ``xheight`` is optional; if
        specified it will fix the points at that height so that they will be at the
        same level across glyphs.
        """
        ...

    @overload
    def stroke(
        self,
        type: Literal["circular"],
        width: float,
        /,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        angle: float = 0,
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["elliptical"],
        width: float,
        minor_width: float,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["calligraphic"],
        width: float,
        height: float,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["convex"],
        nib: contour | layer,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None:
        """
        Strokes the lines of each contour in the layer according to the supplied
        parameters. See the corresponding :meth:`glyph.stroke()` for a description
        of the parameters.
        """
        ...

    def transform(
        self, matrix: tuple[float, float, float, float, float, float]
    ) -> None:
        """Transforms the layer by the matrix"""
        ...

    def nltransform(self, xexpr: str, yexpr: str) -> None:
        """
        xexpr and yexpr are strings specifying non-linear transformations that will
        be applied to all points in the layer (with xexpr being applied to x values,
        and yexpr to y values, of course).
        """
        ...

    def boundingBox(self) -> tuple[float, float, float, float]:
        """
        Returns a tuple representing a rectangle ``(xmin,ymin, xmax,ymax)`` into
        which the layer fits. It is not guaranteed to be the smallest such
        rectangle, but it will often be.
        """
        ...

    def xBoundsAtY(
        self,
        ybottom: float,
        ytop: float | None = None,
    ) -> tuple[float, float] | None:
        """
        Finds the minimum and maximum x positions attained by the contour when y is
        between ybottom and ytop (if ytop is not specified it is assumed the same as
        ybottom). If the layer does not have any y values in the specified range
        then FontForge will return ``None``.
        """
        ...

    def yBoundsAtX(
        self,
        xleft: float,
        xright: float | None = None,
    ) -> tuple[float, float] | None:
        """
        Finds the minimum and maximum y positions attained by the contour when x is
        between xleft and xright (if xright is not specified it is assumed the same
        as xleft). If the layer does not have any x values in the specified range
        then FontForge will return ``None``.
        """
        ...

    def draw(self, pen: glyphPen) -> None:
        """Draw the layer to the pen argument."""
        ...

    def addInflections(self) -> None:
        """Please see :meth:`contour.addInflections()`."""
        ...

    def balance(self) -> None:
        """Please see :meth:`contour.balance()`."""
        ...

    def harmonize(self) -> None:
        """Please see :meth:`contour.harmonize()`."""
        ...

    @override
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int) -> contour: ...
    @overload
    def __getitem__(self, key: slice) -> NoReturn: ...
    def __setitem__(self, key: int, value: contour) -> None: ...
    def __delitem__(self, key: int) -> None: ...
    def __add__(self, other: layer | contour) -> layer: ...
    def __iadd__(self, other: layer | contour) -> layer: ...

# GlyphPen class
class glyphPen:
    """
    This implements the Pen Protocol http://robofab.org/objects/pens.html to
    draw a FontForge :class:`glyph`. You create a :class:`glyphPen` with
    :meth:`glyph.glyphPen()`. You then draw into it with the instance methods.

    This type may not be pickled.

    Example:

    ::

       import fontforge
       font = fontforge.open("Ambrosia.sfd") # Open a font
       pen = font["B"].glyphPen()            # Create a pen to draw into glyph "B"
       pen.moveTo((100,100))                 # draw a square
       pen.lineTo((100,200))
       pen.lineTo((200,200))
       pen.lineTo((200,100))
       pen.closePath()                       # end the contour

       font["A"].draw(pen)                   # or you can copy from one glyph to another
                                             # by having a glyph draw itself into the pen
       pen = None                            # Finalize the pen. This tells FontForge
                                             # that the drawing is done and causes
                                             # it to refresh the display (if a UI is active).
    """

    def moveTo(self, point: tuple[float, float]) -> None:
        """
        With one exception this call begins every contour and creates an on curve
        point at ``(x,y)`` as the start point of that contour. This should be the
        first call after a pen has been created and the call that follows a
        :meth:`glyphPen.closePath()`, :meth:`glyphPen.endPath()`.
        """
        ...

    def lineTo(self, point: tuple[float, float]) -> None:
        """Draws a line from the last point to ``(x,y)`` and adds that to the contour."""
        ...

    @overload
    def curveTo(
        self,
        cp1: tuple[float, float],
        cp2: tuple[float, float],
        end: tuple[float, float],
    ) -> None: ...
    @overload
    def curveTo(self, cp: tuple[float, float], end: tuple[float, float]) -> None:
        """
        This routine has slightly different arguments depending on the type of the
        font. When drawing into a cubic font (PostScript) use the first set of
        arguments (with two control points -- off curve points -- between each on
        curve point). When drawing into a quadratic font (TrueType) use the second
        format with one control point between adjacent on-curve points.

        The standard appears to support super-bezier curves with more than two
        control points between on-curve points. FontForge does not. Nor does
        FontForge allow you to draw a quadratic spline into a cubic font, nor vice versa.
        """
        ...

    def qCurveTo(
        self, *points: tuple[float, float], end: tuple[float, float] | None
    ) -> None:
        """
        This routine may only be used in quadratic (TrueType) fonts and has two
        different formats. It is used to express the TrueType idiom where an on-curve
        point mid-way between its control points may be omitted, leading to a run of
        off-curve points (with implied but unspecified on-curve points between them).

        The first format allows an arbitrary number of off-curve points followed by
        one on-curve point.

        It is possible to have a contour which consists solely of off-curve points.
        When this happens the contour is NOT started with a :meth:`glyphPen.moveTo()`,
        instead the entire contour, all the off curve points, are listed in one call,
        and the argument list is terminated by a ``None`` to indicate there are no
        on-curve points.
        """
        ...

    def closePath(self) -> None:
        """Closes the contour (connects the last point to the first point to make a loop) and ends it."""
        ...

    def endPath(self) -> None:
        """
        Ends the contour without closing it. This is only relevant if you are
        stroking contours.
        """
        ...

    def addComponent(
        self,
        glyph_name: str,
        transform: tuple[float, float, float, float, float, float] = (1, 0, 0, 1, 0, 0),
        selected: bool = False,
    ) -> None:
        """
        Adds a reference (a component) to the glyph. The PostScript transformation
        matrix is a 6 element tuple (with a default of the identity transformation).
        When ``selected`` is true the reference will be marked as selected in the
        UI and related API calls.
        """
        ...

GlyphReference: TypeAlias = (
    tuple[str]
    | tuple[str, tuple[float, float, float, float, float, float]]
    | tuple[str, tuple[float, float, float, float, float, float], bool]
)
"""
A tuple of a glyph-name, a transformation matrix, and whether the reference is
currently selected.
"""

class GlyphMathKerning:
    """
    Represents math kerning data for a glyph.

    All values are a tuple of two element tuples, each of which contains a kerning
    offset and an associated height (in the last entry the height term is
    meaningless, but present).
    """

    bottomLeft: tuple[tuple[int, int], tuple[int, int]]
    """The glyph's math kerning data associated with the bottom left vertex."""

    bottomRight: tuple[tuple[int, int], tuple[int, int]]
    """The glyph's math kerning data associated with the bottom right vertex."""

    topLeft: tuple[tuple[int, int], tuple[int, int]]
    """The glyph's math kerning data associated with the top left vertex."""

    topRight: tuple[tuple[int, int], tuple[int, int]]
    """The glyph's math kerning data associated with the top right vertex."""

class GlyphChangeOptions(TypedDict, total=False):
    """Options for ``glyph.genericGlyphChange`` and ``font.genericGlyphChange``"""

    stemType: Literal["uniform", "horizontalVertical", "thickThin"]
    """
    If "uniform" or omitted, all stems (horizontal and vertical, and thick and thin)
    will be scaled by the same rules. If "horizontalVertical", horizontal and
    vectical stems may be scaled by different rules. If "thickThin", thick
    and thin stems may be scaled by different rules.
    """

    thickThreshold: float
    """
    The size in em-units at which a stem is classified as "thick".
    Required if ``stemType`` is "thickThin".
    """

    stemScale: float
    """
    A scaling factor by which all stems (horizontal and vertical, thick and thin)
    will be scaled. A value of 1.0 means no change.
    Required if ``stemType`` is "uniform" or omitted.
    """

    stemAdd: float
    """
    The number of em-units to add to the width of each stem.
    Only use when ``stemType`` is "uniform" or omitted.
    """

    stemHeightScale: float
    """
    The scaling for the height of horizontal stems.
    Required if ``stemType`` is "horizontalVertical".
    """

    stemHeightAdd: float
    """
    The number of em-units to add to the height of horizontal stems.
    Only use when ``stemType`` is "horizontalVertical".
    """

    stemWidthScale: float
    """
    The scaling for the width of vertical stems.
    Required if ``stemType`` is "horizontalVertical".
    """

    stemWidthAdd: float
    """
    The number of em-units to add to the width of vertical stems.
    Only use when ``stemType`` is "horizontalVertical".
    """

    thinStemScale: float
    """
    The scaling for the width/height of thin stems.
    Required if ``stemType`` is "thickThin".
    """

    thinStemAdd: float
    """
    The number of em-units to add to the width/height of thin stems.
    Only use when ``stemType`` is "thickThin".
    """

    thickStemScale: float
    """
    The scaling for the width/height of thick stems.
    Required if ``stemType`` is "thickThin".
    """

    thickStemAdd: float
    """
    The number of em-units to add to the width/height of thick stems.
    Only use when ``stemType`` is "thickThin".
    """

    processDiagonalStems: bool
    """Whether to process diagonal stems."""

    hCounterType: Literal["uniform", "nonUniform", "center", "retainScale"]
    """
    If "uniform" or omitted, horizontal counters and left and right side bearings will
    all be scaled using the same rules. If "nonUniform", horizontal counters
    and left and right side bearings may be scaled by different rules. If "center",
    then left and right side-bearings will be set so the new glyph is centered
    within the original glyph's width. (Probably more useful for CJK fonts than LGC fonts).
    If "retainScale", then the left and right side bearings will be set so the
    new glyph is within within the original glyph's width, and the side-bearings
    remain in the same proportion to each other as before.
    """

    hCounterScale: float
    """
    The scaling factor for horizontal counters. Also, the scaling factor for
    left and right side bearings when ``hCounterType`` is "uniform" or omitted.
    Required if ``hCounterType`` is "uniform", "nonUniform", or omitted.
    """

    hCounterAdd: float
    """
    The number of em-units to add to horizontal counters. Also, the number of em-units
    to add to left and right side bearings whin ``hCounterType`` is "uniform" or omitted.
    Only use when ``hCounterType`` is "uniform", "nonUniform", or omitted.
    """

    lsbScale: float
    """
    The scaling factor for left side bearings.
    Required if ``hCounterType`` is "nonUniform".
    """

    lsbAdd: float
    """
    The number of em-units to add to left side bearings.
    Only use when``hCounterType`` is "nonUniform".
    """

    rsbScale: float
    """
    The scaling factor for right side bearings.
    Required if ``hCounterType`` is "nonUniform".
    """

    rsbAdd: float
    """
    The number of em-units to add to right side bearings.
    Only use when``hCounterType`` is "nonUniform".
    """

    vCounterType: Literal["mapped", "scaled"]
    """
    If omitted, or is the string "mapped", then certain
    zones on the glyph may be placed at new (or the same) locations -- similar
    to BlueValues. So you can specify a zone for the baseline, one for the
    x-height and another for the top of capitals and ascenders (and perhaps a
    fourth for descenders). Each such zone is specified by the ``vMap`` argument.
    If "scaled", vertical counters and the top and bottom side bearings will
    all be scaled using the same rules. This is probably most useful for CJK fonts.
    """

    vCounterScale: float
    """
    The scaling factor for vertical counters and top and bottom side bearings.
    Required if ``vCounterType`` is "scaled".
    """

    vCounterAdd: float
    """
    The number of em-units to add to vertical counters and top and bottom side bearings.
    Only use if ``vCounterType`` is "scaled".
    """

    vScale: float
    """
    Vertical scaling factor.
    Only use if ``vCounterType`` is "mapped".
    """

    vMap: tuple[tuple[float, float, float], ...]
    """
    A tuple of zones with original location, and final location, and original width.
    Required if ``vCounterType`` is "mapped" or omitted.
    """

# Glyph class
class glyph:
    """
    The glyph type refers to a :class:`glyph` object. It has no independent life
    of its own, it always lives within a font. It has all the things you expect to
    be associated with a glyph: a glyph name, a unicode encoding, a drawing layer,
    GPOS/GSUB features...

    This type may not be pickled.

    This type may not be created directly -- all glyphs are bound to a font and
    must be created through the font. See :meth:`font.createChar()`.
    """

    activeLayer: int
    """
    Returns currently active layer in the glyph (as an integer). May be set to
    an integer or a layer name to change the active layer.
    """

    altuni: tuple[tuple[int, int, int] | int, ...] | None
    """
    Returns additional unicode code points for this glyph. For a primary code
    point, see :attr:`glyph.unicode`.

    Returns either None or a tuple of alternate encodings. Each alternate
    encoding is a tuple of ::

    (unicode-value, variation-selector, reserved-field)

    The first is a unicode value of this alternate code point. The second is an
    integer for variation selector and can be set to -1 if not used. The third
    is an empty field reserved for future use and currently must be set to zero.

    :attr:`glyph.altuni` can be set to None to clear all alternates, or to a
    tuple. The elements of the tuple may be either integers (an alternate
    unicode value with no variation selector) or a tuple with up to 3 values in
    it as explained above.
    """

    anchorPoints: tuple[
        tuple[str, Literal["mark", "base", "basemark", "entry", "exit"], float, float]
        | tuple[str, Literal["ligature"], float, float, int]
    ]
    """
    Returns the list of anchor points in the glyph. Each anchor point is a
    tuple of ::

       (anchor-class-name, type, x,y [,ligature-index])

    The first two are strings, the next two doubles, and the last (which is only
    present if ``type=="ligature"``) is an integer. Type may be

    * ``mark``
    * ``base``
    * ``ligature``
    * ``basemark``
    * ``entry``
    * ``exit``
    """

    anchorPointsWithSel: tuple[
        tuple[
            str,
            Literal["mark", "base", "basemark", "entry", "exit"],
            float,
            float,
            bool,
        ]
        | tuple[str, Literal["ligature"], float, float, bool, int]
    ]
    """
    Same as :attr:``glyph.anchorPoints``, except also includes whether the anchor point is selected
    in the UI. Returns a tuple of all anchor points in the glyph. Each anchor
    point is a tuple of ::

    (anchor-class-name, type, x,y, selected [,ligature-index])

    The first two are strings, the next two doubles, then a boolean, and the
    last (which is only present if ``type=="ligature"``) is an integer.
    Type may be

    * ``mark``
    * ``base``
    * ``ligature``
    * ``basemark``
    * ``entry``
    * ``exit``
    """

    background: layer
    """
    The glyph's background layer. This is a *copy* of the glyph's data. See
    also :attr:`glyph.foreground` and :attr:`glyph.layers`.
    """

    changed: bool
    """
    Whether this glyph has been modified. This is (should be) maintained
    automatically, but you may set it if you wish.
    """

    color: int
    """
    The color of the glyph in the fontview. A 6 hex-digit RGB number or -1 for
    default. 0xffffff is white, 0x0000ff is blue, etc.
    """

    comment: str
    """Any comment you wish to associate with the glyph. UTF-8"""

    dhints: tuple[
        tuple[tuple[float, float], tuple[float, float], tuple[float, float]], ...
    ]
    """
    A tuple with one entry for each diagonal stem hint. Each stem hint is itself
    represented by a tuple of three coordinate pairs (themselves tuples of two
    numbers), these three are: a point on one side of the stem, a point on the
    other side, and a unit vector pointing in the stem's direction.
    """

    encoding: int
    """
    Returns the glyph's encoding in the font's encoding. (readonly)

    If the glyph has multiple encodings, one will be picked at random.

    If the glyph is not in the font's encoding then a number will be returned
    beyond the encoding size (or in some cases -1 will be returned).
    """

    font: font
    """The font containing this glyph. (readonly)"""

    foreground: layer
    """
    The glyph's foreground layer. This is a copy of the glyph's data. See also
    :attr:`glyph.background`, :attr:`glyph.layers` and :attr:`glyph.references`.
    """

    glyphclass: Literal[
        "automatic", "noclass", "baseglyph", "baseligature", "mark", "component"
    ]
    """An opentype glyphclass, one of automatic, noclass, baseglyph, baseligature, mark, component"""

    glyphname: str
    """The name of the glyph"""

    hhints: tuple[tuple[float, float], ...]
    """
    A tuple of all horizontal postscript hints. Each hint is itself a tuple of
    starting locations and widths.
    """

    horizontalComponents: tuple[
        tuple[str]
        | tuple[str, bool]
        | tuple[str, bool, int]
        | tuple[str, bool, int, int]
        | tuple[str, bool, int, int, int],
        ...,
    ]
    """
    A tuple of tuples.

    This allows constructing very large versions of the glyph by stacking the
    components together. Some components may be repeated so there is no bound on the size.

    This is different from ``horizontalVariants`` which expects prebuilt glyphs of
    various fixed sizes.

    The components are stacked in the order they appear in the (top-level) tuple.
    Each sub-tuple represents information on one component. The subtuple should
    contain: (String glyph-name, Boolean is-extender, Int startConnectorLength,
    Int endConnectorLength, Int fullAdvance). Any of these may be omitted (except
    the glyph name) and will be assumed to be 0 if so.
    """

    horizontalComponentItalicCorrection: int
    """The italic correction for any composite glyph made with the horizontalComponents."""

    horizontalVariants: str | tuple[glyph, ...]
    """
    A string containing a list of glyph names. These are
    alternate forms of the current glyph for use in
    typesetting math. Presumably the variants are of different sizes.

    Although ff will always return a string of glyph names, you may assign to it
    with a tuple of glyphs and ff will convert that to corresponding names.
    """

    isExtendedShape: bool
    """A boolean containing the MATH "is extended shape" field."""

    italicCorrection: int
    """
    The glyph's italic correction field. Used by both TeX and MATH. The special
    value :data:`fontforge.unspecifiedMathValue` means the value is unspecified
    (An unspecified value will not go into the output tables, a value of 0 will)
    """

    layer_cnt: int
    """The number of layers in this glyph. (Cannot be set)"""

    layers: dict[str | int, layer]
    """
    A dictionary like object containing the layers of the glyph. It may be
    indexed by either a layer name or an integer between 0 and
    ``glyph.layer_cnt-1`` to produce a :class:`layer` object. Layer 0 is the
    background layer. Layer 1 is the foreground layer.
    """

    layerrefs: dict[str | int, GlyphReference]
    """
    A dictionary like object containing the references in the layers of the
    glyph. It may be indexed by either a layer name, or an integer between 0 and
    ``glyph.layer_cnt-1`` to produce a reference tuple object. Layer 0 is the
    background layer. Layer 1 is the foreground layer.
    """

    lcarets: tuple[int, ...]
    """
    A tuple containing the glyph's ligature caret locations. Setting this will
    also either enable or disable the "Default Ligature Caret Count" flag
    depending from the number of elements in the tuple.
    """

    left_side_bearing: int
    """
    The left side bearing of the glyph. Setting this value will adjust all
    layers so that guides in the background etc will be adjusted with the rest
    of the glyph
    """

    manualHints: int
    """
    The glyph's hints have been set by hand, and the glyph should not be
    autohinted without a specific request from the user. The "Don't AutoHint" flag.
    """

    mathKern: GlyphMathKerning
    """The glyph's math kerning data associated with its vertices."""

    originalgid: int
    """The GID of this glyph in the font it was read from. (readonly)"""

    persistent: object
    """
    Whatever you want (these data will be saved as a pickled object in the
    sfd file. It is your job to ensure that whatever you put here can be pickled).
    See also the :attr:`glyph.temporary` field.
    """

    references: tuple[GlyphReference, ...]
    """
    A tuple of tuples containing, for each reference in the foreground, a
    glyph-name, a transformation matrix, and whether the reference is currently
    selected. When assigning to the object the matrix and ``selected`` values
    are optional. See also :attr:`glyph.foreground` and :attr:`glyph.layerrefs`.
    """

    right_side_bearing: int
    """The right side bearing of the glyph"""

    script: str
    """
    A string containing the OpenType 4 letter tag for the script associated with
    this glyph (readonly)
    """

    temporary: object
    """
    Whatever you want (these data will be lost once the font is closed)

    See also :attr:`glyph.persistent`.
    """

    texheight: int
    """
    The Tex height. The special value :data:`fontforge.unspecifiedMathValue`
    means the field is unspecified (An unspecified value will not go into the
    output tables, a value of 0 will)
    """

    texdepth: int
    """
    The Tex depth. The special value :data:`fontforge.unspecifiedMathValue`
    means the field is unspecified (An unspecified value will not go into the
    output tables, a value of 0 will)
    """

    topaccent: int
    """
    The glyph's top accent position field. Used by MATH. The special value
    :data:`fontforge.unspecifiedMathValue` means the field is unspecified (An
    unspecified value will not go into the output tables, a value of 0 will)
    """

    ttinstrs: bytes
    """Any truetype instructions, returned as a binary string"""

    unicode: int
    """
    The glyph's unicode code point, or -1. In addition to this primary mapping,
    a glyph can have multiple secondary mappings - see :attr:`glyph.altuni`.
    """

    unlinkRmOvrlpSave: int
    """
    A flag that indicates the glyph's references should be unlinked and remove
    overlap run on it before the font is saved (and then the original references
    replaced after the save finishes)
    """

    user_decomp: str
    """Your preferred decomposition for this glyph; used by :meth:`glyph.build()`."""

    vhints: tuple[tuple[float, float], ...]
    """
    A tuple of all vertical postscript hints. Each hint is itself a tuple of
    starting locations and widths.
    """

    validation_state: int
    """
    A bit mask indicating some problems this glyph might have. (readonly)

    0x1:

      If set then this glyph has been validated.

      If unset then other bits are meaningless.

    0x2:

      Glyph has an open contour.

    0x4:

      Glyph intersects itself somewhere.

    0x8:

      At least one contour is drawn in the wrong direction

    0x10:

      At least one reference in the glyph has been flipped

      (and so is drawn in the wrong direction)

    0x20:

      Missing extrema

    0x40:

      A glyph name referred to from this glyph, in an opentype table, is not
      present in the font.

    0x40000:

      Points (or control points) are too far apart. (Coordinates must be
      within 32767)

    **Postscript only**

    0x80:

      PostScript has a limit of 1500 points in a glyph.

    0x100:

      PostScript has a limit of 96 hints in a glyph.

    0x200:

      Invalid glyph name.

    **TrueType only, errors in original file**

    0x400:

      More points in a glyph than allowed in 'maxp'

    0x800:

      More paths in a glyph than allowed in 'maxp'

    0x1000:

      More points in a composite glyph than allowed in 'maxp'

    0x2000:

      More paths in a composite glyph than allowed in 'maxp'

    0x4000:

      Instructions longer than allowed in 'maxp'

    0x8000:

      More references in a glyph than allowed in 'maxp'

    0x10000:

      References nested more deeply than allowed in 'maxp'

    0x40000:

      Points too far apart. TrueType and Type2 fonts are limited to 16 bit
      numbers, and so adjacent points must be within 32767 em-units of each other.

    0x80000:

      Points non-integral. TrueType points and control points must be integer
      aligned. (FontForge will round them if they aren't)

    0x100000:

      Missing anchor. According to the opentype spec, if a glyph contains an
      anchor point for one anchor class in a subtable, it must contain anchor
      points for all anchor classes in the subtable. Even it, logically, they
      do not apply and are unnecessary.

    0x200000:

      Duplicate glyph name. Two (or more) glyphs in this font have the same
      name. When outputting a PostScript font only one of them will ever be seen.

      It's a little hard to detect this in normal use, but if you change the
      encoding to "Glyph Order", and then use Edit->Select->Wildcard and enter
      the glyph name, both of them should be selected.

    0x400000:

      Duplicate unicode code point. Two (or more) glyphs in this font have the
      code point. When outputting an sfnt (TrueType/OpenType) font only one of
      them will ever be seen.

      It's a little hard to detect this in normal use, but if you change the
      encoding to "Glyph Order", and then use Edit->Select->Wildcard and enter
      the code point, both of them should be selected.

    0x800000:

      Overlapped hints. Either the glyph has no hint masks and there are
      overlapped hints, or a hint mask specifies two overlapping hints.
    """

    verticalComponents: tuple[
        tuple[str]
        | tuple[str, bool]
        | tuple[str, bool, int]
        | tuple[str, bool, int, int]
        | tuple[str, bool, int, int, int],
        ...,
    ]
    """
    A tuple of tuples.

    This allows constructing very large versions of the glyph by stacking the
    components together. Some components may be repeated so there is no bound on the size.

    This is different from ``verticalVariants`` which expects prebuilt glyphs of
    various fixed sizes.

    The components are stacked in the order they appear in the (top-level) tuple.
    Each sub-tuple represents information on one component. The subtuple should
    contain: (String glyph-name, Boolean is-extender, Int startConnectorLength,
    Int endConnectorLength, Int fullAdvance). Any of these may be omitted (except
    the glyph name) and will be assumed to be 0 if so.
    """

    verticalComponentItalicCorrection: int
    """The italic correction for any composite glyph made with the verticalComponents."""

    verticalVariants: str
    """
    A string containing a list of glyph names. These are alternate forms
    of the current glyph for use in typesetting math. Presumably the variants
    are of different sizes.
    """

    width: int
    """The advance width of the glyph. See also :attr:`glyph.vwidth`."""

    vwidth: int
    """The vertical advance width of the glyph. See also :attr:`glyph.width`."""

    def addAnchorPoint(
        self,
        anchor_class_name: str,
        anchor_type: Literal["mark", "base", "ligature", "basemark", "entry", "entry"],
        x: float,
        y: float,
        ligature_index: int | None = None,
    ) -> None:
        """
        Adds an anchor point. anchor-type may be one of the strings

        * ``"mark"``
        * ``"base"``
        * ``"ligature"``
        * ``"basemark"``
        * ``"entry"``
        * ``"exit"``

        If there is an anchor point with the same ``anchor_class_name`` and:

        * lookup type is ``"gpos_mark2base"`` or
        * lookup type is ``"gpos_mark2ligature"`` and ``ligature_index`` is the same or
        * ``anchor_type`` is the same

        then the existing anchor will be overwritten.
        """
        ...

    def addExtrema(
        self,
        flags: Literal["all", "only_good", "only_good_rm"] = "only_good",
        emsize: int = 1000,
    ) -> None:
        """
        Extrema should be marked by on-curve points. If a curve lacks a point at an
        extrema this command will add one. Flags may be one of the following strings

        all:

          Add all missing extrema

        only_good:

          Only add extrema on longer splines (with respect to the em-size

        only_good_rm:

          As above but also merge away on-curve points which are very close to,
          but not on, an added extremum
        """
        ...

    def addReference(
        self,
        glyph_name: str,
        transform: tuple[float, float, float, float, float, float] = (1, 0, 0, 1, 0, 0),
        selected: bool = False,
    ) -> None:
        """
        Adds a reference to the specified glyph into the current glyph. Optionally
        specifying a transformation matrix and whether the reference is to be
        marked selected in the UI and related API calls.
        """
        ...

    def addHint(self, is_vertical: bool, start: float, width: float) -> None:
        """
        Adds a postscript hint. Takes a boolean flag indicating whether the hint is
        horizontal or vertical, a start location and the hint's width.
        """
        ...

    @overload
    def addPosSub(self, subtable_name: str, variant: str) -> None: ...
    @overload
    def addPosSub(self, subtable_name: str, variants: tuple[str, ...]) -> None: ...
    @overload
    def addPosSub(
        self, subtable_name: str, ligature_components: tuple[str, ...]
    ) -> None: ...
    @overload
    def addPosSub(
        self, subtable_name: str, xoff: int, yoff: int, xadv: int, yadv: int
    ) -> None: ...
    @overload
    def addPosSub(
        self, subtable_name: str, other_glyph_name: str, kerning: int
    ) -> None: ...
    @overload
    def addPosSub(
        self,
        subtable_name: str,
        other_glyph_name: str,
        xoff1: int,
        yoff1: int,
        xadv1: int,
        yadv1: int,
        xoff2: int,
        yoff2: int,
        xadv2: int,
        yadv2: int,
    ) -> None:
        """
        Adds position/substitution data to the glyph. The number and type of the
        arguments vary according to the type of the lookup containing the subtable.

        The first argument should always be a lookup subtable name.

        If the lookup is for single substitutions then the second argument should be
        a string containing a single glyph name.

        For multiple and alternated substitutions a tuple of glyph names. For
        ligatures, a tuple of the ligature components (glyph names).

        For single positionings the second through fifth arguments should be small
        integers representing the adjustment along the appropriate axis.

        For pairwise positionings (kerning) the second argument should be the name
        of the other glyph being kerned with, and the third through tenth should be
        small integers -- or, if there are exactly three arguments then the third
        specifies traditional, one-axis, kerning.

        If there is a previously existing entry, this will replace it (except for
        ligatures).
        """
        ...

    @overload
    def appendAccent(self, name: str) -> None: ...
    @overload
    def appendAccent(self, unicode: int) -> None:
        """
        Makes a reference to the specified glyph, adds that reference to the current
        layer of this glyph, and positions it to make a reasonable accent.
        """
        ...

    def autoHint(self) -> None:
        """Generates PostScript hints for this glyph."""
        ...

    def autoInstr(self) -> None:
        """Generates TrueType instructions for this glyph."""
        ...

    def autoTrace(self) -> None:
        """Auto traces any background images"""
        ...

    def boundingBox(self) -> tuple[float, float, float, float]:
        """
        Returns a tuple representing a rectangle (xmin,ymin, xmax,ymax) which is
        the minimum bounding box of the glyph.
        """
        ...

    def build(self) -> None:
        """
        If the character is a composite character, then clears it and inserts
        references to its components.
        """
        ...

    def canonicalContours(self) -> None:
        """
        Orders the contours in the current glyph by the x coordinate of their
        leftmost point. (This can reduce the size of the charstring needed to
        describe the glyph(s).
        """
        ...

    def canonicalStart(self) -> None:
        """
        Sets the start point of all the contours of the current glyph to be the
        leftmost point on the contour. (If there are several points with that value
        then use the one which is closest to the baseline). This can reduce the size
        of the charstring needed to describe the glyph(s). By regularizing things it
        can also make more things available to be put in subroutines.
        """
        ...

    def changeWeight(
        self,
        stroke_width: float,
        type: Literal["LCG", "CJK", "auto", "custom"] = "auto",
        serif_height: float = -1,
        serif_fuzz: float = 0.9,
        counter_type: Literal["squish", "retain", "auto"] = "auto",
        removeoverlap: Literal[0, 1] = 0,
        custom_zones: int | tuple[int, int, int, int] | None = None,
    ) -> None:
        """
        ``stroke_width`` is the amount by which all stems are expanded.

        ``type`` is one of ``"LCG"``, ``"CJK"``, ``"auto"``, ``"custom"``.

        ``serif_height`` tells ff not to expand serifs which are that much off the
        baseline, while serif_fuzz specifies the amount of fuzziness allowed in the
        match. If you don't want special serif behavior set this to 0.

        ``counter_type`` is one of ``"squish"``, ``"retain"``, ``"auto"``.

        ``removeoverlap`` (Cleanup Self Intersect) is a boolean int
        (0=false, 1=true). When activated, and FontForge detects that an expanded
        stroke will self-intersect, then setting this option will cause it to try to
        make things nice by removing the intersections.

        ``custom_zones`` is only meaningful if the type argument were ``"custom"``.
        It may be either a number, which specifies the "top hint" value (bottom hint
        is assumed to be 0, others are between), or a tuple of 4 numbers (top hint,
        top zone, bottom zone, bottom hint).
        """
        ...

    def condenseExtend(
        self,
        c_factor: float,
        c_add: float,
        sb_factor: float | None = None,
        sb_add: float | None = None,
        correct: bool = True,
    ) -> None:
        """
        Condenses or extends the size of the counters and side-bearings of the glyph.
        The first two arguments provide information on shrinking/growing the
        counters, the second two the sidebearings. If the last two are omitted they
        default to the same values as the first two.

        A counter's width will become: ::

          new_width = c_factor * old_width + c_add

        If present the ``correct`` argument allows you to specify whether you want
        to correct for the italic angle before condensing the glyph.
        (it defaults to``True``)
        """
        ...

    def clear(self, layer: int | str | None = None) -> None:
        """
        With no arguments, clears the contents of the glyph (and marks it as not
         :meth:`glyph.isWorthOutputting()`).
        It is not possible to clear the guide layer with this function.
        ``layer`` may be either an integer index or a string.
        """
        ...

    def cluster(
        self,
        within: float = 0.1,
        max: float = 0.5,
    ) -> None:
        """
        Moves clustered coordinates to a standard central value.
        See also :meth:`glyph.round()`.
        """
        ...

    def correctDirection(self) -> None:
        """
        Orients all contours so that external ones are clockwise and internal
        counter-clockwise.
        """
        ...

    def doUndoLayer(
        self,
        layer: int | str | None = None,
        redo: bool = False,
    ) -> None:
        """
        When ``redo`` is False this method is equivalent to the "Undo" UI menu item.
        It restores the last preserved layer state discarding the current state.
        When ``redo`` is True it is equivalent to "Redo".  You may omit the
        ``layer`` parameter, in which case the currently active layer will be used.
        Otherwise it must either be a layer name or an integer between 0 and
        ``glyph.layer_cnt-1``.

        ``doUndoLayer`` is normally used in conjunction with
        :meth:`glyph.preserveLayerAsUndo()`
        """
        ...

    def exclude(self, excluded_layer: layer) -> None:
        """
        Removes the excluded area from the current glyph. Takes an argument which is
        a layer. See also :meth:`glyph.removeOverlap()` and :meth:`glyph.intersect()`.
        """
        ...

    @overload
    def export(
        self,
        filename: str,
        *,
        layer: layer = ...,
        pixelsize: int = 100,
        bitdepth: int = 8,
        usetransform: bool = False,
        usesystem: bool = False,
        asksystem: bool = False,
    ) -> None: ...
    @overload
    def export(self, filename: str, layer: layer, /) -> None: ...
    @overload
    def export(self, filename: str, pixelsize: int = 100, bitdepth: int = 8, /) -> None:
        """
        Creates a file with the specified name containing a representation of
        the glyph. Uses the file's extension to determine output file type.

        The following optional keywords modify the export process for various formats:

        layer (default=glyph.activeLayer):

          For vector formats, the layer to export.

        pixelsize:

          For raster formats, the size of the image to output.

        bitdepth:

          For raster formats, the depth of the image to output. Must be 1 or 8.

        usetransform:

          Flip the Y-axis of exported SVGs with a transform element rather than
          modifying the individual Y values.

        usesystem:

          Ignore the above keyword settings and use the values set by the user
          in the Import options dialog.

        asksystem:

          If the UI is present show the Import options dialog to the user
          and use the chosen values (does nothing otherwise).
        """
        ...

    def genericGlyphChange(self, **kwargs: GlyphChangeOptions) -> None:
        """Similar to font.genericGlyphChange, but acting on this glyph only."""
        ...

    def getPosSub(
        self, lookup_subtable_name: str
    ) -> (
        tuple[str, Literal["Position"], int, int, int, int, int]
        | tuple[str, Literal["Pair"], str, int, int, int, int, int, int, int, int]
        | tuple[str, Literal["Substitution"], str]
        | tuple[
            str, Literal["AltSubs", "MultSubs", "Ligature"], Unpack[tuple[str, ...]]
        ]
    ):
        """
        Returns any positioning/substitution data attached to the glyph controlled
        by the lookup-subtable. If the name is ``"*"`` then returns data from all
        subtables.

        The data are returned as a tuple of tuples. The first element of the
        subtuples is the name of the lookup-subtable. The second element will be one
        of the strings: ``"Position"``, ``"Pair"``, ``"Substitution"``,
        ``"AltSubs"``, ``"MultSubs"``, ``"Ligature"``.

        Positioning data will be followed by four small integers representing
        adjustments to the: x position of the glyph, the y position, the horizontal
        advance, and the vertical advance.

        Pair data will be followed by the name of the other glyph in the pair and
        then eight small integers representing adjustments to the: x position of the
        first glyph, the y position, the horizontal advance, and the vertical
        advance, and then a similar foursome for the second glyph.

        Substitution data will be followed by a string containing the name of the
        glyph to replace the current one.

        Multiple and Alternate data will be followed by several strings each
        containing the name of a replacement glyph.

        Ligature data will be followed by several strings each containing the name
        of a ligature component glyph.
        """
        ...

    @overload
    def importOutlines(
        self,
        filename: str,
        *,
        scale: bool = True,
        simplify: bool = True,
        accuracy: float = 0.25,
        default_joinlimit: float = -1,
        handle_eraser: bool = False,
        correctdir: bool = False,
        usesystem: bool = False,
        asksystem: bool = False,
    ) -> None: ...
    @overload
    def importOutlines(
        self,
        filename: str,
        flags: tuple[Literal["handle_eraser", "correctdir"], ...],
        /,
    ) -> None:
        """
        Uses the file's extension to determine behavior. Imports outline descriptions
        (eps, svg, glif files) into the foreground layer. Imports image descriptions
        (bmp, png, xbm, etc.) into the background layer. The following optional
        keywords modify the import process for various formats:

        scale:

          Scale imported images and SVGs to ascender height

        simplify:

          Run simplify on the output of stroked paths

        accuracy:

          The minimum accuracy (in em-units) of stroked paths.

        default_joinlimit:

          Override the format's default miterlimit for stroked paths, which is
          10.0 for PostScript and 4.0 for SVG. (Value -1 means "inherit" those
          defaults.)

        handle_eraser:

          Certain programs use pens with white ink as erasers. When this flag is
          set FontForge will attempt to simulate that.

        correctdir:

          Run "Correct direction" on (some) PostScript paths

        usesystem:

          Ignore the above keyword settings and use the values set by the user
          in the Import options dialog.

        asksystem:

          If the UI is present show the Import options dialog to the user
          and use the chosen values (does nothing otherwise).
        """
        ...

    def intersect(self) -> None:
        """
        Leaves only areas in the intersection of contours. See also
        :meth:`glyph.removeOverlap()` and :meth:`glyph.exclude()`.
        """
        ...

    def isWorthOutputting(self) -> bool:
        """
        Returns whether the glyph is worth outputting into a font file. Basically a
        glyph is worth outputting if it contains any contours, or references or has
        had its width set.
        """
        ...

    def preserveLayerAsUndo(
        self,
        layer: int | str | None = None,
        dohints: bool = False,
    ) -> None:
        """
        Normally undo handling is turned off during python scripting. This method
        preserves the current state of a layer so that whatever you do after can be
        undone by the user. You may omit the ``layer`` parameter, in which case the
        currently active layer will be used. Otherwise it must either be a layer name
        or an integer between 0 and ``glyph.layer_cnt-1``. When ``dohints`` is True
        then hints will also be preserved (they are not by default).
        """
        ...

    def removeOverlap(self) -> None:
        """
        Removes overlapping areas.
        See also :meth:`glyph.intersect()` and :meth:`glyph.exclude()`.
        """
        ...

    def removePosSub(self, lookup_subtable_name: str) -> None:
        """
        Removes all data from the glyph corresponding to the given lookup-subtable.
        If the name is "*" then all data will be removed.
        """
        ...

    def round(self, factor: float = 1) -> None:
        """
        Rounds the x and y coordinates of each point in the glyph. If factor is
        specified then ::

           new-coord = round(factor*old-coord)/factor

        See also :meth:`glyph.cluster()`.
        """
        ...

    def selfIntersects(self) -> bool:
        """
        Returns whether any of the contours in this glyph intersects any other
        contour in the glyph (including itself).
        """
        ...

    def setLayer(
        self,
        layer: layer,
        layer_index: int,
        flags: tuple[
            Literal[
                "select_none",
                "select_all",
                "select_smooth",
                "select_incompat",
                "by_geom",
                "downgrade",
                "check",
                "force",
                "hcurve",
            ],
            ...,
        ] = ("select_all", "by_geom"),
    ) -> None:
        """
        An alternative to assigning to :attr:`glyph.layers`, :attr:`glyph.background`,
        or :attr:`glyph.foreground`, and equivalent to those when not using the
        optional ``flags`` argument. When present, ``flags`` can be used to influence
        the types FontForge will assign to on-curve points. It should be a tuple of
        up to three of the following strings.

        (In the following descriptions *selected* refers to points picked out by the
        chosen ``select_`` flag, which is unrelated to :attr:`point.selected`. At
        most one ``"select_"`` flag and one mode flag should be included.)

        select_none:

          Each (on-curve) point will be assigned a type corresponding to its
          :attr:`point.type` value.

        select_all:

          (default) Each point will have a type assigned according to the chosen mode.

        select_smooth:

          Each point with the type :data:`splineCorner` will retain that type,
          others will be assigned a type according to the chosen mode. This makes
          :attr:`point.type` function like the ``smooth`` tag in the UFO glif
          format and some other spline storage formats.

        select_incompat:

          Each point with a type compatible with its current geometry will retain
          that type, others will be assigned a type according to the chosen mode.

        by_geom:

          (default) In this mode, each *selected* point will be assigned a type
          based on only its geometry. (However, see ``"hvcurve"``` below.)

        downgrade:

          In this mode, each *selected* point will be assigned the most specific
          type compatible with its geometry and its :attr:`point.type`. A point
          marked :data:`splineHVCurve` can keep that type or be downgraded to
          :data:`splineCurve` or :data:`splineCorner`, while a :data:`splineCurve`
          or :data:`splineTangent` can keep that (respective) type or be downgraded
          to :data:`splineCorner`. (:data:`splineCorner` is compatible with any
          geometry.)

        check:

          In this mode, the type of each *selected* point is verified to be
          compatible with its geometry. If it is not compatible the function raises
          an exception. (At present this exception is not very informative. However,
          to identify the specific problem one can duplicate the layer, use
          :meth:`glyph.setLayer()` with ``downgrade``, and then retrieve the layer
          and compare it with the original.)

        force:

          In this mode, the geometry of each *selected* point is altered to match
          its :attr:`point.type`, similar to changing a point's type using the UI.
          Note that FontForge's point conversion algorithm is not sophisticated
          and may not have the desired result.

        hvcurve:

          This extra flag can be used to include :data:`splineHVCurve` among the
          types that can be assigned "by geometry". Normally FontForge assigns
          :data:`splineCurve` to on-curve points with strictly horizontal or
          vertical off-curve points.
        """
        ...

    def simplify(
        self,
        error_bound: float | None = None,
        flags: tuple[
            Literal[
                "ignoreslopes",
                "ignoreextrema",
                "smoothcurves",
                "choosehv",
                "forcelines",
                "nearlyhvlines",
                "mergelines",
                "setstarttoextremum",
                "removesingletonpoints",
            ],
            ...,
        ] = (),
        tan_bounds: float | None = None,
        linefixup: float | None = None,
        linelenmax: float | None = None,
    ) -> None:
        """
        Tries to remove excess points in the glyph if doing so will not perturb the
        curve by more than ``error-bound``. Flags is a tuple of the following strings

        ignoreslopes:

          Allow slopes to change

        ignoreextrema:

          Allow removal of extrema

        smoothcurves:

          Allow curve smoothing

        choosehv:

          Snap to horizontal or vertical

        forcelines:

          flatten bumps on lines

        nearlyhvlines:

          Make nearly horizontal/vertical lines be so

        mergelines:

          Merge adjacent lines into one

        setstarttoextremum:

          Rotate the point list so that the start point is on an extremum

        removesingletonpoints:

          If the contour contains just one point then remove it
        """
        ...

    @overload
    def stroke(
        self,
        type: Literal["circular"],
        width: float,
        /,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        angle: float = 0,
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["elliptical"],
        width: float,
        minor_width: float,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["calligraphic"],
        width: float,
        height: float,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["convex"],
        nib: contour | layer,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None:
        """
        Strokes the contours of the glyph according to the supplied parameters.

        A ``"circular"`` nib just has a ``width`` (the diameter), while an
        ``"elliptical"`` nib has a ``width`` (major axis) and a ``minor_width``
        (minor axis). A ``"calligraphic"`` or ``"rectangular"`` nib is similar in
        that it has a ``width`` and a ``height``. Finally a ``"convex"`` nib is one
        supplied by the user as a :class:`fontforge.contour` or :class:`fontforge.layer`.
        It must be *convex* as defined in the main stroke facility documentation.

        ``ANGLE`` is optional. It can be specified either positionally or with
        ``angle=float``. It must be a floating point number in units of radians and
        defaults to zero. The nib is rotated by this angle before stroking the path.

        ``CAP`` is optional. It can be specified either positionally or with
        ``cap=string``. It must be one of the strings "nib" (the default), "butt",
        "round", and "bevel".

        ``JOIN`` is optional. It can be specified either positionally or with
        ``join=string``. It must be one of the strings "nib" (the default), "bevel",
        "miter", and "miterclip", "round", and "arcs".
        """
        ...

    def transform(
        self,
        matrix: tuple[float, float, float, float, float, float],
        flags: tuple[Literal["partialRefs", "round"], ...] = (),
    ) -> None:
        """
        Transforms the glyph by the matrix. The optional flags argument should be a
        tuple containing any of the following strings:

        partialRefs:

          Don't transform any references in the glyph, but do transform their offsets.
          This is useful if the referred glyph will be (or has been) transformed.

        round:

          Round to int after the transformation is done.
        """
        ...

    def nltransform(self, xexpr: str, yexpr: str) -> None:
        """
        xexpr and yexpr are strings specifying non-linear transformations that will
        be applied to all points in the current layer (with xexpr being applied to x
        values, and yexpr to y values, of course).
        """
        ...

    def unlinkRef(self, ref_name: str | None = None) -> None:
        """
        Unlinks the reference to the glyph named ``ref-name``. If ``ref-name`` is
        omitted, unlinks all references.
        """
        ...

    def unlinkThisGlyph(self) -> None:
        """
        Unlinks all the references to the current glyph within any other glyph in
        the font.
        """
        ...

    def useRefsMetrics(self, ref_name: str, flag: bool = True) -> None:
        """
        Finds a reference with the given name and sets the "use_my_metrics" flag on
        it (so this glyph will have the same advance width as the glyph the
        reference points to).

        If the optional flag argument is False, then the glyph will no longer have
        its metrics bound to the reference.
        """
        ...

    def validate(self, force: bool = False) -> int:
        """
        Validates the glyph and returns the :attr:`validation_state` of the glyph
        (except bit 0x1 will always be clear). If the glyph passed the validation
        then the return value will be 0 (not 0x1). Otherwise the return value will
        be the set of errors found. If force is specified true this will always be
        validated, if force is unspecified (or specified as false) then it will
        return the cached value if it is known, otherwise will validate it.
        """
        ...

    def draw(self, pen: glyphPen) -> None:
        """Draw the glyph's outline to the pen argument. http://robofab.org/objects/pens.html"""
        ...

    def glyphPen(self, replace: bool = True) -> glyphPen:
        """
        Creates a new glyphPen which will draw into the current glyph. By default
        the pen will replace any existing contours and references, but setting the
        optional keyword argument, ``replace`` to false will retain the old contents.
        """
        ...

    def addInflections(self) -> None:
        """Please see :meth:`contour.addInflections()`."""
        ...

    def balance(self) -> None:
        """Please see :meth:`contour.balance()`."""
        ...

    def harmonize(self) -> None:
        """Please see :meth:`contour.harmonize()`."""
        ...

class selection:
    """
    This represents a font's selection. You may index it with an encoding value (in
    the encoding ISO-646-US (ASCII) the character "A" has encoding index 65), or
    with a glyph's name, or with a string like ``"uXXXXX"`` where ``XXXXX``
    represent the glyph's unicode codepoint in hex, or with a
    :class:`fontforge.glyph` object. The value of indexing into a selection will be
    either ``True`` or ``False``. ::

       >>> print(fontforge.activeFont().selection[65])
       True

    This type may not be pickled.
    """

    byGlyphs: selection
    """
    Returns another selection, just the same as this one except that its
    iterator function will return glyphs (rather than encoding slots) and
    will only return those entries for which glyphs exist.

    This is read-only.
    """
    ...

    def __iter__(self) -> Iterator[Any]:
        """
        Returns an iterator for the selection which will return all selected
        encoding slots in encoding order.
        """
        ...

    def all(self) -> None:
        """Select everything."""
        ...

    def none(self) -> None:
        """Deselect everything."""
        ...

    def changed(self) -> None:
        """Select all glyphs which have changed."""
        ...

    def invert(self) -> None:
        """Invert the selection."""
        ...

    def select(
        self,
        *args: str
        | int
        | glyph
        | tuple[
            Literal["unicode", "encoding", "more", "less", "singletons", "ranges"], ...
        ],
    ) -> None:
        """
        There may be an arbitrary number of arguments. Each argument may be either:

        * A glyph name

          Note: There need not be a glyph with this name in the font yet, but if you
          use a standard name (like "A") fontforge will still know where that glyph
          should be.
        * An integer (this will be interpreted as either an encoding index or
          (default) a unicode code point depending on the flags).
        * A fontforge glyph.
        * A tuple of flags.

          (If you wish to specify a single flag it must still be in a tuple, and you
          must append a trailing comma to the flag (so ``("more",)`` rather than
          just ``("more")`` ). FF needs the flags to be in a tuple otherwise it
          can't distinguish them from glyph names)

          unicode:

            Interpret integer arguments as unicode code points

          encoding:

            Interpret integer arguments as encoding indeces.

          more:

            Specified items should be selected

          less:

            Specified items should be deselected.

          singletons:

            Specified items should be interpreted individually and mean the obvious.

          ranges:

            Specified items should be interpreted in pairs and represent all
            encoding slots between the start and end points specified by the pair.
            So ``.select(("ranges",None),"A","Z")`` would select all the upper case
            (latin) letters.

        If the first argument is not a flag argument (or if it doesn't specify
        either "more" or "less") then the selection will be cleared. So
        ``.select("A")`` would produce a selection with only "A" selected,
        ``.select(("more",None),"A")`` would add "A" to the current selection, while
        ``.select(("less",None),"A")`` would remove "A" from the current selection.
        """
        ...

    def __getitem__(self, key: int | str | glyph) -> bool: ...

# Private class
class private(Mapping[str, str | float | int | tuple[float, ...]]):
    """
    This represents a font's postscript private dictionary. You may index it with
    one of the standard names of things that live in the private dictionary.

    This type may not be pickled.
    """

    @override
    def __iter__(self) -> Iterator[str]:
        """Returns an iterator for the dictionary which will return all entries."""
        ...

    def guess(self, name: str) -> None:
        """
        Guess a value for this entry in the private dictionary. If FontForge
        can't make a guess it will simply ignore the request.
        """
        ...

    @override
    def __len__(self) -> int: ...
    @override
    def __getitem__(self, key: str) -> str | float | int | tuple[float, ...]: ...
    def __setitem__(
        self, key: str, value: str | float | int | tuple[float, ...]
    ) -> None: ...

DeviceTable = dict[int, int]
"""
A dictionary with keys representing a font size in pixels and values representing
the corresponding adjustment, e.g. ``{9: -1, 10: -1, 12: -1}``.
"""

class math:
    """
    This represents a font's math constant table. Not all fonts have math tables,
    and checking this field will not create the underlying object, but examining or
    assigning to its members will create it.

    This type may not be pickled.

    Any of the math constant names may be used as member names.

    (These names begin with capital letters, not Python's conventions but Microsoft's)

    These all take (16 bit) integer values.

    Setting a ``DeviceTable`` property to ``None`` will delete it.

    Device table entries can also be queried and assigned by font size ::

       font.math.MathLeadingDeviceTable[12] = 2
       adj = font.math.MathLeadingDeviceTable[12]

    """

    ScriptPercentScaleDown: int
    """Percentage scale down for script level 1."""

    ScriptScriptPercentScaleDown: int
    """Percentage scale down for script level 2."""

    DelimitedSubFormulaMinHeight: int
    """Minimum height at which to treat a delimited expression as a subformula."""

    DisplayOperatorMinHeight: int
    """Minimum height of n-ary operators (integration, summation, etc.)."""

    MathLeading: int
    """White space to be left between math formulae to ensure proper line spacing."""

    MathLeadingDeviceTable: DeviceTable | None
    """White space to be left between math formulae to ensure proper line spacing."""

    AxisHeight: int
    """Axis height of the font."""

    AxisHeightDeviceTable: DeviceTable | None
    """Axis height of the font."""

    AccentBaseHeight: int
    """Maximum (ink) height of accent base that does not require raising the accents."""

    AccentBaseHeightDeviceTable: DeviceTable | None
    """Maximum (ink) height of accent base that does not require raising the accents."""

    FlattenedAccentBaseHeight: int
    """Maximum (ink) height of accent base that does not require flattening the accents."""

    FlattenedAccentBaseHeightDeviceTable: DeviceTable | None
    """Maximum (ink) height of accent base that does not require flattening the accents."""

    SubscriptShiftDown: int
    """
    The standard shift down applied to subscript elements. Positive for
    moving downward.
    """

    SubscriptShiftDownDeviceTable: DeviceTable | None
    """
    The standard shift down applied to subscript elements. Positive for
    moving downward.
    """

    SubscriptTopMax: int
    """
    Maximum height of the (ink) top of subscripts that does not require moving
    subscripts further down.
    """

    SubscriptTopMaxDeviceTable: DeviceTable | None
    """
    Maximum height of the (ink) top of subscripts that does not require moving
    subscripts further down.
    """

    SubscriptBaselineDropMin: int
    """
    Maximum allowed drop of the baseline of subscripts relative to the bottom of
    the base. Used for bases that are treated as a box or extended shape.
    Positive for subscript baseline dropped below base bottom.
    """

    SubscriptBaselineDropMinDeviceTable: DeviceTable | None
    """
    Maximum allowed drop of the baseline of subscripts relative to the bottom of
    the base. Used for bases that are treated as a box or extended shape.
    Positive for subscript baseline dropped below base bottom.
    """

    SuperscriptShiftUp: int
    """Standard shift up applied to superscript elements."""

    SuperscriptShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to superscript elements."""

    SuperscriptShiftUpCramped: int
    """Standard shift of superscript relative to base in cramped mode."""

    SuperscriptShiftUpCrampedDeviceTable: DeviceTable | None
    """Standard shift of superscript relative to base in cramped mode."""

    SuperscriptBottomMin: int
    """
    Minimum allowed height of the bottom of superscripts that does not require
    moving them further up.
    """

    SuperscriptBottomMinDeviceTable: DeviceTable | None
    """
    Minimum allowed height of the bottom of superscripts that does not require
    moving them further up.
    """

    SuperscriptBaselineDropMax: int
    """
    Maximum allowed drop of the baseline of superscripts relative to the top of
    the base. Used for bases that are treated as a box or extended shape.
    Positive for superscript baseline below base top.
    """

    SuperscriptBaselineDropMaxDeviceTable: DeviceTable | None
    """
    Maximum allowed drop of the baseline of superscripts relative to the top of
    the base. Used for bases that are treated as a box or extended shape.
    Positive for superscript baseline below base top.
    """

    SubSuperscriptGapMin: int
    """Minimum gap between the superscript and subscript ink."""

    SubSuperscriptGapMinDeviceTable: DeviceTable | None
    """Minimum gap between the superscript and subscript ink."""

    SuperscriptBottomMaxWithSubscript: int
    """
    The maximum level to which the (ink) bottom of superscript can be pushed to
    increase the gap between superscript and subscript, before subscript starts
    being moved down.
    """

    SuperscriptBottomMaxWithSubscriptDeviceTable: DeviceTable | None
    """
    The maximum level to which the (ink) bottom of superscript can be pushed to
    increase the gap between superscript and subscript, before subscript starts
    being moved down.
    """

    SpaceAfterScript: int
    """Extra white space to be added after each sub/superscript."""

    SpaceAfterScriptDeviceTable: DeviceTable | None
    """Extra white space to be added after each sub/superscript."""

    UpperLimitGapMin: int
    """
    Minimum gap between the bottom of the upper limit, and the top of the base
    operator.
    """

    UpperLimitGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between the bottom of the upper limit, and the top of the base
    operator.
    """

    UpperLimitBaselineRiseMin: int
    """
    Minimum distance between the baseline of an upper limit and the bottom of
    the base operator.
    """

    UpperLimitBaselineRiseMinDeviceTable: DeviceTable | None
    """
    Minimum distance between the baseline of an upper limit and the bottom of
    the base operator.
    """

    LowerLimitGapMin: int
    """
    Minimum gap between (ink) top of the lower limit, and (ink) bottom of the
    base operator.
    """

    LowerLimitGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between (ink) top of the lower limit, and (ink) bottom of the
    base operator.
    """

    LowerLimitBaselineDropMin: int
    """
    Minimum distance between the baseline of the lower limit and bottom of the
    base operator.
    """

    LowerLimitBaselineDropMinDeviceTable: DeviceTable | None
    """
    Minimum distance between the baseline of the lower limit and bottom of the
    base operator.
    """

    StackTopShiftUp: int
    """Standard shift up applied to the top element of a stack."""

    StackTopShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the top element of a stack."""

    StackTopDisplayStyleShiftUp: int
    """
    Standard shift up applied to the top element of a stack in display style.
    """

    StackTopDisplayStyleShiftUpDeviceTable: DeviceTable | None
    """
    Standard shift up applied to the top element of a stack in display style.
    """

    StackBottomShiftDown: int
    """
    Standard shift down applied to the bottom element of a stack. Positive
    values indicate downward motion.
    """

    StackBottomShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the bottom element of a stack. Positive
    values indicate downward motion.
    """

    StackBottomDisplayStyleShiftDown: int
    """
    Standard shift down applied to the bottom element of a stack in display
    style. Positive values indicate downward motion.
    """

    StackBottomDisplayStyleShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the bottom element of a stack in display
    style. Positive values indicate downward motion.
    """

    StackGapMin: int
    """
    Minimum gap between bottom of the top element of a stack, and the top of
    the bottom element.
    """

    StackGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between bottom of the top element of a stack, and the top of
    the bottom element.
    """

    StackDisplayStyleGapMin: int
    """
    Minimum gap between bottom of the top element of a stack and the top of the
    bottom element in display style.
    """

    StackDisplayStyleGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between bottom of the top element of a stack and the top of the
    bottom element in display style.
    """

    StretchStackTopShiftUp: int
    """Standard shift up applied to the top element of the stretch stack."""

    StretchStackTopShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the top element of the stretch stack."""

    StretchStackBottomShiftDown: int
    """
    Standard shift down applied to the bottom element of the stretch stack.
    Positive values indicate downward motion.
    """

    StretchStackBottomShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the bottom element of the stretch stack.
    Positive values indicate downward motion.
    """

    StretchStackGapAboveMin: int
    """
    Minimum gap between the ink of the stretched element and the ink bottom of
    the element above.
    """

    StretchStackGapAboveMinDeviceTable: DeviceTable | None
    """
    Minimum gap between the ink of the stretched element and the ink bottom of
    the element above.
    """

    StretchStackGapBelowMin: int
    """
    Minimum gap between the ink of the stretched element and the ink top of
    the element below.
    """

    StretchStackGapBelowMinDeviceTable: DeviceTable | None
    """
    Minimum gap between the ink of the stretched element and the ink top of
    the element below.
    """

    FractionNumeratorShiftUp: int
    """Standard shift up applied to the numerator."""

    FractionNumeratorShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the numerator."""

    FractionNumeratorDisplayStyleShiftUp: int
    """Standard shift up applied to the numerator in display style."""

    FractionNumeratorDisplayStyleShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the numerator in display style."""

    FractionDenominatorShiftDown: int
    """
    Standard shift down applied to the denominator. Positive values indicate
    downward motion.
    """

    FractionDenominatorShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the denominator. Positive values indicate
    downward motion.
    """

    FractionDenominatorDisplayStyleShiftDown: int
    """
    Standard shift down applied to the denominator in display style. Positive
    values indicate downward motion.
    """

    FractionDenominatorDisplayStyleShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the denominator in display style. Positive
    values indicate downward motion.
    """

    FractionNumeratorGapMin: int
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar.
    """

    FractionNumeratorGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar.
    """

    FractionNumeratorDisplayStyleGapMin: int
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar in display style.
    """

    FractionNumeratorDisplayStyleGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar in display style.
    """

    FractionRuleThickness: int
    """Thickness of the fraction bar."""

    FractionRuleThicknessDeviceTable: DeviceTable | None
    """Thickness of the fraction bar."""

    FractionDenominatorGapMin: int
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar.
    """

    FractionDenominatorGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar.
    """

    FractionDenominatorDisplayStyleGapMin: int
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar in display style.
    """

    FractionDenominatorDisplayStyleGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar in display style.
    """

    SkewedFractionHorizontalGap: int
    """
    Horizontal distance between the top and bottom elements of a skewed fraction.
    """

    SkewedFractionHorizontalGapDeviceTable: DeviceTable | None
    """
    Horizontal distance between the top and bottom elements of a skewed fraction.
    """

    SkewedFractionVerticalGap: int
    """
    Vertical distance between the ink of the top and bottom elements of a skewed
    fraction.
    """

    SkewedFractionVerticalGapDeviceTable: DeviceTable | None
    """
    Vertical distance between the ink of the top and bottom elements of a skewed
    fraction.
    """

    OverbarVerticalGap: int
    """Distance between the overbar and the ink top of the base."""

    OverbarVerticalGapDeviceTable: DeviceTable | None
    """Distance between the overbar and the ink top of the base."""

    OverbarRuleThickness: int
    """Thickness of the overbar."""

    OverbarRuleThicknessDeviceTable: DeviceTable | None
    """Thickness of the overbar."""

    OverbarExtraAscender: int
    """Extra white space reserved above the overbar."""

    OverbarExtraAscenderDeviceTable: DeviceTable | None
    """Extra white space reserved above the overbar."""

    UnderbarVerticalGap: int
    """Distance between underbar and the (ink) bottom of the base."""

    UnderbarVerticalGapDeviceTable: DeviceTable | None
    """Distance between underbar and the (ink) bottom of the base."""

    UnderbarRuleThickness: int
    """Thickness of the underbar."""

    UnderbarRuleThicknessDeviceTable: DeviceTable | None
    """Thickness of the underbar."""

    UnderbarExtraDescender: int
    """Extra white space reserved below the underbar."""

    UnderbarExtraDescenderDeviceTable: DeviceTable | None
    """Extra white space reserved below the underbar."""

    RadicalVerticalGap: int
    """Space between the ink to of the expression and the bar over it."""

    RadicalVerticalGapDeviceTable: DeviceTable | None
    """Space between the ink to of the expression and the bar over it."""

    RadicalDisplayStyleVerticalGap: int
    """
    Space between the ink top of the expression and the bar over it in display
    style.
    """

    RadicalDisplayStyleVerticalGapDeviceTable: DeviceTable | None
    """
    Space between the ink top of the expression and the bar over it in display
    style.
    """

    RadicalRuleThickness: int
    """
    Thickness of the radical rule in designed or constructed radical signs.
    """

    RadicalRuleThicknessDeviceTable: DeviceTable | None
    """
    Thickness of the radical rule in designed or constructed radical signs.
    """

    RadicalExtraAscender: int
    """Extra white space reserved above the radical."""

    RadicalExtraAscenderDeviceTable: DeviceTable | None
    """Extra white space reserved above the radical."""

    RadicalKernBeforeDegree: int
    """
    Extra horizontal kern before the degree of a radical if such be present.
    """

    RadicalKernBeforeDegreeDeviceTable: DeviceTable | None
    """
    Extra horizontal kern before the degree of a radical if such be present.
    """

    RadicalKernAfterDegree: int
    """
    Negative horizontal kern after the degree of a radical if such be present.
    """

    RadicalKernAfterDegreeDeviceTable: DeviceTable | None
    """
    Negative horizontal kern after the degree of a radical if such be present.
    """

    RadicalDegreeBottomRaisePercent: int
    """
    Height of the bottom of the radical degree, if such be present, in
    proportion to the ascender of the radical sign.
    """

    MinConnectorOverlap: int
    """Minimum overlap of connecting glyphs during glyph construction."""

    def exists(self) -> bool:
        """
        Returns whether the font currently has an underlying math table
        associated with it. Note that examining or assigning to one of the members
        will create such a table.
        """
        ...

    def clear(self) -> None:
        """Removes any underlying math table from the font."""
        ...

class FontLayerInfo:
    """Information about a layer of a font."""

    name: str
    """The name of the layer."""

    is_quadratic: bool
    """Whether the layer is quadratic."""

    is_background: bool
    """Whether the layer is a background layer."""

class font:
    """
    The font type refers to a fontforge :class:`font` object. It generally contains
    a list of :class:`glyphs <fontforge.glyph>`, an encoding to order those glyphs,
    a fontname, a list of GPOS/GSUB lookups and many other things.

    This type may not be pickled.
    """

    def __init__(self) -> None:
        """Creates a new font."""
        ...

    activeLayer: int | str
    """
    Returns currently active layer in the font (as an integer).
    May be set to an integer or a layer name to change the active layer.
    """

    ascent: int
    """The font's ascent."""

    bitmapSizes: tuple[int, ...]
    """
    A tuple with an entry for each bitmap strike attached to the font.
    Each strike is identified by pixelsize. If the strike is a grey scale font it
    will be indicated by ``(bitmap-depth<<16)|pixelsize``.

    When setting this value pass in a tuple of the same format. Any existing
    strike not specified in the tuple will be removed. Any new sizes will be
    created (but not rasterized -- use :meth:`font.regenBitmaps()` for that).
    """

    capHeight: float
    """
    (readonly) Computes the Cap Height (the height of capital letters such as
    "E"). A negative number indicates the value could not be computed (the font
    might have no capital letters because it was lower case only, or didn't
    include glyphs for a script with capital letters).
    """

    changed: int
    """
    Bit indicating whether the font has been modified. This is (should be)
    maintained automatically, but you may set it if you wish.
    """

    cidcopyright: str | None
    """Copyright message of the cid-keyed font as a whole (ie. not the current subfont)."""

    cidfamilyname: str | None
    """Family name of the cid-keyed font as a whole (ie. not the current subfont)."""

    cidfontname: str | None
    """Font name of the cid-keyed font as a whole (ie. not the current subfont)."""

    cidfullname: str | None
    """Full name of the cid-keyed font as a whole (ie. not the current subfont)."""

    cidordering: str | None
    """CID Ordering"""

    cidregistry: str | None
    """CID Registry"""

    cidsubfont: int | str
    """
    Returns the number index of the current subfont in the cid-keyed font (or -1
    if this is not a cid-keyed font).

    May be set to an index (an integer) or a subfont fontname (a string) to
    change the current subfont. (To find the name of the current subfont,
    simply use .fontname).
    """

    cidsubfontcnt: int
    """
    Returns the number of subfonts in this cid-keyed font (or 0 if it is not a
    cid-keyed font)
    """

    cidsubfontnames: tuple[str, ...]
    """
    Returns a tuple of the subfont names in this cid-keyed font (or None if it
    is not a cid-keyed font)
    """

    cidsupplement: int
    """CID Supplement"""

    cidversion: float
    """CID Version"""

    cidweight: str | None
    """Weight of the cid-keyed font as a whole."""

    comment: str | None
    """A comment associated with the font. Can be anything."""

    copyright: str | None
    """PostScript copyright notice."""

    cvt: Sequence[int]
    """
    Returns a sequence object containing the font's cvt table. Changes made
    to this object will be made to the font (this is a reference not a copy).

    The object has one additional method ``cvt.find(value[,low,high])`` which
    finds the index of value in the cvt table (or -1 if not found). If low and
    high are specified then the index will be between ``[low,high)``.
    """

    default_base_filename: str | None
    """The default base for the filename when generating a font. """

    descent: int
    """The font's descent."""

    design_size: float
    """Size (in pica points) for which this font was designed. """

    em: int
    """
    The em size of the font.Setting this will scale the entire font to the
    new size.
    """

    encoding: str
    """
    The name of the current encoding. Setting it will change the encoding used
    for indexing. To compact the encoding, first set it to your desired encoding
    (e.g. ``UnicodeBMP``), then set it to ``compacted``.
    """

    familyname: str
    """PostScript font family name."""

    fondname: str | None
    """Mac fond name."""

    fontlog: str | None
    """A comment associated with the font. Can be anything."""

    fontname: str
    """
    PostScript font name.

    Note that in a CID keyed font this will be the name of the current subfont.
    Use cidfontname for the name of the font as a whole.
    """

    fullname: str
    """PostScript font name."""

    gasp: tuple[
        tuple[
            int,
            tuple[
                Literal[
                    "gridfit", "antialias", "symmetric-smoothing", "gridfit+smoothing"
                ],
                ...,
            ],
        ]
    ]
    """
    Returns a tuple of all gasp table entries. Each item in the tuple is itself
    a tuple composed of a ppem (an integer) and a tuple of flags. The flags are
    chosen from:

    * ``gridfit``
    * ``antialias``
    * ``symmetric-smoothing``
    * ``gridfit+smoothing``
    """

    gasp_version: int
    """The version of the 'gasp' table. Currently this may be 0 or 1. """

    gpos_lookups: tuple[str, ...]
    """
    Returns a tuple of all positioning lookup names in the font.
    This member cannot be set.
    """

    gsub_lookups: tuple[str, ...]
    """
    Returns a tuple of all substitution lookup names in the font.
    This member cannot be set.
    """

    guide: layer
    """A copy of the font's guide layer."""

    hasvmetrics: int
    """Flag indicating whether the font contains vertical metrics"""

    head_optimized_for_cleartype: int
    """Whether the font is optimized for cleartype"""

    hhea_ascent: int
    """hhea ascent"""

    hhea_ascent_add: int
    """
    Whether the hhea_ascent field is used as is, or as an offset applied to
    the value FontForge thinks appropriate
    """

    hhea_descent: int
    """hhea descent"""

    hhea_descent_add: int
    """
    Whether the hhea_descent field is used as is, or as an offset applied to
    the value FontForge thinks appropriate
    """

    hhea_linegap: int
    """hhea linegap"""

    horizontalBaseline: (
        tuple[
            tuple[str, ...],
            tuple[
                tuple[
                    str,
                    str | None,
                    tuple[int, ...] | None,
                    tuple[
                        tuple[
                            str,
                            int,
                            int,
                            tuple[
                                tuple[
                                    str,
                                    int,
                                    int,
                                ],
                                ...,
                            ],
                        ],
                        ...,
                    ],
                ],
                ...,
            ],
        ]
        | None
    )
    """
    Returns a tuple of tuples containing the horizontal baseline information in
    the font (the 'BASE' table). If there is no information ``None`` will be
    returned, otherwise the format of the tuple is: ::

       ((tuple of baseline tags used), (tuple of script information))

    The ``(tuple of baseline tags used)`` is simply a tuple of 4 letter strings
    as ``("hang", "ideo", "romn")`` these are standard baseline tag names as
    defined in the opentype spec. The number of entries here, and their order is
    important as there will be subsequent tuples (in the script tuple) which use
    the same ordering.

    The ``(tuple of script information)`` is again a tuple of
    ``script information`` tuples.

    A ``script information`` tuple looks like ::

       (script-tag,default-baseline-tag, (tuple of baseline positions), (tuple of language extents))

    If there are no baseline tags defined (an empty tuple), then the
    ``default-baseline-tag`` and the ``(tuple of baseline positions)`` will be
    ``None``. Otherwise both tags will be 4 character strings, and the ``(tuple
    of baseline positions)`` will be a tuple of numbers (in the same order as the
    ``(tuple of baseline tags used)`` above) specifying the relative positions
    of each baseline for this script.

    A ``(tuple of language extents)`` is a tuple of ``language extent`` tuples.

    A ``language extent`` tuple is ::

       (language-tag,min-extent,max-extent, (tuple of feature extents))

    ``language-tag`` is a 4 letter string specifying an opentype language,
    ``min``/``max-extent`` are numbers specifying how far above and below the
    baseline characters go in this script/language.

    A ``(tuple of feature extents>`` is a tuple of ``feature extent`` tuples.

    A ``feature extent`` tuple is ::

       (feature-tag,min-extent,max-extent)

    ``feature-tag`` is a 4 letter string specifying an opentype (GPOS or GSUB)
    feature tag, ``min``/``max-extent`` are numbers specifying how far above and
    below the baseline characters go in this script/language with the
    feature applied.

    **Example:**

    ::

       (("hang","ideo","romn"),
         (("cyrl","romn",(1405,-288,0),()),
          ("grek","romn",(1405,-288,0),()),
          ("latn","romn",(1405,-288,0),
            (("dflt",-576,1913,
              (("NoAc",-576,1482),
               ("ENG ",-576,1482))
            ),
          )
         )
        )
       )

    (Note: The comma after the ``dflt`` tuple puts it into a one-element tuple.)
    """

    is_cid: int
    """Indicates whether the font is a cid-keyed font or not. (Read-only)"""

    is_quadratic: int
    """
    Deprecated. Whether the contours should be interpreted as a set of quadratic
    or cubic splines. Setting this value has the side effect of converting the
    entire font into the other format

    Now each layer may have its own setting for this value, which should be set
    on the font's :attr:`font.layers`.
    """

    isnew: int
    """A flag indicating that this is a new font."""

    italicangle: float
    """The Italic angle (skewedness) of the font"""

    macstyle: int
    """
    Bit 0:

      Bold (if set to 1)

    Bit 1:

      Italic (if set to 1)

    Bit 2:

      Underline (if set to 1)

    Bit 3:

      Outline (if set to 1)

    Bit 4:

      Shadow (if set to 1)

    Bit 5:

      Condensed (if set to 1)

    Bit 6:

      Extended (if set to 1)

    Bits 7-15:

      Reserved (set to 0).

    (source https://docs.microsoft.com/en-us/typography/opentype/spec/head)
    """

    layer_cnt: int
    """
    The number of layers in the font. (Read only. Can change using ``add``
    and ``del`` operations on the :attr:`font.layers` array)
    """

    layers: dict[str, FontLayerInfo]
    """
    Returns a dictionary like object with information on the layers of the
    font -- a name and a boolean indicating whether the layer is quadratic or not.

    You may remove a layer with ::

      del font.layers["unneeded layer"]

    You may add a new layer with ::

      font.layers.add("layer-name",is_quadratic[, is_background])

    You may change a layer's name with ::

      font.layers["layer"].name = "new-name"

    You may change the type of splines in a layer with ::

      font.layers["layer"].is_quadratic = True

    You may change whether it is a background layer by ::

      font.layers["layer"].is_background = True
    """

    loadState: int
    """
    A bitmask indicating non-fatal errors found when loading the font. (readonly)

    0x01:

      Bad PostScript entry in 'name' table

    0x02:

      Bad 'glyf' or 'loca' table

    0x04:

      Bad 'CFF ' table

    0x08:

      Bad 'hhea', 'hmtx', 'vhea' or 'vmtx' table

    0x10:

      Bad 'cmap' table

    0x20:

      Bad 'EBLC', 'bloc', 'EBDT' or 'bdat' (embedded bitmap) table

    0x40:

      Bad Apple GX advanced typography table

    0x80:

      Bad OpenType advanced typography table (GPOS, GSUB, GDEF, BASE)

    0x100:

      Bad OS/2 version number

      Windows will reject all fonts with a OS/2 version number of 0 and will
      reject OT-CFF fonts with a version number of 1
    """

    maxp_FDEFs: int
    """The number of function definitions used by the tt program"""

    maxp_IDEFs: int
    """The number of instruction definitions used by the tt program"""

    maxp_maxStackDepth: int
    """The maximum stack depth used by the tt program"""

    maxp_storageCnt: int
    """The number of storage locations used by the tt program"""

    maxp_twilightPtCnt: int
    """The number of points in the twilight zone of the tt program"""

    maxp_zones: int
    """The number of zones used in the tt program"""

    multilayer: int
    """Flag indicating whether the font is multilayered (type3) or not (readonly)"""

    onlybitmaps: int
    """A flag indicating that this font only contains bitmaps. No outlines. """

    os2_capheight: int
    """OS/2 Capital Height"""

    os2_codepages: tuple[int, int]
    """A 2 element tuple containing the OS/2 Codepages field"""

    os2_family_class: int
    """OS/2 Family Class"""

    os2_fstype: int
    """OS/2 fstype"""

    os2_panose: tuple[int, int, int, int, int, int, int, int, int, int]
    """The 10 element OS/2 Panose tuple"""

    os2_strikeypos: int
    """OS/2 Strikethrough YPosition"""

    os2_strikeysize: int
    """OS/2 Strikethrough YSize"""

    os2_stylemap: int
    """Write access to fsSelection, keep in sync with :attr:`font.macstyle`"""

    os2_subxoff: int
    """OS/2 Subscript XOffset"""

    os2_subxsize: int
    """OS/2 Subscript XSize"""

    os2_subyoff: int
    """OS/2 Subscript YOffset"""

    os2_subysize: int
    """OS/2 Subscript YSize"""

    os2_supxoff: int
    """OS/2 Superscript XOffset"""

    os2_supxsize: int
    """OS/2 Superscript XSize"""

    os2_supyoff: int
    """OS/2 Superscript YOffset"""

    os2_supysize: int
    """OS/2 Superscript YSize"""

    os2_typoascent: int
    """OS/2 Typographic Ascent"""

    os2_typoascent_add: int
    """
    Whether the os2_typoascent field is used as is, or as an offset applied
    to the value FontForge thinks appropriate
    """

    os2_typodescent: int
    """OS/2 Typographic Descent"""

    os2_typodescent_add: int
    """
    Whether the os2_typodescent field is used as is, or as an offset applied
    to the value FontForge thinks appropriate
    """

    os2_typolinegap: int
    """OS/2 Typographic Linegap"""

    os2_unicoderanges: tuple[int, int, int, int]
    """A 4 element tuple containing the OS/2 Unicode Ranges field"""

    os2_use_typo_metrics: int
    """
    OS/2 Flag MS thinks is necessary to encourage people to follow the
    standard and use typographic metrics
    """

    os2_vendor: str
    """The 4 character OS/2 vendor string"""

    os2_version: int
    """OS/2 table version number"""

    os2_weight: int
    """OS/2 weight"""

    os2_weight_width_slope_only: int
    """OS/2 Flag MS thinks is necessary"""

    os2_width: int
    """OS/2 width"""

    os2_winascent: int
    """OS/2 Windows Ascent"""

    os2_windescent: int
    """OS/2 Windows Descent"""

    os2_xheight: int
    """OS/2 x Height"""

    path: str
    """
    (readonly) Returns a string containing the name of the file from which the
    font was originally read (in this session), or if this is a new font, returns
    a made up filename in the current directory named something like
    "Untitled1.sfd". See also :attr:`font.sfd_path`.
    """

    persistent: object
    """
    Whatever you want -- though it's recommended to store a dict here (these data
    will be saved as a pickled object in the sfd file. It is your job to ensure
    that whatever you put here can be pickled)

    If you do store a dict then the following entries will be treated specially:

    initScriptString:

      If present, and if this is a string, then each time the font is loaded
      from an sfd file, this string will be passed to the python interpreter.

      Note: This is a string, not a function.
      Function code cannot be pickled. Since it is a string it will receive
      no arguments, but the current font will be available in the activeFont
      method of the fontforge module.

      This string will be interpreted before the loadFontHook of the
      :data:`fontforge.hooks` dictionary.

      One possible behavior for this string is to define function hooks to
      be stored in the temporary dict described below.
    """

    math: math
    """
    Returns a :class:`math` object which provides information on the font's
    underlying math constant table.  There is only one of these per font.
    """

    private: private
    """
    Returns a :class:`private` dictionary-like object representing the
    PostScript private dictionary for the font. Changing entries in this object
    will change them in the font. (It's a reference, not a copy).

    There is an iterator associated with this entry.
    """

    privateState: int
    """
    Checks the (PostScript) Private dictionary and returns a bitmask of some
    common errors.

    0x000001:

      Odd number of elements in either the BlueValues or OtherBlues array.

    0x000002:

      Elements in either the BlueValues or OtherBlues are disordered.

    0x000004:

      Too many elements in either the BlueValues or OtherBlues array.

    0x000008:

      Elements in either the BlueValues or OtherBlues array are too close
      (must be at least ``2*BlueFuzz +1`` apart).

    0x000010:

      Elements in either the BlueValues or OtherBlues array are not integers.

    0x000020:

      Alignment zone height in either the BlueValues or OtherBlues array is too
      big for the value of BlueScale.

    0x000100:

      Odd number of elements in either the FamilyBlues or FamilyOtherBlues array.

    0x000200:

      Elements in either the FamilyBlues or FamilyOtherBlues are disordered.

    0x000400:

      Too many elements in either the FamilyBlues or FamilyOtherBlues array.

    0x000800:

      Elements in either the FamilyBlues or FamilyOtherBlues array are too
      close (must be at least ``2*BlueFuzz +1`` apart).

    0x001000:

      Elements in either the FamilyBlues or FamilyOtherBlues array are not
      integers.

    0x002000:

      Alignment zone height in either the FamilyBlues or FamilyOtherBlues array
      is too big for the value of BlueScale.

    0x010000:

      Missing BlueValues entry.

    0x020000:

      Bad BlueFuzz entry.

    0x040000:

      Bad BlueScale entry.

    0x080000:

      Bad StdHW entry.

    0x100000:

      Bad StdVW entry.

    0x200000:

      Bad StemSnapH entry.

    0x400000:

      Bad StemSnapV entry.

    0x800000:

      StemSnapH does not include StdHW.

    0x1000000:

      StemSnapV does not include StdVW.

    0x2000000:

      Bad BlueShift entry.
    """

    selection: selection | tuple[int | bool, ...]
    """
    Returns a reference to a ``selection`` representing the font's selection.
    There is one entry for each encoding slot (there may
    not be a glyph attached to every encoding slot). You may set this with a
    tuple of integers (or boolean values). There should not be more entries in
    the tuple than there are encoding slots in the current encoding. A ``True``
    or non-0 value means the slot is selected.
    """

    sfd_path: str | None
    """
    (readonly) Returns a string (or None) containing the name of the sfd file
    associated with this font. Sometimes this will be the same as :attr:`font.path`.
    """

    sfnt_names: tuple[tuple[str | int, str | int, str], ...]
    """
    The strings in the sfnt 'name' table. A tuple of all MS names. Each name is
    itself a tuple of strings ``(language,strid,string)``. Language may be
    either the (english) name of the language/locale, or the number representing
    that language in Microsoft's specification. Strid may be one of the
    (English) string names ``(Copyright, Family, SubFamily, etc.)`` or the
    numeric value of that item. The string itself is in UTF-8.

    Mac names will be automagically created from MS names
    """

    sfntRevision: float | int | None
    """
    The font revision field stored in the ``'head'`` table of an sfnt. This
    is documented to be a fixed 16.16 number (that is a 32 bit number with the
    binary point between bits 15 and 16).

    The field may be unset (in which case when the font is generated, FontForge
    will guess a default value from one of the version strings).

    The value returned will be ``None`` if the field is unset or a double.

    You may set it to ``None`` which "unsets" it, or to a double value, or to an
    integer. The integer will be treated as a 32 bit integer and right shifted
    by 16 to get a 16.16 value).
    """

    size_feature: (
        tuple[float]
        | tuple[float, float, float, int, tuple[tuple[str | int, str], ...]]
        | None
    )
    """
    The OpenType 'size' feature has two formats. It may either represent the
    design size of the font (and nothing else) or the design size, and range
    (top and bottom point sizes for which this design works), a style id (used
    to represent this design size throughout the font family) and a set of
    language/string pairs used to represent this design size in the menu.

    If no size information is specified in the font FontForge will return None.

    If only the design size is specified, FontForge will return a tuple
    containing a single element: the point size for which the font was designed.
    (This is returned as a real number -- the field can represent tenths of a point).

    Otherwise FontForge returns a tuple containing five elements, the design
    size, the bottom of the design range, the top, the style id and a tuple of
    tuples. Each sub-tuple is a language/string pair. Language may be either
    the (english) name of the language/locale, or the string itself in UTF-8.
    """

    strokedfont: int
    """Is this a stroked font?"""

    strokewidth: float
    """The stroke width of a stroked font"""

    style_set_names: tuple[tuple[str | int, str, str], ...]
    """
    A tuple, each entry of which is a 3-element tuple containing the language name
    (e.g. ``"English (US)"``), the style set tag (e.g. ``"ss01"``) and the style set name.
    """

    temporary: object
    """
    Whatever you want -- though it's recommended you store a dict here (these data
    will be lost once the font is closed)

    If you do store a dict then the following entries will be treated specially:

    generateFontPreHook:

      If present, and if this is a function it will be called just before a
      font is generated. It will be called with the font and the filename to
      which the font will be written.

    generateFontPostHook:

      If present, and if this is a function it will be called just after a font
      is generated. It will be called with the font and the filename to which
      the font will be written.
    """

    texparameters: tuple[
        Literal["text", "mathsym", "mathext", "unset"],
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]
    """
    Returns a tuple of TeX font parameters. TeX font type
    followed by 22 parameters. Font type is one of:

      * ``text``
      * ``mathsym``
      * ``mathext``
      * ``unset``

    In case of ``unset`` default values for font parameters will be returned.
    """

    uniqueid: int
    """PostScript Unique ID"""

    upos: float
    """Underline position."""

    userdata: object
    """Deprecated name for :attr:`font.temporary`"""

    uwidth: float
    """Underline width."""

    version: str
    """PostScript font version string."""

    verticalBaseline: (
        tuple[
            tuple[str, ...],
            tuple[
                tuple[
                    str,
                    str | None,
                    tuple[int, ...] | None,
                    tuple[
                        tuple[
                            str,
                            int,
                            int,
                            tuple[
                                tuple[
                                    str,
                                    int,
                                    int,
                                ],
                                ...,
                            ],
                        ],
                        ...,
                    ],
                ],
                ...,
            ],
        ]
        | None
    )
    """Same format as :attr:`font.horizontalBaseline`. """

    vhea_linegap: int
    """vhea linegap"""

    weight: str
    """PostScript font weight string."""

    woffMajor: int | None
    """
    The major version number of a woff file, an integer.

    The field may be unset (in which case when the font is generated, FontForge
    will guess a default value from one of the version strings).

    The value returned will be ``None`` if the field is unset or an integer.

    You may set it to ``None`` which "unsets" it, or to an integer.
    """

    woffMinor: int | None
    """
    The minor version number of a woff file, an integer.

    The field may be unset (in which case when the font is generated, FontForge
    will guess a default value from one of the version strings).

    The value returned will be ``None`` if the field is unset or an integer.

    You may set it to ``None`` which "unsets" it, or to an integer.
    """

    woffMetadata: str | None
    """
    Any metadata associated with a woff file. This is a utf8 string containing
    unparsed xml.
    """

    xHeight: float
    """
    (readonly) Computes the X Height (the height of lower case letters such as
    "x"). A negative number indicates the value could not be computed (the font
    might have no lower case letters because it was upper case only, or didn't
    include glyphs for a script with lower case letters).
    """

    def __iter__(self) -> Iterator[str]:
        """
        Returns an iterator for the font which will run through the font, in gid
        order, returning glyph names
        """
        ...

    def __contains__(self, name: str) -> bool:
        """Returns whether the font contains a glyph with the given name."""
        ...

    def __len__(self) -> int:
        """The number of glyph slots in the current encoding."""
        ...

    def __getitem__(self, key: int | str) -> glyph:
        """
        If ``key`` is an integer, then returns the glyph at that encoding. If a
        string then returns the glyph with that name. May not be assigned to.
        """
        ...

    def addAnchorClass(
        self, lookup_subtable_name: str, new_anchor_class_name: str
    ) -> None:
        """Adds an anchor class to the specified (anchor) subtable."""
        ...

    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        first_classes: tuple[tuple[str, ...], ...],
        second_classes: tuple[tuple[str, ...], ...],
        offsets: tuple[int, ...],
        after: str | None = None,
    ) -> None: ...
    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        separation: int,
        first_classes: tuple[tuple[str, ...], ...],
        second_classes: tuple[tuple[str, ...], ...],
        onlyCloser: bool = False,
        autokern: bool = True,
        after: str | None = None,
    ) -> None: ...
    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        separation: int,
        class_distance: float,
        first_glyph_list: tuple[tuple[str, ...], ...],
        second_glyph_list: tuple[tuple[str, ...], ...],
        onlyCloser: bool = False,
        autokern: bool = True,
        after: str | None = None,
    ) -> None: ...
    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        separation: int,
        class_distance: float,
        onlyCloser: bool = False,
        autokern: bool = True,
        after: str | None = None,
    ) -> None:
        """
        Creates a new subtable and a new kerning class in the named lookup. The
        classes arguments are tuples of tuples of glyph names (each sub-tuple of
        glyph names is a kerning class). The offsets argument is a tuple of kerning
        offsets. There must be as many entries as ::

          len(first-class)*len(second-class)

        The optional after argument is used to specify the order of the subtable
        within the lookup.

        The second format will cause FontForge to auto kern the subtable. The
        separation argument specifies the desired optical distance between any two
        glyphs (if this is specified as 0 then the kerning class will be designed so
        glyphs just touch each other). Again the user specifies two sets of
        predefined classes. If the (optional) ``onlyCloser`` flag is set true then
        only negative kerning values will be inserted into the table.

        In the third format the user merely specifies two lists of glyphs to be
        used, fontforge will look for similarities among among the glyphs and guess
        at classes. The class-distance argument to determine how precise the classes
        should match (1 is very tight matching, 20 is rather loose).

        In the last format the font's selection will be used to specify the list of
        glyphs to be examined (and the same list will be used for both the left and
        right glyphs -- but fontforge will probably find different classes).
        """
        ...

    def addLookup(
        self,
        new_lookup_name: str,
        type: Literal[
            "gsub_single",
            "gsub_multiple",
            "gsub_alternate",
            "gsub_ligature",
            "gsub_context",
            "gsub_contextchain",
            "gsub_revesechain",
            "morx_indic",
            "morx_context",
            "morx_insert",
            "gpos_single",
            "gpos_pair",
            "gpos_cursive",
            "gpos_mark2base",
            "gpos_mark2ligature",
            "gpos_mark2mark",
            "gpos_context",
            "gpos_contextchain",
            "kern_statemachine",
        ],
        flags: tuple[
            str
            | Literal[
                "right_to_left", "ignore_bases", "ignore_ligatures", "ignore_marks"
            ],
            ...,
        ]
        | None,
        feature_script_lang_tuple: tuple[
            tuple[str, tuple[tuple[str, tuple[str, ...]], ...]], ...
        ],
        after_lookup_name: str | None = None,
    ) -> None:
        """
        Creates a new lookup with the given name, type and flags. It will tag it
        with any indicated features.

        The flags argument is a tuple of strings, or ``None``. At most one of these
        strings may be the name of a mark class. The others are:

        * ``right_to_left``
        * ``ignore_bases``
        * ``ignore_ligatures``
        * ``ignore_marks``

        A feature-script-lang tuple is a tuple with one entry for each feature
        (there may be no entries if there are no features). Each entry is itself a
        two element tuple, the first entry is a string containing a 4 letter feature
        tag, and the second entry is another tuple (potentially empty) with an entry
        for each script for which the feature is active. Each entry here is itself a
        two element tuple. The first element is a 4 letter script tag and the second
        is a tuple of languages. Each entry in the language tuple is a four letter
        language. Example: ``(("liga",(("latn",("dflt")),)),)``

        The optional final argument allows you to specify the ordering of the lookup.
        If not specified the lookup will become the first lookup in its table.
        """
        ...

    def addLookupSubtable(
        self,
        lookup_name: str,
        new_subtable_name: str,
        after_subtable_name: str | None = None,
    ) -> None:
        """
        Creates a new subtable within the specified lookup. The lookup name should
        be a string specifying an existing lookup. The subtable name should also be
        a string and should not match any currently existing subtable in the lookup.
        The optional final argument allows you to specify the ordering within the
        lookup. If not specified this subtable will be first in the lookup.

        If you want to create a subtable in a contextual lookup, then use
        :meth:`font.addContextualSubtable`. If you want to create a kerning class
        subtable, then use :meth:`font.addKerningClass`.
        """
        ...

    @overload
    def addContextualSubtable(
        self,
        lookup_name: str,
        new_subtable_name: str,
        type: Literal["glyph", "coverage", "reversecoverage"],
        rule: str,
        *,
        afterSubtable: str | None = None,
    ) -> None: ...
    @overload
    def addContextualSubtable(
        self,
        lookup_name: str,
        new_subtable_name: str,
        type: Literal["class"],
        rule: str,
        *,
        afterSubtable: str | None = None,
        bclasses: tuple[str | tuple[str, ...]] | None = None,
        mclasses: tuple[str | tuple[str, ...]] | None = None,
        fclasses: tuple[str | tuple[str, ...]] | None = None,
        bclassnames: tuple[str, ...] | None = None,
        mclassnames: tuple[str, ...] | None = None,
        fclassnames: tuple[str, ...] | None = None,
    ) -> None:
        """
        Creates a new subtable within the specified contextual lookup (contextual,
        contextual chaining, or reverse contextual chaining). The lookup name should
        be a string specifying an existing lookup. The subtable name should also be
        a string and should not match any currently existing subtable in the lookup.

        The ``type`` should be one of the strings "glyph", "class", "coverage" or
        "reversecoverage". The ``rule`` should be a string specifying a string to
        match and a set of lookups to apply once the match has been made. (See
        below for more details).

        The remaining arguments are optional, keyword arguments.

        * ``afterSubtable=``, if present this should be followed by a string, the
          name of a subtable after which this one is to be placed in the lookup. If
          not specified this subtable will be first in the lookup.
        * ``bclasses=, fclasses=, mclasses=`` these three arguments specify sets of
          glyph classes for when ``type="class"``. They should be a tuple of
          thingies where each thingy is either a string containing a list of space
          separated glyph names, or another tuple containing a set of strings, each
          a glyph name. Note that the first class is magic and should usually be
          left as a null string.
        * ``bclassnames=, fclassnames=, mclassnames=`` These provide names for the
          glyph classes described above. These names are optional, but can be
          convenient. These are tuples of strings. There should be the same number
          of entries in ``bclassnames`` as there are in ``bclasses``.

        When type="glyph":

          The rule should look something like: ::

            glyph-name1 glyph-name2 | glyph-name3 @<lookup-name> | glyph-name4

          The ``|`` s divide between backtrack, match and lookahead sections. So
          this example would match if the current glyph were named ``glyph-name3``
          and it were preceded by ``glyph-name2`` and that by ``glyph-name1`` and
          followed by ``glyph-name4``. If the match were successful then the lookup
          named ``lookup-name`` would be applied. The ``@<>`` are literal
          characters and should be present in the rule.

          If the invoked lookup is a ligature lookup then it should be invoked
          after the first glyph that forms the lookup (rather than the last) and
          all glyphs that might make up the lookup should be in the match section.
          So... ::

            e | f @<ff-lig> f l | o

          would only apply the ``ff-lig`` lookup if the ``ffl`` were preceded by
          ``e`` and followed by ``o``.

        When type="class":

          The rule should look something like: :::

            class-name1 class-name2 | class-name3 @<lookup-name> | class-name4

          Very similar to the case of glyphs, except that instead of glyph names
          we have class names here. It is possible to have different sets of class
          names in the three different sections (backtrack, match and lookahead).
          If you don't specify any class names then you must use numbers instead,
          each number referring to the class at that position in the tuple (the first
          class will be class 0, the second class 1, and so on).

        When type="coverage":

          The rule should look something like: ::

            [g1 g2] [g3 g4] | [g5 g6 g7] @<lookup-name> | [g8 g9]

          Each entry within brackets, ``[]``, represents a coverage table and
          should be a list of glyph names. The brackets are specified literally.

        When type="reversecoverage":

          The rule should look something like: ::

             [g1 g2] [g3 g4] | [g5 g6 g7] => [rg1 rg2 rg3] | [g8 g9]

          Very similar to normal coverage tables except that instead of specifying
          a lookup there are replacement glyphs inline. There must be the same
          number of replacement glyphs (``rg1, rg2,rg3``) as match glyphs
          (``g5, g6, g7``) and there may be only one coverage table in the match
          section.

        Warning:

          This format has some limitations, if there are multiple lookups they
          will be applied in textual order (First lookup in the string is the first
          one applied). This limitation is also present in Adobe's feature files.
        """
        ...

    def addSmallCaps(
        self,
        *,
        scheight: float | None = None,
        capheight: float | None = None,
        lcstem: float | None = None,
        ucstem: float | None = None,
        symbols: bool = False,
        letter_extension: str = "sc",
        symbol_extension: str = "taboldstyle",
        stem_height_factor: float | None = None,
    ) -> None:
        """
        This function uses keyword parameters. None are required, if omitted a
        default value will be used (generally found by analyzing the font).

        For each selected letter, this function will create a corresponding small
        caps glyph. If you set the ``symbols`` keyword to ``True`` it will also
        create small caps variants of digits and symbols.

        The outlines of the new glyph will be based on the outlines of the
        upper-case variant of the letter. These will then be scaled so that a glyph
        which was ``capheight`` high will now be ``scheight`` high, and so that
        stems which were ``ucstem`` wide will be ``lcstem`` wide. Normally the ratio
        of stem heights is the same as the ratio of stem widths, but you may change
        that with ``stem_height_factor``.

        When it creates a new glyph it will name that glyph by appending ".sc" to
        the original lower case letter name (so "a" would become "a.sc") you may
        change the extension used with ``letter_extension``. Similarly symbols and
        digits will use the extension "taboldstyle", but you may change that with
        ``symbol_extension``.

        When it creates a glyph it also creates two lookups one bound to the feature
        "c2sc" and the other to "smcp". A mapping from the lower case letter to the
        small caps letter will be provided under "smcp", while a mapping from the
        upper case to the small caps under "c2sc". Symbols will have both lookup
        maps attached to the original glyph.
        """
        ...

    def alterKerningClass(
        self,
        subtable_name: str,
        first_classes: tuple[tuple[str, ...], ...],
        second_classes: tuple[tuple[str, ...], ...],
        offsets: tuple[int, ...],
    ) -> None:
        """
        Changes the kerning class in the named subtable. The classes arguments are
        tuples of tuples of glyph names (each sub-tuble of glyph names is a kerning
        class). The offsets argument is a tuple of kerning offsets. There must be as
        many entries as ``len(first-class)*len(second-class)``.
        """
        ...

    @overload
    def autoKern(
        self,
        subtable_name: str,
        separation: int,
        *,
        minKern: int = 10,
        onlyCloser: bool = False,
        touch: int = 0,
    ) -> None: ...
    @overload
    def autoKern(
        self,
        subtable_name: str,
        separation: int,
        glyph_list1: tuple[str, ...],
        glyph_list2: tuple[str, ...],
        *,
        minKern: int = 10,
        onlyCloser: bool = False,
        touch: int = 0,
    ) -> None:
        """
        The named subtable must be a kerning pair subtable that already exists.

        This command will automatically generate kerning pairs for the named
        subtable. If no glyph lists are specified it will look at all pairs of the
        glyphs in the selection; if glyph lists are specified then it will look at
        all pairs that can be made with one glyph from the first list and the second
        from the second list.

        It will attempt to guess a good kerning value between the two glyphs -- a
        value which will make the optical separation between the two appear to be
        ``separation`` em-units. If ``minKern`` is specified and the (absolute
        value of the) kerning correction is less than this number then no kerning
        pair will be generated. If ``onlyCloser`` is set to true then only negative
        kerning offsets will be generated (only thing which moves two glyphs closer
        together). If touch is set to 1 then the kerning offset will not be based on
        optical distance but on the closest approach between the two glyphs.
        """
        ...

    def appendSFNTName(
        self, language: str | int, strid: str | int, string: str
    ) -> None:
        """
        Adds a new (or replaces an old) string in the sfnt 'name' table. Language
        may be either the English name of the language/locale as a string, or the
        number representing that language in MicroSoft's specification. Strid may be
        one of the (english) string names (Copyright, Family, SubFamily, etc.) or
        the numeric value of that item. The string itself is in UTF-8.
        """
        ...

    def buildOrReplaceAALTFeatures(self) -> None:
        """
        Removes any existing AALT features (and any lookups solely controlled by such
        features) and creates new ones containing all possible single and alternate
        substutions available for each glyph.
        """
        ...

    def cidConvertByCMap(self, cmap_filename: str) -> None:
        """
        Converts a normal font into a CID-keyed font with one subfont using
        the CMAP to determine the mapping.
        """

    def cidConvertTo(self, registry: str, ordering: str, supplement: int) -> None:
        """Converts a normal font into a CID-keyed font with one subfont."""

    def cidFlatten(self) -> None:
        """Converts a CID font into a normal font (glyphs will be in CID order)."""

    def cidFlattenByCMap(self, cmap_filename: str) -> None:
        """
        Converts a CID font into a normal font using the encoding specified in the
        CMAP file.
        """

    def cidInsertBlankSubFont(self) -> None:
        """
        Adds a new (blank) sub-font into a cid-keyed font and changes the current
        sub-font to be it.
        """

    def cidRemoveSubFont(self) -> None:
        """Removes the current subfont from a cid-keyed font."""

    def close(self) -> None:
        """
        Frees memory for the current font.

        Warning: Any python references to it will become invalid.
        """
        ...

    def compareFonts(
        self,
        other_font: font,
        filename: str,
        flags_tuple: tuple[
            Literal[
                "outlines",
                "outlines-exactly",
                "warn-outlines-mismatch",
                "hints",
                "warn-refs-unlink",
                "strikes",
                "fontnames",
                "gpos",
                "gsub",
                "add-outlines",
                "create-glyphs",
            ],
            ...,
        ],
    ) -> None:
        """
        This will compare the current font with the font in ``other_font`` (which
        must already have been opened). It will write the results to the
        ``filename``, you may use "-" to send the output to stdout. The ``flags``
        argument is a tuple of strings and controls what will be compared.

        outlines:

          compare outlines

        outlines-exactly:

          compare outlines exactly (otherwise allow slight errors and the unlinking
          of references)

          warn-outlines-mismatch:

          warn if the outlines don't exactly match (but are pretty close)

        hints:

          compare hints

        warn-refs-unlink:

          warn if references need to be unlinked before a match is found

        strikes:

          compare bitmap strikes

        fontnames:

          compare font names

        gpos:

          compare glyph positioning

        gsub:

          compare glyph substitutions

        add-outlines:

          for any glyphs whose outlines differ, add the outlines of the glyph in
          the second font to the background of the glyph in the first

        create-glyphs:

          if a glyph exists in the second font but not the first, create that
          glyph in the first and add the outlines from the second into the
          background layer
        """
        ...

    def createChar(self, uni: int, name: str | None = None) -> glyph:
        """
        Create (and return) a character at the specified unicode codepoint in this
        font and optionally name it. If you wish to create a glyph with no unicode
        codepoint, set the first argument to -1 and specify a name.

        If there is already a character at that (positive) codepoint then it is
        returned. If the optional name parameter is included and differs from its
        current name then the character is also renamed.
        """
        ...

    def createInterpolatedGlyph(
        self, glyph1: glyph, glyph2: glyph, amount: float
    ) -> glyph:
        """
        Create (and return) a glyph with the same unicode code point as glyph1.
        The glyph may not already exist. The contents of the glyph will be formed
        by interpolating between glyph1 and glyph2. If amount==0 the result will
        look like glyph1, or 1 then like glyph2.
        """
        ...

    @overload
    def createMappedChar(self, enc: int) -> glyph: ...
    @overload
    def createMappedChar(self, name: str) -> glyph:
        """
        Create (and return) a character at the specified encoding in this font.
        If there is already a character there, return it
        """
        ...

    def find(
        self,
        contour: contour | layer,
        error_bound: float = 0.01,
        search_flags: tuple[Literal["reverse", "flips", "rotate", "scale"], ...] = (
            "reverse",
            "flips",
        ),
    ) -> Iterator[glyph]:
        """
        Searches the font for all glyphs containing the contour (or layer) and
        returns an iterator which returns those glyphs.

        When found, the glyph.temporary is set to a dict of::

          {
            "findMatchedRefs": matched_refs_bit_map,
            "findMatchedContours": matched_contours_bit_map,
            "findMatchedContoursStart": matched_contours_start_bit_map,
          }
        """
        ...

    @overload
    def findEncodingSlot(self, uni: int) -> int: ...
    @overload
    def findEncodingSlot(self, name: str) -> int:
        """
        Tests whether a glyph with this codepoint or name is in the font's encoding
        and returns the encoding slot. If the glyph is not present it returns -1.

        (If a glyph with that name/unicode is in the font, but is not in the
        encoding, then a value beyond the end of the encoding will be returned).
        """

    def glyphs(self, type: Literal["GID", "encoding"] = "GID") -> Iterator[glyph]:
        """
        Returns an iterator which will return the glyphs in the font. By default
        they will be returned in "GID" order, but if type is specified as "encoding"
        they will be returned in encoding order. If returned in encoding order it
        is possible that a glyph will be returned more than once if there are
        multiple encoding slots which reference it.
        """

    def generate(
        self,
        filename: str,
        *,
        bitmap_type: str | None = None,
        flags: tuple[
            Literal[
                "afm",
                "pfm",
                "tfm",
                "ofm",
                "composites-in-afm",
                "glyph-map-file",
                "short-post",
                "apple",
                "opentype",
                "old-kern",
                "winkern",
                "dummy-dsig",
                "no-FFTM-table",
                "TeX-table",
                "round",
                "no-hints",
                "no-flex",
                "omit-instructions",
                "PfEd-comments",
                "PfEd-colors",
                "PfEd-lookups",
                "PfEd-guidelines",
                "PfEd-background",
                "symbol",
            ],
            ...,
        ] = (),
        bitmap_resolution: int | None = None,
        subfont_directory: str | None = None,
        namelist: str | None = None,
        layer: str | int | None = None,
    ) -> None:
        """
        Generates a font. The type is determined by the font's extension. The bitmap
        type (if specified) is also an extension. If layer is specified, then the
        splines and references in that layer will be used instead of the foreground
        layer.

        Flags is a tuple containing some of

        afm:

          output an afm file

        pfm:

          output a pfm file

        tfm:

          output a tfm file

        ofm:

          output a ofm file

        composites-in-afm:

          Store composite info in the afm file

        glyph-map-file:

          Output a glyph map file giving the mapping between output gid and glyphnames

        short-post:

          Do not include glyphnames in a ttf/otf file

        apple:

          output apple advanced typography tables

        opentype:

          output opentype tables

        old-kern:

          output an old style 'kern' with opentype tables

        winkern:

          only add kern pairs for mapped glyphs (required for kerning in some/all
          versions of Windows)

        dummy-dsig:

          output an empty DSIG table so MS will mark a font with .ttf extension as
          an OpenType font.

        no-FFTM-table:

          Do not generate an 'FFTM' table

        TeX-table:

          Include a 'TeX ' table in an ttf/otf file

        round:

          Round PS coordinates to integers

        no-hints:

          Do not include PS hints

        no-flex:

          Do not include PS flex hints

        omit-instructions:

          Do not include TrueType instructions

        PfEd-comments:

          Include font and glyph comments in the 'PfEd' table

        PfEd-colors:

          Include glyph colors in the 'PfEd' table

        PfEd-lookups:

          Include lookup names in the 'PfEd' table

        PfEd-guidelines:

          Include guideline locations in the 'PfEd' table

        PfEd-background:

          Include background (and spiro) layers in the 'PfEd' table

        symbol:

          Generate an sfnt with a Symbol cmap entry rather than a Unicode entry.

        See also :meth:`font.save()`.
        """
        ...

    def generateTtc(
        self,
        filename: str,
        others: Sequence[font] | font | None,
        *,
        flags: tuple[
            Literal[
                "afm",
                "pfm",
                "tfm",
                "ofm",
                "composites-in-afm",
                "glyph-map-file",
                "short-post",
                "apple",
                "opentype",
                "old-kern",
                "winkern",
                "dummy-dsig",
                "no-FFTM-table",
                "TeX-table",
                "round",
                "no-hints",
                "no-flex",
                "omit-instructions",
                "PfEd-comments",
                "PfEd-colors",
                "PfEd-lookups",
                "PfEd-guidelines",
                "PfEd-background",
                "symbol",
            ],
            ...,
        ] = (),
        ttcflags: tuple[Literal["merge", "cff"], ...] = (),
        namelist: str | None = None,
        layer: str | int | None = None,
    ) -> None:
        """
        Generates a truetype collection file containing the current font and all
        others listed -- the ``others`` argument may be ``None``, a font, or a tuple
        (or list) of fonts.

        Flags are the same as ``font.generate``.

        Ttcflags is a tuple consisting of the following

        merge:

          Try and share tables and glyphs among the various fonts.

        cff:

          Use the CFF glyph format rather than the TrueType format (the OpenType
          documentation says that this does not work, but both the Mac and
          unix/linux accept it).
        """
        ...

    def generateFeatureFile(
        self, filename: str, lookup_name: str | None = None
    ) -> None:
        """
        Generates an adobe feature file for the current font. If a lookup-name is
        specified then only data for that lookup will be generated.
        """
        ...

    def genericGlyphChange(self, **kwargs: GlyphChangeOptions) -> None:
        """Applies generic changes to all glyphs."""
        ...

    def getKerningClass(
        self, subtable_name: str
    ) -> tuple[
        tuple[tuple[str, ...], ...],
        tuple[tuple[str, ...], ...],
        tuple[int, ...],
    ]:
        """
        Returns a tuple whose entries are: (first-classes, second-classes, offsets).
        The classes are themselves tuples of tuples of glyph names. The offsets will
        be a tuple of numeric kerning offsets.
        """
        ...

    def getLookupInfo(
        self, lookup_name: str
    ) -> tuple[
        Literal[
            "gsub_single",
            "gsub_multiple",
            "gsub_alternate",
            "gsub_ligature",
            "gsub_context",
            "gsub_contextchain",
            "gsub_revesechain",
            "morx_indic",
            "morx_context",
            "morx_insert",
            "gpos_single",
            "gpos_pair",
            "gpos_cursive",
            "gpos_mark2base",
            "gpos_mark2ligature",
            "gpos_mark2mark",
            "gpos_context",
            "gpos_contextchain",
            "kern_statemachine",
        ],
        tuple[
            str
            | Literal[
                "right_to_left", "ignore_bases", "ignore_ligatures", "ignore_marks"
            ],
            ...,
        ]
        | None,
        tuple[tuple[str, tuple[tuple[str, tuple[str, ...]], ...]], ...],
    ]:
        """
        Returns a tuple whose entries are: (lookup-type, lookup-flags,
        feature-script-lang-tuple). The lookup type is a string as described in
        :meth:`font.addLookup`, and the feature-script-lang tuple is also described
        there.
        """
        ...

    def getLookupSubtables(self, lookup_name: str) -> tuple[str, ...]:
        """Returns a tuple of all subtable names in that lookup."""
        ...

    def getLookupSubtableAnchorClasses(self, subtable_name: str) -> tuple[str, ...]:
        """Returns a tuple of all anchor class names in that subtable."""
        ...

    def getLookupOfSubtable(self, subtable_name: str) -> str:
        """Returns the name of the lookup containing this subtable."""
        ...

    def getSubtableOfAnchor(self, anchor_class_name: str) -> str:
        """Returns the name of the subtable containing this anchor class."""
        ...

    def importBitmaps(
        self, bitmap_font_file: str, to_background: int | None = None
    ) -> None:
        """Load any bitmap strikes out of the bitmap-font-file into the current font"""
        ...

    def importLookups(
        self,
        another_font: font,
        lookup_names: str | tuple[str, ...],
        before_name: str | None = None,
    ) -> None:
        """
        It will search the other font for the named lookup(s) and import it into the
        current font. (Contextual lookups which invoke other lookups will have any
        nested lookups imported as well).

        Lookups will be imported in the order listed. If a before-name is specified,
        then it is looked up in the current font and all lookups will be added
        before it, if not specified lookups will appear at the end of the list.
        """

    def interpolateFonts(self, fraction: float, filename: str) -> None:
        """
        Interpolates a font between the current font and the font contained in
        filename.
        """
        ...

    def isKerningClass(self, subtable_name: str) -> bool:
        """Returns whether the named subtable contains a kerning class."""
        ...

    def isVerticalKerning(self, subtable_name: str) -> bool:
        """Returns whether the named subtable contains a vertical kerning data"""
        ...

    def italicize(
        self,
        *,
        italic_angle: float = -13,
        ia: float = -13,
        lc_condense: tuple[float, float, float, float] = ...,
        lc: tuple[float, float, float, float] = ...,
        uc_condense: tuple[float, float, float, float] = ...,
        uc: tuple[float, float, float, float] = ...,
        symbol_condense: tuple[float, float, float, float] = ...,
        symbol: tuple[float, float, float, float] = ...,
        deserif_flat: bool = True,
        deserif_slant: bool = True,
        deserif_pen: bool = True,
        baseline_serifs: bool = True,
        xheight_serifs: bool = True,
        ascent_serifs: bool = False,
        descent_serifs: bool = True,
        diagonal_serifs: bool = True,
        a: bool = True,
        f: Literal[0, 1, 2] = 1,
        u0438: bool = True,
        u043F: bool = True,
        u0442: bool = True,
        u0444: bool = True,
        u0448: bool = True,
        u0452: bool = True,
        u045f: bool = True,
    ) -> None:
        """
        This function uses keyword parameters. None are required, if omitted a
        default value will be used. Some keywords have abbreviations ("ia" for
        "italic_angle") you may use either.

        This function will attempt to italicize each selected glyph.

        The ``*_condense`` keywords should be 4 element tuples of floating point
        numbers; these numbers correspond to: Left side bearing condensation,
        stem condensation, counter condensation and right side bearing condensation.
        These numbers should be small numbers around 1 (scale factors, not
        percentages).

        Set at most one of the ``deserif_*`` keywords.

        Setting ``a`` to ``True`` will turn on the transformation that applies to
        the "a" glyph. Setting ``u0438`` will control the transformation that
        applies to the glyph at unicode codepoint U+0438.

        The ``f`` keyword is slightly more complex. Setting it to 0 turns off all
        transformations of glyphs like "f", setting it to 1 will give "f" a tail
        which looks like a rotated version of its head, and setting it to 2 will
        simply extend the main stem of "f" below the baseline.
        """
        ...

    def lookupSetFeatureList(
        self,
        lookup_name: str,
        feature_script_lang_tuple: tuple[
            tuple[str, tuple[tuple[str, tuple[str, ...]], ...]], ...
        ],
    ) -> None:
        """
        Sets the feature list of indicated lookup. The feature-script-lang tuple is
        described at :meth:`font.addLookup()`.
        """
        ...

    def lookupSetFlags(
        self,
        lookup_name: str,
        flags: tuple[
            Literal[
                "right_to_left", "ignore_bases", "ignore_ligatures", "ignore_marks"
            ],
            ...,
        ],
    ) -> None:
        """Sets the lookup flags for the named lookup."""
        ...

    def lookupSetStoreLigatureInAfm(self, lookup_name: str, boolean: bool) -> None:
        """Sets whether this ligature lookup contains data to store in the afm."""
        ...

    @overload
    def mergeFonts(
        self,
        filename: str,
        preserveCrossFontKerning: bool = False,
    ) -> None: ...
    @overload
    def mergeFonts(
        self,
        font: font,
        preserveCrossFontKerning: bool = False,
    ) -> None:
        """Merges the font in the file into the current font."""
        ...

    def mergeFeature(self, filename: str, boolean: bool) -> None:
        """
        Merge feature and lookup information from an adobe feature file, or metrics
        information from the (afm, tfm, etc) file into the current font. The
        optional boolean will try to skip invalid feature lookups containing
        replacement glyphs which do not exist in the font, which can help in reusing
        large feature files.
        """
        ...

    @deprecated("Use mergeFeature instead")
    def mergeKern(self, filename: str) -> None: ...
    def mergeLookups(self, lookup_name1: str, lookup_name2: str) -> None:
        """
        The lookups must be of the same type. All subtables from lookup_name2 will
        be moved to lookup_name1, the features list of lookup_name2 will be merged
        with that of lookup_name1, and lookup_name2 will be removed.
        """
        ...

    def mergeLookupSubtables(self, subtable_name1: str, subtable_name2: str) -> None:
        """
        The subtables must be in the same lookup. Not all lookup types allow their
        subtables to be merged (contextual subtables may not be merged, kerning
        classes may not be (kerning pairs may be)). Any information bound to
        subtable2 will be bound to subtable1 and subtable2 will be removed.
        """

    def printSample(
        self,
        type: Literal[
            "fontdisplay", "chars", "waterfall", "fontsample", "fontsampleinfile"
        ],
        pointsize: int | Sequence[int],
        sample: str,
        output_file: str,
    ) -> None:
        """
        Type is a string which must be one of

        fontdisplay:

          Display all glyphs in the font in encoding order

        chars:

          Display the selected glyphs scaled to fill a page

          Ignores the pointsize argument.

        waterfall:

          Displays the selected glyphs at many pointsizes.

          The pointsize argument should be a tuple of pointsizes here.

        fontsample:

          The third argument should contain a string which will be layed out
          and displayed as well as FontForge can.

        fontsampleinfile:

          The third argument should contain the name of a file which contains
          text to be layed out and displayed.

        If output is to a file (see :func:`fontforge.printSetup()`) then the last
        argument specifies a file name in which to store output.
        """

    def randomText(self, script: str, lang: str | None = None) -> str:
        """
        Returns a random text sample using the letter frequencies of the specified
        script (and optionally language). Both script and language should be
        expressed as strings containing OpenType Script and Language tags. "dflt" is
        a reasonable language tag. If the language is not specified, one will be
        chosen at random. If ff has no frequency information for the script/language
        specified it will use the letters in the script with equal frequencies.
        """

    def reencode(self, encoding: str, force: bool = False) -> None:
        """
        Reencodes the current font into the given encoding. Optionally force
        reencoding.
        """
        ...

    def regenBitmaps(self, tuple_of_sizes: tuple[int, ...]) -> None:
        """
        A tuple with an entry for each bitmap strike to be regenerated
        (rerasterized). Each strike is identified by pixelsize (if the strike is a
        grey scale font it will be indicated by ``(bitmap-depth<<16)|pixelsize``.
        """
        ...

    def removeAnchorClass(self, anchor_class_name: str) -> None:
        """Removes the named AnchorClass (and all associated points) from the font."""
        ...

    def removeLookup(self, lookup_name: str, remove_acs: Literal[0, 1] = 0) -> None:
        """
        Remove the lookup (and any subtables within it). remove_acs (0 or 1),
        specifies whether to remove associated anchor classes and points.
        """

    def removeLookupSubtable(
        self, subtable_name: str, remove_acs: Literal[0, 1] = 0
    ) -> None:
        """
        Remove the subtable (and all data associated with it). remove_acs (0 or 1),
        specifies whether to remove associated anchor classes and points
        """
        ...

    @overload
    def removeGlyph(self, uni: int, name: str | None = None) -> None: ...
    @overload
    def removeGlyph(self, name: str) -> None: ...
    @overload
    def removeGlyph(self, glyph: glyph) -> None:
        """
        You may either pass in a FontForge glyph object (from this font) or identify
        a glyph in the font by unicode code point or name. In any case the glyph
        will be removed from the font.

        If you use (uni,name) to specify a name, set uni to -1.

        Warning:

           This frees FontForge's storage to this glyph. If you have any python
           references to that storage they will be looking at garbage. This does not
           go through the usual python reference mechanism.
        """
        ...

    def replaceAll(
        self, srch: contour | layer, rpl: contour | layer, error_bound: float = 0.01
    ) -> int:
        """
        Searches the font for all occurrences of the srch contour (or layer) and
        replaces them with the replace contour (or layer).
        """

    def revert(self) -> None:
        """
        Reloads the font from the disk.

        Warning:

          If you have any references to glyphs which live in the font those
          references will no longer be valid, and using them will cause crashes.
          This is very un-python-like.
        """
        ...

    def revertFromBackup(self) -> None:
        """
        Reloads the font from the backup file on the disk.

        Warning:

          If you have any references to glyphs which live in the font those
          references will no longer be valid, and using them will cause crashes.
          This is very un-python-like.
        """
        ...

    def save(self, filename: str | None = None) -> None:
        """Saves the font to an sfd file. See also :meth:`font.generate()`"""
        ...

    def saveNamelist(self, filename: str) -> None:
        """Saves the font's namelist to a file."""

    def getTableData(self, table_name: str) -> bytes:
        """
        Gets binary data from any saved table. FF will save 'fpgm', 'prep', 'cvt '
        and 'maxp'. FF may also save tables which you explicitly request. Do not
        expect to get binary data for tables like 'GPOS' or 'glyf' which FF will
        generate when it creates a font... that information is not currently available.

        Returns a binary string.
        """

    def setTableData(
        self, table_name: str, sequence: bytes | Sequence[int] | None
    ) -> None:
        """
        Sets binary data of any saved table. FF will save 'fpgm', 'prep', 'cvt '
        and 'maxp'. FF may also save tables which you explicitly request. Do not
        expect to set binary data for tables like 'GPOS' or 'glyf' which FF will
        generate when it creates a font... that information is not currently available.

        If sequence is None, then the named table will be removed from the font.
        """

    def validate(self, force: int = 0) -> int:
        """
        Validates the font and returns a bit mask of all errors from all glyphs (as
        defined in the ``validation_state`` of a glyph -- except bit 0x1 is clear).
        If the font passed the validation then the return value will be 0 (not 0x1).
        Otherwise the return value will be the set of errors found.

        Note: The set of errors is slightly different for TrueType and PostScript
        output. The returned mask contains the list of potential errors. You must
        figure out which apply to you.

        Normally each glyph will cache its validation_state and it will not be
        recalculated. If you pass a non-zero argument to the routine then it will
        force recalculation of each glyph -- this can be slow.
        """
        ...

    # --- Selection-Based Methods ---

    def addExtrema(self) -> None:
        """
        Extrema should be marked by on-curve points. If a curve in any selected
        glyph lacks a point at a significant extremum this command will add one.
        """
        ...

    def addInflections(self) -> None:
        """Please see :meth:`contour.addInflections()`."""
        ...

    def autoHint(self) -> None:
        """Generates PostScript hints for all selected glyphs."""
        ...

    def autoInstr(self) -> None:
        """Generates TrueType instructions for all selected glyphs."""
        ...

    def autoWidth(
        self,
        separation: int,
        *,
        minBearing: int = 10,
        maxBearing: int = -1,
        height: int = 0,
        loopCnt: int = 1,
    ) -> None:
        """Guesses at reasonable horizontal advance widths for the selected glyphs"""
        ...

    def autoTrace(self) -> None:
        """Auto traces any background images in all selected glyphs"""
        ...

    def build(self) -> None:
        """
        If any of the selected characters is a composite character, then this
        command will clear it and insert references to its components (this command
        can create new glyphs).
        """
        ...

    def canonicalContours(self) -> None:
        """
        Orders the contours in the selected glyphs by the x coordinate of their
        leftmost point. (This can reduce the size of the charstring needed to
        describe the glyph(s).
        """
        ...

    def canonicalStart(self) -> None:
        """
        Sets the start point of all the contours of the selected glyphs to be the
        leftmost point on the contour. (If there are several points with that value
        then use the one which is closest to the baseline). This can reduce the size
        of the charstring needed to describe the glyph(s). By regularizing things it
        can also make more things available to be put in subroutines.
        """
        ...

    @overload
    def changeWeight(
        self,
        stroke_width: float,
        type: Literal["LCG", "CJK", "auto"] = "auto",
        serif_height: int | None = None,
        serif_fuzz: float = 0.9,
        counter_type: Literal["squish", "retain", "auto"] = "auto",
    ) -> None: ...
    @overload
    def changeWeight(
        self,
        stroke_width: float,
        type: Literal["custom"],
        serif_height: int | None = None,
        serif_fuzz: float = 0.9,
        counter_type: Literal["squish", "retain", "auto"] = "auto",
        custom_zones: int | tuple[int, int, int, int] = ...,
    ) -> None:
        """
        Stroke_width is the amount by which all stems are expanded.

        Type is one of "LCG", "CJK", "auto", "custom".

        Serif_height tells ff not to expand serifs which are that much off the
        baseline, while serif_fuzz specifies the amount of fuzziness allowed in the
        match. If you don't want special serif behavior set this to 0.

        Counter_type is one of "squish", "retain", "auto".

        Custom_zones is only meaningful if the type argument were "custom". It may
        be either a number, which specifies the "top hint" value (bottom hint is
        assumed to be 0, others are between), or a tuple of 4 numbers (top hint,
        top zone, bottom zone, bottom hint).
        """
        ...

    def condenseExtend(
        self,
        c_factor: float,
        c_add: float,
        sb_factor: float | None = None,
        sb_add: float | None = None,
        correct: bool = True,
    ) -> None:
        """
        Condenses or extends the size of the counters and side-bearings of the
        selected glyphs. The first two arguments provide information on
        shrinking/growing the counters, the second two the sidebearings. If the last
        two are omitted they default to the same values as the first two.

        A counter's width will become: ::

          new_width = c_factor * old_width + c_add

        If present the ``correct`` argument allows you to specify whether you want
        to correct for the italic angle before condensing the glyph. (it defaults to
        True)
        """
        ...

    def clear(self) -> None:
        """Clears the contents of all selected glyphs"""
        ...

    def cluster(self, within: float = 0.1, max: float = 0.5) -> None:
        """
        Moves clustered coordinates to a standard central value in all selected
        glyphs. See also :meth:`font.round()`.
        """
        ...

    def copy(self) -> None:
        """Copies all selected glyphs into (FontForge's internal) clipboard."""
        ...

    def copyReference(self) -> None:
        """
        Copies all selected glyphs (as references) into (FontForge's internal)
        clipboard.
        """
        ...

    def correctDirection(self) -> None:
        """
        Orients all contours so that external ones are clockwise and internal
        counter-clockwise in all selected glyphs.
        """
        ...

    def correctReferences(self) -> None:
        """
        Checks a font for glyphs with mixed contours and references (or references
        with transformation matrices which cannot be represented in truetype (ie.
        scaling by 2 or more)). If a mixed case is discovered FontForge will take
        the contours out of the glyph, put them in a new glyph, and make a reference
        to the new glyph.
        """
        ...

    def cut(self) -> None:
        """
        Copies all selected glyphs into (FontForge's internal) clipboard. And then
        clears them.
        """
        ...

    def paste(self) -> None:
        """
        Pastes the contents of (FontForge's internal) clipboard into the selected
        glyphs -- and removes what was there before.
        """
        ...

    def intersect(self) -> None:
        """
        Leaves only areas in the intersection of contours in all selected glyphs.
        See also :meth:`font.removeOverlap()`.
        """
        ...

    def pasteInto(self) -> None:
        """
        Pastes the contents of (FontForge's internal) clipboard into the selected
        glyphs -- and retains what was there before.
        """
        ...

    def removeOverlap(self) -> None:
        """
        Removes overlapping areas in all selected glyphs.
        See also :meth:`font.intersect()`.
        """
        ...

    def replaceWithReference(self, fudge: float = 0.01) -> None:
        """
        Finds any glyph which contains an inline copy of one of the selected glyphs,
        and converts that copy into a reference to the appropriate glyph. Selection
        is changed to the set of glyphs which the command alters.

        If specified the fudge argument specifies the error allowed for coordinate
        differences.
        """

    def round(self, factor: float = 1) -> None:
        """
        Rounds the x and y coordinates of each point in all selected glyphs. If
        factor is specified then ::

          new-coord = round(factor*old-coord)/factor

        See also :meth:`font.cluster()`.
        """
        ...

    def simplify(
        self,
        error_bound: float | None = None,
        flags: tuple[
            Literal[
                "ignoreslopes",
                "ignoreextrema",
                "smoothcurves",
                "choosehv",
                "forcelines",
                "nearlyhvlines",
                "mergelines",
                "setstarttoextremum",
                "removesingletonpoints",
            ],
            ...,
        ] = (),
        tan_bounds: float | None = None,
        linefixup: float | None = None,
        linelenmax: float | None = None,
    ) -> None:
        """
        Tries to remove excess points in all selected glyphs if doing so will not
        perturb the curve by more than ``error-bound``. Flags is a tuple of the
        following strings

        ignoreslopes:

          Allow slopes to change

        ignoreextrema:

          Allow removal of extrema

        smoothcurves:

          Allow curve smoothing

        choosehv:

          Snap to horizontal or vertical

        forcelines:

          flatten bumps on lines

        nearlyhvlines:

          Make nearly horizontal/vertical lines be so

        mergelines:

          Merge adjacent lines into one

        setstarttoextremum:

          Rotate the point list so that the start point is on an extremum

        removesingletonpoints:

          If the contour contains just one point then remove it
        """
        ...

    @overload
    def stroke(
        self,
        type: Literal["circular"],
        width: float,
        /,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        angle: float = 0,
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["elliptical"],
        width: float,
        minor_width: float,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["calligraphic"],
        width: float,
        height: float,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: Literal["convex"],
        nib: contour | layer,
        /,
        angle: float = 0,
        cap: Literal["nib", "butt", "round", "bevel"] = "nib",
        join: Literal["nib", "bevel", "miter", "miterclip", "round", "arcs"] = "nib",
        **kwargs: StrokeOptions,
    ) -> None:
        """
        Strokes the lines of the contours in all selected glyphs according to the
        supplied parameters. See :meth:`glyph.stroke()` for a description of the
        syntax.
        """
        ...

    def transform(
        self,
        matrix: tuple[float, float, float, float, float, float],
        flags: tuple[
            Literal[
                "activeLayer", "guide", "noWidth", "round", "simplePos", "kernClasses"
            ],
            ...,
        ] = (),
    ) -> None:
        """
        Transforms all selected glyphs by the matrix. The optional flags argument
        should be a tuple containing any of the following strings:

        activeLayer:

          Transform :attr:`font.activeLayer` only. (By default all layers are
          transformed.)

        guide:

          Also transform :attr:`font.guide` layer.

        noWidth:

          Do not change :attr:`glyph.width`.

        round:

          Round to int after the transformation is done.

        simplePos:

          Also transform simple positioning features and kern pairs.

        kernClasses:

          Also transform kerning classes.
        """
        ...

    def nltransform(self, xexpr: str, yexpr: str) -> None:
        """
        xexpr and yexpr are strings specifying non-linear transformations that will
        be applied to all points in the selected glyphs of the font (with xexpr
        being applied to x values, and yexpr to y values, of course).
        """
        ...

    def unlinkReferences(self) -> None:
        """
        Unlinks all references in all selected glyphs and replaces them with splines.
        """
        ...
