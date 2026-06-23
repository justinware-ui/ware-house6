#!/usr/bin/env python3
"""Inject Suggested Demos carousel under Metrics in dashboard HTML."""

from pathlib import Path

DASHBOARD = Path(__file__).resolve().parents[1] / "public/sections/dashboard/index.html"
MARKER = "data-testid=suggestions-section"
INSERT_AFTER = "data-testid=metrics-grid"

CARDS = [
    {"title": "Quick Start Guide", "image": "quick-start.png", "icon": "dynamic-tour.svg", "favorite": True, "avatar": "AZ", "avatar_bg": "#d1e5ff", "date": "05/09/26"},
    {"title": "Account Setup", "image": "account-setup.png", "icon": "demo-personalized.svg", "favorite": True, "avatar": "JW", "avatar_bg": "#ffdfcf", "date": "05/09/26"},
    {"title": "Data Export Guide", "image": "data-export.png", "icon": "demo-single.svg", "favorite": False, "avatar": "AZ", "avatar_bg": "#ffdfcf", "date": "05/09/26"},
    {"title": "First Login Experience", "image": "first-login-exp.png", "icon": "flow.svg", "favorite": True, "avatar": "SM", "avatar_bg": "#d1e5ff", "date": "05/09/26"},
    {"title": "Onboarding Flow", "image": "onboarding-flow.png", "icon": "flow.svg", "favorite": False, "avatar": "MC", "avatar_bg": "#d1e5ff", "date": "05/09/26"},
    {"title": "Feature Highlights", "image": "feature-highlights.png", "icon": "flow.svg", "favorite": True, "avatar": "AZ", "avatar_bg": "#ffdfcf", "date": "05/09/26"},
    {"title": "Enterprise SSO Walkthrough", "image": "data-export.png", "icon": "flow.svg", "favorite": True, "avatar": "RK", "avatar_bg": "#d1e5ff", "date": "04/18/26"},
    {"title": "Pipeline Review Demo", "image": "account-setup.png", "icon": "demo-personalized.svg", "favorite": False, "avatar": "LT", "avatar_bg": "#ffdfcf", "date": "04/02/26"},
    {"title": "Competitive Battlecard", "image": "first-login-exp.png", "icon": "demo-single.svg", "favorite": True, "avatar": "NP", "avatar_bg": "#ffdfcf", "date": "03/21/26"},
    {"title": "Customer Success Toolkit", "image": "onboarding-flow.png", "icon": "dynamic-tour.svg", "favorite": False, "avatar": "EB", "avatar_bg": "#d1e5ff", "date": "03/14/26"},
    {"title": "QBR Executive Summary", "image": "feature-highlights.png", "icon": "demo-personalized.svg", "favorite": True, "avatar": "CM", "avatar_bg": "#ffdfcf", "date": "02/28/26"},
    {"title": "Partner Enablement Tour", "image": "quick-start.png", "icon": "flow.svg", "favorite": False, "avatar": "DG", "avatar_bg": "#d1e5ff", "date": "02/10/26"},
]

FAVORITE_ICON = (
    '<img src="./assets/suggestions/favorite.svg" width="32" height="32" alt="" aria-hidden="true" />'
)

DEMO_ICON = (
    '<img src="./assets/suggestions/{icon}" width="24" height="24" alt="" aria-hidden="true" />'
)

SEND_ICON = (
    '<img src="./assets/suggestions/share.svg" width="32" height="32" alt="" aria-hidden="true" />'
)

MORE_ICON = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<circle cx="6" cy="12" r="1.5" fill="#172537"/><circle cx="12" cy="12" r="1.5" fill="#172537"/>'
    '<circle cx="18" cy="12" r="1.5" fill="#172537"/></svg>'
)

NAV_ICONS = """
<span class="wh6-suggestions__nav-icon wh6-suggestions__nav-icon--default" aria-hidden="true">
  <img src="./assets/suggestions/carousel-nav-default.svg" width="40" height="40" alt="" />
</span>
<span class="wh6-suggestions__nav-icon wh6-suggestions__nav-icon--hover" aria-hidden="true">
  <img src="./assets/suggestions/carousel-nav-hover.svg" width="40" height="40" alt="" />
</span>
"""

