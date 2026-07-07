#!/usr/bin/env python3
"""Generate a professional classroom PowerPoint for
Class XI Computer Science (AHSEC) - Unit 2: Introduction to C++
Part 1: Getting Started.

Run:  python3 build_ppt_getting_started.py
Output: Unit-2-Part-1-Getting-Started.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ----------------------------------------------------------------------------
# THEME / DESIGN CONSTANTS
# ----------------------------------------------------------------------------
NAVY      = RGBColor(0x0B, 0x2A, 0x4A)   # deep navy  (primary)
BLUE      = RGBColor(0x14, 0x5D, 0xA0)   # medium blue
ACCENT    = RGBColor(0xF5, 0x9E, 0x0B)   # amber accent
TEAL      = RGBColor(0x0E, 0x9E, 0x8E)   # teal accent
LIGHT     = RGBColor(0xED, 0xF2, 0xF7)   # light panel
LIGHTER   = RGBColor(0xF7, 0xFA, 0xFC)   # very light panel
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
DARK      = RGBColor(0x1A, 0x20, 0x2C)   # near-black text
GREY      = RGBColor(0x5A, 0x67, 0x78)   # muted text
CODE_BG   = RGBColor(0x11, 0x1B, 0x2B)   # code panel background
CODE_TXT  = RGBColor(0xE6, 0xED, 0xF3)   # code text
CODE_KEY  = RGBColor(0x7C, 0xD9, 0xC8)   # (unused per-token; kept for ref)
OUT_BG    = RGBColor(0x0A, 0x14, 0x0A)   # terminal green-black
OUT_TXT   = RGBColor(0x7C, 0xF7, 0x9E)   # terminal green

FONT      = "Calibri"
FONT_MONO = "Consolas"

SW = Inches(13.333)
SH = Inches(7.5)

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]

TOTAL_SLIDES = 16  # updated after build for footer numbering


# ----------------------------------------------------------------------------
# LOW-LEVEL HELPERS
# ----------------------------------------------------------------------------
def _set_fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_rect(slide, x, y, w, h, color, line=None, line_w=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = line_w or Pt(1)
    shp.shadow.inherit = False
    return shp


def add_round_rect(slide, x, y, w, h, color, line=None, line_w=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    try:
        shp.adjustments[0] = 0.06
    except Exception:
        pass
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = line_w or Pt(1)
    shp.shadow.inherit = False
    return shp


def add_text(slide, x, y, w, h, lines, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, wrap=True):
    """lines: list of dicts {text,size,bold,color,font,space_after,align,level,bullet}"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = Pt(4)
    tf.margin_right = Pt(4)
    tf.margin_top = Pt(2)
    tf.margin_bottom = Pt(2)
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = ln.get("align", align)
        if "space_after" in ln:
            p.space_after = Pt(ln["space_after"])
        if "space_before" in ln:
            p.space_before = Pt(ln["space_before"])
        p.level = ln.get("level", 0)
        run = p.add_run()
        run.text = ln["text"]
        run.font.size = Pt(ln.get("size", 18))
        run.font.bold = ln.get("bold", False)
        run.font.italic = ln.get("italic", False)
        run.font.name = ln.get("font", FONT)
        run.font.color.rgb = ln.get("color", DARK)
    return tb


def _no_autofit(tf):
    # keep font sizes fixed
    pass


# ----------------------------------------------------------------------------
# SLIDE SCAFFOLDING (background, header, footer)
# ----------------------------------------------------------------------------
slide_no = 0


def new_slide():
    global slide_no
    slide_no += 1
    slide = prs.slides.add_slide(BLANK)
    # white base background
    add_rect(slide, 0, 0, SW, SH, WHITE)
    return slide


def add_footer(slide, section="Unit 2 - Introduction to C++  |  Part 1: Getting Started"):
    # bottom accent line
    add_rect(slide, 0, SH - Inches(0.42), SW, Inches(0.42), NAVY)
    add_rect(slide, 0, SH - Inches(0.46), SW, Inches(0.04), ACCENT)
    add_text(slide, Inches(0.45), SH - Inches(0.40), Inches(9.5), Inches(0.38),
             [{"text": section, "size": 10.5, "color": WHITE, "bold": False}],
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, SW - Inches(2.6), SH - Inches(0.40), Inches(2.15), Inches(0.38),
             [{"text": f"Slide {slide_no} / {TOTAL_SLIDES}", "size": 10.5,
               "color": WHITE, "align": PP_ALIGN.RIGHT}],
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)


def add_header(slide, kicker, title):
    """Standard content-slide header band."""
    add_rect(slide, 0, 0, SW, Inches(1.30), NAVY)
    add_rect(slide, 0, Inches(1.30), SW, Inches(0.06), ACCENT)
    # small side tab
    add_rect(slide, 0, 0, Inches(0.18), Inches(1.30), ACCENT)
    add_text(slide, Inches(0.55), Inches(0.16), Inches(11.8), Inches(0.34),
             [{"text": kicker.upper(), "size": 12.5, "bold": True, "color": ACCENT,
               "font": FONT}])
    add_text(slide, Inches(0.52), Inches(0.46), Inches(12.2), Inches(0.78),
             [{"text": title, "size": 27, "bold": True, "color": WHITE}],
             anchor=MSO_ANCHOR.MIDDLE)


