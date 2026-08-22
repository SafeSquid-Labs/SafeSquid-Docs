# SafeSquid Docs TODO

## Header Navigation Changes (2026-02-24)

### Completed
- ✅ Added 8 main website navigation links (HOME → PRICING) to match production
- ✅ Removed PORTAL link from navbar (not present on production)
- ✅ Removed version dropdown from navbar
- ✅ Fixed PM2 ecosystem config (changed from `npm run dev` to `npm run start`)
- ✅ Fixed blog truncation warnings - added `<!-- truncate -->` markers to 5 blog posts:
  - 2025-06-02-CSRF-Abuse.md
  - 2025-06-02-Cyberslacking.md
  - 2025-06-02-DNS-Tunneling.md
  - 2025-06-02-Last-Mile-Reassembly-of-Drive‑By-Malware.md
  - 2025-05-17-Zero-Hour-Phishing-Beyond-URL-filters.md

### Notes
- **Version Dropdown Removal**: The production site (docs.safesquid.com) does not display a version dropdown in the navbar. This was removed from the local dev config to match production exactly.
  - If versioning is needed in the future, consider:
    - Adding it back with proper version data
    - Using an alternative placement (footer, sidebar, or dedicated versions page)
    - Checking if production has versioning configured but hidden via CSS
- **Blog Truncation Markers**: Added after the introduction/definition section in each post to create clean previews on the blog listing page.

### To Verify
- [ ] Test all navigation links work correctly
- [ ] Verify responsive behavior on mobile
- [ ] Check if versioning functionality is still needed
- [ ] Confirm PORTAL link removal is intentional (or if it should be in footer/elsewhere)

## CSS & Theme Configuration (2026-02-24)

### Current Local Styling (custom.css)
✅ **Primary Colors**:
- Brand color: `#006699` (SafeSquid blue) - set for all primary color variants
- Applied to light and dark themes

✅ **Custom Features**:
- Full-width image styling
- Enhanced table readability with sticky headers
- Table hover effects
- CISO callout/admonition styling
- Print styles for compliance documentation
- Responsive table improvements
- Enhanced search UI styling
- Version dropdown styling (legacy, may need cleanup if version feature removed)

✅ **Navbar**:
- Custom logo sizing for light/dark modes
- SafeSquid branding colors

### Comparison Needed
Since browser tool is unavailable, manual verification required:

1. **Visual Comparison**:
   - [ ] Compare homepage layout: http://localhost:3001 vs https://docs.safesquid.com
   - [ ] Check if hero banner colors match
   - [ ] Verify feature cards styling
   - [ ] Compare footer styling

2. **Typography**:
   - [ ] Font families (body, headings, code)
   - [ ] Font sizes and line heights
   - [ ] Font weights

3. **Colors**:
   - [ ] Primary color (#006699) appears consistent
   - [ ] Secondary/accent colors
   - [ ] Link colors
   - [ ] Background colors
   - [ ] Border colors

4. **Components**:
   - [ ] Button styling
   - [ ] Card styling
   - [ ] Admonitions (notes, warnings, tips)
   - [ ] Code blocks
   - [ ] Tables
   - [ ] Search bar

5. **Homepage Difference**:
   - Local uses: `<QuickLinks />` component (8 cards)
   - Production may use: `<HomepageFeatures />` component (3 feature sections)
   - **Decision pending**: Keep current QuickLinks or switch to match production

### How to Check
```bash
# Compare visually in browser:
# - Open http://localhost:3001
# - Open https://docs.safesquid.com
# - Use browser DevTools to inspect:
#   - Computed styles
#   - CSS variables (--ifm-*)
#   - Component classes

# Check production CSS variables:
# Open browser console on docs.safesquid.com and run:
getComputedStyle(document.documentElement).getPropertyValue('--ifm-color-primary')
```

### Recommendations
1. Keep current custom.css as it includes SafeSquid-specific enhancements
2. Visual comparison needed to identify any missing styles
3. If homepage component differs, decide whether to match production exactly or keep current design
4. Clean up unused version dropdown CSS if versioning removed permanently
