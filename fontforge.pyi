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
    Sequence,
    Callable,
)

# Module attributes

hooks: dict[str, Callable[[Union[font, glyph]], Any]]
"""
A dictionary which the user may fill to associate certain FontForge
events with a python function to be run when those events happen.
The function will be passed the font (or possibly glyph) for which
the relevant event occurred.
"""

splineCorner: int
"""A point type enumeration of value 0"""

splineCurve: int
"""A point type enumeration of value 1"""

splineHVCurve: int
"""A point type enumeration of value 2"""

splineTangent: int
"""A point type enumeration of value 3"""

spiroG4: int
"""A spiro point type enumeration of value 1. A Spiro G4 curve point"""

spiroG2: int
"""A spiro point type enumeration of value 2. A Spiro G2 curve point"""

spiroCorner: int
"""A spiro point type enumeration of value 3. A Spiro corner point"""

spiroLeft: int
"""A spiro point type enumeration of value 4. A Spiro left "tangent" point"""

spiroRight: int
"""A spiro point type enumeration of value 5. A Spiro right "tangent" point"""

spiroOpen: int
"""A spiro point type enumeration of value 6. This may only be used on the first point in a spiro tuple. It indicates that the tuple describes an open contour."""

unspecifiedMathValue: Any
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

def loadEncodingFile(filename: str, encname: Optional[str] = ...) -> Optional[str]:
    """Loads an encoding file, returns the name of the encoding or ``None``."""
    ...

def loadNamelist(filename: str) -> None:
    """Loads a namelist"""
    ...

def loadNamelistDir(dirname: str) -> None:
    """Loads all namelist files in the directory"""
    ...

def preloadCidmap(filename: str, registry: str, order: str, supplement: int) -> None:
    """Loads a FontForge cidmap file (first three args are strings, last is an integer)"""
    ...

def printSetup(
    type: str,
    printer_or_cmd_or_file: Optional[str] = ...,
    width: Optional[float] = ...,
    height: Optional[float] = ...,
) -> None:
    """
    Prepare to print a font sample.
    The first argument may be one of: "lp", "lpr", "ghostview", "command", "ps-file", "pdf-file".
    """
    ...

def nameFromUnicode(uni: int, namelist: Optional[Any] = ...) -> str:
    """Finds the glyph name associated with a given unicode codepoint."""
    ...

def UnicodeAnnotationFromLib(n: int) -> str:
    """Returns the Unicode Annotations for this value as described by www.unicode.org."""
    ...

def UnicodeBlockCountFromLib(n: int) -> int:
    """Return the number of Unicode Blocks as described by www.unicode.org."""
    ...

def UnicodeBlockEndFromLib(n: int) -> int:
    """Returns the Unicode Block end value as described by www.unicode.org."""
    ...

def UnicodeBlockNameFromLib(n: int) -> str:
    """Returns the Unicode Block Name as described by www.unicode.org."""
    ...

def UnicodeBlockStartFromLib(n: int) -> int:
    """Returns the Unicode Block start value as described by www.unicode.org."""
    ...

def unicodeFromName(glyphname: str) -> int:
    """Looks up glyph name in its dictionary and if it is associated with a unicode code point returns that number. Otherwise it returns -1"""
    ...

def UnicodeNameFromLib(n: int) -> str:
    """Returns the Unicode Name for this value as described by www.unicode.org."""
    ...

def UnicodeNamesListVersion() -> str:
    """Return the Unicode Nameslist Version (as described by www.unicode.org)."""
    ...

def UnicodeNames2FromLib(val: int) -> str:
    """This function returns the formal alias for the unicode value given, or an empty string if there is no such alias."""
    ...

def scriptFromUnicode(n: int) -> str:
    """Return the script tag for the given Unicode codepoint."""
    ...

def SpiroVersion() -> str:
    """Returns the version of LibSpiro available to FontForge."""
    ...

def version() -> str:
    """Returns FontForge's version number. This will be a large number like 20070406."""
    ...

def loadPlugins() -> None:
    """Discovers and loads FontForge python plugins according to the current configuration, if not already loaded."""
    ...

def getPluginInfo() -> List[Dict[str, Any]]:
    """Returns a list of dictionary objects describing configured and/or discovered plugins."""
    ...

def configurePlugins(plugins: List[Dict[str, Any]]) -> None:
    """This method allows plugins to be reconfigured using the Python API."""
    ...

def runInitScripts() -> None:
    """Runs the system or user initialization scripts, if not already run."""
    ...

def scriptPath() -> Tuple[str, ...]:
    """Returns a tuple listing the directory paths which are searched for python scripts during FontForge initialization."""
    ...

def fonts() -> Tuple["font", ...]:
    """Returns a tuple of all fonts currently loaded into FontForge for editing"""
    ...

def activeFont() -> Optional["font"]:
    """Returns the font that was active at the time a script was invoked from the UI, otherwise None."""
    ...

def activeGlyph() -> Optional["glyph"]:
    """Returns the glyph that was active at the time a script was invoked from the UI, otherwise None."""
    ...

