# Veinte Por Diez - Design Guide

## Color Palette

### Main Background
- **Dark padel green**: `#1F4D3A`
  - Usage: Base color for overlay on background image
  - CSS Variable: `--color-verde-padel-oscuro`

- **Soft secondary green**: `#2E6B52`
  - Usage: Secondary elements, background variations
  - CSS Variable: `--color-verde-suave-secundario`

- **Graphite gray**: `#1E1E1E`
  - Usage: Alternative dark backgrounds, text on light backgrounds
  - CSS Variable: `--color-gris-grafito`

### Primary Buttons (CTA)
- **Teal blue**: `#0F766E`
  - Usage: Primary action buttons (Create Tournament, Save, etc.)
  - CSS Variable: `--color-btn-primary`
  - CSS Class: `.btn-primary`

- **Hover**: `#115E59`
  - Usage: Hover state for primary buttons
  - CSS Variable: `--color-btn-primary-hover`

- **Text**: `#FFFFFF`
  - Usage: Text on primary buttons
  - CSS Variable: `--color-btn-primary-text`

### Secondary Buttons
- **Light sand**: `#D6C7A1`
  - Usage: Secondary buttons (Cancel, Back, etc.)
  - CSS Variable: `--color-btn-secondary`
  - CSS Class: `.btn-secondary`

- **Hover**: `#C4B38A`
  - Usage: Hover state for secondary buttons
  - CSS Variable: `--color-btn-secondary-hover`

- **Text**: `#1E1E1E`
  - Usage: Text on secondary buttons
  - CSS Variable: `--color-btn-secondary-text`

### Inputs and Forms
- **Input background**: `#F5F5F5`
  - Usage: Background for text fields, select, textarea
  - CSS Variable: `--color-input-bg`

- **Borders**: `#D1D5DB`
  - Usage: Input borders in normal state
  - CSS Variable: `--color-input-border`

- **Focus**: `#0F766E`
  - Usage: Input border when active
  - CSS Variable: `--color-input-focus`

### Text
- **Primary**: `#FFFFFF`
  - Usage: Text on dark backgrounds (titles, navigation)
  - CSS Variable: `--color-text-principal`

- **Secondary**: `#D1D5DB`
  - Usage: Less prominent text on dark backgrounds
  - CSS Variable: `--color-text-secundario`

- **Dark on light backgrounds**: `#111827`
  - Usage: Primary text on cards and light backgrounds
  - CSS Variable: `--color-text-oscuro`

- **Muted**: `#6B7280`
  - Usage: Secondary text on light backgrounds, help text, notes
  - CSS Variable: `--color-text-muted`

## Typography

### Primary Font
- **Montserrat**
  - Weights: 400 (Regular), 600 (SemiBold), 700 (Bold)
  - Google Fonts: `https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap`

### Sizes
- **H1**: 42px - Main titles
- **H2**: 22px - Card titles
- **Body**: 16px - Normal text
- **Small**: 14px - Details, secondary labels
- **Caption**: 12px - Notes, help text

## Spacing

### Padding
- **Cards**: 40px
- **Buttons**: 15px vertical, 35px horizontal
- **Small Buttons**: 10px vertical, 25px horizontal
- **Form Inputs**: 12px

### Margins
- Use utility classes: `.mt-1`, `.mt-2`, `.mt-3`, `.mt-4`
- Values: 10px, 20px, 30px, 40px

### Gaps
- Between flex elements: `.gap-1` (10px), `.gap-2` (20px), `.gap-3` (30px)

## Borders

### Border Radius
- **Buttons**: 25px (rounded)
- **Cards**: 10px
- **Inputs**: 5px
- **Images**: 8px

## Shadows

- **Small**: `0 2px 10px rgba(0, 0, 0, 0.1)` - Subtle elements
- **Medium**: `0 2px 10px rgba(0, 0, 0, 0.2)` - Normal cards
- **Large**: `0 4px 20px rgba(0, 0, 0, 0.3)` - Cards on hover
- **Primary**: `0 4px 12px rgba(15, 118, 110, 0.4)` - Primary buttons on hover
- **Secondary**: `0 4px 12px rgba(214, 199, 161, 0.4)` - Secondary buttons on hover

## Background Image

- **Location**: `static/background/header.png`
- **Description**: Padel court image
- **Overlay**: Linear gradient with `rgba(31, 77, 58, 0.85)` to darken
- **Behavior**: `center/cover no-repeat fixed`

## Components

### Buttons
```html
<!-- Primary button -->
<button class="btn btn-primary">Create Tournament</button>

<!-- Secondary button -->
<button class="btn btn-secondary">Cancel</button>

<!-- Small button -->
<a href="#" class="btn btn-secondary btn-small">Back</a>
```

### Cards
```html
<!-- Basic card -->
<div class="card">
    <h2>Title</h2>
    <p>Content</p>
</div>

<!-- Card with hover -->
<div class="card card-hover">
    <h2>Title</h2>
    <p>Content</p>
</div>
```

### Forms
```html
<div class="form-group">
    <label for="field">Label</label>
    <input type="text" id="field" name="field" required>
    <div class="text-muted mt-1">Help text</div>
</div>
```

## CSS Files

### Variables
- **Location**: `static/css/variables.css`
- **Content**: All color variables and reusable values
- **Import**: Must be included first in all templates

### Global Styles
- **Location**: `static/css/styles.css`
- **Content**: Base styles, utility classes, components
- **Import**: Must be included after variables.css

### Usage in Templates
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/variables.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
```

## Design Principles

1. **Contrast**: Use white text on dark backgrounds, dark text on light backgrounds
2. **Consistency**: Always use the same CSS variables for colors
3. **Accessibility**: Maintain adequate contrast ratios (WCAG AA)
4. **Spacing**: Use consistent scale (10px, 20px, 30px, 40px)
5. **Visual Feedback**: All interactive elements have hover state
6. **Shadows**: Increase shadow on hover to give elevation effect
