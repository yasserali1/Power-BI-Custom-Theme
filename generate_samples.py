"""
Generate SVG sample text images for each text class.
Each SVG renders "Sample Text" with the correct font size, color, and weight.
"""
import os

ICONS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
os.makedirs(ICONS_DIR, exist_ok=True)

# Text class definitions: (name, font_size_pt, color_hex, font_weight, effective_label)
# Inherited values are resolved to their actual values
TEXT_CLASSES = [
    ("callout",         11, "#1C2632", "normal"),
    ("title",           10, "#1C2632", "normal"),
    ("header",          10, "#1C2632", "normal"),
    ("label",           10, "#8793A3", "normal"),
    ("boldLabel",       10, "#8793A3", "bold"),
    ("semiboldLabel",   10, "#8793A3", "600"),
    ("largeLabel",      12, "#8793A3", "normal"),
    ("smallLabel",       9, "#8793A3", "normal"),
    ("lightLabel",      10, "#595B69", "normal"),
    ("largeLightLabel", 12, "#8793A3", "normal"),
    ("smallLightLabel",  9, "#595B69", "normal"),
    ("largeTitle",      14, "#1C2632", "normal"),
]

def generate_svg(name, font_size_pt, color, font_weight):
    """Generate an SVG with 'Sample Text' rendered in the given style."""
    # Convert pt to px for SVG (1pt ≈ 1.333px)
    font_size_px = round(font_size_pt * 1.333)
    
    # Calculate SVG dimensions based on font size
    # Approximate text width: ~6.5px per character at 13px font size, scale proportionally
    char_width_ratio = font_size_px * 0.58
    if font_weight in ("bold", "600"):
        char_width_ratio = font_size_px * 0.63  # bold text is wider
    text_width = round(len("Sample Text") * char_width_ratio)
    svg_width = text_width + 4  # small padding
    svg_height = font_size_px + 6  # vertical padding
    text_y = font_size_px + 1  # baseline offset
    
    # Use Calibri with common fallbacks
    font_family = "Calibri, Segoe UI, Arial, sans-serif"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}">
  <text x="2" y="{text_y}" font-family="{font_family}" font-size="{font_size_px}px" font-weight="{font_weight}" fill="{color}">Sample Text</text>
</svg>'''
    
    filename = f"sample-{name.lower()}.svg"
    filepath = os.path.join(ICONS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
    
    print(f"  {filename}: {font_size_pt}pt ({font_size_px}px), {color}, weight={font_weight}, {svg_width}x{svg_height}")
    return filename

# Generate all SVGs
print("Generating text class sample SVGs:")
for name, size, color, weight in TEXT_CLASSES:
    generate_svg(name, size, color, weight)

print(f"\nDone! {len(TEXT_CLASSES)} SVG files generated in: {ICONS_DIR}")
