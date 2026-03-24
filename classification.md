---
layout: default
title: Rhododendron Classification
---

Collections loaded: {{ site.collections | map: "label" }}

rrn_taxa count: {{ site.rrn_taxa | size }}

Root contains rrn_taxa folder:
{{ site.static_files | where_exp: "f", "f.path contains 'rrn_taxa/'" | size }}

# Rhododendron Classification

This section provides an overview and data related to the Rhododendron classification used by the R‑RN project.

## Species List

- [Rhododendron aberconwayi](rrn-taxa/rhododendron_aberconwayi.md)

{% assign rrn-taxa = site.rrn-taxa | default: empty %}
{% if rrn-taxa != empty %}
  {% assign sorted = rrn-taxa | sort: "title" %}
  {% for t in sorted %}
    {{ t.title }}
  {% endfor %}
{% else %}
  <p>No taxa found.</p>
{% endif %}

