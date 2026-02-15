# Power BI Custom Theme

A comprehensive, production-ready Power BI theme with complete documentation, customization guides, and real-world examples.

![Before and After applying the theme](preview.png)

## 📋 Overview

This repository contains a complete Power BI theme designed for professional, cohesive visual experiences across all Power BI reports and dashboards. The theme defines colors, typography, and visual styling for 40+ Power BI visualization types, following a hierarchical 4-level structure.

**Key Features:**
- ✅ 40+ visualization types styled
- ✅ Semantic colors (good/bad/neutral) support
- ✅ Professional typography system
- ✅ Customizable at multiple levels (global → visual → preset)
- ✅ Complete schema validation with autocomplete support
- ✅ Extensive documentation with examples

## 📁 Contents

| File | Purpose |
|------|---------|
| **Custom_Theme_Styles.json** | The main theme file — ready to use in Power BI |
| **Power_BI_Theme_Guide.md** | Complete guide: structure, colors, typography, customization, examples |
| **Power_BI_Theme_Guide.html** | HTML version of the guide (formatted for viewing in browser) |
| **reportThemeSchema-2.149.json** | Microsoft Power BI theme schema — enables autocomplete in VS Code |
| **Theme_Preview.pbix** | Sample Power BI file with this theme pre-applied |

## 🚀 Quick Start

### Apply the Theme

1. Open any Power BI report in **Power BI Desktop**
2. Go to **View** → **Themes** → **Browse for themes**
3. Select **Custom_Theme_Styles.json** and click **Open**
4. The theme is applied immediately to all visuals in the report

### Make It Default

To use this theme for all new reports:
1. Apply the theme once (see steps above)
2. Save the report as a template (.pbit)
3. Any report created from that template will inherit the theme automatically

## 📖 Documentation

Read the complete guide in **Power_BI_Theme_Guide.md** for:

- **Section 1**: Overview & How to Apply
- **Section 2**: Theme Properties (name, schema, icons)
- **Section 3**: Color Palette (theme colors, semantic colors, ranges)
- **Section 4**: Typography & Text Classes
- **Section 5**: Theme File Structure (4-level hierarchy explained)
- **Section 6**: Visual Name Reference (40+ visual JSON names)
- **Section 7**: How to Customize This Theme (2 proven methods)
  - Method 1: Schema + Editor Autocomplete
  - Method 2: AI-Assisted with Schema
- **Section 8**: Real Examples by Visual Type (copy-paste ready)
- **Section 9**: Quick Reference & Notes
- **Section 10**: Version & References

**Prefer HTML?** Open `Power_BI_Theme_Guide.html` in your browser for a formatted version with collapsible sections.

## 🎨 Customization Methods

### Method 1: VS Code + Schema Autocomplete
1. Open `Custom_Theme_Styles.json` in VS Code
2. Add `"$schema": "reportThemeSchema-2.149.json"` at the top
3. Start typing property names — autocomplete shows all options
4. Save and reload in Power BI

**Best for:** Exploring options interactively, precise control

### Method 2: AI-Assisted (ChatGPT, Claude, Copilot)
1. Describe what you want to change
2. Provide the schema file as reference
3. AI generates the correct JSON structure
4. Review, paste, and test in Power BI

**Best for:** "I want to change X but don't know where", bulk changes

See **Section 7 (How to Customize This Theme)** in the guide for detailed examples and troubleshooting.

## 📊 Structure Overview

The theme uses a **4-level hierarchy**:

```
Level 1: Global Settings (colors, fonts, semantic colors)
  ↓
Level 2: General Visual Properties (page, layout, borders)
  ↓
Level 3: Visual-Specific Defaults (card → labels, table → headers)
  ↓
Level 4: Visual Presets (WithBackground, WithoutBackground)
```

Lower levels override upper levels. User manual formatting overrides all theme settings.

## 🔗 Visual Name Reference

The theme includes styling for 40+ Power BI visuals. Common visual names:

| Visual | JSON Name |
|--------|-----------|
| Card | `card` |
| Table (new) | `tableEx` |
| Bar Chart (stacked) | `barChart` |
| Clustered Bar Chart | `clusteredBarChart` |
| Line Chart | `lineChart` |
| Matrix | `pivotTable` |
| Slicer | `slicer` |

See **Section 6 (Visual Name Reference)** for the complete list of 40+ visuals.

## 🎯 Example: Customizing Card Values

**Goal:** Make card values 25pt bold with light background

Add this to your `Custom_Theme_Styles.json`:

```json
"visualStyles": {
  "card": {
    "*": {
      "stylePreset": [
        {
          "name": "WithBackground",
          "style": {
            "labels": [
              {
                "fontSize": 25,
                "bold": true,
                "color": { "solid": { "color": "#595B69" } }
              }
            ]
          }
        }
      ]
    }
  }
}
```

See **Section 8 (Real Examples by Visual Type)** for more copy-paste ready examples.

## 🛠️ Troubleshooting

**Theme doesn't load after editing:**
- Check VS Code Problems panel for JSON syntax errors
- Ensure all braces `{}` and brackets `[]` match
- Color properties must use nested `"solid"` structure
- Reload via **View → Themes → Browse for themes**

**Changes not visible:**
- Confirm property path is correct (visual → `*` → property)
- Check for typos in visual names (use [Visual Name Reference](#-visual-name-reference) table)
- Reload the theme after editing

**Need help?** See **Section 7.5 (Tips & Troubleshooting)** in the guide.

## 📝 Schema Information

- **Schema Version:** reportThemeSchema-2.149.json
- **Power BI Compatibility:** Power BI Desktop 2.115+
- **Last Updated:** February 2026

## 🎓 Learning Resources

- [Microsoft Power BI Themes Documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes)
- [Power BI Theme JSON Structure](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#export-report-themes)

## 📄 License

This theme is provided as-is for use with Microsoft Power BI. Modify and distribute freely for your organization's reporting needs.

## 💬 Contributing

Found an issue or have a suggestion? Feel free to open an issue or submit a pull request.

---

**Ready to customize?** Start with **Section 7: How to Customize This Theme** in `Power_BI_Theme_Guide.md`, or check **Section 8** for real, copy-paste ready examples.
