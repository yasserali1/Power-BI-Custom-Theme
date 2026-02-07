# Power BI Custom Theme — Complete Guide

<div style="margin:12px 0;display:flex;gap:8px;flex-wrap:wrap;">
  <button type="button" onclick="document.querySelectorAll('details.collapsible-section').forEach(d => d.open = true)" style="background:#F3F3F3;color:#595B69;border:0;border-radius:5px;padding:6px 12px;font-weight:bold;cursor:pointer;border-bottom:2px solid #1C2632;">Expand All</button>
  <button type="button" onclick="document.querySelectorAll('details.collapsible-section').forEach(d => d.open = false)" style="background:#F3F3F3;color:#595B69;border:0;border-radius:5px;padding:6px 12px;font-weight:bold;cursor:pointer;border-bottom:2px solid #1C2632;">Collapse All</button>
</div>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="table-of-contents">Table of Contents</span></summary>

1. [Overview & How to Apply](#overview--how-to-apply)
2. [Theme Properties](#theme-properties)
   - [2.1 Basic Information](#basic-information)
   - [2.2 Custom Icons](#custom-icons)
3. [Color Palette](#color-palette)
   - [3.1 Theme Colors](#theme-colors)
   - [3.2 Semantic Status Colors](#semantic-status-colors)
   - [3.3 Scale & Range Colors](#scale--range-colors)
   - [3.4 Background & Foreground Colors](#background--foreground-colors)
4. [Typography & Text Classes](#typography--text-classes)
   - [4.1 Font Face](#font-face)
   - [4.2 Text Classes Reference](#text-classes-reference)
5. [Theme File Structure](#theme-file-structure)
   - [5.1 Summary Hierarchy Overview](#summary-hierarchy-overview)
   - [5.2 Complete Hierarchy Diagram](#complete-hierarchy-diagram)
   - [5.3 Level 1: Global Theme Settings](#level-1-global-theme-settings)
   - [5.4 Level 2: General Visual Settings](#level-2-general-visual-settings)
   - [5.5 Level 3: Visual-Specific Settings](#level-3-visual-specific-settings)
   - [5.6 Level 4: Visual Preset Styles](#level-4-visual-preset-styles)
   - [5.7 Settings Application Order](#settings-application-order-priority)
6. [Visual Name Reference](#visual-name-reference)
7. [How to Customize This Theme](#how-to-customize-this-theme)
   - [7.1 What You'll Need](#what-youll-need)
   - [7.2 Setting Up VS Code for Autocomplete](#setting-up-vs-code)
   - [7.3 Method 1: Schema + Editor Autocomplete](#method-1-schema--editor-autocomplete)
   - [7.4 Method 2: AI-Assisted with Schema](#method-2-ai-assisted-with-schema)
   - [7.5 Tips & Troubleshooting](#tips--troubleshooting)
8. [Real Examples by Visual Type](#real-examples-by-visual-type)
   - [8.1 Card — Value Font Size & Category Label](#example-card)
   - [8.2 Table — Headers, Values & Totals](#example-table)
   - [8.3 Bar Chart — Data Labels & Legend](#example-bar-chart)
   - [8.4 Line Chart — Line Styles & Markers](#example-line-chart)
   - [8.5 All Visuals — Default Title, Border & Padding](#example-all-visuals)
9. [Quick Reference & Notes](#quick-reference--notes)
10. [Version & References](#version--references)

---

</details>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="overview--how-to-apply">1. Overview & How to Apply</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

The **Custom_Theme_Styles.json** is a comprehensive Power BI theme file designed to provide a cohesive, professional visual experience across all Power BI reports and dashboards. This theme defines colors, typography, and visual styling for all 40+ Power BI visualization types.

The theme follows a hierarchical 4-level structure that ensures consistency while allowing visual customization at multiple levels.

#### How to Apply This Theme

1. Open your Power BI report in **Power BI Desktop**
2. Go to **View** → **Themes** → **Browse for themes**
3. Select **Custom_Theme_Styles.json** and click **Open**
4. The theme is applied immediately to all visuals in the report

> **Tip**: To make this the default for new reports, apply it once and save the report as a template (.pbit). Any report created from that template will inherit the theme automatically.
>
> **To update an already-applied theme**: After editing the JSON file, reload it via **View → Themes → Browse for themes** again. Power BI will reapply the updated styles.
>
> **Ready to customize?** See [How to Customize This Theme](#how-to-customize-this-theme) (Section 7) for step-by-step methods using VS Code autocomplete or AI assistance.

---

</details>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="theme-properties">2. Theme Properties</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

#### <span id="basic-information">2.1 Basic Information</span>

| Property | Value | Description |
|----------|-------|-------------|
| **Name** | Custom_Theme | Official theme name |
| **Schema** | reportThemeSchema-2.149.json | Power BI theme schema version |
| **Icons** | 15 | Custom SVG icon set |

</details>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="custom-icons">2.2 Custom Icons</span></summary>

The theme includes 15 custom SVG icons for use in Power BI reports and filters.

#### <span id="icon-summary-with-snippets">2.2.1 Icon Summary (with Snippets)</span>

| Category | Count | Purpose | Snippets |
|----------|-------|---------|----------|
| **Directional Indicators** | 5 | KPI trends, status changes, directional metrics | <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><g clip-path=%22url(%23clip0_951_46030)%22><path d=%22M7.99967 14.6668C11.6815 14.6668 14.6663 11.682 14.6663 8.00016C14.6663 4.31826 11.6815 1.3335 7.99967 1.3335C4.31777 1.3335 1.33301 4.31826 1.33301 8.00016C1.33301 11.682 4.31777 14.6668 7.99967 14.6668Z%22 fill=%22%23F5E9EC%22 stroke=%22%23c2255c%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/><path d=%22M8.00033 5.3335V10.6668M8.00033 10.6668L10.3337 8.3335M8.00033 10.6668L5.66699 8.3335%22 stroke=%22%23c2255c%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></g><defs><clipPath id=%22clip0_951_46030%22><rect width=%2216%22 height=%2216%22 fill=%22white%22/></clipPath></defs></svg>" alt="Arrow Down Bad" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><g clip-path=%22url(%23clip0_952_46050)%22><path d=%22M7.99967 14.6668C11.6815 14.6668 14.6663 11.682 14.6663 8.00016C14.6663 4.31826 11.6815 1.3335 7.99967 1.3335C4.31777 1.3335 1.33301 4.31826 1.33301 8.00016C1.33301 11.682 4.31777 14.6668 7.99967 14.6668Z%22 fill=%22%23E9F9F7%22 fill-opacity=%221%22 stroke=%22%2309B39D%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/><path d=%22M8.00033 5.3335V10.6668M8.00033 10.6668L10.3337 8.3335M8.00033 10.6668L5.66699 8.3335%22 stroke=%22%2309B39D%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></g><defs><clipPath id=%22clip0_952_46050%22><rect width=%2216%22 height=%2216%22 fill=%22white%22/></clipPath></defs></svg>" alt="Arrow Down Good" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><g clip-path=%22url(%23clip0_951_46033)%22><path d=%22M7.99967 14.6668C11.6815 14.6668 14.6663 11.682 14.6663 8.00016C14.6663 4.31826 11.6815 1.3335 7.99967 1.3335C4.31777 1.3335 1.33301 4.31826 1.33301 8.00016C1.33301 11.682 4.31777 14.6668 7.99967 14.6668Z%22 fill=%22%23F4F4F4%22 stroke=%22%23404040%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/><path d=%22M5.33301 7.99984H10.6663M10.6663 7.99984L8.33301 5.6665M10.6663 7.99984L8.33301 10.3332%22 stroke=%22%23404040%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></g><defs><clipPath id=%22clip0_951_46033%22><rect width=%2216%22 height=%2216%22 fill=%22white%22/></clipPath></defs></svg>" alt="Arrow Right Neutral" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><g clip-path=%22url(%23clip0_952_46052)%22><path d=%22M7.99967 14.6668C11.6815 14.6668 14.6663 11.682 14.6663 8.00016C14.6663 4.31826 11.6815 1.3335 7.99967 1.3335C4.31777 1.3335 1.33301 4.31826 1.33301 8.00016C1.33301 11.682 4.31777 14.6668 7.99967 14.6668Z%22 fill=%22%23F5E9EC%22 stroke=%22%23c2255c%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/><path d=%22M8.00033 10.6668V5.3335M8.00033 5.3335L10.3337 7.66683M8.00033 5.3335L5.66699 7.66683%22 stroke=%22%23c2255c%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></g><defs><clipPath id=%22clip0_952_46052%22><rect width=%2216%22 height=%2216%22 fill=%22white%22/></clipPath></defs></svg>" alt="Arrow Up Bad" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><g clip-path=%22url(%23clip0_950_46027)%22><path d=%22M7.99967 14.6668C11.6815 14.6668 14.6663 11.682 14.6663 8.00016C14.6663 4.31826 11.6815 1.3335 7.99967 1.3335C4.31777 1.3335 1.33301 4.31826 1.33301 8.00016C1.33301 11.682 4.31777 14.6668 7.99967 14.6668Z%22 fill=%22%23E9F9F7%22 fill-opacity=%221%22 stroke=%22%2309B39D%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/><path d=%22M8.00033 10.6668V5.3335M8.00033 5.3335L10.3337 7.66683M8.00033 5.3335L5.66699 7.66683%22 stroke=%22%2309B39D%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></g><defs><clipPath id=%22clip0_950_46027%22><rect width=%2216%22 height=%2216%22 fill=%22white%22/></clipPath></defs></svg>" alt="Arrow Up Good" style="width:16px;height:16px;" /> |
| **Status & Validation** | 3 | Success/failure states, validation indicators | <img src="data:image/svg+xml;utf8,<svg viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22><path fill-rule=%22evenodd%22 clip-rule=%22evenodd%22 d=%22M14.667 8A6.667 6.667 0 1 1 1.333 8a6.667 6.667 0 0 1 13.334 0M11.21 6.387a.667.667 0 1 0-1.085-.775L7.249 9.639 5.806 8.195a.667.667 0 0 0-.943.943l2 2a.667.667 0 0 0 1.013-.084z%22 fill=%22%2309b39d%22/></svg>" alt="Check Mark Green" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg fill=%22%23c2255c%22 viewBox=%220 0 16 16%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22><path d=%22M8 1.333A6.667 6.667 0 1 0 14.667 8 6.667 6.667 0 0 0 8 1.333m2.473 8.193a.667.667 0 0 1 0 .947.667.667 0 0 1-.947 0L8 8.947l-1.527 1.527a.667.667 0 0 1-.947 0 .667.667 0 0 1 0-.947L7.053 8 5.527 6.473a.667.667 0 0 1 .947-.947L8 7.053l1.527-1.527a.667.667 0 0 1 .947.947L8.947 8Z%22/></svg>" alt="X Mark Red" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg fill=%22%23000000%22 viewBox=%220 0 16 16%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22><path d=%22M8 1.333A6.667 6.667 0 1 0 14.667 8 6.667 6.667 0 0 0 8 1.333Zm2.473 8.193a.667.667 0 0 1 0 .947.667.667 0 0 1-.947 0L8 8.947l-1.527 1.527a.667.667 0 0 1-.947 0 .667.667 0 0 1 0-.947L7.053 8 5.527 6.473a.667.667 0 0 1 .947-.947L8 7.053l1.527-1.527a.667.667 0 0 1 .947.947L8.947 8Z%22/></svg>" alt="X Mark Black" style="width:16px;height:16px;" /> |
| **Alert & Warning** | 2 | Warning messages, attention needed | <img src="data:image/svg+xml;utf8,<svg viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22><path fill-rule=%22evenodd%22 clip-rule=%22evenodd%22 d=%22M7.333 8.667a.667.667 0 1 0 1.333 0v-2a.667.667 0 1 0-1.333 0zm1.333 1.993a.667.667 0 1 0-1.333 0v.007a.667.667 0 1 0 1.333 0zM6.251 3.107c.762-1.371 2.735-1.371 3.497 0l4.401 7.921c.741 1.333-.223 2.971-1.748 2.971H3.599c-1.525 0-2.489-1.638-1.749-2.971z%22 fill=%22%23efbc1b%22/></svg>" alt="Alert Triangle" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22><path fill-rule=%22evenodd%22 clip-rule=%22evenodd%22 d=%22M1.333 8a6.667 6.667 0 1 1 13.334 0A6.667 6.667 0 0 1 1.333 8m6 .667a.667.667 0 1 0 1.333 0V5.333a.667.667 0 1 0-1.333 0zm1.333 1.993a.667.667 0 1 0-1.333 0v.007a.667.667 0 1 0 1.333 0z%22 fill=%22%23efbc1b%22/></svg>" alt="Alert Circle" style="width:16px;height:16px;" /> |
| **Filter Controls** | 2 | Active/inactive filter states | <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><path fill-rule=%22evenodd%22 clip-rule=%22evenodd%22 d=%22M3.663 6.042c0-.439.28-.812.671-.95V3.7H2.333A.333.333 0 0 0 2 4.033v8a.333.333 0 0 0 .333.333h4.322a.333.333 0 1 1 0 .667H2.333a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1h2.001v-.659a.333.333 0 1 1 .667 0v.659h3a.333.333 0 0 1 .333.333v5.706a1.008 1.008 0 0 1 0 1.904v1.391h5.333a.333.333 0 0 0 .333-.333v-8a.333.333 0 0 0-.333-.333H9.334a.333.333 0 1 1 0-.667h1.667V2.38a.333.333 0 1 1 .667 0v.653h1.999a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H8.334v.634a.333.333 0 1 1-.667 0v-2.692a1.008 1.008 0 0 1 0-1.9V3.7H5v1.391a1.008 1.008 0 0 1 0 1.905v4.356a.333.333 0 1 1-.667 0V6.993a1.01 1.01 0 0 1-.671-.951m1.018.341h-.023a.341.341 0 1 1 .023 0M11 8.992a1.009 1.009 0 0 1 0-1.901V4.717a.333.333 0 1 1 .667 0v2.374a1.008 1.008 0 0 1 0 1.905v2.356a.333.333 0 1 1-.667 0zm.677-.951a.341.341 0 1 0-.681 0 .341.341 0 0 0 .681 0m-3.333 1.983a.341.341 0 1 0-.682 0 .341.341 0 0 0 .682 0%22 fill=%22%23404143%22/></svg>" alt="Filter Dark Grey" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><path fill-rule=%22evenodd%22 clip-rule=%22evenodd%22 d=%22M3.663 6.042c0-.439.28-.812.671-.95V3.7H2.333A.333.333 0 0 0 2 4.033v8a.333.333 0 0 0 .333.333h4.322a.333.333 0 1 1 0 .667H2.333a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1h2.001v-.659a.333.333 0 1 1 .667 0v.659h3a.333.333 0 0 1 .333.333v5.706a1.008 1.008 0 0 1 0 1.904v1.391h5.333a.333.333 0 0 0 .333-.333v-8a.333.333 0 0 0-.333-.333H9.334a.333.333 0 1 1 0-.667h1.667v-.653a.333.333 0 1 1 .667 0v.652h1.999a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H8.334v.634a.333.333 0 1 1-.667 0v-2.692a1.008 1.008 0 0 1 0-1.9V3.7H5v1.391a1.008 1.008 0 0 1 0 1.905v4.356a.333.333 0 1 1-.667 0V6.993a1.01 1.01 0 0 1-.671-.951m1.018.341h-.023a.341.341 0 1 1 .023 0M11 8.992a1.009 1.009 0 0 1 0-1.901V4.717a.333.333 0 1 1 .667 0v2.374a1.008 1.008 0 0 1 0 1.905v2.356a.333.333 0 1 1-.667 0zm.677-.951a.341.341 0 1 0-.681 0 .341.341 0 0 0 .681 0m-3.333 1.983a.341.341 0 1 0-.682 0 .341.341 0 0 0 .682 0%22 fill=%22%23da3f45%22/></svg>" alt="Filter Red" style="width:16px;height:16px;" /> |
| **Close Actions** | 2 | Dialog close, dismissal actions | <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22><path d=%22m13.63 3.65-1.28-1.27L8 6.73 3.64 2.38 2.37 3.65l4.35 4.36-4.34 4.34 1.27 1.28L8 9.28l4.35 4.36 1.28-1.28-4.36-4.35z%22 fill=%22%23000000%22/></svg>" alt="Close Black" style="width:16px;height:16px;" /> <img src="data:image/svg+xml;utf8,<svg width=%2216%22 height=%2216%22 fill=%22%23d83f47%22 viewBox=%220 0 16 16%22 xmlns=%22http://www.w3.org/2000/svg%22><path d=%22m13.63 3.65-1.28-1.27L8 6.73 3.64 2.38 2.37 3.65l4.35 4.36-4.34 4.34 1.27 1.28L8 9.28l4.35 4.36 1.28-1.28-4.36-4.35z%22/></svg>" alt="Close Red" style="width:16px;height:16px;" /> |
| **Utility** | 1 | Collapse, minimize actions | <img src="data:image/svg+xml;utf8,<svg viewBox=%220 0 16 16%22 fill=%22none%22 xmlns=%22http://www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22><path fill-rule=%22evenodd%22 clip-rule=%22evenodd%22 d=%22M1.333 8a6.667 6.667 0 1 1 13.334 0A6.667 6.667 0 0 1 1.333 8m4 0A.667.667 0 0 1 6 7.333h4a.667.667 0 1 1 0 1.333H6a.667.667 0 0 1-.667-.667%22 fill=%22%23404040%22/></svg>" alt="Minus Dark Grey" style="width:16px;height:16px;" /> |

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="color-palette">3. Color Palette</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

> **For detailed information on how colors are applied to visual elements, structural color classes, and foreground/background color hierarchy, see [Microsoft Power BI Color Palette Documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#report-theme-json-file-format).**

#### <span id="theme-colors">3.1 Theme Colors</span>

<div style="display:grid;grid-template-columns:repeat(4,140px);gap:20px;">
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#4F73B8;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#4F73B8<br><span style="color:#6b7280;">Data 1</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#49A9D5;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#49A9D5<br><span style="color:#6b7280;">Data 2</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#D7A767;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#D7A767<br><span style="color:#6b7280;">Data 3</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#DC7653;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#DC7653<br><span style="color:#6b7280;">Data 4</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#8783FF;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#8783FF<br><span style="color:#6b7280;">Data 5</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#1C2632;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#1C2632<br><span style="color:#6b7280;">Data 6</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#8793A3;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#8793A3<br><span style="color:#6b7280;">Data 7</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#DBDFE4;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#DBDFE4<br><span style="color:#6b7280;">Data 8</span></div>
  </div>
</div>

> **Purpose**: Colors are applied in sequence (first series gets color 0, second gets color 1, etc.) for multi-color visualizations.

#### <span id="semantic-status-colors">3.2 Semantic Status Colors</span>

<div style="display:grid;grid-template-columns:repeat(3,140px);gap:20px;">
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#09B39D;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#09B39D<br><span style="color:#6b7280;">Positive / Good</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#404040;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#404040<br><span style="color:#6b7280;">Neutral / Middle</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#c2255c;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#c2255c<br><span style="color:#6b7280;">Negative / Bad</span></div>
  </div>
</div>

> **Purpose**: Used for KPIs, gauges, and conditional formatting to indicate status and values.

#### <span id="scale--range-colors">3.3 Scale & Range Colors</span>

| Property | Hex Code | Purpose |
|----------|----------|---------|
| **maximum** | <span style="display:inline-block;width:12px;height:12px;background-color:#4F73B8;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#4F73B8 | Maximum value indicator (Primary Blue) |
| **center** | <span style="display:inline-block;width:12px;height:12px;background-color:#95A9CE;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#95A9CE | Center/neutral value indicator |
| **minimum** | <span style="display:inline-block;width:12px;height:12px;background-color:#DBDFE4;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#DBDFE4 | Minimum value indicator (Light Gray) |

> **Purpose**: Used for heat maps, range visualizations, and color scales.

#### <span id="background--foreground-colors">3.4 Background & Foreground Colors</span>

##### Visual Background Palette

<div style="display:grid;grid-template-columns:repeat(3,140px);gap:20px;">
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#F9F9F9;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#F9F9F9<br><span style="color:#6b7280;">Main Background</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#DBDFE4;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#DBDFE4<br><span style="color:#6b7280;">Background Light</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#F6F8FB;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#F6F8FB<br><span style="color:#6b7280;">Page Background</span></div>
  </div>
</div>

##### Visual Text Color Examples

<div style="display:grid;grid-template-columns:repeat(3,140px);gap:20px;">
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#1C2632;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#1C2632<br><span style="color:#6b7280;">Primary Text</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#8793A3;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#8793A3<br><span style="color:#6b7280;">Secondary Text</span></div>
  </div>
  <div>
    <div style="width:140px;height:44px;border-radius:8px;background:#4F73B8;border:1px solid #e1e5ee;"></div>
    <div style="margin-top:8px;font-size:12px;color:#374151;">#4F73B8<br><span style="color:#6b7280;">Tertiary Text</span></div>
  </div>
</div>

##### All Text & Background Color Properties

| Property | Hex Code | Purpose |
|----------|----------|---------|
| **foreground** | <span style="display:inline-block;width:12px;height:12px;background-color:#1C2632;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#1C2632 | Primary text color (Dark Blue-Gray) |
| **foregroundNeutralSecondary** | <span style="display:inline-block;width:12px;height:12px;background-color:#1C2632;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#1C2632 | Secondary text (Dark Blue-Gray) |
| **foregroundNeutralTertiary** | <span style="display:inline-block;width:12px;height:12px;background-color:#4F73B8;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#4F73B8 | Tertiary text (Primary Blue) |
| **background** | <span style="display:inline-block;width:12px;height:12px;background-color:#F9F9F9;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#F9F9F9 | Main background (Light Gray) |
| **backgroundLight** | <span style="display:inline-block;width:12px;height:12px;background-color:#DBDFE4;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#DBDFE4 | Light background elements |
| **backgroundNeutral** | <span style="display:inline-block;width:12px;height:12px;background-color:#B4BAC3;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#B4BAC3 | Neutral background tint |
| **tableAccent** | <span style="display:inline-block;width:12px;height:12px;background-color:#426871;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#426871 | Table accent color (Dark Teal) |

> **For comprehensive details on structural color classes and their usage across visual elements, see [Microsoft Power BI Structural Colors Documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#set-structural-colors).**

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="typography--text-classes">4. Typography & Text Classes</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

#### <span id="font-face">4.1 Font Face</span>

All text elements use **Calibri** as the primary font family.

#### <span id="text-classes-reference">4.2 Text Classes Reference</span>

| Class | Type | Inherits From | Font Size | Font | Color | Sample | Used In |
|-------|------|---|-----------|------|-------|--------|----------|
| **callout** | Primary | - | 11pt | Calibri | <span style="display:inline-block;width:12px;height:12px;background-color:#1C2632;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#1C2632 | <span style="font-family:Calibri;font-size:11pt;color:#1C2632;">Sample Text</span> | Card data labels, KPI indicators |
| **title** | Primary | - | 10pt | Calibri | <span style="display:inline-block;width:12px;height:12px;background-color:#1C2632;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#1C2632 | <span style="font-family:Calibri;font-size:10pt;color:#1C2632;">Sample Text</span> | Category/Value axis titles, Multi-row card titles, Slicer headers |
| **header** | Primary | - | Default | Calibri | <span style="display:inline-block;width:12px;height:12px;background-color:#1C2632;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#1C2632 | <span style="font-family:Calibri;color:#1C2632;">Sample Text</span> | Key influencers headers |
| **label** | Primary | - | 10pt | Calibri | <span style="display:inline-block;width:12px;height:12px;background-color:#8793A3;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#8793A3 | <span style="font-family:Calibri;font-size:10pt;color:#8793A3;">Sample Text</span> | Table/Matrix column & row headers, grid, values |
| **boldLabel** | Secondary | label | Inherited | Calibri | Inherited | <span style="font-family:Calibri;font-size:10pt;color:#8793A3;font-weight:bold;">Sample Text</span> | Matrix subtotals, grand totals, Table totals |
| **semiboldLabel** | Secondary | label | Inherited | Calibri | Inherited | <span style="font-family:Calibri;font-size:10pt;color:#8793A3;font-weight:600;">Sample Text</span> | Key influencers profile text |
| **largeLabel** | Secondary | label | 12pt | Inherited | Inherited | <span style="font-family:Calibri;font-size:12pt;color:#8793A3;">Sample Text</span> | Multi-row card data labels |
| **smallLabel** | Secondary | label | 9pt | Inherited | Inherited | <span style="font-family:Calibri;font-size:9pt;color:#8793A3;">Sample Text</span> | Reference line labels, Slicer input text, Key influencers text |
| **lightLabel** | Secondary | label | Inherited | Inherited | <span style="display:inline-block;width:12px;height:12px;background-color:#595B69;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#595B69 | <span style="font-family:Calibri;font-size:10pt;color:#595B69;">Sample Text</span> | Legend text, Button text, Category axis labels, Gauge target |
| **largeLightLabel** | Secondary | label | 12pt | Inherited | <span style="display:inline-block;width:12px;height:12px;background-color:#8793A3;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#8793A3 | <span style="font-family:Calibri;font-size:12pt;color:#8793A3;">Sample Text</span> | Card/Gauge category labels, Multi-row card category labels |
| **smallLightLabel** | Secondary | label | 9pt | Inherited | <span style="display:inline-block;width:12px;height:12px;background-color:#595B69;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span>#595B69 | <span style="font-family:Calibri;font-size:9pt;color:#595B69;">Sample Text</span> | Data labels, Value axis labels |
| **largeTitle** | Secondary | title | 14pt | Inherited | Inherited | <span style="font-family:Calibri;font-size:14pt;color:#1C2632;">Sample Text</span> | Visual titles |

> **Note**: Secondary classes automatically inherit properties from their primary class. Properties shown in the table are explicitly defined in the theme JSON file. For example, `boldLabel` explicitly defines `fontFace: "Calibri"` even though it matches the parent `label` class. Properties not explicitly defined are inherited from the parent class.
> For complete details on text class usage and formatting options, see [Microsoft Power BI Text Classes Documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes#set-formatted-text-defaults).

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="theme-file-structure">5. Theme File Structure</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

The Custom_Theme_Styles.json file follows a hierarchical structure with four main levels. Each level builds upon the previous one, with more specific settings overriding general ones.

#### <span id="summary-hierarchy-overview">5.1 Summary Hierarchy Overview</span>

| Level | Name | Key Components |
|-------|------|-----------------|
| **1** | Global Theme Settings | • Colors (8 data, 3 semantic, scale)<br>• Foreground/background colors<br>• Text classes (12 typography styles) |
| **2** | General Visual Settings | • Universal visual properties<br>• Page background & outspace<br>• Default spacing & padding |
| **3** | Visual-Specific Settings | • Individual visual type configs<br>• lineChart, pieChart, slicer, table<br>• 40+ visualization types |
| **4** | Preset Styles | • WithBackground (modern style)<br>• WithoutBackground (minimal style)<br>• Visual chrome & spacing overrides |

**Hierarchy Flow**: Level 1 → Level 2 → Level 3 → Level 4 (each level refines and overrides previous settings)

#### <span id="complete-hierarchy-diagram">5.2 Complete Hierarchy Diagram</span>

```
Custom_Theme_Styles.json
│
├─── LEVEL 1: GLOBAL THEME SETTINGS
│    ├─ name
│    ├─ $schema
│    ├─ icons
│    ├─ dataColors[] (8 colors)
│    ├─ Semantic Colors (good, neutral, bad)
│    ├─ Scale Colors (maximum, center, minimum)
│    ├─ Text/Foreground Colors
│    ├─ Background Colors
│    ├─ tableAccent
│    │
│    └─ textClasses (Typography)
│       ├─ callout
│       ├─ title
│       ├─ header
│       ├─ label
│       ├─ smallLightLabel
│       ├─ largeLightLabel
│       ├─ boldLabel
│       ├─ lightLabel
│       ├─ smallLabel
│       ├─ largeLabel
│       ├─ semiboldLabel
│       └─ largeTitle
│
└─── LEVEL 2-4: VISUAL STYLES
     └─ visualStyles
        │
        ├─ "*": "*" (GENERAL VISUAL SETTINGS - Level 2)
        │  ├─ general[]
        │  ├─ subtotals[]
        │  ├─ background[]
        │  ├─ border[]
        │  ├─ title[]
        │  ├─ subTitle[]
        │  ├─ divider[]
        │  ├─ spacing[]
        │  ├─ padding[]
        │  ├─ categoryAxis[]
        │  └─ valueAxis[]
        │
        ├─ page (LEVEL 2: PAGE SETTINGS)
        │  └─ "*"
        │     ├─ outspace[]
        │     └─ background[]
        │
        ├─ lineChart (LEVEL 3: VISUAL-SPECIFIC - Example)
        │  ├─ "*" (Default settings)
        │  │  ├─ stylePreset[]
        │  │  ├─ legend[]
        │  │  ├─ labels[]
        │  │  ├─ lineStyles[]
        │  │  └─ ... (visual-specific properties)
        │  │
        │  ├─ WithBackground (LEVEL 4: PRESET STYLE)
        │  │  ├─ background[]
        │  │  └─ border[]
        │  │
        │  └─ WithoutBackground (LEVEL 4: PRESET STYLE)
        │     ├─ background[]
        │     ├─ border[]
        │     ├─ title[]
        │     ├─ padding[]
        │     └─ ... (preset overrides)
        │
        ├─ clusteredColumnChart
        ├─ pieChart
        ├─ donutChart
        ├─ gauge
        ├─ slicer
        ├─ card
        ├─ table
        ├─ pivotTable
        ├─ tableEx
        ├─ textbox
        ├─ ... (40+ visual types)
        │
        └─ filter, group (special containers)
```

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="level-1-global-theme-settings">5.3 Level 1: Global Theme Settings</span></summary>

Global theme settings are defined at the root level and apply universally across the entire Power BI report.

#### <span id="basic-theme-metadata">5.3.1 Basic Theme Metadata</span>

```json
{
  "name": "Custom_Theme",
  "$schema": "reportThemeSchema-2.149.json",
  "icons": []
}
```

| Property | Value | Description |
|----------|-------|-------------|
| **name** | Custom_Theme | Identifies the theme in Power BI |
| **$schema** | reportThemeSchema-2.149.json | Specifies the Power BI schema version |
| **icons** | [] | Array for custom icon definitions |

#### <span id="global-color-palette">5.3.2 Global Color Palette</span>

The color palette includes:

- **Data Colors**: 8 sequential colors for visualization series
- **Semantic Colors**: good (teal), neutral (gray), bad (red)
- **Scale Colors**: maximum, center, minimum for heat maps
- **Text Colors**: Hierarchy of foreground colors for text elements
- **Background Colors**: Main, light, and neutral background options

See the [Color Palette](#color-palette) section above for detailed color visualization.

#### <span id="global-text-classes">5.3.3 Global Text Classes</span>

Text classes define typography styles used throughout the theme. These are part of the global settings and apply to text elements systematically:

```json
"textClasses": {
  "callout": {
    "fontFace": "Calibri",
    "fontSize": 11,
    "color": "#1C2632"
  },
  // ... additional text classes
}
```

12 typography styles defined with font family, size, and color specifications. See the [Typography & Text Classes](#typography--text-classes) section for complete reference.


</details>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="level-2-general-visual-settings">5.4 Level 2: General Visual Settings</span></summary>

General visual settings apply to **all visuals** and define default behavior. These are defined in `"visualStyles": { "*": { "*": { ... } } }`.

#### <span id="general-layout-properties">5.4.1 General Layout Properties</span>

```json
"general": [
  {
    "responsive": false,
    "responsiveLegacy": false,
    "keepLayerOrder": true,
    "layout": "Tabular"
  }
]
```

| Property | Value | Purpose |
|----------|-------|---------|
| **responsive** | false | Disable responsive layout |
| **responsiveLegacy** | false | Disable legacy responsive mode |
| **keepLayerOrder** | true | Maintain layer/visual order |
| **layout** | Tabular | Table-based layout system |

#### <span id="subtotals-configuration">5.4.2 Subtotals Configuration</span>

```json
"subtotals": [
  {
    "rowSubtotalsPosition": "Bottom"
  }
]
```

Position subtotals at bottom of tables/matrices.

#### <span id="background-configuration">5.4.3 Background Configuration</span>

```json
"background": [
  {
    "show": true
  }
]
```

Enable backgrounds for all visuals by default.

#### <span id="border-configuration">5.4.4 Border Configuration</span>

```json
"border": [
  {
    "show": true,
    "radius": 7,
    "color": {
      "solid": {
        "color": "#FFFFFF"
      }
    }
  }
]
```

| Property | Value | Purpose |
|----------|-------|---------|
| **show** | true | Display borders |
| **radius** | 7 | Border corner radius (pixels) |
| **color** | #FFFFFF | White border color |

#### <span id="title-configuration">5.4.5 Title Configuration</span>

```json
"title": [
  {
    "show": true,
    "alignment": "left",
    "titleWrap": true,
    "fontFamily": "Calibri",
    "fontSize": 12,
    "fontColor": {
      "solid": {
        "color": "#8793A3"
      }
    },
    "bold": false
  }
]
```

#### <span id="subtitle-configuration">5.4.6 Subtitle Configuration</span>

```json
"subTitle": [
  {
    "show": false,
    "alignment": "left",
    "titleWrap": true,
    "fontFamily": "Calibri",
    "fontSize": 10.5,
    "fontColor": {
      "solid": {
        "color": "#B7BEC8"
      }
    },
    "bold": true
  }
]
```

#### <span id="divider-configuration">5.4.7 Divider Configuration</span>

```json
"divider": [
  {
    "show": true,
    "color": {
      "solid": {
        "color": "#FFFFFF"
      }
    },
    "ignorePadding": false,
    "style": "solid",
    "width": 1.5
  }
]
```

#### <span id="spacing-padding-configuration">5.4.8 Spacing & Padding Configuration</span>

```json
"spacing": [
  {
    "verticalSpacing": 2
  }
],
"padding": [
  {
    "top": 10,
    "bottom": 10,
    "left": 10,
    "right": 10
  }
]
```

- **Vertical Spacing**: 2px
- **Padding**: 10px all sides

#### <span id="axis-configuration">5.4.9 Axis Configuration</span>

**Category Axis**:
```json
"categoryAxis": [
  {
    "show": true,
    "fontSize": 10,
    "maxMarginFactor": 50,
    "concatenateLabels": false,
    "showAxisTitle": false,
    "titleFontSize": 12
  }
]
```

**Value Axis**:
```json
"valueAxis": [
  {
    "show": false,
    "position": "Left",
    "gridlineShow": false,
    "axisScale": "Linear",
    "fontSize": 10,
    "fontFamily": "wf_standard-font",
    "bold": true
    // ... additional properties
  }
]
```

#### <span id="page-specific-settings">5.4.10 Page-Specific Settings</span>

Page-level settings (also part of Level 2) apply to report pages themselves:

```json
"page": {
  "*": {
    "outspace": [
      {
        "color": {
          "solid": {
            "color": "#FFFFFF"
          }
        }
      }
    ],
    "background": [
      {
        "color": {
          "solid": {
            "color": "#F6F8FB"
          }
        },
        "transparency": 0
      }
    ]
  }
}
```

- **Outspace**: White canvas area
- **Background**: Light blue-gray page background


</details>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="level-3-visual-specific-settings">5.5 Level 3: Visual-Specific Settings</span></summary>

Each visualization type has its own settings that override general defaults from Level 2:

```json
"visualType": {
  "*": {                           // Default settings
    "stylePreset": [...],
    "legend": [...],
    "labels": [...],
    // ... visual-specific properties
  },
  "WithBackground": {              // Preset 1
    "background": [...],
    "border": [...]
  },
  "WithoutBackground": {           // Preset 2
    "background": [...],
    "border": [...]
  }
}
```

#### <span id="example-line-chart-structure">5.5.1 Example: Line Chart Structure</span>

```json
"lineChart": {
  "*": {
    "stylePreset": [
      {
        "name": "WithBackground"
      }
    ],
    "legend": [
      {
        "legendMarkerRendering": "markerOnly",
        "matchLineColor": true,
        "show": true,
        "position": "TopCenter",
        "showTitle": false,
        "fontSize": 10,
        "defaultToCircle": true
      }
    ],
    "labels": [
      {
        "color": {
          "solid": {
            "color": "#595B69"
          }
        },
        "fontFamily": "wf_standard-font",
        "bold": true,
        "show": true,
        "enableBackground": true,
        "backgroundColor": {
          "solid": {
            "color": "#E5EEFF"
          }
        },
        "backgroundTransparency": 15
      }
    ],
    "lineStyles": [
      {
        "strokeWidth": 4,
        "lineStyle": "solid",
        "lineChartType": "smooth",
        "showMarker": true,
        "markerShape": "circle",
        "markerSize": 5
      }
    ]
  },
  "WithBackground": {
    // Override settings
  },
  "WithoutBackground": {
    // Override settings
  }
}
```


</details>

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="level-4-visual-preset-styles">5.6 Level 4: Visual Preset Styles</span></summary>

Style presets (the final level) allow different visual appearances for the same chart type within visual-specific settings.

#### <span id="withbackground-preset">5.6.1 WithBackground Preset</span>

```json
"WithBackground": {
  "background": [
    {
      "show": true
    }
  ],
  "border": [
    {
      "show": true,
      "radius": 7,
      "color": {
        "solid": {
          "color": "#FFFFFF"
        }
      }
    }
  ]
}
```

**Characteristics**:
- Visible background container
- White border with 7px radius
- 10px padding
- Full visual chrome

#### <span id="withoutbackground-preset">5.6.2 WithoutBackground Preset</span>

```json
"WithoutBackground": {
  "background": [
    {
      "show": false
    }
  ],
  "border": [
    {
      "show": false
    }
  ],
  "title": [
    {
      "show": false
    }
  ],
  "subTitle": [
    {
      "show": false
    }
  ],
  "divider": [
    {
      "show": false
    }
  ],
  "padding": [
    {
      "left": 5,
      "right": 5,
      "bottom": 5,
      "top": 5
    }
  ]
}
```

**Characteristics**:
- No visible background
- No border
- Hidden title/subtitle
- 5px padding (tighter spacing)
- Minimal visual elements

<div style="height:1px;border-top:1px dashed #e5e7eb;margin:18px 0;"></div>

</details>

#### <span id="settings-application-order-priority">5.7 Settings Application Order (Priority)</span>

When Power BI renders a visual, settings are applied in this order (later overrides earlier):

1. **Global theme settings** (Level 1) - Colors, text classes, semantic colors
2. **General visual settings** (Level 2) - Universal visual properties and page settings
3. **Visual-specific defaults** (Level 3) - `"visualType": "*"`
4. **Visual preset overrides** (Level 4) - `"visualType": "PresetName"`
5. **User-level formatting** (Manual edits in desktop application)

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="visual-name-reference">6. Visual Name Reference</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

Use this table to find the correct JSON key name for any Power BI visual when editing the theme file.

| Visual | JSON Name |
|--------|-----------|
| All visuals (defaults) | `*` |
| Action button | `actionButton` |
| Button slicer | `advancedSlicerVisual` |
| AI narratives | `aiNarratives` |
| Area chart | `areaChart` |
| Azure map | `azureMap` |
| Stacked bar chart | `barChart` |
| Bookmark navigator | `bookmarkNavigator` |
| Card (legacy) | `card` |
| Card (new) | `cardVisual` |
| Clustered bar chart | `clusteredBarChart` |
| Clustered column chart | `clusteredColumnChart` |
| Stacked column chart | `columnChart` |
| Decomposition tree | `decompositionTreeVisual` |
| Donut chart | `donutChart` |
| Filled map | `filledMap` |
| Filter | `filter` |
| Funnel | `funnel` |
| Gauge | `gauge` |
| Group (container) | `group` |
| 100% stacked area chart | `hundredPercentStackedAreaChart` |
| 100% stacked bar chart | `hundredPercentStackedBarChart` |
| 100% stacked column chart | `hundredPercentStackedColumnChart` |
| Image | `image` |
| Key influencers | `keyDriversVisual` |
| KPI | `kpi` |
| Line chart | `lineChart` |
| Line + clustered column combo | `lineClusteredColumnComboChart` |
| Line + stacked column combo | `lineStackedColumnComboChart` |
| List slicer | `listSlicer` |
| Map | `map` |
| Multi-row card | `multiRowCard` |
| Page | `page` |
| Page navigator | `pageNavigator` |
| Pie chart | `pieChart` |
| Matrix | `pivotTable` |
| Python visual | `pythonVisual` |
| Q&A visual | `qnaVisual` |
| RDL visual | `rdlVisual` |
| Report (report-level) | `report` |
| Ribbon chart | `ribbonChart` |
| Scatter chart | `scatterChart` |
| Scorecard | `scorecard` |
| Script visual | `scriptVisual` |
| Shape | `shape` |
| Shape map | `shapeMap` |
| Slicer | `slicer` |
| Stacked area chart | `stackedAreaChart` |
| Table (legacy) | `table` |
| Table (new) | `tableEx` |
| Text box | `textbox` |
| Text slicer | `textSlicer` |
| Treemap | `treemap` |
| Waterfall chart | `waterfallChart` |

> **Gotcha**: Some names don't match what you'd expect — `barChart` is actually the **stacked** bar chart, not the clustered one. `pivotTable` is the **Matrix** visual. `tableEx` is the **new** table (most reports use this). `card` is the **legacy** card visual, while `cardVisual` is the **new** card visual introduced in recent Power BI updates. Always check this table if a change isn't applying.

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="how-to-customize-this-theme">7. How to Customize This Theme</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

Now that you understand the theme's [color palette](#color-palette) (Section 3), [typography](#typography--text-classes) (Section 4), [4-level file structure](#theme-file-structure) (Section 5), and [visual JSON names](#visual-name-reference) (Section 6), you're ready to customize it.

There are **two proven methods** to customize the theme while maintaining consistency across all reports. Both work by editing the theme JSON file directly—the difference is how you discover property names and structure.

#### <span id="what-youll-need">7.1 What You'll Need</span>

| File | Purpose |
|------|---------|
| **Custom_Theme_Styles.json** | Your theme file (the one you're customizing) |
| **reportThemeSchema-2.149.json** | The property reference — enables autocomplete and validation |
| **VS Code** | Recommended editor (enables autocomplete with schema) |

#### <span id="setting-up-vs-code">7.2 Setting Up VS Code for Autocomplete</span>

Add this line at the top of your theme JSON file to enable IntelliSense:

```json
{
  "$schema": "reportThemeSchema-2.149.json",
  "name": "Custom_Theme"
}
```

**What this does**: As you type, VS Code suggests valid property names with descriptions—no need to memorize or search the schema manually.

> **Key Microsoft References:**
>
> | What You're Looking For | Where to Find It |
> |------------------------|------------------|
> | Which text class affects which element | [Microsoft Theme Documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes) |
> | What semantic colors (good/bad/neutral) apply to | Same link above, section on structural colors |
> | Full property list | The schema file itself (autocomplete shows all options) |

#### <span id="method-1-schema--editor-autocomplete">7.3 Method 1: Schema + Editor Autocomplete</span>

**Best for**: Exploring options interactively, discovering what's available, precise control

**How It Works**:
1. Open your theme file in VS Code (with `$schema` reference)
2. Start typing a property name → autocomplete shows options
3. Navigate the suggestions to find what you need
4. VS Code validates your JSON in real-time

**Example — Change Card Visual Value Font Size:**

Goal: Make card values larger (25pt instead of default)

1. Navigate to the card visual section in your theme
2. Type `"labels"` and autocomplete shows available properties
3. Add the styling:

```json
{
  "visualStyles": {
    "card": {
      "*": {
        "labels": [
          {
            "fontSize": 25,
            "fontFamily": "wf_standard-font",
            "color": {
              "solid": {
                "color": "#595B69"
              }
            }
          }
        ]
      }
    }
  }
}
```

> **Reference**: The visual name `"card"` comes from the [Visual Name Reference](#visual-name-reference) table in Section 6. The color `#595B69` is the theme's primary text color — see [Color Palette](#color-palette) (Section 3).

**Example — Customize Table Column Headers:**

Goal: Change table header font color and background

1. Navigate to `visualStyles` → `tableEx` (the new table visual — see [Section 6](#visual-name-reference))
2. Use autocomplete to find `columnHeaders` properties
3. Add the styling:

```json
{
  "visualStyles": {
    "tableEx": {
      "*": {
        "columnHeaders": [
          {
            "fontColor": {
              "solid": {
                "color": "#595B69"
              }
            },
            "backColor": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "fontFamily": "Calibri",
            "fontSize": 11,
            "bold": true
          }
        ]
      }
    }
  }
}
```

> **Reference**: This follows the Level 3 visual-specific structure described in [Theme File Structure](#level-3-visual-specific-settings) (Section 5.5). The font `Calibri` is set as the theme default in [Typography](#font-face) (Section 4.1).

✅ Real-time validation catches errors immediately
✅ Autocomplete shows ALL available options — no external tools needed
❌ Requires navigating nested structures and knowing roughly where to look

#### <span id="method-2-ai-assisted-with-schema">7.4 Method 2: AI-Assisted with Schema</span>

**Best for**: "I want to change X but don't know where it is", bulk changes, learning the structure

**How It Works**:
1. Describe what you want to change to an AI (ChatGPT, Copilot, Claude)
2. Provide the schema file as reference
3. AI generates the correct JSON structure
4. Review, paste into your theme, test in Power BI

**Example — Add Data Labels to Bar Charts:**

What you tell AI:

> "Using this Power BI theme schema, show me how to enable data labels on clustered bar charts with a light blue background (#E5EEFF) and bold dark text (#595B69). Include the exact JSON structure I need."

AI generates:

```json
{
  "visualStyles": {
    "clusteredBarChart": {
      "*": {
        "labels": [
          {
            "show": true,
            "color": {
              "solid": {
                "color": "#595B69"
              }
            },
            "bold": true,
            "enableBackground": true,
            "backgroundColor": {
              "solid": {
                "color": "#E5EEFF"
              }
            }
          }
        ]
      }
    }
  }
}
```

> **Tip — Two ways to use AI:**
> - **From scratch**: Provide only the schema → AI returns minimal structure with just what you asked for
> - **Modify existing**: Provide your theme file + schema → AI returns your existing styling with the requested changes added

**Example — Alternating Row Colors for Tables:**

What you tell AI:

> "Using this Power BI theme schema, show me how to set alternating row colors for the tableEx visual. Rows should be #EEF1F7 with Calibri 10pt bold in #595B69."

AI generates:

```json
{
  "visualStyles": {
    "tableEx": {
      "*": {
        "values": [
          {
            "fontColorPrimary": {
              "solid": {
                "color": "#595B69"
              }
            },
            "backColorPrimary": {
              "solid": {
                "color": "#EEF1F7"
              }
            },
            "fontColorSecondary": {
              "solid": {
                "color": "#595B69"
              }
            },
            "backColorSecondary": {
              "solid": {
                "color": "#EEF1F7"
              }
            },
            "fontFamily": "Calibri",
            "fontSize": 10,
            "bold": true
          }
        ]
      }
    }
  }
}
```

✅ Fastest way to find complex property paths — AI explains what each property does
✅ Great for bulk changes across multiple visuals
❌ Must verify the output (AI can make mistakes with property names)

#### <span id="tips--troubleshooting">7.5 Tips & Troubleshooting</span>

**JSON Syntax Errors — Theme doesn't load:**
- Check VS Code's Problems panel (red squiggles)
- Ensure all braces `{}` and brackets `[]` match
- Check for missing commas between properties
- Properties in visual styles use arrays `[ ]` around objects — this is the most common mistake

**Changes Not Appearing after editing:**
- Reload the theme: **View → Themes → Browse for themes**
- Check property path is correct (visual name → `*` → property) — see [Theme File Structure](#theme-file-structure) (Section 5) for the 4-level hierarchy
- Color properties require the `"solid"` → `"color"` nested structure:
  ```json
  "color": { "solid": { "color": "#595B69" } }
  ```

**Not sure which visual name to use?** See the [Visual Name Reference](#visual-name-reference) table in Section 6.

**Want to see complete working examples?** Jump to [Real Examples by Visual Type](#real-examples-by-visual-type) (Section 8) for copy-pasteable JSON blocks.

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="real-examples-by-visual-type">8. Real Examples by Visual Type</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

Each example shows the complete, copy-pasteable JSON structure. Place these inside the `"visualStyles"` object of your theme file.

#### <span id="example-card">8.1 Card — Value Font Size & Category Label</span>

**Goal**: Display card values at 25pt with a visible category label below

```json
"card": {
  "*": {
    "stylePreset": [
      {
        "name": "WithBackground"
      }
    ],
    "labels": [
      {
        "fontSize": 25,
        "fontFamily": "wf_standard-font",
        "color": {
          "solid": {
            "color": "#595B69"
          }
        }
      }
    ],
    "categoryLabels": [
      {
        "show": true,
        "fontSize": 15,
        "color": {
          "solid": {
            "color": "#8793A3"
          }
        }
      }
    ]
  }
}
```

> **Why this matters**: Without explicit `categoryLabels`, Power BI may hide the label or default to a small size. Setting `show: true` and a readable font size ensures users always see what the KPI represents.

#### <span id="example-table">8.2 Table — Headers, Values & Totals</span>

**Goal**: Style table headers (bold, white background), row values (alternating colors), and totals row

```json
"tableEx": {
  "*": {
    "stylePreset": [
      {
        "name": "WithBackground"
      }
    ],
    "columnHeaders": [
      {
        "fontColor": {
          "solid": {
            "color": "#595B69"
          }
        },
        "backColor": {
          "solid": {
            "color": "#FFFFFF"
          }
        },
        "fontFamily": "Calibri",
        "fontSize": 11,
        "bold": true
      }
    ],
    "values": [
      {
        "fontColorPrimary": {
          "solid": {
            "color": "#595B69"
          }
        },
        "backColorPrimary": {
          "solid": {
            "color": "#EEF1F7"
          }
        },
        "fontColorSecondary": {
          "solid": {
            "color": "#595B69"
          }
        },
        "backColorSecondary": {
          "solid": {
            "color": "#EEF1F7"
          }
        },
        "fontFamily": "Calibri",
        "fontSize": 10,
        "bold": true
      }
    ],
    "total": [
      {
        "totals": true,
        "fontColor": {
          "solid": {
            "color": "#595B69"
          }
        },
        "backColor": {
          "solid": {
            "color": "#EFEFEF"
          }
        },
        "fontSize": 11,
        "bold": true
      }
    ]
  }
}
```

> **Insight**: Use `backColorPrimary` and `backColorSecondary` to create alternating row stripes. Setting them to the same color (#EEF1F7) gives a uniform look; use two different shades (e.g., #FFFFFF and #EEF1F7) for zebra striping.

#### <span id="example-bar-chart">8.3 Bar Chart — Data Labels & Legend</span>

**Goal**: Show bold data labels with a light background, legend centered at top without title

```json
"clusteredBarChart": {
  "*": {
    "stylePreset": [
      {
        "name": "WithBackground"
      }
    ],
    "layout": [
      {
        "autoScaleVisualToFitFlexibleWidth": false
      }
    ],
    "labels": [
      {
        "show": true,
        "color": {
          "solid": {
            "color": "#595B69"
          }
        },
        "bold": true,
        "enableBackground": true,
        "backgroundColor": {
          "solid": {
            "color": "#E5EEFF"
          }
        }
      }
    ],
    "legend": [
      {
        "showTitle": false,
        "position": "TopCenter",
        "fontSize": 10
      }
    ]
  }
}
```

> **Insight**: `enableBackground: true` with a subtle `backgroundColor` makes data labels readable even when placed over bars. Without this, labels can be hard to read on certain data color fills.

#### <span id="example-line-chart">8.4 Line Chart — Line Styles & Markers</span>

**Goal**: Smooth 4px lines with circle markers, matching legend colors

```json
"lineChart": {
  "*": {
    "stylePreset": [
      {
        "name": "WithBackground"
      }
    ],
    "legend": [
      {
        "legendMarkerRendering": "markerOnly",
        "matchLineColor": true,
        "show": true,
        "position": "TopCenter",
        "showTitle": false,
        "fontSize": 10,
        "defaultToCircle": true
      }
    ],
    "labels": [
      {
        "color": {
          "solid": {
            "color": "#595B69"
          }
        },
        "fontFamily": "wf_standard-font",
        "bold": true,
        "show": true,
        "enableBackground": true,
        "backgroundColor": {
          "solid": {
            "color": "#E5EEFF"
          }
        },
        "backgroundTransparency": 15
      }
    ],
    "lineStyles": [
      {
        "strokeWidth": 4,
        "lineStyle": "solid",
        "lineChartType": "smooth",
        "showMarker": true,
        "markerShape": "circle",
        "markerSize": 5
      }
    ]
  }
}
```

> **Insight**: `matchLineColor: true` syncs legend marker colors with line colors automatically. `legendMarkerRendering: "markerOnly"` shows dots instead of line segments in the legend, which looks cleaner at small sizes.

#### <span id="example-all-visuals">8.5 All Visuals — Default Title, Border & Padding</span>

**Goal**: Set consistent defaults for every visual in the report

```json
"*": {
  "*": {
    "title": [
      {
        "show": true,
        "alignment": "left",
        "titleWrap": true,
        "fontFamily": "Calibri",
        "fontSize": 12,
        "fontColor": {
          "solid": {
            "color": "#8793A3"
          }
        },
        "bold": false
      }
    ],
    "border": [
      {
        "show": true,
        "radius": 7,
        "color": {
          "solid": {
            "color": "#FFFFFF"
          }
        }
      }
    ],
    "padding": [
      {
        "top": 10,
        "bottom": 10,
        "left": 10,
        "right": 10
      }
    ]
  }
}
```

> **Insight**: These `"*"` → `"*"` defaults are the foundation of the theme. Any visual-specific setting (e.g., `"card"` → `"*"`) will override these values. This is why you can set a 12px title here but override it to 14px for cards specifically — the hierarchy handles it automatically.

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="quick-reference--notes">9. Quick Reference & Notes</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

#### Key Design Decisions in This Theme

| Decision | Value | Why |
|----------|-------|-----|
| **Border radius** | 7px | Modern card look without over-rounding |
| **Padding** | 10px all sides | Enough breathing room without wasting space |
| **Value axis** | Hidden | Declutters charts — values are shown via data labels instead |
| **Responsive layout** | Disabled | Ensures consistent layout across screen sizes and prevents Power BI from auto-resizing elements |
| **Title font color** | #8793A3 (gray) | Keeps titles subtle so data stays prominent |
| **Data label backgrounds** | #E5EEFF (light blue) | Makes labels readable on any bar/line color |

#### Color Quick Reference

| Use Case | Color | Hex |
|----------|-------|-----|
| Primary text | <span style="display:inline-block;width:12px;height:12px;background-color:#1C2632;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Dark Blue-Gray | #1C2632 |
| Secondary text / titles | <span style="display:inline-block;width:12px;height:12px;background-color:#8793A3;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Medium Gray | #8793A3 |
| Data labels & axis text | <span style="display:inline-block;width:12px;height:12px;background-color:#595B69;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Dark Gray | #595B69 |
| Main background | <span style="display:inline-block;width:12px;height:12px;background-color:#F9F9F9;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Near White | #F9F9F9 |
| Page background | <span style="display:inline-block;width:12px;height:12px;background-color:#F6F8FB;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Light Blue-Gray | #F6F8FB |
| Table accent | <span style="display:inline-block;width:12px;height:12px;background-color:#426871;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Dark Teal | #426871 |
| Positive / Good | <span style="display:inline-block;width:12px;height:12px;background-color:#09B39D;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Teal | #09B39D |
| Negative / Bad | <span style="display:inline-block;width:12px;height:12px;background-color:#c2255c;border:1px solid #ddd;vertical-align:middle;margin-right:4px;"></span> Red-Pink | #c2255c |

#### File Metrics

| Metric | Value |
|--------|-------|
| **Total Visual Types** | 40+ |
| **Total JSON Lines** | ~5,024 |
| **Primary Data Colors** | 8 |
| **Semantic Status Colors** | 3 |
| **Text Classes** | 12 |

#### Format Reference

- All color values are in hexadecimal format (#RRGGBB)
- Measurements are in pixels unless noted (font sizes are in points)
- Transparency values: 0 = fully opaque, 100 = fully transparent
- Properties in `visualStyles` use arrays `[ ]` around objects — this is required

</details>

---

<details open class="collapsible-section">
<summary style="cursor:pointer;margin:10px 0;font-size:16px;font-weight:bold;"><span id="version--references">10. Version & References</span></summary>

<div style="height:1px;background:#e5e7eb;margin:10px 0 18px;"></div>

#### Version Information

| Item | Details |
|------|---------|
| **Theme Name** | Custom_Theme |
| **Schema Version** | 2.149 |
| **Last Updated** | January 2026 |
| **Compatible With** | Power BI Desktop & Service |
| **Total Visualization Types** | 40+ |

#### References

### <span id="microsoft-documentation---report-themes-in-power-bi-desktop">1. [Microsoft Documentation - Report Themes in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes)</span>

Official Microsoft documentation on using report themes in Power BI Desktop. This resource covers how to apply, customize, and manage themes in Power BI, including importing custom JSON theme files.

<br>

### <span id="numerro---power-bi-theme-inspiration">2. [Numerro - Power BI Theme Inspiration](https://www.numerro.io/)</span>

This custom theme was inspired by and built using one of Numerro's professional Power BI themes as the foundation. Numerro provides high-quality, pre-designed themes for Power BI reports.

<br>

### <span id="power-bi-theme-json-schema---github-repository">3. [Power BI Theme JSON Schema - GitHub Repository](https://github.com/microsoft/powerbi-desktop-samples/blob/main/Report%20Theme%20JSON%20Schema/README.md)</span>

Official repository containing JSON schema files for validating Power BI report themes. This is the authoritative source for all possible properties, attributes, and structure of a theme file. Essential reference for advanced theme development and validation.

<br>

### <span id="power-bi-theme-generator-by-point-gmbh">4. [Power BI Theme Generator by Point GmbH](https://themegenerator.point-gmbh.com/en/Home)</span>

An interactive web-based tool for editing Power BI themes visually. Note: Style presets must be removed from the theme file for this tool to work properly. This tool provides a user-friendly interface for customizing colors, typography, and basic visual settings.

<br>

### <span id="re-using-visual-formatting-across-power-bi-reports---sqlbi">5. [Re-using Visual Formatting Across Power BI Reports - SQLBI](https://www.sqlbi.com/articles/re-using-visual-formatting-in-and-across-power-bi-reports/)</span>

Comprehensive article by SQLBI explaining how to save development time by effectively using themes to apply consistent formatting across multiple reports and visuals. Covers best practices and strategies for theme-based formatting efficiency.

<br>

</details>

**Documentation Created**: January 2026
**Theme Name**: Custom_Theme_Styles.json
**Purpose**: Complete Power BI theme reference & customization guide for enterprise dashboards and reports
**Version**: 2.0 (Merged)
