---
name: apple-style-ui-audit
description: >-
  Use this when auditing or building a web or app UI to Apple-style design
  quality, before changing screens or reviewing a frontend PR.
---
# Apple-style UI audit

## 0. First-impression UX test (always first, outranks every item below)
Open the home page cold (mobile 390x844 and desktop 1440x900) and judge only the first screen, without scrolling:
- In 5 seconds, can a stranger say what this site is and who it is for? (one identity line, no jargon)
- Is the one thing a visitor most likely wants to click obvious? Max 1 primary action and 1 secondary on the first screen.
- Measure: links, words, cards and nav items on the first screen; clicks from home to the main content (target 1-2).
- Flow: home -> content -> next content should need no explanation or reading of long text. Cut, merge or hide anything that does not serve the primary action.
Fail this test and stop: simplify the flow before touching colors or typography.

## 0a. Primary visitor job (decide before designing any screen)
Every site has ONE main reason a visitor arrives. Name it, then make the first screen do exactly that job:
- Read articles -> one featured piece visible at once, short list below, a clear way to continue; contribute/like actions only if the product truly supports them.
- Find something nearby -> ask for location consent in context (with a no-location fallback such as city or district picker), show nearby results first, interest filters at the top; never a bare endless list.
- Discover what I did not know I wanted -> show a few recommendations with a reason or social proof (real reviews only) and one obvious next step.
- Search is the job -> large centered search box as the hero.
Output of this step: one sentence (visitor, job, first action), the first-screen wireframe, and what is removed from the first screen. Check repo rules (no fake reviews, no tracking, static hosting limits) before proposing features that need a backend.

Score each item pass / fail / n.a. with evidence (screenshot path or measured value). Never mark pass from reading code alone.

## Layout and spacing
- 8pt grid: all margins, padding, gaps are multiples of 4 or 8. Flag one-off values.
- Generous whitespace; one clear focal point per screen; content first, chrome second.
- Consistent max content width, aligned edges, no orphan elements.

## Typography
- System font stack first (-apple-system, BlinkMacSystemFont, system-ui, then a Korean-capable fallback such as Pretendard or Noto Sans KR). Never ship SF Pro files, Apple logos, icons or photos (licensing).
- Clear hierarchy: large title, headline, body, caption. Max 3-4 sizes per screen. Body 16px or more on mobile.
- Korean text: `word-break: keep-all`, line-height 1.5-1.7, no mid-word breaks, tight tracking only on large headings.

## Color and depth
- Neutral base with one accent color. Semantic tokens only (no raw hex in components).
- WCAG AA contrast (4.5:1 body, 3:1 large text) in light and dark.
- Dark mode is designed, not inverted: elevated surfaces lighter, softer borders.
- Blur / translucency only for overlays, nav bars and sheets; always with a solid fallback.
- Soft, low-opacity layered shadows; large radii (12-24px cards, pill buttons) used consistently.

## Motion
- 150-400ms, ease-out or spring-like curves; animate transform and opacity only.
- Motion explains state change; no decorative loops.
- Respect `prefers-reduced-motion`.

## Interaction and accessibility
- Touch targets at least 44x44px; visible focus ring; full keyboard path.
- Labels for icon-only buttons; alt text; correct landmarks and heading order.
- Every state exists: loading (skeleton), empty, error, disabled, hover, pressed.
- Safe areas on mobile, no horizontal scroll, works at 320px to 1440px.

## Output
Reply with: table of failed items (item, evidence, fix), then the smallest ordered list of fixes. Label each claim measured, inferred or guess. Do not hand back a check you could run yourself.
