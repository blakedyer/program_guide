document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-contact-toggle]").forEach((shell) => {
    const button = shell.querySelector(".contact-compact__button");
    const panel = shell.querySelector(".contact-compact__panel");

    if (!button || !panel) {
      return;
    }

    const applyExpanded = (expanded) => {
      shell.classList.toggle("is-open", expanded);
      button.setAttribute("aria-expanded", String(expanded));
      panel.hidden = !expanded;
    };

    button.addEventListener("click", () => {
      const expanded = button.getAttribute("aria-expanded") === "true";
      applyExpanded(!expanded);
    });

    applyExpanded(false);
  });

  document.querySelectorAll("[data-card-filter]").forEach((panel) => {
    const grid = panel.parentElement?.querySelector("[data-filter-grid]");
    const emptyState = panel.parentElement?.querySelector("[data-filter-empty]");
    const buttons = Array.from(panel.querySelectorAll("[data-filter-group]"));
    const searchInput = panel.querySelector("[data-filter-search-input]");

    if (!grid) {
      return;
    }

    const cards = Array.from(grid.children);

    const activeFilters = {};
    buttons.forEach((button) => {
      const group = button.getAttribute("data-filter-group");
      if (!group || activeFilters[group]) {
        return;
      }
      const activeButton =
        buttons.find(
          (candidate) =>
            candidate.getAttribute("data-filter-group") === group &&
            candidate.classList.contains("is-active"),
        ) ||
        buttons.find((candidate) => candidate.getAttribute("data-filter-group") === group);
      if (activeButton) {
        activeFilters[group] = activeButton.getAttribute("data-filter-value") || "all";
      }
    });

    const applyFilters = () => {
      const query = (searchInput?.value || "").trim().toLowerCase();
      let visibleCount = 0;

      cards.forEach((card) => {
        const matchesSearch = !query || (card.getAttribute("data-filter-search") || "").includes(query);
        const matchesGroups = Object.entries(activeFilters).every(([group, value]) => {
          if (!value || value === "all") {
            return true;
          }
          const haystack = card.getAttribute(`data-filter-${group}`) || "";
          return haystack.split(/\s+/).includes(value);
        });
        const isVisible = matchesSearch && matchesGroups;
        card.classList.toggle("is-hidden", !isVisible);
        if (isVisible) {
          visibleCount += 1;
        }
      });

      if (emptyState) {
        emptyState.classList.toggle("is-hidden", visibleCount !== 0);
      }
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const group = button.getAttribute("data-filter-group");
        const value = button.getAttribute("data-filter-value") || "all";
        if (!group) {
          return;
        }
        activeFilters[group] = value;
        buttons.forEach((candidate) => {
          if (candidate.getAttribute("data-filter-group") !== group) {
            return;
          }
          const isActive = candidate === button;
          candidate.classList.toggle("is-active", isActive);
          candidate.setAttribute("aria-pressed", String(isActive));
        });
        applyFilters();
      });
    });

    if (searchInput) {
      searchInput.addEventListener("input", applyFilters);
    }

    applyFilters();
  });

  document.querySelectorAll("[data-graph-switcher]").forEach((shell) => {
    const graphObject = shell.querySelector("[data-graph-object]");
    const graphFallback = shell.querySelector("[data-graph-fallback]");
    const graphLink = shell.querySelector("[data-graph-link]");
    const modeCopy = shell.querySelector("[data-graph-mode-copy]");
    const buttons = Array.from(shell.querySelectorAll("[data-graph-mode]"));

    if (!graphObject || buttons.length === 0) {
      return;
    }

    const applyMode = (button) => {
      const src = button.getAttribute("data-graph-src");
      const download = button.getAttribute("data-graph-download") || src;
      const copy = button.getAttribute("data-graph-copy") || "";

      if (src) {
        graphObject.setAttribute("data", src);
        if (graphFallback) {
          graphFallback.setAttribute("src", src);
        }
      }

      if (graphLink && download) {
        graphLink.setAttribute("href", download);
      }

      if (modeCopy) {
        modeCopy.textContent = copy;
      }

      buttons.forEach((candidate) => {
        const isActive = candidate === button;
        candidate.classList.toggle("is-active", isActive);
        candidate.setAttribute("aria-pressed", String(isActive));
      });
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => applyMode(button));
    });

    const activeButton = buttons.find((button) => button.classList.contains("is-active")) || buttons[0];
    applyMode(activeButton);
  });
});