def activeLayer() -> int:
    """This returns the currently active layer as an integer."""
    ...

def fontsInFile(filename: str) -> Tuple[str, ...]:
    """Returns a tuple of all font names found in the specified file."""
    ...

def open(filename: str, flags: Union[int, Tuple[str, ...]] = ...) -> "font":
    """Opens a filename and returns the font it contains (if any)."""
    ...

def parseTTInstrs(string: str) -> bytes:
    """Returns a binary string each byte of which corresponds to a truetype instruction."""
    ...

def unParseTTInstrs(sequence: bytes) -> str:
    """Reverse of parseTTInstrs. Converts a binary string into a human readable string."""
    ...

def unitShape(n: int) -> "contour":
    """Returns a closed contour which is a regular n-gon."""
    ...

def registerGlyphSeparationHook(hook: Optional[Callable]) -> None:
    """Registers a python routine which FontForge will call to figure out the optical separation between two glyphs."""
    ...

# User Interface Module Functions
def hasUserInterface() -> bool:
    """Returns ``True`` if this session of FontForge has a user interface"""
    ...

@overload
def registerMenuItem(
    callback: Callable,
    enable: Callable,
    data: Any,
    context: str,
    hotkey: str,
    submenu_names: Tuple[Union[str, Tuple[str, ...]], ...],
    name: Union[str, Tuple[str, ...]],
) -> None: ...
@overload
def registerMenuItem(
    callback: Callable,
    enable: Optional[Callable] = ...,
    data: Optional[Any] = ...,
    context: str = ...,
    hotkey: Optional[str] = ...,
    name: Union[str, Tuple[str, ...]] = ...,
    submenu: Optional[Union[str, Tuple[str, ...], List[Any]]] = ...,
    keyword_only: bool = False,
) -> None: ...
@overload
def registerMenuItem(
    context: str,
    divider: bool,
    submenu: Optional[Union[str, Tuple[str, ...], List[Any]]] = ...,
) -> None: ...
def registerMenuItem(*args, **kwargs) -> None:
    """Adds a menu item to the FontForge menu(s) specified by the ``context`` parameter."""
    ...

def registerImportExport(
    import_function: Optional[Callable],
    export_function: Optional[Callable],
    data: Any,
    name: str,
    extension: str,
    extension_list: Optional[str] = ...,
) -> None:
    """This will add the capability to import or export files of a given type."""
    ...

def logWarning(msg: str) -> None:
    """Adds the message (a string) to FontForge's Warnings window."""
    ...

def postError(win_title: str, msg: str) -> None:
    """Creates a popup dialog to display the message (a string) in that dlg."""
    ...

def postNotice(win_title: str, msg: str) -> None:
    """Creates a little window which will silently vanish after a minute or two and displays the message (a string) in that window."""
    ...

def openFilename(
    question: str, def_name: Optional[str] = ..., filter: Optional[str] = ...
) -> Optional[str]:
    """Pops up a file-open dialog. The result is either a filename or ``None`` if the user canceled the dialog."""
    ...

def saveFilename(
    question: str, def_name: Optional[str] = ..., filter: Optional[str] = ...
) -> Optional[str]:
    """Pops up a file-save dialog. The result is either a filename or ``None`` if the user canceled the dialog."""
    ...

def ask(
    title: str,
    question: str,
    answers: Tuple[str, ...],
    default: Optional[int] = ...,
    cancel: Optional[int] = ...,
) -> int:
    """Allows you to ask the user a multiple choice question with buttons."""
    ...

def askChoices(
    title: str,
    question: str,
    answers: Tuple[str, ...],
    default: Optional[Union[int, Tuple[bool, ...]]] = ...,
    multiple: bool = ...,
) -> Union[int, Tuple[int, ...]]:
    """Allows you to ask the user a multiple choice question with a scrollable list."""
    ...

def askString(
    title: str, question: str, def_string: Optional[str] = ...
) -> Optional[str]:
    """Allows you to ask the user a question for which a string is the answer."""
    ...

def askMulti(title: str, specification: Any) -> Optional[Dict[str, Any]]:
    """This method raises a dialog with multiple questions for the user."""
    ...

# Point class
class point:
    """Creates a new point. Optionally specifying its x,y location, on-curve status and selected status."""

    x: float
    y: float
    on_curve: bool
    selected: bool
    type: int
    interpolated: bool
    name: str

    def __init__(
        self,
        x: Optional[float] = ...,
        y: Optional[float] = ...,
        on_curve: bool = ...,
        type: int = ...,
        selected: bool = ...,
    ) -> None: ...
    def dup(self) -> "point":
        """Returns a copy of the current point."""
        ...
    def transform(
        self, matrix: Tuple[float, float, float, float, float, float]
    ) -> None:
        """Transforms the point by the transformation matrix"""
        ...
    def __reduce__(self) -> Any:
        """This function allows the pickler to work on this type."""
        ...

