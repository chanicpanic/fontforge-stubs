"""
The primary module for interacting with FontForge
"""

from typing import (
    Any,
    Tuple,
    List,
    Dict,
    Union,
    Optional,
    Iterator,
    overload,
    override,
    Sequence,
    TypedDict,
    Callable,
    Final,
    Literal,
    Iterable,
    TypeVar,
    Hashable,
    TypeAlias,
)

from typing_extensions import (
    NotRequired,
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

def registerGlyphSeparationHook[T](
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
def registerMenuItem[T](
    callback: Callable[[T | None, glyph | font], None],
    enable: Callable[[T | None, glyph | font], bool] | None,
    data: T | None,
    context: Literal["Font", "Glyph"] | tuple[Literal["Font"], Literal["Glyph"]],
    hotkey: str | None,
    *submenu_names: str | tuple[str, str] | tuple[str, str, str],
    name: str | tuple[str, str] | tuple[str, str, str],
) -> None: ...
@overload
def registerMenuItem[T](
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
) -> None: ...
def registerMenuItem(*args, **kwargs) -> None:
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

def registerImportExport[T](
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
    ...
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

# Layer class
class layer(Sequence[contour]):
    """A layer is a collection of contours. All the contours must be of the same order (all quadratic or all cubic)."""
    def is_quadratic(self) -> bool:
        """Whether the contours should be interpreted as a set of quadratic or cubic splines."""
        ...
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[contour]:
        """Returns an iterator for the layer which will return the contours in order."""
        ...
    def __reduce__(self) -> Any:
        """This function allows the pickler to work on this type."""
        ...
    def dup(self) -> "layer":
        """Returns a deep copy of the layer."""
        ...
    def isEmpty(self) -> bool:
        """Returns whether the layer is empty (contains no contour)"""
        ...
    def addExtrema(
        self, flags: Optional[str] = ..., emsize: Optional[int] = ...
    ) -> None:
        """If a curve lacks a point at an extrema this command will add one."""
        ...
    def cluster(
        self, within: Optional[float] = ..., max: Optional[float] = ...
    ) -> None:
        """Moves clustered coordinates to a standard central value."""
        ...
    def correctDirection(self) -> None:
        """Orients all contours so that external ones are clockwise and internal counter-clockwise."""
        ...
    def export(self, filename: str, **kwargs) -> None:
        """Exports the current layer (in outline format) to a file."""
        ...
    def exclude(self, excluded_layer: "layer") -> None:
        """Removes the excluded area from the current contours."""
        ...
    def intersect(self) -> None:
        """Leaves only areas in the intersection of contours."""
        ...
    def removeOverlap(self) -> None:
        """Removes overlapping areas."""
        ...
    def interpolateNewLayer(self, other_layer: "layer", amount: float) -> "layer":
        """Creates (and returns) a new layer which contains splines interpolated from the current layer and the first argument."""
        ...
    def round(self, factor: Optional[float] = ...) -> None:
        """Rounds the x and y coordinates."""
        ...
    def selfIntersects(self) -> bool:
        """Returns whether any of the contours on this layer intersects any other contour (including itself)."""
        ...
    def similar(self, other_layer: "layer", error: Optional[float] = ...) -> bool:
        """Checks whether this layer is similar to the other one."""
        ...
    def simplify(
        self,
        error_bound: Optional[float] = ...,
        flags: Optional[Tuple[str, ...]] = ...,
        tan_bounds: Optional[Any] = ...,
        linefixup: Optional[Any] = ...,
        linelenmax: Optional[Any] = ...,
    ) -> None:
        """Tries to remove excess points on the layer."""
        ...
    def stemControl(
        self,
        stem_width_scale: float,
        hscale: Optional[float] = ...,
        stem_height_scale: Optional[float] = ...,
        vscale: Optional[float] = ...,
        xheight: Optional[float] = ...,
    ) -> None:
        """Allows you to scale counters and stems independently of each other."""
        ...
    def stroke(self, type: str, *args, **kwargs) -> "layer":
        """Strokes the lines of each contour in the layer according to the supplied parameters."""
        ...
    def transform(
        self, matrix: Tuple[float, float, float, float, float, float]
    ) -> None:
        """Transforms the layer by the matrix"""
        ...
    def nltransform(self, xexpr: str, yexpr: str) -> None:
        """Applies non-linear transformations to all points in the layer."""
        ...
    def boundingBox(self) -> Tuple[float, float, float, float]:
        """Returns a tuple representing a rectangle ``(xmin,ymin, xmax,ymax)`` into which the layer fits."""
        ...
    def xBoundsAtY(
        self, ybottom: float, ytop: Optional[float] = ...
    ) -> Optional[Tuple[float, float]]:
        """Finds the minimum and maximum x positions attained by the layer within a y-range."""
        ...
    def yBoundsAtX(
        self, xleft: float, xright: Optional[float] = ...
    ) -> Optional[Tuple[float, float]]:
        """Finds the minimum and maximum y positions attained by the layer within an x-range."""
        ...
    def draw(self, pen: "glyphPen") -> None:
        """Draw the layer to the pen argument."""
        ...
    def addInflections(self) -> None:
        """Please see contour.addInflections()."""
        ...
    def balance(self) -> None:
        """Please see contour.balance()."""
        ...
    def harmonize(self) -> None:
        """Please see contour.harmonize()."""
        ...
    def __len__(self) -> int:
        """The number of contours in the layer"""
        ...
    @overload
    def __getitem__(self, i: int) -> contour: ...
    @overload
    def __getitem__(self, s: slice) -> "layer": ...
    @overload
    def __setitem__(self, i: int, c: contour) -> None: ...
    @overload
    def __setitem__(self, s: slice, l: "layer") -> None: ...
    def __delitem__(self, i: Union[int, slice]) -> None: ...
    def __add__(self, other: Union["layer", contour]) -> "layer":
        """A layer concatenating l and m."""
        ...
    def __iadd__(self, other: Union["layer", contour]) -> "layer":
        """Appends m to l."""
        ...

# GlyphPen class
class glyphPen:
    """This implements the Pen Protocol to draw a FontForge glyph."""
    def moveTo(self, pt: Tuple[float, float]) -> None:
        """Begins every contour and creates an on curve point at (x,y) as the start point of that contour."""
        ...
    def lineTo(self, pt: Tuple[float, float]) -> None:
        """Draws a line from the last point to (x,y) and adds that to the contour."""
        ...
    @overload
    def curveTo(
        self,
        cp1: Tuple[float, float],
        cp2: Tuple[float, float],
        end: Tuple[float, float],
    ) -> None: ...
    @overload
    def curveTo(self, cp: Tuple[float, float], end: Tuple[float, float]) -> None: ...
    def curveTo(self, *args) -> None:
        """Draws a cubic or quadratic curve."""
        ...
    def qCurveTo(self, *points: Union[Tuple[float, float], None]) -> None:
        """This routine may only be used in quadratic (TrueType) fonts and expresses the idiom where on-curve points may be omitted."""
        ...
    def closePath(self) -> None:
        """Closes the contour (connects the last point to the first point to make a loop) and ends it."""
        ...
    def endPath(self) -> None:
        """Ends the contour without closing it."""
        ...
    def addComponent(
        self,
        glyph_name: str,
        transform: Tuple[float, float, float, float, float, float] = ...,
        selected: bool = ...,
    ) -> None:
        """Adds a reference (a component) to the glyph."""
        ...

# Glyph class
class glyph:
    """The glyph type refers to a glyph object. It has no independent life of its own, it always lives within a font."""

    activeLayer: int
    """Returns currently active layer in the glyph (as an integer). May be set to an integer or a layer name to change the active layer."""
    altuni: Optional[Tuple[Tuple[int, int, int], ...]]
    """Returns additional unicode code points for this glyph. For a primary code point, see glyph.unicode ."""
    anchorPoints: Tuple[Tuple[str, str, float, float, Optional[int]], ...]
    """Returns the list of anchor points in the glyph."""
    anchorPointsWithSel: Tuple[Tuple[str, str, float, float, bool, Optional[int]], ...]
    """Same as the above, except also includes whether the anchor point is selected in the UI."""
    background: layer
    """The glyph's background layer. This is a *copy* of the glyph's data."""
    changed: bool
    """Whether this glyph has been modified. This is (should be) maintained automatically, but you may set it if you wish."""
    color: int
    """The color of the glyph in the fontview. A 6 hex-digit RGB number or -1 for default."""
    comment: str
    """Any comment you wish to associate with the glyph. UTF-8"""
    dhints: Tuple[
        Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float]], ...
    ]
    """A tuple with one entry for each diagonal stem hint."""
    encoding: int
    """Returns the glyph's encoding in the font's encoding. (readonly)"""
    font: "font"
    """The font containing this glyph. (readonly)"""
    foreground: layer
    """The glyph's foreground layer. This is a *copy* of the glyph's data."""
    glyphclass: str
    """An opentype glyphclass, one of automatic, noclass, baseglyph, baseligature, mark, component"""
    glyphname: str
    """The name of the glyph"""
    hhints: Tuple[Tuple[float, float], ...]
    """A tuple of all horizontal postscript hints. Each hint is itself a tuple of starting locations and widths."""
    horizontalComponents: Tuple[Tuple[str, bool, int, int, int], ...]
    """A tuple of tuples. Allows constructing very large versions of the glyph by stacking the components together."""
    horizontalComponentItalicCorrection: float
    """The italic correction for any composite glyph made with the horizontalComponents."""
    horizontalVariants: str
    """A string containing a list of glyph names. These are alternate forms of the current glyph for use in typesetting math."""
    isExtendedShape: bool
    """A boolean containing the MATH "is extended shape" field."""
    italicCorrection: float
    """The glyph's italic correction field. Used by both TeX and MATH."""
    layer_cnt: int
    """The number of layers in this glyph. (Cannot be set)"""
    layers: Dict[Union[str, int], layer]
    """A dictionary like object containing the layers of the glyph."""
    layerrefs: Dict[Union[str, int], Tuple[Tuple[str, Tuple[float, ...], bool], ...]]
    """A dictionary like object containing the references in the layers of the glyph."""
    lcarets: Tuple[int, ...]
    """A tuple containing the glyph's ligature caret locations."""
    left_side_bearing: float
    """The left side bearing of the glyph. Setting this value will adjust all layers."""
    manualHints: bool
    """The glyph's hints have been set by hand, and the glyph should not be autohinted without a specific request from the user."""
    mathKern: Any  # This is a complex object with bottomLeft, bottomRight, etc.
    """The glyph's math kerning data associated with its vertices."""
    originalgid: int
    """The GID of this glyph in the font it was read from. (readonly)"""
    persistent: Any
    """Whatever you want (these data will be saved as a pickled object in the sfd file)."""
    references: Tuple[Tuple[str, Tuple[float, ...], bool], ...]
    """A tuple of tuples containing, for each reference in the foreground, a glyph-name, a transformation matrix, and whether the reference is currently selected."""
    right_side_bearing: float
    """The right side bearing of the glyph"""
    script: str
    """A string containing the OpenType 4 letter tag for the script associated with this glyph (readonly)"""
    temporary: Any
    """Whatever you want (these data will be lost once the font is closed)"""
    texheight: float
    """The Tex height."""
    texdepth: float
    """The Tex depth."""
    topaccent: float
    """The glyph's top accent position field. Used by MATH."""
    ttinstrs: bytes
    """Any truetype instructions, returned as a binary string"""
    unicode: int
    """The glyph's unicode code point, or -1. In addition to this primary mapping, a glyph can have multiple secondary mappings."""
    unlinkRmOvrlpSave: bool
    """A flag that indicates the glyph's references should be unlinked and remove overlap run on it before the font is saved."""
    user_decomp: Any
    """Your preferred decomposition for this glyph; used by glyph.build()."""
    vhints: Tuple[Tuple[float, float], ...]
    """A tuple of all vertical postscript hints. Each hint is itself a tuple of starting locations and widths."""
    validation_state: int
    """A bit mask indicating some problems this glyph might have. (readonly)"""
    verticalComponents: Tuple[Tuple[str, bool, int, int, int], ...]
    """A tuple of tuples. Allows constructing very large versions of the glyph by stacking the components together."""
    verticalComponentItalicCorrection: float
    """The italic correction for any composite glyph made with the verticalComponents."""
    verticalVariants: str
    """A string containing a list of glyph names. These are alternate forms of the current glyph for use in typesetting math."""
    width: float
    """The advance width of the glyph."""
    vwidth: float
    """The vertical advance width of the glyph."""

    def addAnchorPoint(
        self,
        anchor_class_name: str,
        anchor_type: str,
        x: float,
        y: float,
        ligature_index: Optional[int] = ...,
    ) -> None:
        """Adds an anchor point."""
        ...
    def addExtrema(
        self, flags: Optional[str] = ..., emsize: Optional[int] = ...
    ) -> None:
        """Extrema should be marked by on-curve points. If a curve lacks a point at an extrema this command will add one."""
        ...
    def addReference(
        self, glyph_name: str, transform: Tuple[float, ...] = ..., selected: bool = ...
    ) -> None:
        """Adds a reference to the specified glyph into the current glyph."""
        ...
    def addHint(self, is_vertical: bool, start: float, width: float) -> None:
        """Adds a postscript hint. Takes a boolean flag indicating whether the hint is horizontal or vertical, a start location and the hint's width."""
        ...
    def addPosSub(self, subtable_name: str, *args) -> None:
        """Adds position/substitution data to the glyph."""
        ...
    @overload
    def appendAccent(self, name: str) -> None: ...
    @overload
    def appendAccent(self, unicode: int) -> None: ...
    def appendAccent(self, **kwargs) -> None:
        """Makes a reference to the specified glyph, adds that reference to the current layer of this glyph, and positions it to make a reasonable accent."""
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
    def boundingBox(self) -> Tuple[float, float, float, float]:
        """Returns a tuple representing a rectangle (xmin,ymin, xmax,ymax) which is the minimum bounding box of the glyph."""
        ...
    def build(self) -> None:
        """If the character is a composite character, then clears it and inserts references to its components."""
        ...
    def canonicalContours(self) -> None:
        """Orders the contours in the current glyph by the x coordinate of their leftmost point."""
        ...
    def canonicalStart(self) -> None:
        """Sets the start point of all the contours of the current glyph to be the leftmost point on the contour."""
        ...
    def changeWeight(self, stroke_width: float, **kwargs) -> None:
        """Changes the weight (thickness) of the glyph."""
        ...
    def condenseExtend(
        self,
        c_factor: float,
        c_add: float,
        sb_factor: Optional[float] = ...,
        sb_add: Optional[float] = ...,
        correct: bool = ...,
    ) -> None:
        """Condenses or extends the size of the counters and side-bearings of the glyph."""
        ...
    def clear(self, layer: Optional[Union[int, str]] = ...) -> None:
        """Clears the contents of the glyph."""
        ...
    def cluster(
        self, within: Optional[float] = ..., max: Optional[float] = ...
    ) -> None:
        """Moves clustered coordinates to a standard central value."""
        ...
    def correctDirection(self) -> None:
        """Orients all contours so that external ones are clockwise and internal counter-clockwise."""
        ...
    def doUndoLayer(
        self, layer: Optional[Union[int, str]] = ..., redo: bool = ...
    ) -> None:
        """Equivalent to the 'Undo' or 'Redo' UI menu item for a layer."""
        ...
    def exclude(self, excluded_layer: layer) -> None:
        """Removes the excluded area from the current glyph. Takes an argument which is a layer."""
        ...
    def export(self, filename: str, **kwargs) -> None:
        """Creates a file with the specified name containing a representation of the glyph."""
        ...
    def genericGlyphChange(self, **kwargs) -> None:
        """Similar to font.genericGlyphChange, but acting on this glyph only."""
        ...
    def getPosSub(self, lookup_subtable_name: str) -> Tuple[Tuple[str, str, Any], ...]:
        """Returns any positioning/substitution data attached to the glyph controlled by the lookup-subtable."""
        ...
    def importOutlines(self, filename: str, **kwargs) -> None:
        """Imports outline descriptions (eps, svg, glif files) or image descriptions (bmp, png, xbm, etc.)."""
        ...
    def intersect(self) -> None:
        """Leaves only areas in the intersection of contours."""
        ...
    def isWorthOutputting(self) -> bool:
        """Returns whether the glyph is worth outputting into a font file."""
        ...
    def preserveLayerAsUndo(
        self, layer: Optional[Union[int, str]] = ..., dohints: bool = ...
    ) -> None:
        """Preserves the current state of a layer so that whatever you do after can be undone by the user."""
        ...
    def removeOverlap(self) -> None:
        """Removes overlapping areas."""
        ...
    def removePosSub(self, lookup_subtable_name: str) -> None:
        """Removes all data from the glyph corresponding to the given lookup-subtable."""
        ...
    def round(self, factor: Optional[float] = ...) -> None:
        """Rounds the x and y coordinates of each point in the glyph."""
        ...
    def selfIntersects(self) -> bool:
        """Returns whether any of the contours in this glyph intersects any other contour in the glyph (including itself)."""
        ...
    def setLayer(
        self,
        layer_obj: layer,
        layer_index: Union[int, str],
        flags: Optional[Tuple[str, ...]] = ...,
    ) -> None:
        """An alternative to assigning to glyph.layers, glyph.background, or glyph.foreground."""
        ...
    def simplify(self, error_bound: Optional[float] = ..., **kwargs) -> None:
        """Tries to remove excess points in the glyph if doing so will not perturb the curve by more than error-bound."""
        ...
    def stroke(self, type: str, *args, **kwargs) -> None:
        """Strokes the contours of the glyph according to the supplied parameters."""
        ...
    def transform(
        self, matrix: Tuple[float, ...], flags: Optional[Tuple[str, ...]] = ...
    ) -> None:
        """Transforms the glyph by the matrix."""
        ...
    def nltransform(self, xexpr: str, yexpr: str) -> None:
        """Applies non-linear transformations to all points in the current layer."""
        ...
    def unlinkRef(self, ref_name: Optional[str] = ...) -> None:
        """Unlinks the reference to the glyph named ref-name."""
        ...
    def unlinkThisGlyph(self) -> None:
        """Unlinks all the references to the current glyph within any other glyph in the font."""
        ...
    def useRefsMetrics(self, ref_name: str, flag: bool = ...) -> None:
        """Finds a reference with the given name and sets the 'use_my_metrics' flag on it."""
        ...
    def validate(self, force: bool = ...) -> int:
        """Validates the glyph and returns the validation_state of the glyph."""
        ...
    def draw(self, pen: "glyphPen") -> None:
        """Draw the glyph's outline to the pen argument."""
        ...
    def glyphPen(self, replace: bool = ...) -> "glyphPen":
        """Creates a new glyphPen which will draw into the current glyph."""
        ...
    def addInflections(self) -> None:
        """Please see contour.addInflections()."""
        ...
    def balance(self) -> None:
        """Please see contour.balance()."""
        ...
    def harmonize(self) -> None:
        """Please see contour.harmonize()."""
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

    @property
    def byGlyphs(self) -> selection:
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
        """
        Select everything.
        """
        ...

    def none(self) -> None:
        """
        Deselect everything.
        """
        ...

    def changed(self) -> None:
        """
        Select all glyphs which have changed.
        """
        ...

    def invert(self) -> None:
        """
        Invert the selection.
        """
        ...

    def select(self, *args: SelectionArg) -> None:
        """
        Select items based on the provided arguments.

        Args:
            *args: An arbitrary number of arguments. Each argument may be:
                - A glyph name (str)
                - An integer (interpreted as an encoding index or unicode
                  code point depending on flags)
                - A fontforge.glyph object
                - A tuple of flags (e.g., ("more",), ("unicode", "ranges"))

        The first argument can be a tuple of flags to modify the selection behavior.
        If the first argument is not a flag tuple, or doesn't specify "more"
        or "less", the selection is cleared before adding the new items.
        """
        ...

    def __getitem__(self, key: Union[int, str, Glyph]) -> bool:
        """
        Gets the selection status of a glyph by its encoding value, name,
        unicode string, or glyph object.

        Args:
            key: The value to check for selection. Can be an integer, string
                 (glyph name or "uXXXXX"), or a fontforge.glyph object.

        Returns:
            bool: True if the glyph is selected, False otherwise.
        """
        ...

# Private class
class private(dict[str, Any]):
    """
    This represents a font's postscript private dictionary. You may index it with
    one of the standard names of things that live in the private dictionary.

    This type may not be pickled.
    """
    def __iter__(self) -> Iterator[str]: ...
    """
    Returns an iterator for the dictionary which will return all entries.
    """
    def guess(self, name: str) -> None: ...
    """
    Guess a value for this entry in the private dictionary. If FontForge
    can't make a guess it will simply ignore the request.
    """

DeviceTable = dict[int, int]
"""
A dictionary with keys representing a font size in pixels and values representing
the corresponding adjustment, e.g. ``{9: -1, 10: -1, 12: -1}``.
"""

class Math:
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

    AxisHeight: int
    """Axis height of the font."""

    AccentBaseHeight: int
    """Maximum (ink) height of accent base that does not require raising the accents."""

    FlattenedAccentBaseHeight: int
    """Maximum (ink) height of accent base that does not require flattening the accents."""

    SubscriptShiftDown: int
    """
    The standard shift down applied to subscript elements. Positive for
    moving downward.
    """

    SubscriptTopMax: int
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

    SuperscriptShiftUp: int
    """Standard shift up applied to superscript elements."""

    SuperscriptShiftUpCramped: int
    """Standard shift of superscript relative to base in cramped mode."""

    SuperscriptBottomMin: int
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

    SubSuperscriptGapMin: int
    """Minimum gap between the superscript and subscript ink."""

    SuperscriptBottomMaxWithSubscript: int
    """
    The maximum level to which the (ink) bottom of superscript can be pushed to
    increase the gap between superscript and subscript, before subscript starts
    being moved down.
    """

    SpaceAfterScript: int
    """Extra white space to be added after each sub/superscript."""

    UpperLimitGapMin: int
    """
    Minimum gap between the bottom of the upper limit, and the top of the base
    operator.
    """

    UpperLimitBaselineRiseMin: int
    """
    Minimum distance between the baseline of an upper limit and the bottom of
    the base operator.
    """

    LowerLimitGapMin: int
    """
    Minimum gap between (ink) top of the lower limit, and (ink) bottom of the
    base operator.
    """

    LowerLimitBaselineDropMin: int
    """
    Minimum distance between the baseline of the lower limit and bottom of the
    base operator.
    """

    StackTopShiftUp: int
    """Standard shift up applied to the top element of a stack."""

    StackTopDisplayStyleShiftUp: int
    """
    Standard shift up applied to the top element of a stack in display style.
    """

    StackBottomShiftDown: int
    """
    Standard shift down applied to the bottom element of a stack. Positive
    values indicate downward motion.
    """

    StackBottomDisplayStyleShiftDown: int
    """
    Standard shift down applied to the bottom element of a stack in display
    style. Positive values indicate downward motion.
    """

    StackGapMin: int
    """
    Minimum gap between bottom of the top element of a stack, and the top of
    the bottom element.
    """

    StackDisplayStyleGapMin: int
    """
    Minimum gap between bottom of the top element of a stack and the top of the
    bottom element in display style.
    """

    StretchStackTopShiftUp: int
    """Standard shift up applied to the top element of the stretch stack."""

    StretchStackBottomShiftDown: int
    """
    Standard shift down applied to the bottom element of the stretch stack.
    Positive values indicate downward motion.
    """

    StretchStackGapAboveMin: int
    """
    Minimum gap between the ink of the stretched element and the ink bottom of
    the element above.
    """

    StretchStackGapBelowMin: int
    """
    Minimum gap between the ink of the stretched element and the ink top of
    the element below.
    """

    FractionNumeratorShiftUp: int
    """Standard shift up applied to the numerator."""

    FractionNumeratorDisplayStyleShiftUp: int
    """Standard shift up applied to the numerator in display style."""

    FractionDenominatorShiftDown: int
    """
    Standard shift down applied to the denominator. Positive values indicate
    downward motion.
    """

    FractionDenominatorDisplayStyleShiftDown: int
    """
    Standard shift down applied to the denominator in display style. Positive
    values indicate downward motion.
    """

    FractionNumeratorGapMin: int
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar.
    """

    FractionNumeratorDisplayStyleGapMin: int
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar in display style.
    """

    FractionRuleThickness: int
    """Thickness of the fraction bar."""

    FractionDenominatorGapMin: int
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar.
    """

    FractionDenominatorDisplayStyleGapMin: int
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar in display style.
    """

    SkewedFractionHorizontalGap: int
    """
    Horizontal distance between the top and bottom elements of a skewed fraction.
    """

    SkewedFractionVerticalGap: int
    """
    Vertical distance between the ink of the top and bottom elements of a skewed
    fraction.
    """

    OverbarVerticalGap: int
    """Distance between the overbar and the ink top of the base."""

    OverbarRuleThickness: int
    """Thickness of the overbar."""

    OverbarExtraAscender: int
    """Extra white space reserved above the overbar."""

    UnderbarVerticalGap: int
    """Distance between underbar and the (ink) bottom of the base."""

    UnderbarRuleThickness: int
    """Thickness of the underbar."""

    UnderbarExtraDescender: int
    """Extra white space reserved below the underbar."""

    RadicalVerticalGap: int
    """Space between the ink to of the expression and the bar over it."""

    RadicalDisplayStyleVerticalGap: int
    """
    Space between the ink top of the expression and the bar over it in display
    style.
    """

    RadicalRuleThickness: int
    """
    Thickness of the radical rule in designed or constructed radical signs.
    """

    RadicalExtraAscender: int
    """Extra white space reserved above the radical."""

    RadicalKernBeforeDegree: int
    """
    Extra horizontal kern before the degree of a radical if such be present.
    """

    RadicalKernAfterDegree: int
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

    MathLeadingDeviceTable: DeviceTable | None
    """
    White space to be left between math formulae to ensure proper line spacing.
    """

    AxisHeightDeviceTable: DeviceTable | None
    """Axis height of the font."""

    AccentBaseHeightDeviceTable: DeviceTable | None
    """
    Maximum (ink) height of accent base that does not require raising the accents.
    """

    FlattenedAccentBaseHeightDeviceTable: DeviceTable | None
    """
    Maximum (ink) height of accent base that does not require flattening the accents.
    """

    SubscriptShiftDownDeviceTable: DeviceTable | None
    """
    The standard shift down applied to subscript elements. Positive for
    moving downward.
    """

    SubscriptTopMaxDeviceTable: DeviceTable | None
    """
    Maximum height of the (ink) top of subscripts that does not require moving
    subscripts further down.
    """

    SubscriptBaselineDropMinDeviceTable: DeviceTable | None
    """
    Maximum allowed drop of the baseline of subscripts relative to the bottom of
    the base. Used for bases that are treated as a box or extended shape.
    Positive for subscript baseline dropped below base bottom.
    """

    SuperscriptShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to superscript elements."""

    SuperscriptShiftUpCrampedDeviceTable: DeviceTable | None
    """Standard shift of superscript relative to base in cramped mode."""

    SuperscriptBottomMinDeviceTable: DeviceTable | None
    """
    Minimum allowed height of the bottom of superscripts that does not require
    moving them further up.
    """

    SuperscriptBaselineDropMaxDeviceTable: DeviceTable | None
    """
    Maximum allowed drop of the baseline of superscripts relative to the top of
    the base. Used for bases that are treated as a box or extended shape.
    Positive for superscript baseline below base top.
    """

    SubSuperscriptGapMinDeviceTable: DeviceTable | None
    """Minimum gap between the superscript and subscript ink."""

    SuperscriptBottomMaxWithSubscriptDeviceTable: DeviceTable | None
    """
    The maximum level to which the (ink) bottom of superscript can be pushed to
    increase the gap between superscript and subscript, before subscript starts
    being moved down.
    """

    SpaceAfterScriptDeviceTable: DeviceTable | None
    """Extra white space to be added after each sub/superscript."""

    UpperLimitGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between the bottom of the upper limit, and the top of the base
    operator.
    """

    UpperLimitBaselineRiseMinDeviceTable: DeviceTable | None
    """
    Minimum distance between the baseline of an upper limit and the bottom of
    the base operator.
    """

    LowerLimitGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between (ink) top of the lower limit, and (ink) bottom of the
    base operator.
    """

    LowerLimitBaselineDropMinDeviceTable: DeviceTable | None
    """
    Minimum distance between the baseline of the lower limit and bottom of the
    base operator.
    """

    StackTopShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the top element of a stack."""

    StackTopDisplayStyleShiftUpDeviceTable: DeviceTable | None
    """
    Standard shift up applied to the top element of a stack in display style.
    """

    StackBottomShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the bottom element of a stack. Positive
    values indicate downward motion.
    """

    StackBottomDisplayStyleShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the bottom element of a stack in display
    style. Positive values indicate downward motion.
    """

    StackGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between bottom of the top element of a stack, and the top of
    the bottom element.
    """

    StackDisplayStyleGapMinDeviceTable: DeviceTable | None
    """
    Minimum gap between bottom of the top element of a stack and the top of the
    bottom element in display style.
    """

    StretchStackTopShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the top element of the stretch stack."""

    StretchStackBottomShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the bottom element of the stretch stack.
    Positive values indicate downward motion.
    """

    StretchStackGapAboveMinDeviceTable: DeviceTable | None
    """
    Minimum gap between the ink of the stretched element and the ink bottom of
    the element above.
    """

    StretchStackGapBelowMinDeviceTable: DeviceTable | None
    """
    Minimum gap between the ink of the stretched element and the ink top of
    the element below.
    """

    FractionNumeratorShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the numerator."""

    FractionNumeratorDisplayStyleShiftUpDeviceTable: DeviceTable | None
    """Standard shift up applied to the numerator in display style."""

    FractionDenominatorShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the denominator. Positive values indicate
    downward motion.
    """

    FractionDenominatorDisplayStyleShiftDownDeviceTable: DeviceTable | None
    """
    Standard shift down applied to the denominator in display style. Positive
    values indicate downward motion.
    """

    FractionNumeratorGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar.
    """

    FractionNumeratorDisplayStyleGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink bottom of the numerator and the ink of
    the fraction bar in display style.
    """

    FractionRuleThicknessDeviceTable: DeviceTable | None
    """Thickness of the fraction bar."""

    FractionDenominatorGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar.
    """

    FractionDenominatorDisplayStyleGapMinDeviceTable: DeviceTable | None
    """
    Minimum tolerated gap between the ink top of the denominator and the ink of
    the fraction bar in display style.
    """

    SkewedFractionHorizontalGapDeviceTable: DeviceTable | None
    """
    Horizontal distance between the top and bottom elements of a skewed fraction.
    """

    SkewedFractionVerticalGapDeviceTable: DeviceTable | None
    """
    Vertical distance between the ink of the top and bottom elements of a skewed
    fraction.
    """

    OverbarVerticalGapDeviceTable: DeviceTable | None
    """Distance between the overbar and the ink top of the base."""

    OverbarRuleThicknessDeviceTable: DeviceTable | None
    """Thickness of the overbar."""

    OverbarExtraAscenderDeviceTable: DeviceTable | None
    """Extra white space reserved above the overbar."""

    UnderbarVerticalGapDeviceTable: DeviceTable | None
    """Distance between underbar and the (ink) bottom of the base."""

    UnderbarRuleThicknessDeviceTable: DeviceTable | None
    """Thickness of the underbar."""

    UnderbarExtraDescenderDeviceTable: DeviceTable | None
    """Extra white space reserved below the underbar."""

    RadicalVerticalGapDeviceTable: DeviceTable | None
    """Space between the ink to of the expression and the bar over it."""

    RadicalDisplayStyleVerticalGapDeviceTable: DeviceTable | None
    """
    Space between the ink top of the expression and the bar over it in display
    style.
    """

    RadicalRuleThicknessDeviceTable: DeviceTable | None
    """
    Thickness of the radical rule in designed or constructed radical signs.
    """

    RadicalExtraAscenderDeviceTable: DeviceTable | None
    """Extra white space reserved above the radical."""

    RadicalKernBeforeDegreeDeviceTable: DeviceTable | None
    """
    Extra horizontal kern before the degree of a radical if such be present.
    """

    RadicalKernAfterDegreeDeviceTable: DeviceTable | None
    """
    Negative horizontal kern after the degree of a radical if such be present.
    """

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

    # ------------------
    # -- ATTRIBUTES --
    # ------------------

    activeLayer: Union[int, str]
    """
    Returns currently active layer in the font (as an integer). 
    May be set to an integer or a layer name to change the active layer. 
    """

    ascent: int
    """The font's ascent. """

    bitmapSizes: Tuple[int, ...]
    """
    A tuple with an entry for each bitmap strike attached to the font. 
    Each strike is identified by pixelsize. If the strike is a grey scale font it
    will be indicated by ``(bitmap-depth<<16)|pixelsize``. 

    When setting this value pass in a tuple of the same format.
    """

    changed: bool
    """Bit indicating whether the font has been modified. This is (should be)
    maintained automatically, but you may set it if you wish."""

    cidcopyright: str
    """Copyright message of the cid-keyed font as a whole. """

    cidfamilyname: str
    """Family name of the cid-keyed font as a whole. """

    cidfontname: str
    """Font name of the cid-keyed font as a whole. """

    cidfullname: str
    """Full name of the cid-keyed font as a whole. """

    cidordering: Any
    """(No documentation provided in source)"""

    cidregistry: Any
    """(No documentation provided in source)"""

    cidsubfont: Union[int, str]
    """
    Returns the number index of the current subfont in the cid-keyed font. 
    May be set to an index (an integer) or a subfont fontname (a string) to
    change the current subfont. 
    """

    cidsupplement: Any
    """(No documentation provided in source)"""

    cidversion: Any
    """(No documentation provided in source)"""

    cidweight: str
    """Weight of the cid-keyed font as a whole."""

    comment: str
    """A comment associated with the font. Can be anything. """

    copyright: str
    """PostScript copyright notice."""

    cvt: Sequence[int]
    """
    Returns a sequence object containing the font's cvt table. 
    Changes made to this object will be made to the font (this is a reference not a copy). 
    The object has one additional method ``cvt.find(value[,low,high])`` which
    finds the index of value in the cvt table (or -1 if not found). 
    """

    default_base_filename: str
    """The default base for the filename when generating a font. """

    descent: int
    """The font's descent."""

    design_size: float
    """Size (in pica points) for which this font was designed. """

    em: int
    """
    The em size of the font. 
    Setting this will scale the entire font to the new size. 
    """

    encoding: str
    """
    The name of the current encoding. 
    Setting it will change the encoding used for indexing. 
    To compact the encoding, set it to your desired encoding (e.g. ``UnicodeBMP``),
    then set it to ``compacted``. 
    """

    familyname: str
    """PostScript font family name."""

    fondname: str
    """Mac fond name."""

    fontlog: str
    """A comment associated with the font. Can be anything. """

    fontname: str
    """
    PostScript font name. 
    Note that in a CID keyed font this will be the name of the current subfont. 
    Use cidfontname for the name of the font as a whole. 
    """

    fullname: str
    """PostScript font name."""

    gasp: Tuple[Tuple[int, Tuple[str, ...]], ...]
    """
    Returns a tuple of all gasp table entries. Each item is a tuple composed
    of a ppem (integer) and a tuple of flags ('gridfit', 'antialias', etc.). 
    """

    gasp_version: int
    """The version of the 'gasp' table. Currently this may be 0 or 1. """

    guide: layer
    """A copy of the font's guide layer."""

    hasvmetrics: Any
    """(No documentation provided in source)"""

    head_optimized_for_cleartype: Any
    """(No documentation provided in source)"""

    hhea_ascent: Any
    """(No documentation provided in source)"""

    hhea_ascent_add: Any
    """(No documentation provided in source)"""

    hhea_descent: Any
    """(No documentation provided in source)"""

    hhea_descent_add: Any
    """(No documentation provided in source)"""

    hhea_linegap: Any
    """(No documentation provided in source)"""

    horizontalBaseline: Optional[Tuple[Tuple[str, ...], Tuple[Any, ...]]]
    """
    A tuple of tuples containing horizontal baseline information ('BASE' table). 
    Returns None if there is no information. 
    """

    is_quadratic: bool
    """
    Deprecated. Whether contours are quadratic or cubic. 
    Setting this value converts the entire font. Now each layer has its own setting. 
    """

    isnew: bool
    """A flag indicating that this is a new font."""

    italicangle: float
    """(No documentation provided in source)"""

    layers: Dict[str, layer]
    """
    Returns a dictionary-like object with information on the layers of the font. 
    You may add, remove, and modify layers through this object. 
    Note: These layers are different from layers in a glyph. 
    """

    macstyle: int
    """
    A bitmask for Mac style settings.
    Bit 0: Bold, Bit 1: Italic, Bit 2: Underline, Bit 3: Outline, Bit 4: Shadow,
    Bit 5: Condensed , Bit 6: Extended. 
    """

    math: math
    """
    Returns a :class:`math` object which provides information on the font's
    underlying math constant table.  There is only one of these per font. 
    """

    multilayer: Any
    """(No documentation provided in source)"""

    onlybitmaps: bool
    """A flag indicating that this font only contains bitmaps. No outlines. """

    persistent: Dict[str, Any]
    """
    A dictionary for user data that will be saved as a pickled object in the sfd file.
    If the key 'initScriptString' is present, the associated string will be executed
    by the python interpreter each time the font is loaded. 
    """

    private: private
    """
    Returns a :class:`private` dictionary-like object representing the
    PostScript private dictionary for the font. 
    Changing entries in this object will change them in the font. 
    """

    selection: selection
    """
    Returns a reference to an array-like object representing the font's selection. 
    You may set this with a tuple of integers or boolean values. 
    """

    sfntRevision: Optional[Union[float, int]]
    """
    The font revision field from the 'head' table. May be None if unset. 
    Can be set to None, a double, or an integer. 
    """

    size_feature: Optional[
        Union[
            Tuple[float],
            Tuple[float, float, float, int, Tuple[Tuple[Union[str, int], str], ...]],
        ]
    ]
    """
    The OpenType 'size' feature.
    If only design size is specified, returns a single-element tuple. 
    Otherwise, returns a five-element tuple with design size, range, style id,
    and language/string pairs.  Returns None if no size info is present. 
    """

    strokedfont: bool
    """Is this a stroked font? """

    strokewidth: float
    """The stroke width of a stroked font. """

    temporary: Dict[str, Any]
    """
    A dictionary for user data that will be lost once the font is closed.
    Special keys 'generateFontPreHook' and 'generateFontPostHook' can be assigned
    functions to be called before and after font generation. [cite: 115, 117]
    """

    uniqueid: Any
    """(No documentation provided in source)"""

    upos: float
    """Underline position."""

    uwidth: float
    """Underline width."""

    version: str
    """PostScript font version string."""

    verticalBaseline: Optional[Tuple[Tuple[str, ...], Tuple[Any, ...]]]
    """Same format as :attr:`font.horizontalBaseline`. """

    weight: str
    """PostScript font weight string."""

    woffMajor: Optional[int]
    """
    The major version number of a woff file.
    The value returned will be None if the field is unset or an integer. 
    You may set it to None which "unsets" it, or to an integer. 
    """

    woffMinor: Optional[int]
    """
    The minor version number of a woff file.
    The value returned will be None if the field is unset or an integer. 
    You may set it to None which "unsets" it, or to an integer. 
    """

    woffMetadata: str
    """Any metadata associated with a woff file. This is a utf8 string containing unparsed xml. [cite: 130, 131]"""

    # ---------------------------
    # -- READ-ONLY ATTRIBUTES --
    # ---------------------------

    @property
    def capHeight(self) -> int:
        """
        (readonly) Computes the Cap Height (height of capital letters).
        A negative number indicates the value could not be computed.
        """
        ...

    @property
    def cidsubfontcnt(self) -> int:
        """(readonly) Returns the number of subfonts in this cid-keyed font."""
        ...

    @property
    def cidsubfontnames(self) -> Optional[Tuple[str, ...]]:
        """(readonly) Returns a tuple of the subfont names in this cid-keyed font."""
        ...

    @property
    def gpos_lookups(self) -> Tuple[str, ...]:
        """(readonly) Returns a tuple of all positioning lookup names in the font."""
        ...

    @property
    def gsub_lookups(self) -> Tuple[str, ...]:
        """(readonly) Returns a tuple of all substitution lookup names in the font."""
        ...

    @property
    def is_cid(self) -> bool:
        """(readonly) Indicates whether the font is a cid-keyed font or not."""
        ...

    @property
    def layer_cnt(self) -> int:
        """(readonly) The number of layers in the font."""
        ...

    @property
    def loadState(self) -> int:
        """(readonly) A bitmask indicating non-fatal errors found when loading the font."""
        ...

    @property
    def path(self) -> str:
        """
        (readonly) Returns the name of the file from which the font was read.
        For a new font, returns a made up filename like "Untitled1.sfd".
        """
        ...

    @property
    def privateState(self) -> int:
        """(readonly) Checks the (PostScript) Private dictionary and returns a bitmask of common errors."""
        ...

    @property
    def sfd_path(self) -> Optional[str]:
        """(readonly) Returns a string (or None) containing the name of the sfd file associated with this font."""
        ...

    @property
    def sfnt_names(self) -> Tuple[Tuple[Union[str, int], Union[str, int], str], ...]:
        """
        (readonly) The strings in the sfnt 'name' table. A tuple of all MS names.
        Each name is a tuple of ``(language, strid, string)``.
        """
        ...

    @property
    def xHeight(self) -> int:
        """
        (readonly) Computes the X Height (height of lower case letters).
        A negative number indicates the value could not be computed.
        """
        ...

    # ------------------
    # -- DUNDER METHODS --
    # ------------------

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator for the font which will run through the font, in gid order, returning glyph names."""
        ...

    def __contains__(self, name: str) -> bool:
        """Returns whether the font contains a glyph with the given name."""
        ...

    def __len__(self) -> int:
        """The number of glyph slots in the current encoding."""
        ...

    def __getitem__(self, key: Union[int, str]) -> glyph:
        """
        If ``key`` is an integer, returns the glyph at that encoding.
        If a string, returns the glyph with that name. May not be assigned to. [cite: 135, 136]
        """
        ...

    # ------------------
    # -- METHODS --
    # ------------------

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
        first_classes: Tuple[Tuple[str, ...], ...],
        second_classes: Tuple[Tuple[str, ...], ...],
        offsets: Tuple[int, ...],
        after: Optional[str] = None,
    ) -> None: ...
    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        separation: int,
        first_classes: Tuple[Tuple[str, ...], ...],
        second_classes: Tuple[Tuple[str, ...], ...],
        onlyCloser: Optional[bool] = None,
        autokern: Optional[bool] = None,
        after: Optional[str] = None,
    ) -> None: ...
    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        separation: int,
        class_distance: int,
        first_glyph_list: List[str],
        second_glyph_list: List[str],
        onlyCloser: Optional[bool] = None,
        autokern: Optional[bool] = None,
        after: Optional[str] = None,
    ) -> None: ...
    @overload
    def addKerningClass(
        self,
        lookup_name: str,
        new_subtable_name: str,
        separation: int,
        class_distance: int,
        onlyCloser: Optional[bool] = None,
        autokern: Optional[bool] = None,
        after: Optional[str] = None,
    ) -> None: ...
    def addKerningClass(self, *args, **kwargs) -> None:
        """
        Creates a new subtable and a new kerning class in the named lookup.
        This method has multiple signatures for manual kerning, auto-kerning with
        pre-defined classes, auto-kerning with glyph lists, and auto-kerning with
        the font's selection. [cite: 138, 141, 145, 147]
        """
        ...

    def addLookup(
        self,
        new_lookup_name: str,
        type: str,
        flags: Optional[Tuple[str, ...]],
        feature_script_lang_tuple: Tuple[
            Tuple[str, Tuple[Tuple[str, Tuple[str, ...]], ...]], ...
        ],
        after_lookup_name: Optional[str] = None,
    ) -> None:
        """
        Creates a new lookup with the given name, type and flags.
        It will tag it with any indicated features.
        """
        ...

    def addLookupSubtable(
        self,
        lookup_name: str,
        new_subtable_name: str,
        after_subtable_name: Optional[str] = None,
    ) -> None:
        """
        Creates a new subtable within the specified lookup.
        If you want to create a contextual subtable, use :meth:`font.addContextualSubtable`.
        """
        ...

    def addContextualSubtable(
        self,
        lookup_name: str,
        new_subtable_name: str,
        type: str,
        rule: str,
        afterSubtable: Optional[str] = None,
        bclasses: Optional[Tuple[Union[str, Tuple[str, ...]], ...]] = None,
        mclasses: Optional[Tuple[Union[str, Tuple[str, ...]], ...]] = None,
        fclasses: Optional[Tuple[Union[str, Tuple[str, ...]], ...]] = None,
        bclassnames: Optional[Tuple[str, ...]] = None,
        mclassnames: Optional[Tuple[str, ...]] = None,
        fclassnames: Optional[Tuple[str, ...]] = None,
    ) -> None:
        """
        Creates a new subtable within the specified contextual lookup.
        The ``type`` should be one of "glyph", "class", "coverage" or "reversecoverage".
        The ``rule`` specifies a string to match and lookups to apply.
        """
        ...

    def addSmallCaps(
        self,
        scheight: Optional[float] = None,
        capheight: Optional[float] = None,
        lcstem: Optional[float] = None,
        ucstem: Optional[float] = None,
        symbols: Optional[bool] = None,
        letter_extension: Optional[str] = None,
        symbol_extension: Optional[str] = None,
        stem_height_factor: Optional[float] = None,
    ) -> None:
        """
        For each selected letter, this function will create a corresponding small caps glyph.
        If you set the ``symbol`` keyword to ``True`` it will also create small caps
        variants of digits and symbols.
        """
        ...

    def alterKerningClass(
        self,
        subtable_name: str,
        first_classes: Tuple[Tuple[str, ...], ...],
        second_classes: Tuple[Tuple[str, ...], ...],
        offsets: Tuple[int, ...],
    ) -> None:
        """
        Changes the kerning class in the named subtable.
        The classes arguments are tuples of tuples of glyph names.
        """
        ...

    @overload
    def autoKern(
        self,
        subtable_name: str,
        separation: int,
        minKern: Optional[int] = None,
        onlyCloser: Optional[bool] = None,
        touch: Optional[int] = None,
    ) -> None: ...
    @overload
    def autoKern(
        self,
        subtable_name: str,
        separation: int,
        glyph_list1: List[str],
        glyph_list2: List[str],
        minKern: Optional[int] = None,
        onlyCloser: Optional[bool] = None,
        touch: Optional[int] = None,
    ) -> None: ...
    def autoKern(self, *args, **kwargs) -> None:
        """
        This command will automatically generate kerning pairs for the named subtable.
        If no glyph lists are specified it will look at all pairs of the glyphs in the selection.
        """
        ...

    def appendSFNTName(
        self, language: Union[str, int], strid: Union[str, int], string: str
    ) -> None:
        """
        Adds a new (or replaces an old) string in the sfnt 'name' table.
        Language may be either the English name of the language/locale or its numeric ID.
        Strid may be one of the (english) string names (Copyright, etc.) or its numeric value.
        """
        ...

    def buildOrReplaceAALTFeatures(self) -> None:
        """
        Removes any existing AALT features and creates new ones containing all
        possible single and alternate substutions available for each glyph.
        """
        ...

    def close(self) -> None:
        """
        Frees memory for the current font.
        Warning: Any python references to it will become invalid.
        """
        ...

    def createChar(self, uni: int, name: Optional[str] = None) -> glyph:
        """
        Create (and return) a character at the specified unicode codepoint.
        To create a glyph with no unicode codepoint, set the first argument to -1
        and specify a name.
        """
        ...

    def generate(
        self,
        filename: str,
        bitmap_type: Optional[str] = None,
        flags: Optional[Tuple[str, ...]] = None,
        bitmap_resolution: Optional[int] = None,
        subfont_directory: Optional[str] = None,
        namelist: Optional[str] = None,
        layer: Optional[Union[str, int]] = None,
    ) -> None:
        """
        Generates a font. The type is determined by the font's extension.
        Flags can be 'apple', 'opentype', 'no-hints', etc.
        """
        ...

    def mergeFonts(
        self,
        filename: Union[str, font],
        preserveCrossFontKerning: Optional[bool] = None,
    ) -> None:
        """Merges the font in the file into the current font."""
        ...

    def reencode(self, encoding: str, force: Optional[bool] = None) -> None:
        """Reencodes the current font into the given encoding."""
        ...

    def revert(self) -> None:
        """
        Reloads the font from the disk.
        Warning: If you have any references to glyphs which live in the font those
        references will no longer be valid, and using them will cause crashes. [cite: 342, 343]
        """
        ...

    def save(self, filename: Optional[str] = None) -> None:
        """Saves the font to an sfd file."""
        ...

    # --- Selection-Based Methods ---

    def addExtrema(self) -> None:
        """If a curve in any selected glyph lacks a point at a significant extremum, this command will add one."""
        ...

    def autoHint(self) -> None:
        """Generates PostScript hints for all selected glyphs."""
        ...

    def autoInstr(self) -> None:
        """Generates TrueType instructions for all selected glyphs."""
        ...

    def build(self) -> None:
        """
        If any selected character is a composite, this command clears it and inserts
        references to its components.
        """
        ...

    def copy(self) -> None:
        """Copies all selected glyphs into FontForge's internal clipboard."""
        ...

    def cut(self) -> None:
        """Copies all selected glyphs into FontForge's internal clipboard and then clears them."""
        ...

    def paste(self) -> None:
        """Pastes the clipboard into the selected glyphs, removing what was there before."""
        ...

    def removeOverlap(self) -> None:
        """Removes overlapping areas in all selected glyphs."""
        ...

    def round(self, factor: Optional[float] = None) -> None:
        """
        Rounds the x and y coordinates of each point in all selected glyphs.
        If factor is specified: new_coord = round(factor*old-coord)/factor.
        """
        ...

    @overload
    def stroke(
        self,
        type: str,
        width: float,
        CAP: Optional[str] = None,
        JOIN: Optional[str] = None,
        ANGLE: Optional[float] = None,
        **kwargs,
    ) -> None: ...
    @overload
    def stroke(
        self,
        type: str,
        width: float,
        minor_width: float,
        ANGLE: Optional[float] = None,
        CAP: Optional[str] = None,
        JOIN: Optional[str] = None,
        **kwargs,
    ) -> None: ...
    @overload
    def stroke(
        self, type: str, width: float, height: float, angle: float, **kwargs
    ) -> None: ...
    @overload
    def stroke(self, type: str, contour: contour, **kwargs) -> None: ...
    def stroke(self, *args, **kwargs) -> None:
        """
        Strokes the lines of the contours in all selected glyphs according to the
        supplied parameters.  Supports "circular", "elliptical", "calligraphic",
        and "convex" stroke types.
        """
        ...

    def transform(
        self,
        matrix: Tuple[float, float, float, float, float, float],
        flags: Optional[Tuple[str, ...]] = None,
    ) -> None:
        """
        Transforms all selected glyphs by the matrix.
        Flags include 'activeLayer', 'guide', 'noWidth', 'round', etc. [cite: 400, 401, 402, 403]
        """
        ...

    def unlinkReferences(self) -> None:
        """Unlinks all references in all selected glyphs and replaces them with splines."""
        ...
