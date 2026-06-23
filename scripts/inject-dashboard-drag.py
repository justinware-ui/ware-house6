#!/usr/bin/env python3
"""Inject draggable grabber handles and reorder logic into dashboard HTML."""

from pathlib import Path

DASHBOARD = Path(__file__).resolve().parents[1] / "public/sections/dashboard/index.html"
GRABBER = Path(__file__).resolve().parents[1] / "public/sections/dashboard/assets/grabber.svg"
MARKER = "data-wh6-dashboard-drag"

DRAGGABLE_IDS = [
    "insights-grid",
    "metrics-grid",
    "suggestions-section",
    "library-widget",
    "onboarding-video-widget",
]


def build_block() -> str:
    ids_json = str(DRAGGABLE_IDS)

    return f"""
<style>
.wh6-dash-draggable {{
  position: relative;
  transition: box-shadow 0.25s ease;
}}
.wh6-dash-grabber {{
  align-items: center;
  background: transparent;
  border: none;
  cursor: grab;
  display: flex;
  height: 28px;
  justify-content: center;
  left: 50%;
  padding: 0;
  position: absolute;
  top: 12px;
  transform: translateX(-50%);
  width: 28px;
  z-index: 100;
}}
.wh6-dash-grabber img {{
  display: block;
  height: 16px;
  pointer-events: none;
  width: 16px;
}}
.wh6-dash-grabber:active {{
  cursor: grabbing;
}}
.wh6-dash-draggable.is-dragging {{
  box-shadow: 0 24px 48px rgba(48, 41, 33, 0.18);
  opacity: 0.96;
  transition: none;
}}
.wh6-dash-drop-placeholder {{
  background: rgba(252, 104, 57, 0.06);
  border: 2px dashed #fc6839;
  border-radius: 32px;
  box-sizing: border-box;
  margin: 0;
  transition: height 0.2s ease, opacity 0.2s ease;
}}
</style>
<script {MARKER}>
(function () {{
  var STORAGE_KEY = "wh6-dashboard-order";
  var IDS = {ids_json};

  function init() {{
    var app = document.querySelector('[data-testid="app-component"]')
      || document.querySelector("[data-testid=app-component]");
    if (!app) return;

    flattenGrid(app);
    promoteSuggestions(app);
    restoreOrder(app);

    getItems(app).forEach(prepareItem);
    setupSortable(app);
  }}

  function flattenGrid(app) {{
    var grid = app.querySelector(".styles-module__gridContainer--MdvdO");
    if (!grid) return;

    Array.prototype.slice.call(grid.children).forEach(function (child) {{
      app.appendChild(child);
    }});
    grid.remove();
  }}

  function promoteSuggestions(app) {{
    var suggestions = document.querySelector('[data-testid="suggestions-section"]')
      || document.querySelector("[data-testid=suggestions-section]");
    if (!suggestions) return;

    var metrics = app.querySelector('[data-testid="metrics-grid"]')
      || app.querySelector("[data-testid=metrics-grid]");
    if (!metrics || !metrics.contains(suggestions)) return;

    if (metrics.nextSibling) {{
      app.insertBefore(suggestions, metrics.nextSibling);
      return;
    }}
    app.appendChild(suggestions);
  }}

  function getItems(app) {{
    return IDS.map(function (id) {{
      return app.querySelector('[data-testid="' + id + '"]')
        || app.querySelector("[data-testid=" + id + "]");
    }}).filter(Boolean);
  }}

  function prepareItem(item) {{
    item.classList.add("wh6-dash-draggable");
    item.setAttribute("data-wh6-draggable", item.getAttribute("data-testid") || "");
    if (item.querySelector(".wh6-dash-grabber")) return;

    var handle = document.createElement("button");
    handle.type = "button";
    handle.className = "wh6-dash-grabber";
    handle.setAttribute("aria-label", "Drag to reorder section");
    handle.innerHTML =
      '<img src="./assets/grabber.svg" width="16" height="16" alt="" aria-hidden="true" />';
    item.insertBefore(handle, item.firstChild);
  }}

  function setupSortable(app) {{
    var dragging = null;
    var placeholder = null;
    var offsetY = 0;

    app.addEventListener("pointerdown", function (event) {{
      var handle = event.target.closest(".wh6-dash-grabber");
      if (!handle) return;

      var item = handle.closest(".wh6-dash-draggable");
      if (!item) return;

      event.preventDefault();
      handle.setPointerCapture(event.pointerId);

      dragging = item;
      dragging.classList.add("is-dragging");

      var rect = item.getBoundingClientRect();
      offsetY = event.clientY - rect.top;

      placeholder = document.createElement("div");
      placeholder.className = "wh6-dash-drop-placeholder";
      placeholder.style.height = rect.height + "px";
      item.parentNode.insertBefore(placeholder, item);

      item.style.position = "fixed";
      item.style.width = rect.width + "px";
      item.style.left = rect.left + "px";
      item.style.top = rect.top + "px";
      item.style.zIndex = "1000";
      item.style.pointerEvents = "none";
    }});

    app.addEventListener("pointermove", function (event) {{
      if (!dragging || !placeholder) return;

      dragging.style.top = (event.clientY - offsetY) + "px";

      var afterElement = getDragAfterElement(app, event.clientY);
      if (!afterElement) {{
        app.appendChild(placeholder);
        return;
      }}
      app.insertBefore(placeholder, afterElement);
    }});

    function finishDrag() {{
      if (!dragging || !placeholder) return;

      dragging.classList.remove("is-dragging");
      dragging.style.position = "";
      dragging.style.width = "";
      dragging.style.left = "";
      dragging.style.top = "";
      dragging.style.zIndex = "";
      dragging.style.pointerEvents = "";

      app.insertBefore(dragging, placeholder);
      placeholder.remove();

      dragging = null;
      placeholder = null;
      saveOrder(app);
    }}

    app.addEventListener("pointerup", finishDrag);
    app.addEventListener("pointercancel", finishDrag);
  }}

  function getDragAfterElement(app, y) {{
    var items = Array.prototype.slice.call(
      app.querySelectorAll(".wh6-dash-draggable:not(.is-dragging)")
    );

    return items.reduce(function (closest, child) {{
      var box = child.getBoundingClientRect();
      var offset = y - box.top - box.height / 2;
      if (offset < 0 && offset > closest.offset) {{
        return {{ offset: offset, element: child }};
      }}
      return closest;
    }}, {{ offset: Number.NEGATIVE_INFINITY, element: null }}).element;
  }}

  function saveOrder(app) {{
    var order = Array.prototype.slice.call(app.querySelectorAll(".wh6-dash-draggable"))
      .map(function (item) {{ return item.getAttribute("data-testid"); }})
      .filter(Boolean);

    try {{
      localStorage.setItem(STORAGE_KEY, JSON.stringify(order));
    }} catch (error) {{}}
  }}

  function restoreOrder(app) {{
    var saved = null;
    try {{
      saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    }} catch (error) {{
      saved = null;
    }}
    if (!Array.isArray(saved)) return;

    saved.forEach(function (id) {{
      var item = app.querySelector('[data-testid="' + id + '"]')
        || app.querySelector("[data-testid=" + id + "]");
      if (item) app.appendChild(item);
    }});
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", init);
  }} else {{
    init();
  }}
}})();
</script>"""


def remove_existing(html: str) -> str:
    start = html.find("<style>\n.wh6-dash-draggable")
    if start == -1:
        start = html.find(f"<script {MARKER}>")
    if start == -1:
        return html

    end = html.find("</script>", start)
    if end == -1:
        return html[:start]
    return html[:start] + html[end + len("</script>") :]


def find_insert_point(html: str) -> int:
    anchor = html.find("<div class=styles-module__gridContainer--MdvdO>")
    if anchor != -1:
        return anchor

    suggestions = html.find("data-testid=suggestions-section")
    if suggestions != -1:
        script_end = html.find("</script>", suggestions)
        if script_end != -1:
            return script_end + len("</script>")

    return len(html)


def main() -> None:
    html = DASHBOARD.read_text(encoding="utf-8")
    had_existing = MARKER in html
    html = remove_existing(html)
    insert_at = find_insert_point(html)
    block = build_block().strip()
    html = html[:insert_at] + block + html[insert_at:]

    if had_existing:
        print("Updated dashboard drag-and-drop")
    else:
        print("Injected dashboard drag-and-drop")

    DASHBOARD.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