FILTER_BTN = (
    "_button_46m2g_1UiKit_1_8_2 _secondary_1vh7j_39UiKit_1_8_2 "
    "_option_1m63n_1UiKit_1_8_2 _primary_1m63n_9UiKit_1_8_2 _small_1m63n_21UiKit_1_8_2"
)
FILTER_SELECTED = "_optionSelected_1m63n_37UiKit_1_8_2"
FILTER_CHECKMARK = """
<div class="successWrapper _successWrapper_46m2g_73UiKit_1_8_2 sf-hidden">
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="var(--color-secondary-500, #293748)" viewBox="0 0 24 24" class="_icon_144be_1UiKit_1_8_2" data-testid="CheckmarkIcon" aria-hidden="true">
<path d="M9.55 17.575q-.2 0-.375-.063a.9.9 0 0 1-.325-.212L4.55 13q-.275-.275-.263-.713.014-.437.288-.712a.95.95 0 0 1 .7-.275q.425 0 .7.275L9.55 15.15l8.475-8.475q-.275-.275.713-.275t.712.275q.275.274.275.712t-.275.713l-9.2 9.2q-.15.15-.325.212a1.1 1.1 0 0 1-.375.063"/>
</svg>
</div>"""

FILTERS = ["Trending", "Most Viewed", "Most Shared"]


def filter_button(label: str, *, selected: bool = False) -> str:
    classes = FILTER_BTN
    if selected:
        classes += f" {FILTER_SELECTED}"
    selected_attr = "true" if selected else "false"
    return (
        f'<button type="button" class="{classes}" role="tab" '
        f'aria-selected="{selected_attr}">{FILTER_CHECKMARK}'
        f'<span class="_children_46m2g_44UiKit_1_8_2">{label}</span></button>'
    )


def filters_html() -> str:
    buttons = "".join(
        filter_button(label, selected=i == 0) for i, label in enumerate(FILTERS)
    )
    return (
        '<div class="_container_12rlc_1UiKit_1_8_2 _small_12rlc_14UiKit_1_8_2" '
        'data-testid="suggestions-filters" role="tablist" aria-label="Sort suggestions">'
        f"{buttons}</div>"
    )


def card_html(card: dict) -> str:
    fav = (
        f'<div class="wh6-suggestions__favorite">{FAVORITE_ICON}</div>'
        if card["favorite"]
        else ""
    )
    return f"""
<article class="wh6-suggestions__card">
  <div class="wh6-suggestions__thumb">
    <div class="wh6-suggestions__thumb-image">
      <img src="./assets/suggestions/{card['image']}" alt="{card['title']} preview" />
    </div>
    {fav}
    <div class="wh6-suggestions__avatar" style="background:{card['avatar_bg']}">{card['avatar']}</div>
  </div>
  <div class="wh6-suggestions__body">
    <div class="wh6-suggestions__type">{DEMO_ICON.format(icon=card['icon'])}</div>
    <h3 class="wh6-suggestions__card-title">{card['title']}</h3>
    <div class="wh6-suggestions__footer">
      <span class="wh6-suggestions__date">{card['date']}</span>
      <div class="wh6-suggestions__actions">
        <button type="button" class="wh6-suggestions__icon-btn" aria-label="Share">{SEND_ICON}</button>
        <button type="button" class="wh6-suggestions__icon-btn" aria-label="More options">{MORE_ICON}</button>
      </div>
    </div>
  </div>
</article>"""


