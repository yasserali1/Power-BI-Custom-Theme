"""
Fix GitHub Markdown Rendering
==============================
GitHub strips data: URIs, inline styles, and onclick handlers from Markdown.
This script converts all those elements to GitHub-compatible alternatives:

1. Base64 SVG icons (16x16) → saved as .svg files, referenced with relative paths
2. Base64 color swatches (120x40) → placehold.co external URLs
3. Base64 color boxes (12x12) → placehold.co external URLs
4. Styled <summary> tags → clean <summary> without style attr
5. Expand/Collapse buttons → removed (onclick doesn't work on GitHub)
6. Styled <div> dividers → Markdown ---
"""

import re
import base64
import os

# --- Configuration ---
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILE = os.path.join(REPO_DIR, "Power BI Theme Guide.md")
ICONS_DIR = os.path.join(REPO_DIR, "icons")

# --- Step 1: Read the file ---
with open(MD_FILE, "r", encoding="utf-8") as f:
    content = f.read()

print(f"Read {len(content)} chars from: {MD_FILE}")

# --- Step 2: Extract and save SVG icons ---
os.makedirs(ICONS_DIR, exist_ok=True)

# Match icon <img> tags: width="16" height="16" with non-hex alt text
icon_pattern = re.compile(
    r'<img\s+src="data:image/svg\+xml;base64,([^"]+)"\s+alt="([^#][^"]*)"\s+width="16"\s+height="16"\s*/?>',
    re.IGNORECASE
)

# Build a map of alt_text -> filename
icon_map = {}
saved_icons = set()

def slugify(text):
    """Convert alt text to a kebab-case filename."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

# First pass: find all unique icons and save them
for match in icon_pattern.finditer(content):
    b64_data = match.group(1)
    alt_text = match.group(2)
    
    if alt_text in icon_map:
        continue  # Already saved
    
    slug = slugify(alt_text)
    filename = f"{slug}.svg"
    filepath = os.path.join(ICONS_DIR, filename)
    
    try:
        svg_bytes = base64.b64decode(b64_data)
        with open(filepath, "wb") as f:
            f.write(svg_bytes)
        icon_map[alt_text] = filename
        saved_icons.add(alt_text)
        print(f"  Saved icon: {filename} (alt='{alt_text}')")
    except Exception as e:
        print(f"  ERROR saving icon '{alt_text}': {e}")

print(f"\nTotal icons saved: {len(icon_map)}")

# --- Step 3: Replace icon <img> tags with relative paths ---
def replace_icon(match):
    alt_text = match.group(2)
    if alt_text in icon_map:
        filename = icon_map[alt_text]
        return f'<img src="icons/{filename}" alt="{alt_text}" width="16" height="16" />'
    return match.group(0)  # Keep unchanged if not mapped

content, icon_count = icon_pattern.subn(replace_icon, content)
print(f"Replaced {icon_count} icon references with relative paths")

# --- Step 4: Replace color swatches (120x40) with placehold.co URLs ---
swatch_pattern = re.compile(
    r'<img\s+src="data:image/svg\+xml;base64,[^"]+"\s+alt="(#[0-9A-Fa-f]{6})"\s+width="120"\s+height="40"\s*/?>',
    re.IGNORECASE
)

def replace_swatch(match):
    hex_color = match.group(1).lstrip('#')
    return f'<img src="https://placehold.co/120x40/{hex_color}/{hex_color}.png" alt="#{hex_color}" width="120" height="40" />'

content, swatch_count = swatch_pattern.subn(replace_swatch, content)
print(f"Replaced {swatch_count} color swatches (120x40) with placehold.co URLs")

# --- Step 5: Replace color boxes (12x12) with placehold.co URLs ---
# These appear as: <img src="data:..." alt="#HEX" width="12" height="12" />#HEX
box_pattern = re.compile(
    r'<img\s+src="data:image/svg\+xml;base64,[^"]+"\s+alt="(#[0-9A-Fa-f]{6})"\s+width="12"\s+height="12"\s*/?>',
    re.IGNORECASE
)

def replace_box(match):
    hex_color = match.group(1).lstrip('#')
    return f'<img src="https://placehold.co/12x12/{hex_color}/{hex_color}.png" alt="#{hex_color}" width="12" height="12" />'

content, box_count = box_pattern.subn(replace_box, content)
print(f"Replaced {box_count} color boxes (12x12) with placehold.co URLs")

# --- Step 6: Clean styled <summary> tags ---
# Remove style="..." from <summary> tags (GitHub strips them anyway)
summary_pattern = re.compile(
    r'<summary\s+style="[^"]*">',
    re.IGNORECASE
)

content, summary_count = summary_pattern.subn('<summary>', content)
print(f"Cleaned {summary_count} styled <summary> tags")

# --- Step 7: Remove Expand All / Collapse All buttons ---
# These use onclick which GitHub strips; they're non-functional
button_block_pattern = re.compile(
    r'<div\s+style="[^"]*">\s*<button\s+type="button"\s+onclick="[^"]*"[^>]*>Expand All</button>\s*<button\s+type="button"\s+onclick="[^"]*"[^>]*>Collapse All</button>\s*</div>\n?',
    re.IGNORECASE | re.DOTALL
)

content, button_count = button_block_pattern.subn('', content)
print(f"Removed {button_count} Expand/Collapse button block(s)")

# --- Step 8: Replace styled <div> dividers with Markdown --- ---
divider_pattern = re.compile(
    r'<div\s+style="height:1px;[^"]*"></div>',
    re.IGNORECASE
)

content, divider_count = divider_pattern.subn('---', content)
print(f"Replaced {divider_count} styled <div> dividers with Markdown ---")

# --- Step 9: Catch any remaining data: URI images ---
remaining = re.findall(r'data:image/svg\+xml;base64,', content)
if remaining:
    print(f"\n⚠ WARNING: {len(remaining)} data: URIs still remain in the file!")
    # Show line numbers
    for i, line in enumerate(content.split('\n'), 1):
        if 'data:image/svg+xml;base64,' in line:
            print(f"  Line {i}: {line[:120]}...")
else:
    print("\n✓ All data: URIs have been replaced!")

# --- Step 10: Write the file ---
with open(MD_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nFile saved: {MD_FILE}")
print(f"\nSummary:")
print(f"  Icons extracted: {len(icon_map)}")
print(f"  Icon refs replaced: {icon_count}")
print(f"  Color swatches replaced: {swatch_count}")
print(f"  Color boxes replaced: {box_count}")
print(f"  Summary tags cleaned: {summary_count}")
print(f"  Button blocks removed: {button_count}")
print(f"  Divider tags replaced: {divider_count}")
