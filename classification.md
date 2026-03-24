---
layout: default
title: Rhododendron Classification
---



# Rhododendron Classification

This section provides an overview and data related to the Rhododendron classification used by the R‑RN project.

## Species List

- [Rhododendron aberconwayi](rrn-taxa/rhododendron_aberconwayi.md)

{% assign rrn_taxa = site.rrn_taxa | default: empty %}
{% if rrn_taxa != empty %}
  {% assign sorted = rrn_taxa | sort: "title" %}
  <ul>
  {% for t in sorted %}
    <li><a href="{{ t.url }}">{{ t.title }}</a></li>
  {% endfor %}
  </ul>
{% else %}
  <p>No taxa found.</p>
{% endif %}