# Contour class
class contour(Sequence[point]):
    """Creates a new contour. A contour is a collection of points."""

    is_quadratic: bool
    closed: bool
    name: str
    spiros: Tuple[Tuple[float, float, int, int], ...]

    def __init__(self, is_quadratic: bool = ...) -> None: ...
    def dup(self) -> "contour":
        """Returns a deep copy of the contour."""
        ...
    def isEmpty(self) -> bool:
        """Returns whether the contour is empty (contains no points)"""
        ...
    def boundingBox(self) -> Tuple[float, float, float, float]:
        """Returns a tuple representing a rectangle ``(xmin,ymin, xmax,ymax)`` into which the contour fits."""
        ...
    def getSplineAfterPoint(
        self, pos: int
    ) -> Tuple[Tuple[float, ...], Tuple[float, ...]]:
        """Returns a tuple of two four-element tuples. These tuples are x and y splines for the curve after the specified point."""
        ...
    def draw(self, pen: "glyphPen") -> None:
        """Draw the contour to the pen argument."""
        ...
    def __reduce__(self) -> Any:
        """This function allows the pickler to work on this type."""
        ...
    def __iter__(self) -> Iterator[point]:
        """Returns an iterator for the contour which will return the points in order."""
        ...
    @overload
    def __getitem__(self, i: int) -> point: ...
    @overload
    def __getitem__(self, s: slice) -> "contour": ...
    @overload
    def __setitem__(self, i: int, p: Union[point, Tuple]) -> None: ...
    @overload
    def __setitem__(self, s: slice, c: Union["contour", Sequence[Tuple]]) -> None: ...
    def __delitem__(self, i: Union[int, slice]) -> None: ...
    def __len__(self) -> int:
        """The number of points in the contour"""
        ...
    def __add__(self, other: Union["contour", point, Tuple]) -> "contour":
        """A contour concatenating c and d."""
        ...
    def __iadd__(self, other: Union["contour", point, Tuple]) -> "contour":
        """Appends d to c."""
        ...
    def __contains__(self, p: Union[point, Tuple[float, float]]) -> bool:
        """When p is a point, returns whether some point ``(p.x, p.y)`` is in the contour c."""
        ...
    def moveTo(self, x: float, y: float) -> None:
        """Adds an initial, on-curve point at ``(x,y)`` to the contour"""
        ...
    def lineTo(self, x: float, y: float, pos: Optional[int] = ...) -> None:
        """Adds an line to the contour."""
        ...
    def cubicTo(
        self,
        cp1: Tuple[float, float],
        cp2: Tuple[float, float],
        end: Tuple[float, float],
        pos: Optional[int] = ...,
    ) -> None:
        """Adds a cubic curve to the contour."""
        ...
    def quadraticTo(
        self,
        cp: Tuple[float, float],
        end: Tuple[float, float],
        pos: Optional[int] = ...,
    ) -> None:
        """Adds a quadratic curve to the contour."""
        ...
    def insertPoint(self, p: Union[point, Tuple], pos: Optional[int] = ...) -> None:
        """Adds point to the contour."""
        ...
    def makeFirst(self, pos: int) -> None:
        """Rotate the point list so that the pos'th point becomes the first point"""
        ...
    def isClockwise(self) -> int:
        """Returns whether the contour is drawn in a clockwise direction."""
        ...
    def reverseDirection(self) -> None:
        """Reverse the order in which the contour is drawn."""
        ...
    def similar(self, other_contour: "contour", error: Optional[float] = ...) -> bool:
        """Checks whether this contour is similar to the other one."""
        ...
    def xBoundsAtY(
        self, ybottom: float, ytop: Optional[float] = ...
    ) -> Optional[Tuple[float, float]]:
        """Finds the minimum and maximum x positions attained by the contour within a y-range."""
        ...
    def yBoundsAtX(
        self, xleft: float, xright: Optional[float] = ...
    ) -> Optional[Tuple[float, float]]:
        """Finds the minimum and maximum y positions attained by the contour within an x-range."""
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
    def merge(self, pos: Union[int, Tuple[int, ...]]) -> None:
        """Removes the on-curve point a the given position."""
        ...
    def round(self, factor: Optional[float] = ...) -> None:
        """Rounds the x and y coordinates."""
        ...
    def selfIntersects(self) -> bool:
        """Returns whether this contour intersects itself."""
        ...
    def simplify(
        self,
        error_bound: Optional[float] = ...,
        flags: Optional[Tuple[str, ...]] = ...,
        tan_bounds: Optional[Any] = ...,
        linefixup: Optional[Any] = ...,
        linelenmax: Optional[Any] = ...,
    ) -> None:
        """Tries to remove excess points on the contour."""
        ...
    def transform(
        self, matrix: Tuple[float, float, float, float, float, float]
    ) -> None:
        """Transforms the contour by the matrix"""
        ...
    def addInflections(self) -> None:
        """Break the spline so that there will be a point at all points of inflection."""
        ...
    def balance(self) -> None:
        """For all cubic bezier splines of the contour make the line between the control points parallel to the chord."""
        ...
    def harmonize(self) -> None:
        """For all bezier splines of the contour move the smooth on-curve points between its adjacent control points."""
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