def build_section() -> str:
    cards = "".join(card_html(c) for c in CARDS)
    return f"""
<style>
.wh6-suggestions {{
  background: #fff;
  border: 1px solid #d6d1cb;
  border-radius: 32px;
  box-shadow: 0 20px 20px -20px rgba(48, 41, 33, 0.25);
  margin: 0;
  overflow: visible;
  padding: 24px;
}}
.wh6-suggestions__header {{
  align-items: center;
  display: flex;
  justify-content: space-between;
  margin-bottom: 24px;
}}
.wh6-suggestions__title {{
  color: #172537;
  font-family: Poppins, sans-serif;
  font-size: 16px;
  font-weight: 600;
  line-height: 24px;
  margin: 0;
}}
.wh6-suggestions__carousel {{
  position: relative;
  width: 100%;
}}
.wh6-suggestions__viewport {{
  overflow: hidden;
  width: 100%;
}}
.wh6-suggestions__track {{
  display: flex;
  gap: 16px;
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}}
.wh6-suggestions__card {{
  background: #fff;
  border: 1px solid #d0cbc6;
  border-radius: 16px;
  display: flex;
  flex: 0 0 var(--wh6-card-width, 200px);
  flex-direction: column;
  min-height: 285px;
  overflow: hidden;
  width: var(--wh6-card-width, 200px);
}}
.wh6-suggestions__nav {{
  background: transparent;
  border: none;
  cursor: pointer;
  height: 40px;
  padding: 0;
  position: absolute;
  top: 50%;
  width: 40px;
  z-index: 4;
}}
.wh6-suggestions__nav--prev {{
  left: -8px;
  transform: translateY(-50%) scaleX(-1);
}}
.wh6-suggestions__nav--next {{
  right: -8px;
  transform: translateY(-50%);
}}
.wh6-suggestions__nav-icon {{
  display: block;
  height: 40px;
  inset: 0;
  position: absolute;
  width: 40px;
}}
.wh6-suggestions__nav-icon img {{
  display: block;
  height: 40px;
  width: 40px;
}}
.wh6-suggestions__nav-icon--hover {{
  opacity: 0;
}}
.wh6-suggestions__nav:hover .wh6-suggestions__nav-icon--default,
.wh6-suggestions__nav:focus-visible .wh6-suggestions__nav-icon--default {{
  opacity: 0;
}}
.wh6-suggestions__nav:hover .wh6-suggestions__nav-icon--hover,
.wh6-suggestions__nav:focus-visible .wh6-suggestions__nav-icon--hover {{
  opacity: 1;
}}
.wh6-suggestions__nav:active .wh6-suggestions__nav-icon--hover img {{
  transform: scale(0.94);
}}
.wh6-suggestions__nav:disabled {{
  cursor: default;
  opacity: 0.35;
  pointer-events: none;
}}
.wh6-suggestions__thumb {{
  position: relative;
}}
.wh6-suggestions__thumb-image {{
  border-radius: 15px 15px 0 0;
  height: 150px;
  overflow: hidden;
}}
.wh6-suggestions__thumb-image img {{
  height: 100%;
  object-fit: cover;
  width: 100%;
}}
.wh6-suggestions__favorite {{
  display: block;
  height: 32px;
  left: 11px;
  position: absolute;
  top: 11px;
  width: 32px;
}}
.wh6-suggestions__favorite img {{
  display: block;
  height: 32px;
  width: 32px;
}}
.wh6-suggestions__avatar {{
  align-items: center;
  border: 2px solid #fff;
  border-radius: 50%;
  bottom: -20px;
  box-sizing: border-box;
  color: #172537;
  display: flex;
  font-family: Poppins, sans-serif;
  font-size: 16px;
  height: 40px;
  justify-content: center;
  position: absolute;
  right: 12px;
  width: 40px;
  z-index: 2;
}}
.wh6-suggestions__body {{
  display: flex;
  flex: 1;
  flex-direction: column;
  padding: 28px 16px 16px;
  position: relative;
  z-index: 1;
}}
.wh6-suggestions__type {{
  margin-bottom: 8px;
}}
.wh6-suggestions__type img {{
  display: block;
  height: 24px;
  width: 24px;
}}
.wh6-suggestions__card-title {{
  color: #172537;
  font-family: Poppins, sans-serif;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
  margin: 0 0 auto;
}}
.wh6-suggestions__footer {{
  align-items: center;
  display: flex;
  justify-content: space-between;
  margin-top: 16px;
}}
.wh6-suggestions__date {{
  color: #6f6f6f;
  font-family: Poppins, sans-serif;
  font-size: 12px;
  line-height: 18px;
}}
.wh6-suggestions__actions {{
  display: flex;
  gap: 4px;
}}
.wh6-suggestions__icon-btn {{
  align-items: center;
  background: transparent;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: inline-flex;
  height: 32px;
  justify-content: center;
  padding: 0;
  width: 32px;
}}
.wh6-suggestions__icon-btn img {{
  display: block;
  height: 32px;
  width: 32px;
}}
</style>
<section class="wh6-suggestions" data-testid="suggestions-section">
  <div class="wh6-suggestions__header">
    <h2 class="wh6-suggestions__title">Suggested Demos for You</h2>
    {filters_html()}
  </div>
  <div class="wh6-suggestions__carousel">
    <div class="wh6-suggestions__viewport">
      <div class="wh6-suggestions__track">{cards}</div>
    </div>
    <button type="button" class="wh6-suggestions__nav wh6-suggestions__nav--prev" aria-label="Previous suggested demos">{NAV_ICONS}</button>
    <button type="button" class="wh6-suggestions__nav wh6-suggestions__nav--next" aria-label="Next suggested demos">{NAV_ICONS}</button>
  </div>
</section>
<script>
(function () {{
  var section = document.querySelector('[data-testid="suggestions-section"]');
  if (!section) return;

  var viewport = section.querySelector('.wh6-suggestions__viewport');
  var track = section.querySelector('.wh6-suggestions__track');
  var prevBtn = section.querySelector('.wh6-suggestions__nav--prev');
  var nextBtn = section.querySelector('.wh6-suggestions__nav--next');
  var cards = Array.prototype.slice.call(section.querySelectorAll('.wh6-suggestions__card'));
  if (!viewport || !track || !prevBtn || !nextBtn || !cards.length) return;

  var index = 0;

  function syncCardWidths() {{
    var available = viewport.getBoundingClientRect().width;
    if (!available) return;

    var gridGap = 16;
    var minCol = 200;
    var cols = Math.max(1, Math.floor((available + gridGap) / (minCol + gridGap)));
    var cardWidth = (available - (cols - 1) * gridGap) / cols;

    section.style.setProperty('--wh6-card-width', cardWidth + 'px');
    track.style.gap = gridGap + 'px';
  }}

  function gap() {{
    return parseFloat(getComputedStyle(track).gap || '16') || 16;
  }}

  function visibleCount() {{
    var card = cards[0];
    if (!card) return 1;
    var cardWidth = card.getBoundingClientRect().width;
    var available = viewport.getBoundingClientRect().width;
    return Math.max(1, Math.floor((available + gap()) / (cardWidth + gap())));
  }}

  function maxIndex() {{
    return Math.max(0, cards.length - visibleCount());
  }}

  function stepSize() {{
    var card = cards[0];
    if (!card) return 0;
    return card.getBoundingClientRect().width + gap();
  }}

  function update() {{
    syncCardWidths();
    index = Math.min(index, maxIndex());
    track.style.transform = 'translateX(' + (-index * stepSize()) + 'px)';
    prevBtn.disabled = index <= 0;
    nextBtn.disabled = index >= maxIndex();
  }}

  prevBtn.addEventListener('click', function () {{
    index = Math.max(0, index - 1);
    update();
  }});

  nextBtn.addEventListener('click', function () {{
    index = Math.min(maxIndex(), index + 1);
    update();
  }});

  window.addEventListener('resize', update);
  requestAnimationFrame(function () {{
    requestAnimationFrame(update);
  }});

  var filters = Array.prototype.slice.call(
    section.querySelectorAll('[data-testid="suggestions-filters"] button')
  );
  filters.forEach(function (filter) {{
    filter.addEventListener('click', function () {{
      filters.forEach(function (btn) {{
        btn.classList.remove('_optionSelected_1m63n_37UiKit_1_8_2');
        btn.setAttribute('aria-selected', 'false');
      }});
      filter.classList.add('_optionSelected_1m63n_37UiKit_1_8_2');
      filter.setAttribute('aria-selected', 'true');
    }});
  }});
}})();
</script>"""