def bullets(slide, x, y, w, h, items, size=17, gap=8, color=DARK):
    """items: list of (level, text, bold?) ; bullets drawn with markers."""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, it in enumerate(items):
        lvl, txt = it[0], it[1]
        bold = it[2] if len(it) > 2 else False
        col = it[3] if len(it) > 3 else color
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap)
        p.level = 0
        marker = "•  " if lvl == 0 else "–  "
        indent = "" if lvl == 0 else "      "
        r1 = p.add_run()
        r1.text = indent + marker
        r1.font.size = Pt(size)
        r1.font.name = FONT
        r1.font.bold = True
        r1.font.color.rgb = ACCENT if lvl == 0 else TEAL
        r2 = p.add_run()
        r2.text = txt
        r2.font.size = Pt(size if lvl == 0 else size - 1)
        r2.font.name = FONT
        r2.font.bold = bold
        r2.font.color.rgb = col
    return tb


def code_panel(slide, x, y, w, h, code_lines, title="C++ Program", font_size=13.5):
    add_round_rect(slide, x, y, w, h, CODE_BG)
    # title bar dots
    add_text(slide, x + Inches(0.22), y + Inches(0.10), w - Inches(0.4), Inches(0.3),
             [{"text": "‹/›  " + title, "size": 11.5, "bold": True,
               "color": RGBColor(0x8B, 0xA6, 0xC9), "font": FONT_MONO}])
    tb = slide.shapes.add_textbox(x + Inches(0.24), y + Inches(0.42),
                                  w - Inches(0.44), h - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, ln in enumerate(code_lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(1)
        r = p.add_run()
        r.text = ln if ln else " "
        r.font.name = FONT_MONO
        r.font.size = Pt(font_size)
        r.font.color.rgb = CODE_TXT
    return tb


def output_panel(slide, x, y, w, h, out_lines, title="Output", font_size=13.5):
    add_round_rect(slide, x, y, w, h, OUT_BG)
    add_text(slide, x + Inches(0.22), y + Inches(0.10), w - Inches(0.4), Inches(0.3),
             [{"text": "▷  " + title, "size": 11.5, "bold": True,
               "color": RGBColor(0x5A, 0xC0, 0x74), "font": FONT_MONO}])
    tb = slide.shapes.add_textbox(x + Inches(0.24), y + Inches(0.42),
                                  w - Inches(0.44), h - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, ln in enumerate(out_lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(1)
        r = p.add_run()
        r.text = ln if ln else " "
        r.font.name = FONT_MONO
        r.font.size = Pt(font_size)
        r.font.color.rgb = OUT_TXT
    return tb


def panel_heading(slide, x, y, w, text, color=BLUE, size=15):
    add_round_rect(slide, x, y, w, Inches(0.42), color)
    add_text(slide, x, y, w, Inches(0.42),
             [{"text": text, "size": size, "bold": True, "color": WHITE,
               "align": PP_ALIGN.CENTER}],
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)


def make_table(slide, x, y, w, h, data, col_widths=None, header=True,
               font=11.5, header_font=12):
    rows = len(data)
    cols = len(data[0])
    gtab = slide.shapes.add_table(rows, cols, x, y, w, h).table
    # style: turn off default banding via first row/col flags
    gtab.first_row = False
    gtab.horz_banding = False
    if col_widths:
        for ci, cw in enumerate(col_widths):
            gtab.columns[ci].width = cw
    for r in range(rows):
        for c in range(cols):
            cell = gtab.cell(r, c)
            cell.margin_left = Pt(6)
            cell.margin_right = Pt(6)
            cell.margin_top = Pt(3)
            cell.margin_bottom = Pt(3)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if header and r == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHTER if (r % 2 == 1) else LIGHT
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = str(data[r][c])
            run.font.name = FONT
            if header and r == 0:
                run.font.size = Pt(header_font)
                run.font.bold = True
                run.font.color.rgb = WHITE
            else:
                run.font.size = Pt(font)
                run.font.color.rgb = DARK
                run.font.bold = (c == 0)
    return gtab


# ============================================================================
# SLIDE 1 — TITLE
# ============================================================================
s = new_slide()
add_rect(s, 0, 0, SW, SH, NAVY)
# decorative bands
add_rect(s, 0, 0, SW, Inches(0.22), ACCENT)
add_rect(s, 0, SH - Inches(0.22), SW, Inches(0.22), ACCENT)
# right decorative panel
add_rect(s, SW - Inches(4.4), 0, Inches(4.4), SH, BLUE)
add_rect(s, SW - Inches(4.5), 0, Inches(0.10), SH, ACCENT)
# big code glyph on the right
add_text(s, SW - Inches(4.4), Inches(2.3), Inches(4.4), Inches(2.6),
         [{"text": "C++", "size": 120, "bold": True, "color": WHITE,
           "align": PP_ALIGN.CENTER}],
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
add_text(s, SW - Inches(4.4), Inches(4.7), Inches(4.4), Inches(0.6),
         [{"text": "cout << \"Hello, World\";", "size": 15,
           "color": RGBColor(0xBFD6EE if False else 0xBF, 0xD6, 0xEE),
           "font": FONT_MONO, "align": PP_ALIGN.CENTER}],
         align=PP_ALIGN.CENTER)
# left title text
add_text(s, Inches(0.7), Inches(1.5), Inches(8.0), Inches(0.5),
         [{"text": "CLASS XI  •  COMPUTER SCIENCE", "size": 15, "bold": True,
           "color": ACCENT}])
add_text(s, Inches(0.66), Inches(2.15), Inches(8.2), Inches(2.0),
         [{"text": "Unit 2: Introduction to C++", "size": 40, "bold": True,
           "color": WHITE, "space_after": 6},
          {"text": "Part 1 — Getting Started", "size": 30, "bold": True,
           "color": RGBColor(0x9E, 0xC5, 0xE8)}])
add_text(s, Inches(0.7), Inches(4.6), Inches(8.0), Inches(1.4),
         [{"text": "A first look at programming with C++", "size": 17,
           "italic": True, "color": RGBColor(0xCF, 0xDD, 0xEC), "space_after": 14},
          {"text": "Assam Higher Secondary First Year (AHSEC)", "size": 14,
           "color": RGBColor(0xB9, 0xCA, 0xDD)},
          {"text": "For students learning programming for the very first time",
           "size": 13, "color": RGBColor(0x9F, 0xB4, 0xCB)}])

# ============================================================================
# SLIDE 2 — LEARNING OBJECTIVES
# ============================================================================
s = new_slide()
add_header(s, "Lesson Roadmap", "What You Will Learn Today")
left = bullets(s, Inches(0.6), Inches(1.7), Inches(6.0), Inches(5.0),
    [(0, "What C++ is, and a short history"),
     (0, "The C++ character set"),
     (0, "Tokens: identifiers, keywords, constants, operators"),
     (0, "Structure of a C++ program"),
     (0, "Header files: iostream.h and iomanip.h"),
    ], size=17, gap=13)
right = bullets(s, Inches(6.9), Inches(1.7), Inches(6.0), Inches(5.0),
    [(0, "Output with cout and input with cin"),
     (0, "Operators << and >>, endl, setw()"),
     (0, "Cascading of input / output operators"),
     (0, "Editor, Compilation, Linking, Execution"),
     (0, "Types of error messages"),
    ], size=17, gap=13)
# objective banner
add_round_rect(s, Inches(0.6), Inches(6.15), Inches(12.1), Inches(0.62), LIGHT)
add_text(s, Inches(0.8), Inches(6.15), Inches(11.8), Inches(0.62),
         [{"text": "Goal:  By the end, you will be able to read, write and run a "
                   "simple C++ program with confidence.",
           "size": 14.5, "bold": True, "color": NAVY}],
         anchor=MSO_ANCHOR.MIDDLE)
add_footer(s)

# ============================================================================
# SLIDE 3 — INTRODUCTION TO C++
# ============================================================================
s = new_slide()
add_header(s, "Topic 1", "Introduction to C++")
add_round_rect(s, Inches(0.6), Inches(1.6), Inches(7.3), Inches(0.95), LIGHT)
add_text(s, Inches(0.85), Inches(1.6), Inches(6.9), Inches(0.95),
         [{"text": "C++ is a high-level, general-purpose programming language "
                   "used to write instructions for a computer.",
           "size": 15.5, "bold": True, "color": NAVY}],
         anchor=MSO_ANCHOR.MIDDLE)
bullets(s, Inches(0.6), Inches(2.8), Inches(7.4), Inches(3.6),
    [(0, "Developed by Bjarne Stroustrup at Bell Labs, USA."),
     (0, "First created in 1979; named \"C++\" in 1983."),
     (0, "Old name was \"C with Classes\"."),
     (0, "C++ is an extension (superset) of the C language."),
     (0, "The ++ means \"one more than C\" (C incremented)."),
     (0, "Used for games, apps, browsers and system software."),
    ], size=15.5, gap=10)
# fact card
add_round_rect(s, Inches(8.35), Inches(1.6), Inches(4.35), Inches(4.7), NAVY)
add_rect(s, Inches(8.35), Inches(1.6), Inches(4.35), Inches(0.5), BLUE)
add_text(s, Inches(8.35), Inches(1.6), Inches(4.35), Inches(0.5),
         [{"text": "QUICK FACTS", "size": 14, "bold": True, "color": WHITE,
           "align": PP_ALIGN.CENTER}], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
add_text(s, Inches(8.6), Inches(2.25), Inches(3.9), Inches(4.0),
    [{"text": "Creator", "size": 12.5, "bold": True, "color": ACCENT, "space_after": 0},
     {"text": "Bjarne Stroustrup", "size": 15, "bold": True, "color": WHITE, "space_after": 10},
     {"text": "Year", "size": 12.5, "bold": True, "color": ACCENT, "space_after": 0},
     {"text": "1979 (named 1983)", "size": 15, "bold": True, "color": WHITE, "space_after": 10},
     {"text": "Place", "size": 12.5, "bold": True, "color": ACCENT, "space_after": 0},
     {"text": "Bell Laboratories, USA", "size": 15, "bold": True, "color": WHITE, "space_after": 10},
     {"text": "Based on", "size": 12.5, "bold": True, "color": ACCENT, "space_after": 0},
     {"text": "The C language", "size": 15, "bold": True, "color": WHITE}])
add_footer(s)

# ============================================================================
# SLIDE 4 — C++ CHARACTER SET
# ============================================================================
s = new_slide()
add_header(s, "Topic 2", "The C++ Character Set")
add_text(s, Inches(0.6), Inches(1.55), Inches(12.1), Inches(0.55),
         [{"text": "Character set = the complete group of characters that C++ "
                   "understands and lets us use in a program.",
           "size": 15, "italic": True, "color": GREY}])
make_table(s, Inches(0.6), Inches(2.25), Inches(12.1), Inches(3.0),
    [["Category", "Characters Allowed"],
     ["Letters", "A - Z  (capital)   and   a - z  (small)"],
     ["Digits", "0  1  2  3  4  5  6  7  8  9"],
     ["Special Symbols", "+  -  *  /  %  =  < >  ( )  { }  [ ]  ;  ,  .  \"  '  #  &  |  _"],
     ["White Spaces", "Blank space, Tab, New line (Enter)"]],
    col_widths=[Inches(3.0), Inches(9.1)], font=14, header_font=14)
add_round_rect(s, Inches(0.6), Inches(5.5), Inches(12.1), Inches(1.1), LIGHT)
bullets(s, Inches(0.85), Inches(5.6), Inches(11.7), Inches(1.0),
    [(0, "C++ is case-sensitive:  'A' and 'a' are treated as different."),
     (0, "White spaces separate words but are ignored during execution."),
    ], size=14, gap=4, color=NAVY)
add_footer(s)

# ============================================================================
# SLIDE 5 — C++ TOKENS (OVERVIEW)
# ============================================================================
s = new_slide()
add_header(s, "Topic 3", "C++ Tokens — The Building Blocks")
add_text(s, Inches(0.6), Inches(1.5), Inches(12.1), Inches(0.5),
         [{"text": "A token is the smallest individual (meaningful) unit of a "
                   "C++ program.", "size": 15, "italic": True, "color": GREY}])
cards = [
    ("1", "Keywords", "Reserved words\nint, float, if", NAVY),
    ("2", "Identifiers", "Names we give\nsum, marks", BLUE),
    ("3", "Constants", "Fixed values\n10, 3.14, 'A'", TEAL),
    ("4", "Operators", "Action symbols\n+  -  *  /  =", ACCENT),
    ("5", "Punctuators", "Separators\n;   { }   ( )", GREY),
]
cw = Inches(2.28)
gap = Inches(0.18)
x0 = Inches(0.6)
for i, (num, head, body, col) in enumerate(cards):
    x = x0 + i * (cw + gap)
    add_round_rect(s, x, Inches(2.15), cw, Inches(2.55), col)
    add_text(s, x, Inches(2.28), cw, Inches(0.6),
             [{"text": num, "size": 30, "bold": True, "color": WHITE,
               "align": PP_ALIGN.CENTER}], align=PP_ALIGN.CENTER)
    add_text(s, x, Inches(2.98), cw, Inches(0.45),
             [{"text": head, "size": 15.5, "bold": True, "color": WHITE,
               "align": PP_ALIGN.CENTER}], align=PP_ALIGN.CENTER)
    add_text(s, x + Inches(0.1), Inches(3.5), cw - Inches(0.2), Inches(1.1),
             [{"text": body, "size": 12.5, "color": WHITE,
               "align": PP_ALIGN.CENTER}], align=PP_ALIGN.CENTER)
# example strip
add_round_rect(s, Inches(0.6), Inches(5.0), Inches(12.1), Inches(1.55), LIGHT)
add_text(s, Inches(0.85), Inches(5.1), Inches(11.6), Inches(0.4),
         [{"text": "Example — every part of  int sum = a + b;  is a token:",
           "size": 14.5, "bold": True, "color": NAVY}])
bullets(s, Inches(0.95), Inches(5.55), Inches(11.5), Inches(1.0),
    [(0, "int → keyword    •    sum, a, b → identifiers"),
     (0, "= , + → operators    •    ; → punctuator"),
    ], size=13.5, gap=3, color=DARK)
add_footer(s)

# ============================================================================
# SLIDE 6 — IDENTIFIERS & KEYWORDS
# ============================================================================
s = new_slide()
add_header(s, "Tokens in Detail", "Identifiers & Keywords")
panel_heading(s, Inches(0.6), Inches(1.55), Inches(6.0), "IDENTIFIERS  (names we create)", BLUE)
bullets(s, Inches(0.6), Inches(2.1), Inches(6.0), Inches(2.4),
    [(0, "Must begin with a letter or underscore _"),
     (0, "May contain letters, digits, underscore"),
     (0, "No blank spaces, no special symbols"),
     (0, "A keyword cannot be an identifier"),
    ], size=13.5, gap=6)
make_table(s, Inches(0.6), Inches(4.25), Inches(6.0), Inches(1.9),
    [["Valid", "Invalid"],
     ["total", "2total"],
     ["_marks", "my marks"],
     ["roll_no", "sum-1"]],
    col_widths=[Inches(3.0), Inches(3.0)], font=12.5, header_font=13)

panel_heading(s, Inches(6.9), Inches(1.55), Inches(5.8), "KEYWORDS  (reserved words)", NAVY)
bullets(s, Inches(6.9), Inches(2.1), Inches(5.8), Inches(2.4),
    [(0, "Meaning is already fixed in C++"),
     (0, "Always written in lower case"),
     (0, "Cannot be used as variable names"),
    ], size=13.5, gap=6)
make_table(s, Inches(6.9), Inches(4.0), Inches(5.8), Inches(2.15),
    [["Common Keywords", "", ""],
     ["int", "float", "char"],
     ["if", "else", "for"],
     ["void", "const", "long"],
     ["return", "double", "while"]],
    col_widths=[Inches(1.93), Inches(1.93), Inches(1.93)], font=12.5, header_font=13)
add_footer(s)

# ============================================================================
# SLIDE 7 — CONSTANTS & OPERATORS
# ============================================================================
s = new_slide()
add_header(s, "Tokens in Detail", "Constants & Operators")
panel_heading(s, Inches(0.6), Inches(1.55), Inches(6.0), "CONSTANTS  (fixed values)", TEAL)
make_table(s, Inches(0.6), Inches(2.1), Inches(6.0), Inches(2.5),
    [["Type", "Example"],
     ["Integer", "10 , -45 , 0"],
     ["Floating point", "3.14 , -0.5"],
     ["Character", "'A' , '5'  (single quotes)"],
     ["String", "\"Hello\"  (double quotes)"]],
    col_widths=[Inches(2.4), Inches(3.6)], font=12.5, header_font=13)
add_round_rect(s, Inches(0.6), Inches(4.8), Inches(6.0), Inches(1.4), LIGHT)
add_text(s, Inches(0.8), Inches(4.9), Inches(5.7), Inches(1.3),
    [{"text": "Remember the quotes!", "size": 13.5, "bold": True, "color": NAVY,
      "space_after": 4},
     {"text": "'A'  →  one character", "size": 13, "color": DARK, "font": FONT_MONO,
      "space_after": 2},
     {"text": "\"A\"  →  a string", "size": 13, "color": DARK, "font": FONT_MONO}])

panel_heading(s, Inches(6.9), Inches(1.55), Inches(5.8), "OPERATORS  (action symbols)", ACCENT)
make_table(s, Inches(6.9), Inches(2.1), Inches(5.8), Inches(2.9),
    [["Type", "Symbols"],
     ["Arithmetic", "+  -  *  /  %"],
     ["Relational", "<  >  <=  >=  ==  !="],
     ["Logical", "&&   ||   !"],
     ["Assignment", "="],
     ["Increment / Decrement", "++   --"]],
    col_widths=[Inches(2.7), Inches(3.1)], font=12, header_font=13)
add_round_rect(s, Inches(6.9), Inches(5.2), Inches(5.8), Inches(1.0), LIGHT)
add_text(s, Inches(7.1), Inches(5.2), Inches(5.5), Inches(1.0),
    [{"text": "An operator works on operands.\nIn a + b, the + is the operator; "
              "a and b are operands.", "size": 12.5, "color": NAVY}],
    anchor=MSO_ANCHOR.MIDDLE)
add_footer(s)

# ============================================================================
# SLIDE 8 — STRUCTURE OF A C++ PROGRAM
# ============================================================================
s = new_slide()
add_header(s, "Topic 4", "Structure of a C++ Program")
code_panel(s, Inches(0.6), Inches(1.65), Inches(6.7), Inches(3.7),
    ["#include<iostream.h>   // header file",
     "",
     "void main()            // main function",
     "{",
     "    cout << \"Hello\";    // statement",
     "}"],
    title="Basic Skeleton", font_size=15)
bullets(s, Inches(7.55), Inches(1.7), Inches(5.15), Inches(3.7),
    [(0, "Header file", True), (1, "brings in ready-made features (cout, cin)"),
     (0, "main() function", True), (1, "execution ALWAYS starts here"),
     (0, "Braces { }", True), (1, "mark the start and end of the body"),
     (0, "Statements", True), (1, "instructions ending with a semicolon ;"),
    ], size=14, gap=5)
add_round_rect(s, Inches(0.6), Inches(5.55), Inches(12.1), Inches(1.05), NAVY)
add_text(s, Inches(0.85), Inches(5.6), Inches(11.6), Inches(1.0),
    [{"text": "Golden rules:  every program needs main() • each statement ends "
              "with ;  • the #include line has NO semicolon.",
      "size": 14.5, "bold": True, "color": WHITE}], anchor=MSO_ANCHOR.MIDDLE)
add_footer(s)

# ============================================================================
# SLIDE 9 — HEADER FILES
# ============================================================================
s = new_slide()
add_header(s, "Topic 5", "Header Files")
add_text(s, Inches(0.6), Inches(1.5), Inches(12.1), Inches(0.5),
         [{"text": "A header file contains ready-made functions we can use by "
                   "writing #include at the top of the program.",
           "size": 15, "italic": True, "color": GREY}])
# two big cards
add_round_rect(s, Inches(0.6), Inches(2.25), Inches(5.9), Inches(3.3), NAVY)
add_rect(s, Inches(0.6), Inches(2.25), Inches(5.9), Inches(0.62), BLUE)
add_text(s, Inches(0.6), Inches(2.25), Inches(5.9), Inches(0.62),
         [{"text": "iostream.h", "size": 19, "bold": True, "color": WHITE,
           "font": FONT_MONO, "align": PP_ALIGN.CENTER}],
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
add_text(s, Inches(0.9), Inches(3.05), Inches(5.3), Inches(2.4),
    [{"text": "input – output stream", "size": 14, "italic": True,
      "color": ACCENT, "space_after": 8},
     {"text": "Used for input and output.", "size": 14.5, "color": WHITE, "space_after": 6},
     {"text": "Contains:  cin , cout , << , >> , endl", "size": 14, "color": WHITE,
      "font": FONT_MONO}])

add_round_rect(s, Inches(6.8), Inches(2.25), Inches(5.9), Inches(3.3), TEAL)
add_rect(s, Inches(6.8), Inches(2.25), Inches(5.9), Inches(0.62), RGBColor(0x0B, 0x7A, 0x6E))
add_text(s, Inches(6.8), Inches(2.25), Inches(5.9), Inches(0.62),
         [{"text": "iomanip.h", "size": 19, "bold": True, "color": WHITE,
           "font": FONT_MONO, "align": PP_ALIGN.CENTER}],
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
add_text(s, Inches(7.1), Inches(3.05), Inches(5.3), Inches(2.4),
    [{"text": "input – output manipulation", "size": 14, "italic": True,
      "color": RGBColor(0x0B, 0x2A, 0x2A), "space_after": 8},
     {"text": "Used to format the output.", "size": 14.5, "color": WHITE, "space_after": 6},
     {"text": "Contains:  setw() , setprecision()", "size": 14, "color": WHITE,
      "font": FONT_MONO}])
add_round_rect(s, Inches(0.6), Inches(5.75), Inches(12.1), Inches(0.72), LIGHT)
add_text(s, Inches(0.85), Inches(5.75), Inches(11.6), Inches(0.72),
    [{"text": "Tip:  cout / cin need iostream.h   •   setw() needs iomanip.h   •   "
              "the #include line has no ;", "size": 13.5, "bold": True, "color": NAVY}],
    anchor=MSO_ANCHOR.MIDDLE)
add_footer(s)

# ============================================================================
# SLIDE 10 — OUTPUT: cout & <<
# ============================================================================
s = new_slide()
add_header(s, "Topic 6", "Output using  cout  and  <<")
bullets(s, Inches(0.6), Inches(1.65), Inches(5.7), Inches(3.4),
    [(0, "cout (\"see-out\") sends output to the screen."),
     (0, "It uses the insertion operator  <<"),
     (0, "Text must be inside double quotes \" \""),
     (0, "Defined in iostream.h"),
     (0, "Arrow trick: cout <<  data flows OUT to screen"),
    ], size=15, gap=10)
code_panel(s, Inches(6.55), Inches(1.65), Inches(6.15), Inches(2.55),
    ["#include<iostream.h>",
     "void main()",
     "{",
     "    cout << \"Total marks = \";",
     "    cout << 95;",
     "}"], title="cout example", font_size=13.5)
output_panel(s, Inches(6.55), Inches(4.35), Inches(6.15), Inches(1.1),
    ["Total marks = 95"], font_size=14)
add_round_rect(s, Inches(0.6), Inches(5.4), Inches(5.7), Inches(1.05), LIGHT)
add_text(s, Inches(0.8), Inches(5.4), Inches(5.4), Inches(1.05),
    [{"text": "Common mistake:", "size": 13, "bold": True, "color": ACCENT,
      "space_after": 3},
     {"text": "cout uses <<  (not >>).  Do not forget the double quotes around text.",
      "size": 13, "color": NAVY}], anchor=MSO_ANCHOR.MIDDLE)
add_footer(s)

# ============================================================================
# SLIDE 11 — INPUT: cin & >>
# ============================================================================
s = new_slide()
add_header(s, "Topic 7", "Input using  cin  and  >>")
bullets(s, Inches(0.6), Inches(1.65), Inches(5.7), Inches(3.4),
    [(0, "cin (\"see-in\") reads input from the keyboard."),
     (0, "It uses the extraction operator  >>"),
     (0, "The value is stored in a variable."),
     (0, "Defined in iostream.h"),
     (0, "Arrow trick: cin >>  data flows IN to variable"),
    ], size=15, gap=10)
code_panel(s, Inches(6.55), Inches(1.65), Inches(6.15), Inches(2.85),
    ["#include<iostream.h>",
     "void main()",
     "{",
     "    int age;",
     "    cout << \"Enter age: \";",
     "    cin >> age;",
     "    cout << \"Your age is \" << age;",
     "}"], title="cin example", font_size=13)
output_panel(s, Inches(6.55), Inches(4.6), Inches(6.15), Inches(1.15),
    ["Enter age: 16", "Your age is 16"], font_size=13.5)
add_round_rect(s, Inches(0.6), Inches(5.4), Inches(5.7), Inches(1.05), LIGHT)
add_text(s, Inches(0.8), Inches(5.4), Inches(5.4), Inches(1.05),
    [{"text": "Remember:", "size": 13, "bold": True, "color": ACCENT,
      "space_after": 3},
     {"text": "cin uses >>  and always stores the value into a variable.",
      "size": 13, "color": NAVY}], anchor=MSO_ANCHOR.MIDDLE)
add_footer(s)

# ============================================================================
# SLIDE 12 — endl, setw(), CASCADING
# ============================================================================
s = new_slide()
add_header(s, "Topic 8", "endl, setw() and Cascading")
panel_heading(s, Inches(0.6), Inches(1.55), Inches(3.8), "endl", BLUE)
add_text(s, Inches(0.6), Inches(2.05), Inches(3.8), Inches(1.9),
    [{"text": "Moves the cursor to a new line.", "size": 13, "color": DARK,
      "space_after": 5},
     {"text": "Works like \\n.", "size": 13, "color": DARK, "space_after": 5},
     {"text": "cout<<\"A\"<<endl<<\"B\";", "size": 12, "color": NAVY, "font": FONT_MONO}])

panel_heading(s, Inches(4.65), Inches(1.55), Inches(3.8), "setw(n)", TEAL)
add_text(s, Inches(4.65), Inches(2.05), Inches(3.8), Inches(1.9),
    [{"text": "Sets field width for the next value.", "size": 13, "color": DARK,
      "space_after": 5},
     {"text": "Needs iomanip.h", "size": 13, "color": DARK, "space_after": 5},
     {"text": "Value shifts to the right.", "size": 13, "color": DARK}])

panel_heading(s, Inches(8.7), Inches(1.55), Inches(4.0), "Cascading", ACCENT)
add_text(s, Inches(8.7), Inches(2.05), Inches(4.0), Inches(1.9),
    [{"text": "Using << or >> many times in one statement.", "size": 13,
      "color": DARK, "space_after": 5},
     {"text": "Makes code short & clear.", "size": 13, "color": DARK}])

code_panel(s, Inches(0.6), Inches(4.0), Inches(6.0), Inches(2.4),
    ["cout << setw(6) << 5 << endl;",
     "cout << setw(6) << 100 << endl;",
     "",
     "cin  >> a >> b;      // cascaded input",
     "cout << \"Sum=\" << a+b; // cascaded output"],
    title="Examples", font_size=13)
output_panel(s, Inches(6.75), Inches(4.0), Inches(5.95), Inches(2.4),
    ["     5", "   100", "", "(a and b are read together,", " then the sum is shown)"],
    font_size=13)
add_footer(s)

# ============================================================================
# SLIDE 13 — FIRST COMPLETE PROGRAM
# ============================================================================
s = new_slide()
add_header(s, "Putting It Together", "Your First Complete C++ Program")
code_panel(s, Inches(0.6), Inches(1.65), Inches(7.2), Inches(4.5),
    ["#include<iostream.h>",
     "void main()",
     "{",
     "    int a, b, sum;",
     "    cout << \"Enter two numbers: \";",
     "    cin  >> a >> b;",
     "    sum = a + b;",
     "    cout << \"Sum = \" << sum << endl;",
     "}"], title="add_two_numbers.cpp", font_size=14)
output_panel(s, Inches(8.05), Inches(1.65), Inches(4.65), Inches(1.9),
    ["Enter two numbers: 4 6", "Sum = 10"], font_size=13.5)
add_round_rect(s, Inches(8.05), Inches(3.75), Inches(4.65), Inches(2.4), LIGHT)
add_text(s, Inches(8.3), Inches(3.85), Inches(4.2), Inches(2.3),
    [{"text": "How it works", "size": 14, "bold": True, "color": NAVY, "space_after": 6},
     {"text": "1.  Declare variables a, b, sum", "size": 12.5, "color": DARK, "space_after": 4},
     {"text": "2.  cin reads two numbers", "size": 12.5, "color": DARK, "space_after": 4},
     {"text": "3.  Add them into sum", "size": 12.5, "color": DARK, "space_after": 4},
     {"text": "4.  cout shows the result", "size": 12.5, "color": DARK}])
add_footer(s)

# ============================================================================
# SLIDE 14 — HOW A PROGRAM RUNS (4 STAGES)
# ============================================================================
s = new_slide()
add_header(s, "Topic 9", "How a Program Runs: 4 Stages")
stages = [
    ("EDITOR", "Type & save the\nsource code", ".cpp", NAVY),
    ("COMPILATION", "Compiler turns it\ninto object code", ".obj", BLUE),
    ("LINKING", "Linker joins library\nto make .exe", ".exe", TEAL),
    ("EXECUTION", "Run the file and\nsee the output", "Output", ACCENT),
]
cw = Inches(2.75)
gap = Inches(0.30)
x0 = Inches(0.6)
y = Inches(2.0)
for i, (head, body, tag, col) in enumerate(stages):
    x = x0 + i * (cw + gap)
    add_round_rect(s, x, y, cw, Inches(2.7), col)
    add_text(s, x, y + Inches(0.18), cw, Inches(0.5),
             [{"text": f"STEP {i+1}", "size": 12, "bold": True,
               "color": RGBColor(0xFF, 0xE3, 0xB0), "align": PP_ALIGN.CENTER}],
             align=PP_ALIGN.CENTER)
    add_text(s, x, y + Inches(0.6), cw, Inches(0.5),
             [{"text": head, "size": 16.5, "bold": True, "color": WHITE,
               "align": PP_ALIGN.CENTER}], align=PP_ALIGN.CENTER)
    add_text(s, x + Inches(0.1), y + Inches(1.15), cw - Inches(0.2), Inches(1.0),
             [{"text": body, "size": 12.5, "color": WHITE,
               "align": PP_ALIGN.CENTER}], align=PP_ALIGN.CENTER)
    add_text(s, x, y + Inches(2.2), cw, Inches(0.4),
             [{"text": tag, "size": 12.5, "bold": True,
               "color": RGBColor(0x0B, 0x1B, 0x2B) if col == ACCENT else RGBColor(0xCB, 0xE3, 0xF7),
               "align": PP_ALIGN.CENTER, "font": FONT_MONO}], align=PP_ALIGN.CENTER)
    if i < 3:
        add_text(s, x + cw - Inches(0.02), y + Inches(1.0), gap + Inches(0.1), Inches(0.6),
                 [{"text": "➜", "size": 22, "bold": True, "color": GREY,
                   "align": PP_ALIGN.CENTER}], align=PP_ALIGN.CENTER)
add_round_rect(s, Inches(0.6), Inches(5.4), Inches(12.1), Inches(1.0), LIGHT)
add_text(s, Inches(0.85), Inches(5.4), Inches(11.6), Inches(1.0),
    [{"text": "Order to remember:  Editor  →  Compilation  →  Linking  →  Execution",
      "size": 15.5, "bold": True, "color": NAVY, "align": PP_ALIGN.CENTER}],
    anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
add_footer(s)

# ============================================================================
# SLIDE 15 — ERROR MESSAGES
# ============================================================================
s = new_slide()
add_header(s, "Topic 10", "Error Messages")
add_text(s, Inches(0.6), Inches(1.5), Inches(12.1), Inches(0.5),
         [{"text": "An error message is shown by the compiler when there is a "
                   "mistake in the program.", "size": 15, "italic": True,
           "color": GREY}])
make_table(s, Inches(0.6), Inches(2.2), Inches(12.1), Inches(2.6),
    [["Type of Error", "Meaning", "Example"],
     ["Syntax Error", "Breaking a grammar rule of C++", "missing ; or }"],
     ["Logical Error", "Program runs but gives wrong output (no message!)",
      "using + instead of *"],
     ["Run-time Error", "Error while the program is running", "division by zero"]],
    col_widths=[Inches(2.7), Inches(6.0), Inches(3.4)], font=13, header_font=13.5)
add_round_rect(s, Inches(0.6), Inches(5.05), Inches(12.1), Inches(1.4), LIGHT)
bullets(s, Inches(0.85), Inches(5.15), Inches(11.6), Inches(1.3),
    [(0, "Syntax errors are caught by the compiler before running."),
     (0, "Logical errors are hardest — the program runs but the answer is wrong."),
     (0, "A program that compiles is not always correct!"),
    ], size=13.5, gap=4, color=NAVY)
add_footer(s)

# ============================================================================
# SLIDE 16 — SUMMARY / KEY TAKEAWAYS
# ============================================================================
s = new_slide()
add_rect(s, 0, 0, SW, SH, NAVY)
add_rect(s, 0, 0, SW, Inches(0.22), ACCENT)
add_rect(s, 0, 0, Inches(0.20), SH, ACCENT)
add_text(s, Inches(0.6), Inches(0.45), Inches(12), Inches(0.9),
         [{"text": "Key Takeaways", "size": 32, "bold": True, "color": WHITE}])
add_rect(s, Inches(0.62), Inches(1.35), Inches(3.0), Inches(0.06), ACCENT)
left = [
    "C++ → Bjarne Stroustrup, 1979, Bell Labs.",
    "5 tokens: keyword, identifier, constant, operator, punctuator.",
    "Execution always begins from main().",
    "cout << (output) and cin >> (input) need iostream.h.",
]
right = [
    "setw() needs iomanip.h;  endl and \\n → new line.",
    "'A' is a character;  \"A\" is a string.",
    "Stages: Editor → Compilation → Linking → Execution.",
    "Errors: syntax, logical, run-time.",
]
def summary_col(x, items):
    tb = s.shapes.add_textbox(x, Inches(1.75), Inches(5.9), Inches(4.6))
    tf = tb.text_frame; tf.word_wrap = True
    for i, t in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(16)
        r1 = p.add_run(); r1.text = "▸  "
        r1.font.size = Pt(16); r1.font.bold = True; r1.font.color.rgb = ACCENT; r1.font.name = FONT
        r2 = p.add_run(); r2.text = t
        r2.font.size = Pt(15.5); r2.font.color.rgb = WHITE; r2.font.name = FONT
summary_col(Inches(0.7), left)
summary_col(Inches(6.9), right)
add_round_rect(s, Inches(0.7), Inches(6.15), Inches(11.9), Inches(0.7), BLUE)
add_text(s, Inches(0.7), Inches(6.15), Inches(11.9), Inches(0.7),
    [{"text": "Next: Part 2 — Data Types, Variables and Constants",
      "size": 15, "bold": True, "color": WHITE, "align": PP_ALIGN.CENTER}],
    anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

# ----------------------------------------------------------------------------
# Fix footer slide-count now that build is complete
# ----------------------------------------------------------------------------
prs.save("Unit-2-Part-1-Getting-Started.pptx")
print("Saved Unit-2-Part-1-Getting-Started.pptx with", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
