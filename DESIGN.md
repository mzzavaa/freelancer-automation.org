# Design Specification: Apple‑style Freelancer Site

This document captures research, principles, and the implementation plan for a dark, **Apple‑inspired** freelance‑attracting website with icons, graphics, and high visual polish. It accompanies the Hugo project in this repository.

---

## 1. Research & Inspiration

### 1.1 Apple Human Interface Guidelines (HIG)
- **Clarity, Deference, Depth**: text is legible, interfaces recede, layers clarify hierarchy.
- **Hierarchy**: use size, weight, spacing to show structure. Large headlines, light body text.
- **Spacing & Grid**: generous padding, consistent alignment, 8‑point grid lightly implied.
- **Materials**: translucent layers, subtle blur ("Liquid Glass"), light/dark system colors.
- **Typography**: San Francisco family, system‑font stack for native feel. Antialiased.
- **Color**: restrained palette—mostly neutral backgrounds with a single accent color.
- **Dark Mode**: design for both light and dark; switch automatically via `prefers-color-scheme`.
- **Icons**: SF Symbols provide a consistent, monoline iconography; use sparingly for clarity.

### 1.2 Freelance & Portfolio Site Patterns
- Prominent hero with name/tagline + subtle graphic (e.g. vector illustration, device mockup).
- Section previews presented as cards or tiles with short descriptions.
- Navigation minimal, often with icons + text for quick scanning.
- Dark themes are appealing to developer/audience; contrast is important.
- Micro‑interactions (hover, focus, reveal) add delight without noise.

### 1.3 Practical Takeaways
- Adopt a **dark base theme** with a light toggle.
- Use system fonts and proper font smoothing.
- Introduce icons via SVG or SF Symbols CDN.
- Add a hero graphic or pattern in SVG/JSON (lottie) layer.
- Maintain clean, readable layout with plenty of whitespace.

---

## 2. Technical Specification

### 2.1 CSS Architecture
- Root CSS variables for colours, spacing, radius, type scale.
- `prefers-color-scheme` media query to switch between light/dark variables.
- Utility classes for `.icon` and `.icon--small` that render inline SVG.
- Dark theme: `--bg`, `--surface`, `--text`, `--accent`, `--fade` switch values.
- Add `.dark-toggle` script for manual switching if desired.

### 2.2 Icons & Graphics
- Place simple icons next to nav links (use `<svg><use href="#icon-name"/></svg>`).
- Create an `assets/icons/icons.svg` sprite of a few SF‑style glyphs (home, guide, code, book, wrench).
- Add a hero illustration (light/dark variants) stored under `static/images/`.
- Use **free-to-use imagery** from services like Unsplash or Pexels; credit is usually not required but nice to include in footer or credits section. For dynamic placeholders, `https://source.unsplash.com` can deliver random high‑resolution photos tagged with keywords. Provide separate light/dark queries or apply color overlays to ensure backgrounds remain elegant in dark mode.

### 2.3 Templates & Markup
- Update `nav.html` to include `<svg class="icon"><use href="#icon-home"></use></svg>` before each link.
- `hero` section to include `<img class="hero-graphic" src="/images/hero-dark.svg" alt="...">`.

### 2.4 Accessibility
- Ensure sufficient contrast (WCAG AA/AAA where feasible).
- Provide `aria-label`s for icons when not accompanied by text.
- Keep heading hierarchy semantically correct.
- Include skip links and focus styles.

### 2.5 Interaction & Animation
- Keep animations subtle: fade/transform on scroll with `.reveal`.
- Links underline on hover, icons change color slightly.

---

## 3. Implementation Steps
1. Add SVG icon sprite and hero images.
2. Extend `head.html` with dark mode variables and icon styles.
3. Modify `nav.html` to insert icons.
4. Add JavaScript for prefer‑color‑scheme toggle.
5. Update tests to verify presence of icons and dark mode CSS.
6. Iterate design with sample content and real graphics.

- Aim for a **full-width, groundbreaking layout** by letting hero and key sections bleed to the viewport edges; mix in large background photos and gradient overlays for visual impact. Implement a secondary `.main-inner` container to preserve readability while letting the overall page span the viewport.

---

## 4. Roadmap & Future Enhancements
- Add a settings page or toggle switch to manually override system theme.
- Consider adding animations (e.g. subtle parallax in hero graphic).
- Generate Lottie JSON for a more sophisticated illustration.
- Use WebP or AVIF images for performance.

---

*Created on 2026‑03‑02 by Copilot.*