def remove_all_suggestions(html: str) -> str:
    script_needle = (
        '<script>\n(function () {\n  var section = document.querySelector(\'[data-testid="suggestions-section"]\')'
    )

    while True:
        start = html.find("<style>\n.wh6-suggestions")
        if start == -1:
            start = html.find('<section class="wh6-suggestions"')
        if start == -1:
            break

        script_end = html.find("</script>", start)
        section_end = html.find("</section>", start)
        if script_end != -1 and (section_end == -1 or script_end < section_end):
            end = script_end + len("</script>")
        elif section_end != -1:
            end = section_end + len("</section>")
        else:
            break

        html = html[:start] + html[end:]

    while script_needle in html:
        start = html.find(script_needle)
        end = html.find("</script>", start)
        if end == -1:
            break
        html = html[:start] + html[end + len("</script>") :]

    return html


def find_metrics_card_end(html: str) -> int:
    idx = html.find(INSERT_AFTER)
    if idx == -1:
        raise SystemExit("Metrics container not found")

    card_start = html.rfind('<div class="_card_hy4m5_', 0, idx)
    depth = 0
    i = card_start
    while i < len(html):
        if html.startswith("<div", i):
            depth += 1
            i = html.find(">", i) + 1
        elif html.startswith("</div>", i):
            depth -= 1
            i += 6
            if depth == 0:
                return i
        else:
            i += 1
    raise SystemExit("Could not find end of metrics card")


def main() -> None:
    html = DASHBOARD.read_text(encoding="utf-8")
    had_existing = MARKER in html
    html = remove_all_suggestions(html)
    insert_at = find_metrics_card_end(html)
    html = html[:insert_at] + build_section() + html[insert_at:]

    if had_existing:
        print("Replaced suggestions section with carousel")
    else:
        print("Inserted suggestions carousel under Metrics")

    DASHBOARD.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
